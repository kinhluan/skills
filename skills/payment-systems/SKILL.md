---
name: payment-systems
description: Design, review, or debug systems that move money, such as wallets, payment gateways, checkout, payouts, refunds, and bank or card integrations. Use for money representation, double-entry ledgers, payment state machines, idempotency keys, timeouts with unknown outcome, retries, webhooks, outbox events, reconciliation, refunds and chargebacks, fraud limits, and PCI DSS scope.
metadata:
  tags: ["payments", "fintech", "ledger", "idempotency", "reconciliation", "pci-dss", "distributed-systems", "security"]
---

# Payment Systems

Payment bugs are paid for in real money, and every one is a security bug. Design for three facts:

1. **Networks fail in the middle.** A timeout means *unknown*, not *failed*.
2. **Everything is delivered at least once.** Requests, webhooks, and events all repeat.
3. **Every movement must be explainable later**, to customers, auditors, and reconciliation.

Regulatory rules vary by country and licence (in Vietnam, the State Bank of Vietnam). Confirm them with the compliance team; this skill covers engineering, not legal advice.

## Money

- Store **integer minor units** plus an **ISO 4217 currency**: `amount_minor BIGINT`, `currency CHAR(3)`. The exponent varies (VND 0, USD 2, KWD 3), so read it from a currency table instead of assuming 2.
- **Never** use binary floating point. In Java use `long` minor units or `BigDecimal` with an explicit scale and `RoundingMode`. Never use `new BigDecimal(double)`.
- Define a rounding rule for each calculation (fees, FX, tax, interest) and **where the remainder goes**. When splitting, allocate the remainder deterministically (largest remainder), so the parts always sum to the whole.
- An FX conversion is two ledger legs with a recorded rate, rate source, and timestamp, not a currency change on one row.

## State Machine

Model each payment as an explicit state machine with guarded transitions and an append-only history:

```text
CREATED ─▶ PENDING ─▶ SUCCEEDED ─▶ (PARTIALLY_)REFUNDED
              │  ▲          └────▶ REVERSED / CHARGED_BACK
              ▼  │
           UNKNOWN ──(inquiry)──▶ SUCCEEDED | FAILED
              │
              └──▶ FAILED / EXPIRED / CANCELLED
```

- Transition with a compare-and-set: `UPDATE payment SET status='SUCCEEDED' WHERE id=? AND status IN ('PENDING','UNKNOWN')`. Zero rows updated means someone else already won; read the row and act on its state.
- Terminal states are terminal. A correction is a new journal, such as a refund or reversal, never an edit.
- Store the provider's raw status and code next to your own normalised status.

## Idempotency

- Each money-moving command carries an **idempotency key**, unique per client scope (`UNIQUE(merchant_id, idempotency_key)`).
- Store a **hash of the canonical request** with the key:

  | Request | Response |
  |---|---|
  | Same key and same body | Replay the stored response |
  | Same key and different body | `409`/`422` conflict |
  | Same key while the first is still in progress | `409`, "retry later" |

- Keep keys at least as long as the longest client retry window, plus reconciliation time.
- Use the **same provider reference** (your outbound idempotency key) on every retry to a downstream provider. Generating a new reference per attempt is how double charges happen.

## Calling Providers: Timeouts and Retries

1. Persist intent **before** the call: status `PENDING` and the `provider_ref`.
2. Call with explicit connect and read timeouts.
3. Handle the outcome:
   - A **definitive response** (success or decline) goes to a terminal state.
   - A **timeout, 5xx, or connection reset** goes to `UNKNOWN`. Do not refund the user, and do not retry with a new reference.
4. Resolve `UNKNOWN` by **status inquiry** (provider query API), with backoff, and then through reconciliation if inquiry is not conclusive.
5. Retry only operations the provider documents as idempotent for the same reference.
6. Bound everything: a maximum number of attempts, a circuit breaker per provider, and an alert when `UNKNOWN` ages past its SLA.

