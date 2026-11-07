---
name: database-design
description: Design, review, or evolve database schemas and data access for relational (PostgreSQL, MySQL, Oracle) and wide-column or key-value stores (Cassandra, ScyllaDB, Redis). Use for data modeling, choosing keys, constraints and indexes, transaction isolation and locking, zero-downtime migrations, multi-tenancy, row-level security, encryption of sensitive columns, retention, and backup and recovery.
metadata:
  tags: ["database", "data-modeling", "sql", "cassandra", "indexing", "migrations", "transactions", "data-security"]
---

# Database Design

Data outlives code. Design the schema for the **queries, invariants, and failure modes** you must survive, not for the object model of the current service.

## 1. Start From Access Patterns and Invariants

Before drawing tables, write down:

| Item | Example |
|---|---|
| Entities and owners | `payment` is owned by Payments; only that service writes it |
| Invariants | A wallet balance is never negative; one active subscription per user |
| Queries and frequencies | "Last 20 transactions by user": 5k req/s, p99 < 20 ms |
| Write rates and growth | 50M rows/month, kept for 10 years |
| Consistency needs | Strong for balances; eventual for analytics |
| Sensitivity and retention | Phone number is PII; logs kept 90 days |

Then choose the store:

- **Relational** when invariants span rows, queries are varied, or you need transactions. This is the default.
- **Wide-column** (Cassandra/Scylla) when you need very high write throughput, multi-region availability, and the queries are known in advance and few.
- **Key-value or cache** (Redis) for derived, rebuildable data, sessions, rate limits, and locks with leases. It is never the only copy of money or other critical state.

## 2. Relational Modeling Rules

- **Normalise first** (to 3NF), then denormalise deliberately: add a measured read model or a cached projection, with the owner of its freshness written down.
- **Enforce invariants in the database:** `NOT NULL`, `CHECK`, `UNIQUE` (including partial or filtered unique indexes), and foreign keys inside a service boundary. Application checks alone race.
- **Keys:**
  - Use a surrogate primary key: `BIGINT` identity, or **UUIDv7** (RFC 9562, time-ordered) when ids are generated outside the database or must not be guessable in sequence.
  - Avoid random UUIDv4 as a clustered key on InnoDB, Oracle IOTs, and SQL Server, because random inserts fragment the B-tree.
  - Keep natural keys (e-mail, order number) as `UNIQUE` constraints, not as the primary key.
- **Types:**
  - Exact numerics for money (integer minor units or `DECIMAL`).
  - `TIMESTAMP WITH TIME ZONE`, or UTC by convention, for instants.
  - Check constraints or lookup tables for enums. Avoid database `ENUM` types that need a migration to extend.
- **Audit columns:** `created_at`, `updated_at`, and, where useful, `created_by` and a `version` column for optimistic locking.
- **Soft delete** only with a reason. It complicates every unique constraint and query; prefer archive tables, or a status with partial indexes.

Index design, isolation anomalies, and locking are in [relational](references/relational.md).

## 3. Indexes

- Index for the **actual query plans** of hot queries. Verify with `EXPLAIN` (or `EXPLAIN ANALYZE`) on production-like data volumes.
- In a composite index, put the most selective equality columns first, then the range or sort column. Add `INCLUDE` or covering columns to avoid table lookups for hot reads.
- Every foreign key used in joins or cascades needs an index on the child side.
- Each index slows writes and uses memory, so remove unused indexes using the database's usage statistics.
- Use keyset pagination (`WHERE (created_at, id) < (:t, :id) ORDER BY created_at DESC, id DESC LIMIT 20`), not a large `OFFSET`.

## 4. Transactions and Concurrency

- Know your engine's **default isolation** and what it permits. Lost updates and write skew are the bugs that reach production.
- Make check-then-act atomic. Use a conditional `UPDATE ... WHERE`, `SELECT ... FOR UPDATE`, a unique constraint, or serializable isolation with retry.
- Keep transactions short. Never hold one open across a network call or user think time.
- Lock in a consistent order; retry deadlocks and serialization failures with bounded attempts and jitter.

