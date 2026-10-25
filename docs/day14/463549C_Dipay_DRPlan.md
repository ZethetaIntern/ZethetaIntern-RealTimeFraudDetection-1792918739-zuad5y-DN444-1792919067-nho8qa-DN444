# Disaster recovery

| Tier | Services | RPO | RTO | Replication |
|---|---|---|---|---|
| 1 | ingest, rules, risk, audit produce | < 1 min | < 5 min | PG sync in-region; Kafka RF=3; DR async + MM2 |
| 2 | case, notify, analytics, graph writer | < 15 min | < 30 min | async |
| 3 | reporting, admin | < 1 h | < 4 h | snapshots |

Primary Mumbai, secondary Singapore. DNS health checks 30s. Failover authorised by on-call **plus** CTO for planned, on-call alone if P1 region dead 5 min.
