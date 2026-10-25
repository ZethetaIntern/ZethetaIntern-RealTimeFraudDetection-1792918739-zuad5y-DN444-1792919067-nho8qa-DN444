# CQRS read models

Write side: detection pipeline (strong). Read side: Kafka Streams / ksqlDB materialised views.

| View | Source topics | Logic | Sink | Freshness |
|---|---|---|---|---|
| Real-time fraud stats | fraud.decisions | Tumbling 1h window: count by action, channel, market | PG `mv_fraud_stats_hourly` + compact topic | ≤ 5 s |
| Geo heatmap | fraud.alerts + enriched country | Count fraud attempts by region each 1 min | Redis GEO + PG | 1 min |
| Rule effectiveness | RuleEvaluationResult + case outcomes | Per rule_id: trigger, TP, FP, rates | PG `mv_rule_perf` | daily join to labels; intra-day triggers real-time |
| Model performance | AnomalyScore + chargebacks | AUC/precision/recall/F1 per model_version | PG `mv_model_perf` | daily (labels lag 30–90 d) |
| Case backlog | CaseEvent | Open by priority, assignee, avg age | PG `mv_case_backlog` | ≤ 5 s |

ksqlDB sketch:

```sql
CREATE TABLE mv_fraud_stats_hourly WITH (kafka_topic='cqrs.fraud_stats', value_format='AVRO') AS
  SELECT action, channel, WINDOWSTART as hour,
         COUNT(*) as n
  FROM decisions
  WINDOW TUMBLING (SIZE 1 HOUR)
  GROUP BY action, channel;
```

Analytics queries never hit the authorisation PostgreSQL primaries.