## 5. Schema Evolution Without Downtime

Use **expand → migrate → contract**:

1. **Expand.** Add nullable columns or new tables, and create indexes online. Old code keeps working.
2. **Dual-write or backfill.** Deploy code that writes both shapes. Backfill in small batches with throttling and resumable checkpoints.
3. **Switch reads** behind a flag, and verify with comparison queries.
4. **Contract.** Drop old columns only after every running version has stopped using them, at least one release later.

Make migrations versioned, reviewed, and idempotent (Flyway or Liquibase for the JVM). Never edit an applied migration. Engine-specific online DDL tools are listed in [relational](references/relational.md#online-schema-changes).

## 6. Wide-Column Stores (Cassandra / ScyllaDB)

Model **one table per query**: the partition key answers "which partition", and the clustering columns answer "in what order". Bound partition size with time buckets. Avoid `ALLOW FILTERING`, unbounded partitions, and tombstone-heavy delete patterns. Use lightweight transactions sparingly. Details are in [wide-column](references/wide-column.md).

## 7. Security and Privacy

- **Least privilege:**
  - Separate credentials for migration (DDL), application (DML on its own schema), and read-only reporting.
  - No application connects as the owner or superuser.
  - Credentials come from a secret manager and are rotated.
- **Injection:** parameterised queries only. Where identifiers must be dynamic (sort column, table name), map them through an **allow list**; bind parameters cannot replace identifiers.
- **Multi-tenancy:**
  - Choose shared tables with a `tenant_id`, schema-per-tenant, or database-per-tenant, deliberately.
  - With shared tables, put `tenant_id` in every key and index, and enforce it with **row-level security** (PostgreSQL RLS, Oracle VPD) or a mandatory repository filter, plus tests that try cross-tenant reads.
- **Sensitive columns:**
  - Classify the data. Encrypt PII and secrets at the application level or with column encryption, with keys in a KMS.
  - Use deterministic encryption, or a keyed hash (HMAC) column, only where equality search is needed.
  - Never put secrets in plaintext columns or logs.
- **Encryption** in transit (TLS with certificate verification) and at rest (storage or TDE).
- **Auditing:** log privileged and DDL operations. Keep audit records outside the reach of the audited account.
- **Retention and erasure:** a TTL or purge job per data class. For personal-data deletion requests, know every copy: replicas, caches, search indexes, backups, and analytics.

## 8. Operations

- **Backups:** automated full backups plus a log or WAL archive for point-in-time recovery, copied to another account or region and encrypted. **Restore drills** happen on a schedule; an untested backup is a hope, not a backup.
- Define an RPO and RTO per database, and design replication and failover to meet them.
- Monitor slow queries, lock waits, replication lag, connection-pool saturation, table and index bloat, and disk growth.
- Capacity: connection pools sized to the database's limits, and partitioning or sharding planned before the largest table hits operational limits.

## Review Output

1. **Access patterns and invariants**, and how the schema enforces each.
2. **Schema** (DDL or ER diagram) with keys, constraints, and indexes justified by queries.
3. **Concurrency** risks and the chosen protection.
4. **Migration plan** (expand, migrate, contract) with rollback.
5. **Security**: roles, tenancy enforcement, encrypted columns, retention.
6. **Operations**: backup, PITR, RPO/RTO, and monitoring.

## Related Skills

- [payment-systems](../payment-systems/SKILL.md) for ledgers and idempotency tables.
- [ddd-tactical](../ddd-tactical/SKILL.md) and [ddd-patterns](../ddd-patterns/SKILL.md) for aggregate boundaries and outbox.
- [c4-level4-code](../c4-level4-code/SKILL.md) for ER diagrams.
- [security-analysis](../security-analysis/SKILL.md) for injection and data-exposure review.
