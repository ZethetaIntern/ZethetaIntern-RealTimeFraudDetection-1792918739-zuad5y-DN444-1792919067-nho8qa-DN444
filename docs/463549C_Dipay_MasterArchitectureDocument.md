# Aegis Real-Time Fraud Detection — Master Architecture Document

**Candidate:** Dipay · **Status:** Architecture proposal and rough prototype  

## Contents

1. [Executive summary](#1-executive-summary)
2. [Business problem and objectives](#2-business-problem-and-objectives)
3. [Proposed architecture](#3-proposed-architecture)
4. [Transaction and decision flow](#4-transaction-and-decision-flow)
5. [Data, contracts, and persistence](#5-data-contracts-and-persistence)
6. [Detection and explainability](#6-detection-and-explainability)
7. [Security, resilience, and compliance](#7-security-resilience-and-compliance)
8. [Operations, migration, and recovery](#8-operations-migration-and-recovery)
9. [Prototype scope](#9-prototype-scope)
10. [Economics, risks, and open decisions](#10-economics-risks-and-open-decisions)
11. [Day-wise artifact index](#11-day-wise-artifact-index)

## 1. Executive summary

Aegis is a proposed event-driven fraud decision platform for ShieldPay. It decomposes the legacy transaction-processing monolith into independently deployable services and combines deterministic rules, anomaly/ML signals, and entity-graph signals. The design target is p99 ≤ 100 ms for detection fan-out and p99 ≤ 200 ms end-to-end authorization; these are objectives, not measured results. Every decision should include score components and reason codes and produce durable audit evidence.

## 2. Business problem and objectives

The brief describes 2.4 million transactions/day, a 15-minute batch scoring gap, and a rise in quarterly losses from ₹12 crore to ₹53 crore during a period when fraud attempts rose 340%. Aegis aims to close the scoring gap while reducing false positives and improving investigator and regulator traceability. Target metrics in the design are >95% detection and <0.5% false positive rate; measurement requires labelled production data and controlled rollout.

## 3. Proposed architecture

The design uses 12 bounded contexts/services: Transaction Ingestion; Enrichment & Customer Profile; Reference Data; Fraud Rule Evaluation; Anomaly Detection; Graph Analysis; Risk Scoring; Case Management; Notification; Audit & Compliance; Alert Correlation & Containment; and Integrity & Channel Monitoring. Each context owns its persistence and communicates through versioned APIs or events. Kong/API Gateway fronts external APIs; Istio provides service identity and traffic policy; Kafka is the asynchronous event backbone.

### UML source references

- [C4 Level 1 system context](../diagrams/c4_level1_system_context.puml)
- [C4 Level 2 containers](../diagrams/c4_level2_container.puml)
- [C4 Level 3 component views](../diagrams/c4_level3_transaction_ingestion.puml), [rules](../diagrams/c4_level3_rule_engine.puml), [anomaly](../diagrams/c4_level3_anomaly_detection.puml), [risk scoring](../diagrams/c4_level3_risk_scoring.puml)
- [Event Storming (initial)](../diagrams/day01_event_storming.puml) and [expanded](../diagrams/day06_event_storming.puml)
- [Transaction saga](../diagrams/saga_transaction_processing.puml), [investigation saga](../diagrams/saga_fraud_investigation.puml), [card blocking saga](../diagrams/saga_card_blocking.puml)
- [Deployment topology](../diagrams/deployment_topology.puml)

These are source files; no rendered graphic is included.

## 4. Transaction and decision flow

1. A channel submits an authorization request. Ingestion validates and normalises it, tokenises PAN, assigns correlation identifiers, and records the event using an outbox pattern.
2. Enrichment adds device, geography, BIN/MCC, customer profile, and velocity features.
3. Rule, anomaly, and graph services evaluate in parallel with bounded deadlines. Missing optional signals use documented fallbacks and are represented in the decision explanation.
4. Risk Scoring combines signals into a 0–1000 score and applies market/channel policy: 0–199 approve; 200–599 step up; 600–799 manual review; 800–1000 decline.
5. Decisions publish events for notification, case management, audit, alert correlation, and CQRS views.

## 5. Data, contracts, and persistence

Kafka topics and consumer groups are specified in [Day 4 topology](day04/463549C_Dipay_KafkaTopicTopology.md); Avro records are under [`api-specs/avro`](../api-specs/avro/). External REST contracts are in [`api-specs/openapi.yaml`](../api-specs/openapi.yaml), with internal gRPC definitions in [`api-specs/proto/aegis.proto`](../api-specs/proto/aegis.proto). PostgreSQL supports transactional records, Redis supports online features/counters, Neo4j supports relationship queries, and time-series/search stores support operational analysis. See [persistence rationale](day03/463549C_Dipay_PolyglotPersistence.md).

## 6. Detection and explainability

Versioned rules provide deterministic controls; ML/anomaly serving adds behavioural signals with feature freshness and drift monitoring; graph analysis identifies shared infrastructure and suspicious paths. The final record retains component scores, rule IDs, feature attributions where available, graph evidence references, model/rule versions, trace ID, and final action. Shadow evaluation and champion/challenger comparisons precede promotion.

## 7. Security, resilience, and compliance

The proposal uses PAN tokenisation, encryption in transit and at rest, secrets/key management, mTLS, least privilege, rate limits, auditable configuration changes, and jurisdiction-aware data retention. The compliance mapping is a design aid and requires review by qualified security/compliance owners against current PCI DSS, RBI/FIU-IND, and GDPR obligations. Circuit breakers, bulkheads, bounded retries, idempotent consumers, DLQs, and explicit fallback policies reduce cascading failures. See [`docs/day10`](day10/).

## 8. Operations, migration, and recovery

The migration follows Strangler Fig: introduce an anti-corruption layer, compare shadow decisions, route a small canary share, then expand only when latency, fraud outcome, and operational gates pass. Prometheus/Grafana, structured logs, trace propagation, runbooks, error budgets, CI/CD, multi-region DR, and chaos exercises are documented in Days 12–14. Recovery objectives and failover require rehearsal before production use.

## 9. Prototype scope

[`prototype/`](../prototype/README.md) is a single-process Python HTTP sketch with toy rules, a placeholder anomaly heuristic, and a stub graph signal. It has no durable state, real model, broker, authentication, or production controls. Its outputs are not model performance evidence.

## 10. Economics, risks, and open decisions

The existing order-of-magnitude estimate is approximately $83k/month assuming AWS ap-south-1 and a 50k TPS peak sizing target. It needs workload validation and current provider quotes. Key risks: latency under burst load, false positives and customer friction, stale graph/features, model drift, data residency, migration parity, and dependency outages. Open decisions include final jurisdiction-specific retention, provider contracts, validated capacity, exact fallback policy per channel, and final rendered submission format.

## 11. Day-wise artifact index

See [`DELIVERABLE_CHECKLIST.md`](../DELIVERABLE_CHECKLIST.md) for the full requirement-by-requirement status and locations. The source pack includes days 1–15 in varying completion states; missing Day 15 assets have been added, while external repository transfer and rendered PDF/slide output remain candidate steps.
