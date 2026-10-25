# Grafana dashboard specifications

JSON in this folder is a **spec** (panel list + queries), not a full Grafana export. Recreate in Grafana Cloud using Prometheus datasource `aegis`.

Dashboards:

1. `transaction_processing.json` — TPS, p50/p95/p99, approve/decline mix, gateway 429s  
2. `fraud_detection.json` — detection rate, FPR, rule triggers, PSI, graph hops  
3. `case_management.json` — open cases, SLA 4h, assignee load  
4. `infrastructure.json` — CPU/mem, Kafka lag, Neo4j, Redis hit rate, HPA replicas  
