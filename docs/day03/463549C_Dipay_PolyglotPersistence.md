# Polyglot persistence justification

| Store | Owner | Why | Consistency |
|---|---|---|---|
| PostgreSQL | Ingestion, Profile, Rules, Cases, Scoring, Reference, Audit index | ACID for financial writes, JSONB for explanations, mature backups | Strong on write path |
| Redis | Features, velocity, rate limits, compiled rules | Sub-ms GET, atomic INCR, TTL windows | Strong for counters; eventual for profile replica |
| Neo4j | Graph | Index-free adjacency, Cypher, GDS (Louvain, PageRank) | Near-real-time async (+1–5 s) with daily reconcile |
| TimescaleDB | Integrity monitor, some analytics | Time partitioning, high ingest of switch/CBS logs | Eventual minutes |
| Elasticsearch | Logs, case full-text | Inverted index | Eventual |
| Kafka log | Audit source of truth | Immutable, infinite retention topic `audit.events` | Append-only |
| Amazon QLDB or equivalent hash-chain table | Audit verify | Merkle/document hash API for regulators | Strong append |

**Rejected:** one shared Oracle (monolith failure mode). **Rejected:** 2PC across services.

Graph **asynchronous** update chosen: 5–15 ms sync would blow the 100 ms detect budget under Louvain-adjacent writes. Staleness window 1–5 s; reconciliation job daily. High-risk cards can opt into sync lookup of last-write-cache in Redis.

Strongly consistent: decision for txn T uses features as of T’s enrich event and rule cache version stamped on the explanation.  
Eventually consistent: dashboards (≤ 5 s), profiles (≤ 5 s), graph (≤ 5 s).
