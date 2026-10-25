# Day-wise deliverable checklist — 463549C

This checklist compares the supplied PDF brief with files present in this repository. **Generated** means a source artifact exists; it does not mean the artifact has been independently validated, deployed, or rendered. **Partial** means some required sub-parts are absent. **Not generated** means no corresponding local artifact exists. Diagrams are provided as editable UML/Mermaid source as requested; rendered images are intentionally omitted.

## Day 1 — Domain immersion

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Glossary (50+ terms) | Generated | `docs/day01/463549C_Dipay_DomainGlossary.md` (60 terms) |
| Legacy monolith analysis: capabilities, integrations, pain points | Generated | `docs/day01/463549C_Dipay_LegacyMonolithAnalysis.md` |
| Initial event storm (events, commands, aggregates) | Generated | `diagrams/day01_event_storming.puml` and `.mmd` |
| Day 1 work log | Generated | `daily-commits/Day01.md` |

## Day 2 — Contexts and service decomposition

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Bounded context map and relationships | Generated | `docs/day02/463549C_Dipay_BoundedContextMap.md` |
| C4 Level 1 system context | Generated (source) | `diagrams/c4_level1_system_context.puml` and `.mmd` |
| Draft C4 Level 2 containers | Generated (source) | `diagrams/c4_level2_container.puml` and `.mmd` |
| Service decomposition table with tech, store, ownership | Generated | `docs/day02/463549C_Dipay_ServiceDecompositionTable.md` |
| Day 2 work log | Generated | `daily-commits/Day02.md` |

## Day 3 — C4, SLAs, persistence

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Final C4 Level 2 with sync/async flows | Generated (source) | `diagrams/c4_level2_container.puml` and `.mmd`; review topic/RPC labels for consistency |
| Four C4 Level 3 component diagrams | Generated (source) | `diagrams/c4_level3_{transaction_ingestion,rule_engine,anomaly_detection,risk_scoring}.puml` |
| Service SLA table incl. p50/p95/p99, availability, throughput, budget, dependencies | Generated | `docs/day03/463549C_Dipay_ServiceSLAs.md` |
| Polyglot persistence rationale | Generated | `docs/day03/463549C_Dipay_PolyglotPersistence.md` |
| Per-hop latency budget | Generated | `docs/day03/463549C_Dipay_LatencyBudget.md` |
| Day 3 work log | Generated | `daily-commits/Day03.md` |

## Day 4 — Kafka topics and schemas

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| At least 8 lifecycle topics with partitions, RF, retention, key, consumers | Generated | `docs/day04/463549C_Dipay_KafkaTopicTopology.md` (10+ topics) |
| Event schemas for lifecycle event types | Generated | `api-specs/avro/` (9 `.avsc` files) |
| Schema Registry compatibility/configuration | Generated | `docs/day04/463549C_Dipay_SchemaRegistry.md` |
| DLQ and replay strategy | Generated | `docs/day04/463549C_Dipay_DLQStrategy.md` |
| Day 4 work log | Generated | `daily-commits/Day04.md` |

## Day 5 — API contracts

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| OpenAPI 3.0 external contract | Generated | `api-specs/openapi.yaml` |
| Internal Protobuf/gRPC contracts | Generated | `api-specs/proto/aegis.proto` |
| Gateway route configuration | Generated | `docs/day05/463549C_Dipay_GatewayRouting.md` |
| Authentication and authorization scheme | Generated | `docs/day05/463549C_Dipay_AuthScheme.md` |
| Day 5 work log | Generated | `daily-commits/Day05.md` |

## Day 6 — Event-driven architecture

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Complete event storm with 50+ events, commands/aggregates | Generated | `docs/day06/463549C_Dipay_EventStorming.md`; diagram source `diagrams/day06_event_storming.puml` |
| Saga orchestration diagrams | Generated (source) | `diagrams/saga_{transaction_processing,fraud_investigation,card_blocking}.puml` |
| CQRS read-model specifications | Generated | `docs/day06/463549C_Dipay_CQRSReadModels.md` |
| Day 6 work log | Generated | `daily-commits/Day06.md` |

## Day 7 — Rule engine

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| YAML rule format and JSON Schema | Generated | `configs/rules/rule.schema.json`, `docs/day07/463549C_Dipay_RuleSchema.md` |
| 20 sample rules | Generated | `configs/rules/sample_rules.yaml` |
| Rule lifecycle state machine | Generated (source) | `diagrams/rule_lifecycle.puml` |
| Simulation and performance monitoring design | Generated | `docs/day07/463549C_Dipay_RuleSimulation.md`, `docs/day07/463549C_Dipay_RulePerformanceMonitoring.md` |
| Day 7 work log | Generated | `daily-commits/Day07.md` |

## Day 8 — ML architecture

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Model serving architecture | Generated | `docs/day08/463549C_Dipay_MLServing.md` |
| Online/offline feature store | Generated | `docs/day08/463549C_Dipay_FeatureStore.md` |
| Model drift/monitoring | Generated | `docs/day08/463549C_Dipay_ModelMonitoring.md` |
| Champion/challenger design | Generated | `docs/day08/463549C_Dipay_ChampionChallenger.md` |
| Day 8 work log | Generated | `daily-commits/Day08.md` |

