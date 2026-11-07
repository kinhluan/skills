# Wide-Column and Key-Value Stores

## Cassandra / ScyllaDB: Query-First Modeling

1. List every query the service needs, with its filters, sort order, and page size.
2. Create **one table per query shape**. Duplicating data across tables is expected; keep the copies consistent with a **logged batch** (eventually atomic across tables, but slower: use it for a few related writes, not for bulk loading), or with idempotent asynchronous writers that can be replayed.
3. **Partition key** = what the query filters by equality and what distributes load. **Clustering columns** = the sort order inside the partition.

```sql
-- Query: latest transactions for a user, newest first, one month at a time
CREATE TABLE txn_by_user (
  user_id    bigint,
  month      text,          -- bucket, for example '2026-11', bounds the partition size
  created_at timestamp,
  txn_id     uuid,
  amount     bigint,
  status     text,
  PRIMARY KEY ((user_id, month), created_at, txn_id)
) WITH CLUSTERING ORDER BY (created_at DESC, txn_id ASC);
```

## Rules

- **Bound every partition.** Add a time or hash bucket so no partition grows without limit; large partitions cause latency spikes, repair pain, and memory pressure. Read the large-partition warnings in the node logs and table statistics.
- **Avoid hot partitions.** One celebrity user or one merchant can saturate a replica set; spread it with a bucket suffix.
- **No `ALLOW FILTERING` in production paths.** It scans. If you need the query, you need a table for it.
- **Secondary indexes and materialized views** have consistency and performance caveats that differ between Cassandra and ScyllaDB versions; read the current documentation and load-test before relying on them.
- **Tombstones.** Deletes and TTL expiry write tombstones. Many of them in one partition slow reads and can fail queries (`tombstone_failure_threshold`). Prefer partitions that age out whole, through time buckets plus TTL, over row-by-row deletes. Never use the table as a queue.
- **Lightweight transactions** (`IF NOT EXISTS`, `IF col = ?`) use Paxos with several round trips; reserve them for uniqueness such as idempotency keys, not for every write.
- **Counters** are not idempotent: a retried increment can double count. Do not use them for money.
- **Consistency levels.** Use `LOCAL_QUORUM` for reads and writes for read-your-writes within one datacenter. Choose per query and document it.
- **Idempotent writes.** Make writes upserts with a deterministic primary key, so driver retries and replays are harmless. Mark statements idempotent in the driver only when they truly are.
- **Time.** Last-write-wins uses timestamps, so clock skew can silently lose writes. Run NTP everywhere, and avoid read-modify-write patterns.

## Redis

- Use it as a **cache or ephemeral store**. Design for it to be emptied at any time: data can be rebuilt from the source of truth, and the eviction policy (`maxmemory-policy`) is set deliberately.
- **Keys:** use namespaced names (`svc:entity:{id}:field`), a TTL on every cache key, and jitter on TTLs to avoid stampedes. Use hash tags `{...}` only to co-locate keys in Redis Cluster.
- **Cache-aside** with a stampede guard: single-flight or a short lock on miss, or stale-while-revalidate.
- **Atomicity:**
  - Use `MULTI`/`EXEC`, or a Lua script or Function, for multi-key changes on one node.
  - Rate limiting is atomic with `INCR` plus `EXPIRE` in one script.
  - Distributed locks need a lease (`SET key value NX PX ttl`), a unique value checked on release, and **fencing tokens** at the protected resource.
- **Security:**
  - Require authentication with ACL users per application, and TLS.
  - Never expose it to untrusted networks.
  - Disable or rename dangerous commands (`FLUSHALL`, `CONFIG`, `KEYS`) for application users.
- **Large values and `KEYS *`** block the single-threaded command loop; use `SCAN` and keep values small.
