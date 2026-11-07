# Relational Design Details

## Isolation Levels and Anomalies

| Anomaly | Example | Prevented by |
|---|---|---|
| Lost update | Two requests read stock 10, both write 9 | Atomic `UPDATE stock = stock - 1 WHERE stock > 0`, `SELECT ... FOR UPDATE`, or a `version` check |
| Write skew | Two doctors each check "another doctor is on call", and both go off call | A true `SERIALIZABLE` level, a constraint, or locking the rows *read* (`FOR UPDATE`) |
| Phantom | A count check passes, then a concurrent insert breaks the rule | A unique or exclusion constraint, a serializable level, or a lock on a parent row |
| Non-repeatable read | The same row read twice in a report gives different values | REPEATABLE READ or snapshot, or read once |

Engine defaults and caveats:

| Engine | Default | Caveat |
|---|---|---|
| PostgreSQL | READ COMMITTED | `SERIALIZABLE` is true serializable snapshot isolation (SSI); retry on `40001` |
| MySQL InnoDB | REPEATABLE READ | Plain `SELECT` reads a snapshot, while `UPDATE` and locking reads see the latest committed row; gap locks can deadlock |
| Oracle | READ COMMITTED | `SERIALIZABLE` is snapshot isolation and **still allows write skew**; retry on `ORA-08177` |

Rule: when correctness depends on a read, either encode the rule as a constraint, or lock what you read.

## Locking Patterns

- **Atomic conditional update.** `UPDATE t SET qty = qty - :n WHERE id = :id AND qty >= :n`, then require exactly 1 updated row. This is the simplest correct pattern.
- **Pessimistic.** `SELECT ... FOR UPDATE` (add `NOWAIT` or `SKIP LOCKED` for queues), in a consistent order.
- **Optimistic.** `UPDATE ... SET version = version + 1 WHERE id = :id AND version = :v`; zero rows means a conflict, so reload and retry.
- **Work queues.** `SELECT ... FOR UPDATE SKIP LOCKED LIMIT n` (PostgreSQL, MySQL 8, Oracle) lets several workers claim rows without blocking each other.
- **Advisory or distributed locks** only with a lease or timeout and a fencing token. A lock without fencing does not protect writes after a pause.

## Index Design

- **Equality columns first, then range, then sort.** For `WHERE tenant_id = ? AND status = ? AND created_at > ? ORDER BY created_at`, use `(tenant_id, status, created_at)`.
- **Covering indexes** remove the table lookup: `INCLUDE (amount)` in PostgreSQL, or trailing columns in a MySQL or Oracle composite index.
- **Partial or filtered indexes** shrink hot sets: `CREATE INDEX ... WHERE status = 'PENDING'` (PostgreSQL). Oracle has no direct equivalent: index a function that returns NULL for rows to exclude.
- **Uniqueness that ignores deleted rows:** a partial unique index (PostgreSQL), a unique index on a generated column (MySQL), or a function-based unique index (Oracle).
- **Keyset pagination with a row-value comparison** `(created_at, id) < (:t, :id)` works in PostgreSQL, MySQL, and SQLite. Oracle needs `created_at < :t OR (created_at = :t AND id < :id)`.
- Watch for low-selectivity leading columns, functions on indexed columns (`WHERE LOWER(email) = ?` needs a function index), implicit type casts, and leading-wildcard `LIKE '%x'`.

## Keys

| Option | Pros | Cons |
|---|---|---|
| `BIGINT` identity or sequence | Compact, ordered, fast joins | Reveals volume and order; needs the database to issue it |
| UUIDv7 (RFC 9562) | Generated anywhere, time-ordered, good B-tree locality | 16 bytes; embeds a creation timestamp |
| UUIDv4 | Generated anywhere, unguessable | Random inserts fragment clustered indexes |
| Natural key | Meaningful | Changes in real life and leaks business data |

Store UUIDs as native `uuid` (PostgreSQL), `BINARY(16)` (MySQL), or `RAW(16)` (Oracle), not as 36-character strings. Never use any identifier as an authorisation check; an unguessable id is not access control.

## Online Schema Changes

| Engine | Online tools and options |
|---|---|
| PostgreSQL | `CREATE INDEX CONCURRENTLY`; `ADD COLUMN` with a constant default is metadata-only (11+); `ADD CONSTRAINT ... NOT VALID`, then `VALIDATE CONSTRAINT`; set `lock_timeout` on every DDL |
| MySQL 8 | `ALGORITHM=INSTANT` or `INPLACE, LOCK=NONE` where supported; `gh-ost` or `pt-online-schema-change` for large tables |
| Oracle | `CREATE INDEX ... ONLINE`; `DBMS_REDEFINITION` for table restructuring; Edition-Based Redefinition for application cut-over |

Practices:

- Run DDL with a lock timeout and retries, because a migration blocked behind a long transaction blocks everyone behind *it*.
- Backfill in batches of about 1–10k rows, commit each batch, sleep between batches, and checkpoint progress so the job can resume.
- Rename in two steps: add the new column, dual-write and backfill, switch reads, then drop the old column.

## Partitioning and Retention

- Partition large append-heavy tables by time (range) to make retention a cheap `DROP` or `TRUNCATE PARTITION` instead of a long `DELETE`.
- Partition pruning needs the partition key in the query predicate. Global uniqueness across partitions usually requires the key to include the partition column.
- Shard only after vertical scaling, read replicas, partitioning, and archiving are exhausted. Choose a shard key that matches the dominant access path, such as `tenant_id` or `user_id`.