## Day 9 — Graph analysis

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Graph node/edge/property schema and indexes | Generated | `docs/day09/463549C_Dipay_GraphSchema.md` |
| Five or more Cypher patterns | Generated | `configs/graph/cypher_queries.cypher` |
| Graph synchronization strategy | Generated | `docs/day09/463549C_Dipay_GraphSync.md` |
| Pruning and maintenance | Generated | `docs/day09/463549C_Dipay_GraphPruning.md` |
| Day 9 work log | Generated | `daily-commits/Day09.md` |

## Day 10 — Security and service mesh

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Istio policies/configuration | Generated | `configs/istio/` |
| Service communication matrix | Generated | `docs/day10/463549C_Dipay_ServiceCommunicationMatrix.md` |
| Encryption strategy and key management design | Generated | `docs/day10/463549C_Dipay_EncryptionStrategy.md` |
| PCI DSS / RBI / GDPR mapping | Generated | `docs/day10/463549C_Dipay_ComplianceMapping.md` (requires compliance-owner validation) |
| Day 10 work log | Generated | `daily-commits/Day10.md` |

## Day 11 — API gateway

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Gateway configuration | Generated | `docs/day11/463549C_Dipay_GatewayConfig.md` |
| Five-tier rate limiting | Generated | `docs/day11/463549C_Dipay_RateLimiting.md` |
| Authentication flow UML | Generated (source) | `diagrams/auth_flows.puml`, `diagrams/auth_analyst.puml` |
| Day 11 work log | Generated | `daily-commits/Day11.md` |

## Day 12 — Monitoring

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Four Grafana dashboard specifications | Generated | `configs/grafana/` (four JSON dashboards + README) |
| Prometheus alerting rules | Generated | `configs/prometheus/alerting_rules.yaml` |
| P1/P2 runbooks | Generated | `docs/day12/463549C_Dipay_Runbooks.md` |
| Day 12 work log | Generated | `daily-commits/Day12.md` |

## Day 13 — Observability and SLAs

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Structured logging | Generated | `docs/day13/463549C_Dipay_LoggingSpec.md` |
| OpenTelemetry tracing configuration | Generated | `docs/day13/463549C_Dipay_Tracing.md` |
| Formal SLA specification | Generated | `docs/day13/463549C_Dipay_SLADocument.md` |
| Day 13 work log | Generated | `daily-commits/Day13.md` |

## Day 14 — CI/CD and deployment

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| CI/CD pipeline design | Generated | `docs/day14/463549C_Dipay_CICD.md` |
| Multi-region topology UML | Generated (source) | `diagrams/deployment_topology.puml` |
| DR plan and failover runbook | Generated | `docs/day14/463549C_Dipay_DRPlan.md`, `docs/day14/463549C_Dipay_FailoverRunbook.md` |
| Chaos engineering plan | Generated | `docs/day14/463549C_Dipay_ChaosEngineering.md` |
| Cost estimate | Generated | `docs/day14/463549C_Dipay_CostEstimate.md` |
| Dockerfiles for 2+ services | Generated (sample) | `samples/docker/` |
| Kubernetes Deployment and Service for 2+ services | Generated (sample) | `samples/k8s/rule-engine.yaml`, `samples/k8s/anomaly-detection.yaml` |
| HPA, PDB, and NetworkPolicy for each of 2+ services | Generated (sample) | Rule Engine resources in `samples/k8s/rule-engine.yaml`; Anomaly Detection HPA + NetworkPolicy in `samples/k8s/anomaly-detection-additional-policies.yaml`, PDB in `samples/k8s/anomaly-detection.yaml`. HPA custom metric requires a metrics adapter/exporter. |
| Helm chart (optional bonus) | Not generated | Optional per brief |
| Day 14 work log | Partial | `daily-commits/Day14.md` exists but contains only heading/tag; add substantive decisions/blockers/output summary |

## Day 15 — Final assembly and submission

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Master Architecture Document with navigation/cross references | Generated | `docs/463549C_Dipay_MasterArchitectureDocument.md` |
| Board presentation covering required lenses | Generated | Editable 8-slide PowerPoint `presentation/463549C_Dipay_BoardPresentation.pptx`; companion speaker outline `presentation/463549C_Dipay_BoardPresentation.md` |
| README repository navigation and project summary | Generated | `README.md` |
| Embedded error findings | Generated (candidate review) | `docs/ERROR_DETECTION.md`; brief does not disclose answer locations, findings need owner verification |
| AI acknowledgement | Generated | `docs/AI_USAGE.md` |
| Self-review against seven dimensions / 1000-point rubric | Generated (qualitative) | `docs/day15/463549C_Dipay_RubricSelfReview.md`; brief provides no per-dimension weights |
| Day 15 work log | Generated | `daily-commits/Day15.md` |
| Final PDF export, if required | Not generated | PowerPoint deck is present; PDF export was not requested |

## Additional rubric and case-study coverage

| Item | Status | Location |
|---|---|---|
| Target, Cosmos Bank, Netflix, Wirecard case-study lessons | Not generated | No case-study incorporation file is present; lessons are referenced in README/other design rationale |
| Prototype dashboard/alerts design | Generated | Grafana and Prometheus configs above |
| Rough prototype implementation | Generated | `prototype/app.py`, `prototype/README.md` |
| UML source instead of rendered graphics | Generated | `diagrams/` (`.puml` and `.mmd`) |