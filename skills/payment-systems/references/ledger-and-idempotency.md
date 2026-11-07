# Ledger and Idempotency: Reference Design

The schema and flow below are portable SQL. They were exercised with SQLite (7 tests: balanced posting, duplicate replay, key reuse with a different body, insufficient-funds rollback, unbalanced-journal refusal, reversal, and balance-equals-entries). Adapt the types and upsert syntax to your database.

## Schema

```sql
CREATE TABLE account (
  id            BIGINT PRIMARY KEY,
  currency      CHAR(3) NOT NULL,
  kind          VARCHAR(20) NOT NULL,          -- user_wallet, merchant, fee, clearing, suspense
  balance_minor BIGINT NOT NULL DEFAULT 0,
  allow_negative BOOLEAN NOT NULL DEFAULT FALSE,
  version       BIGINT NOT NULL DEFAULT 0,
  CHECK (allow_negative OR balance_minor >= 0)
);

CREATE TABLE payment (
  id              BIGINT PRIMARY KEY,
  merchant_id     BIGINT NOT NULL,
  idempotency_key VARCHAR(64) NOT NULL,
  request_hash    CHAR(64) NOT NULL,              -- SHA-256 of the canonical request
  amount_minor    BIGINT NOT NULL CHECK (amount_minor > 0),
  currency        CHAR(3) NOT NULL,
  status          VARCHAR(20) NOT NULL,           -- CREATED, PENDING, UNKNOWN, SUCCEEDED, FAILED, REVERSED
  provider_ref    VARCHAR(64),                    -- generated once, reused on every retry
  response_body   TEXT,                           -- replayed for duplicate requests
  created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (merchant_id, idempotency_key)
);

CREATE TABLE journal (                             -- one business event = one balanced journal
  id          BIGINT PRIMARY KEY,
  payment_id  BIGINT REFERENCES payment(id),
  kind        VARCHAR(20) NOT NULL,                -- PAYMENT, REFUND, REVERSAL, FEE, SETTLEMENT
  reverses_id BIGINT REFERENCES journal(id),
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE entry (                               -- immutable: never UPDATE or DELETE
  id           BIGINT PRIMARY KEY,
  journal_id   BIGINT NOT NULL REFERENCES journal(id),
  account_id   BIGINT NOT NULL REFERENCES account(id),
  amount_minor BIGINT NOT NULL CHECK (amount_minor <> 0),   -- signed: + into the account, - out of it
  currency     CHAR(3) NOT NULL
);

CREATE TABLE outbox (
  id          BIGINT PRIMARY KEY,
  aggregate   VARCHAR(40) NOT NULL,
  aggregate_id BIGINT NOT NULL,
  event_type  VARCHAR(60) NOT NULL,
  payload     TEXT NOT NULL,
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  published_at TIMESTAMP
);
```

Notes:

- `entry.amount_minor` is **signed**: positive means money into the account and negative means out. Each journal sums to zero per currency. This avoids the debit/credit naming confusion between asset and liability accounts. Present debit and credit columns in reports if accountants expect them.
- `account.balance_minor` is a cached projection of `SUM(entry.amount_minor)`, updated in the same transaction. Keep an hourly or daily job that recomputes and alerts on drift.
- Opening balances are journals too (from an equity or funding account), so the invariant `balance = SUM(entries)` holds from day one.
- High-contention accounts, such as one merchant receiving thousands of payments per second, become a hotspot. Shard them into sub-accounts, or append entries and compute balances asynchronously for accounts that may not go negative. Never relax overdraft checks on user wallets to gain throughput.

## Payment Flow (one transaction)

```text
BEGIN
  1. INSERT payment (merchant_id, idempotency_key, request_hash, ..., status='CREATED', provider_ref=new)
       ON CONFLICT (merchant_id, idempotency_key) DO NOTHING
  2. SELECT the row by (merchant_id, idempotency_key)
       - request_hash differs        -> ROLLBACK, return 409 (key reused)
       - row existed, terminal state -> ROLLBACK, replay stored response
       - row existed, in progress    -> ROLLBACK, return 409 retry-later
  3. UPDATE account SET balance_minor = balance_minor - :amt
       WHERE id = :wallet AND balance_minor >= :amt         -- exactly 1 row, or insufficient funds
  4. INSERT journal + balanced entries (wallet -amt, merchant +amt-fee, fee +fee)
  5. UPDATE payment SET status = 'SUCCEEDED', response_body = :resp
  6. INSERT outbox (PaymentSucceeded)
COMMIT
```

For an **external** provider, split the flow at the network call. Never hold a database transaction open across one.

1. Transaction A: insert the payment (`PENDING`, `provider_ref`), reserve funds (move them to a hold account), and write the outbox entry.
2. Call the provider with `provider_ref` as its idempotency key.
3. Transaction B: on success, post the capture journal from hold to merchant; on decline, release the hold; on timeout, set `UNKNOWN` and schedule an inquiry.

## Database-Specific Upserts

| Database | Insert-if-absent on the idempotency key |
|---|---|
| PostgreSQL, SQLite | `INSERT ... ON CONFLICT (merchant_id, idempotency_key) DO NOTHING` |
| MySQL / MariaDB | `INSERT IGNORE ...` (also hides other errors; prefer catching duplicate-key error 1062) or `INSERT ... ON DUPLICATE KEY UPDATE id = id` |
| Oracle | Catch `ORA-00001` on the unique index, or `MERGE ... WHEN NOT MATCHED THEN INSERT` |

## Concurrency Notes

- The conditional `UPDATE ... WHERE balance_minor >= :amt` is safe under the default isolation of PostgreSQL and Oracle (READ COMMITTED) and MySQL InnoDB (REPEATABLE READ). Each takes a row lock and evaluates the predicate against the latest committed version. A read-then-write in application code (`SELECT balance`, compare in Java, then `UPDATE`) is **not** safe without `SELECT ... FOR UPDATE`.
- Transfers that touch two balance rows lock them in ascending account id order.
- Optimistic locking (`version` column) suits low-contention rows. Retry on conflict a bounded number of times with jitter.

## Invariant Queries

```sql
-- Every journal balances per currency
SELECT journal_id, currency FROM entry GROUP BY journal_id, currency HAVING SUM(amount_minor) <> 0;

-- Cached balances match the entries
SELECT a.id FROM account a LEFT JOIN entry e ON e.account_id = a.id
GROUP BY a.id, a.balance_minor HAVING a.balance_minor <> COALESCE(SUM(e.amount_minor), 0);

-- Payments stuck in UNKNOWN beyond the SLA (interval syntax: PostgreSQL/Oracle; MySQL uses NOW() - INTERVAL 15 MINUTE)
SELECT id, provider_ref, created_at FROM payment
WHERE status = 'UNKNOWN' AND created_at < CURRENT_TIMESTAMP - INTERVAL '15' MINUTE;
```

Run them as scheduled checks that page someone, and as assertions in integration tests.

## Testing Checklist

- Property test: random sequences of payments, refunds, and reversals keep every invariant true.
- Fault injection: kill the process or drop the connection after each step of the external flow, then verify recovery ends in a correct terminal state.
- Concurrency: N parallel spends against one wallet never overdraw it, and the successes sum to at most the opening balance.
- Duplicates: the same request, webhook, and event delivered twice or out of order change nothing.
