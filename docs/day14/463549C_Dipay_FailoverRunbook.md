# Failover runbook

1. **Detect:** synthetic auth probe fail 3 consecutive + region health.  
2. **Decide:** P1 channel; if Mumbai control plane dead, auto Route53.  
3. **Execute:** promote PG replica (Tier 1 accept RPO seconds); switch Kafka consumers to MM2 translated offsets; scale DR HPA from warm 20% to 100%.  
4. **Verify:** p99, TPS, decision distribution vs 10-min baseline.  
5. **Rollback:** only after Mumbai healthy 60 min and CRO ok; reverse MM2.

Cardholder impact: brief STEP_UP bias during degraded graph (safety margin).