## Ledger

Use a **double-entry ledger**. Every business event writes one journal whose entries sum to zero per currency, and balances are derived from entries.

- Use accounts for every party and purpose: user wallets, merchants, fees, provider clearing, settlement, and suspense.
- Entries are **immutable**. Fix mistakes with a reversal journal that references the original.
- Write the payment row, the journal, the balance update, and the outbox event in **one database transaction**.
- Prevent overdraft atomically: `UPDATE account SET balance = balance - :a WHERE id = :id AND balance >= :a`, then check that exactly one row changed. A `CHECK` constraint backs it up. When locking several accounts, lock them in a consistent order (by id) to avoid deadlocks.
- Continuously verify invariants: each journal sums to zero, `balance = SUM(entries)`, and no orphan entries.

The tested schema and flow are in [ledger-and-idempotency](references/ledger-and-idempotency.md).

## Events and Webhooks

- Publish domain events through a **transactional outbox**; consumers deduplicate by event id. Kafka and RabbitMQ deliver at least once.
- **Inbound webhooks:**
  - Verify the signature (HMAC over the *raw* body, constant-time compare, timestamp tolerance), or use mTLS or an IP allowlist if that is what the provider offers.
  - Respond quickly and process asynchronously.
  - Deduplicate by provider event id.
  - **Treat the payload as a hint.** Fetch the authoritative status from the provider API before moving money.
- Out-of-order delivery is normal. Apply transitions through the state machine, which rejects illegal moves.

## Reconciliation

Reconciliation is how you find the bugs that the design missed.

1. Ingest provider and bank settlement files on schedule, and archive the raw files immutably.
2. Match on provider reference, amount, currency, and date. Classify each break:
   - matched
   - missing internally (money arrived, no record)
   - missing externally (recorded, no money)
   - amount or status mismatch
3. Route unresolved items to a **suspense account**, with an owner and an age-based escalation.
4. Resolve with explicit adjustment journals, never by editing history. Report daily totals and break counts.

## Refunds, Reversals, Chargebacks

- A refund is a new entity and journal, capped at `captured − already_refunded`, idempotent per refund key, and may be partial.
- A reversal or void before settlement differs from a refund after settlement; model both explicitly.
- Chargebacks follow the scheme lifecycle (notification, representment, final). Hold or debit merchant funds according to contract.

## Security and Compliance

Card data, authentication, fraud controls, and audit requirements are in [security-and-compliance](references/security-and-compliance.md). In short:

- Keep primary account numbers (PANs) out of your systems: use hosted fields, an iframe, a redirect, or network tokens.
- Never store CVV or PIN after authorization.
- Strong customer authentication or step-up for risky operations.
- Velocity and amount limits.
- Signed or HSM-held keys.
- An immutable audit log.

## Review Checklist

- [ ] Money stored as integer minor units with a currency; no floats.
- [ ] An idempotency key with a request hash on every money-moving endpoint and outbound call.
- [ ] A timeout leads to `UNKNOWN` and inquiry, never a blind retry or an automatic refund.
- [ ] A double-entry, immutable, balanced ledger written in the same transaction as the state change.
- [ ] Atomic overdraft protection and consistent lock ordering.
- [ ] An outbox for events; idempotent consumers; webhooks verified and confirmed by API.
- [ ] Daily reconciliation, a suspense account, and owned break resolution.
- [ ] Tests for duplicates, timeouts at every step, out-of-order webhooks, partial refunds, and concurrent spends.

## Related Skills

- [database-design](../database-design/SKILL.md) for isolation levels, locking, and schema evolution.
- [ddd-patterns](../ddd-patterns/SKILL.md) for outbox, sagas, and anti-corruption layers to providers.
- [api-security](../api-security/SKILL.md) and [threat-modeling](../threat-modeling/SKILL.md) for endpoint and abuse-case review.
- [security-analysis](../security-analysis/SKILL.md) for code review of payment services.
