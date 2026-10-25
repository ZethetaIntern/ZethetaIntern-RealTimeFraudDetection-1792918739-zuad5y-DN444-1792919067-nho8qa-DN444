# Graph synchronisation

**Chosen strategy: asynchronous** (Kafka `graph.updates` from `transactions.enriched`).  

Justification: sync write 5–15 ms plus lock risk vs 1–5 s staleness. Organised rings persist hours/days; 5 s lag is acceptable. Hot-path **reads** a read replica; if node missing, treat graph score as 0 + small uncertainty (+15) rather than block.

Update logic: MERGE node on hash; MERGE edge; set last timestamps. Idempotent on `transaction_id`.

Read replicas: GDS community jobs on **analytics replica** (minutes); OLTP lookups on **hot replica** with indexes only.
