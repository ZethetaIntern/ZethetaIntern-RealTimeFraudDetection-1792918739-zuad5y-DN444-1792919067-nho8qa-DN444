# OpenTelemetry tracing

- SDK in all services; W3C `traceparent` on gRPC and Kafka headers.  
- Sampler: parent-based; head 10% prod, 100% if `score>=600` or errors (tail-ish via attribute).  
- Custom spans: `rule.eval`, `ml.infer`, `graph.lookup`, `kafka.produce`.  
- Backend: Jaeger; 7-day retention.  
- Every decision log includes `trace_id` for regulator replay.
