# Feature store

Two tiers (Feast-like, implemented with Spark + Redis).

## Batch (daily Spark → PostgreSQL → Redis midnight sync)

- avg_amount_30/60/90d, txn_frequency, top10 merchants, typical hours, home geo, card_age  
- historical_pos_share, mcc histogram

## Real-time (Kafka Streams on `transactions.enriched` → Redis TTL)

- counts 1/5/10/30/60 min  
- amount sum 1/6/12/24 h  
- distinct merchants 1 h, distinct countries 24 h  
- km from last txn / home  
- device match score, is_proxy  

gRPC `GetFeatures` p99 < 1 ms (Redis MGET). If Redis miss: population averages + `degraded_features=true` (Netflix fallback).
