# Rule performance monitoring

Grafana panel per `rule_id`: trigger rate, TP rate, FP rate, p99 eval latency, skip rate (timeout).

Alerts: P3 if FPR +20% vs 7-day baseline; P2 if eval p99 > `max_evaluation_time_ms`. Auto-suggest deprecate when TP=0 for 14 days and trigger rate > 0.1%.
