# Runbooks (P1 / P2)

Routing: P1 PagerDuty + escalate 5 min; P2 Slack #alerts 30 min; P3 email digest; P4 weekly.

## P1 Pipeline down

**Symptoms:** `up{txn-ingestion}=0` or auth timeouts from networks.  
**Diagnose:** k8s pods, Kafka ISR, PG primary.  
**Remediate:** fail over ingestion HPA; if region dead, DNS failover Mumbai → Singapore (see DR).  
**Fallback:** networks retry; do **not** auto-approve globally. If scoring dead but ingest live, rule-only conservative threshold (approve < 100).  
**Escalate:** CTO after 5 min.

## P1 Detection rate < 80%

**Symptoms:** confirmed fraud slipping.  
**Diagnose:** rule deploy, model canary, watchlist empty, graph replica lag.  
**Remediate:** rollback last rule/model; widen VEL-001 temporarily in shadow then activate.  
**Escalate:** CRO.

## P1 Data-breach indicators

Vendor API at 3am, mass GET. Disable that Kong credential; rotate. Target-style correlation may already have opened a composite incident.

## P2 Latency SLA 5 min

Trace Jaeger p99; look for graph 50 ms timeout; shed graph first.

## P2 Kafka lag > 10k

Scale consumer group; check poison DLQ.

## P2 Single service error > 1%

Circuit open? Roll back that Deployment.
