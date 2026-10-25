# Graph pruning and maintenance

- Drop TRACTED_WITH / USED_IP edges older than **180 days** to cold S3 dump nightly.  
- Keep SHARED_* edges 365 days (ring evidence).  
- Daily reconcile: sample 1% of cards from PG vs Neo4j; repair missing edges; P3 if mismatch > 0.5%.  
- Indexes rebuilt on analytics replica, swapped.
