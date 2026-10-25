# CI/CD per service

Stages: **source → build → test → scan → stage → canary → production**.

| Stage | Tools |
|---|---|
| Source | GitHub, conventional commits, required review |
| Build | Docker multi-stage, SBOM |
| Test | unit + contract (Buf/OpenAPI) + consumer tests |
| Scan | Trivy/Grype, no critical CVEs |
| Stage | namespace `aegis-staging` soak |
| Canary | Istio weights 5-25-50-100; Kayenta-like compare error, latency, FPR |
| Production | see per-service strategy |

Per-service deploy:

- **ML:** canary (accuracy on live).  
- **Rules:** blue-green (atomic rule set).  
- **Ingestion:** rolling + readiness; drain Kafka consumers.  
- **DB:** expand-contract schema.

Zero message loss sketch: pod `preStop` sleeps 10s after removing from Service; consumer commits offsets only after handler success; HPA min 2; PDB `minAvailable: 2` for rule-engine. During roll, old pods keep processing until new `/healthz` and `/ready` pass (Kafka assigned). Mathematical bound: in-flight ≤ `concurrency × shutdown_timeout`; with acks=all, uncommitted messages remain on topic.
