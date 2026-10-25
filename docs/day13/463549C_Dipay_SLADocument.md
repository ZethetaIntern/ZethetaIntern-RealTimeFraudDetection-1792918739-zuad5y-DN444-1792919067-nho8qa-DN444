# Formal SLA document

Measurement: Prometheus recording rules, 30-day windows. Error budget = 1 − availability target.

| Path | Availability | Latency | Quality |
|---|---|---|---|
| Authorisation scoring | 99.99% | p50<50ms p95<150ms p99<200ms e2e; detect fan-out p99<100ms | detection >95%, FPR <0.5% |
| Case UI | 99.9% | p99 < 1s | review queue SLA 4h |
| Kafka lag | — | <1000 msgs/partition steady | — |
| ML infer | included in detect | p99 < 10ms | PSI alert 0.25 |
| Graph hot lookup | 99.95% | p99 < 50ms | fallback on timeout |

When error budget exhausted: production deploys frozen except P1. Multi-window burn: 2% budget in 1h → P2; 10% in 1h → P1.
