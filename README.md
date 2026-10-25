# ShieldPay Real-Time Fraud Detection Platform

**Working title:** Real-Time Fraud Detection Microservices Architecture  
**Role simulated:** Platform Architect, ShieldPay Financial Services  
**Sprint:** 15 days — AI-driven system design & architecture  

This repository contains a 15-day architecture pack for a proposed production-grade, event-driven fraud platform. It documents a design that decomposes ShieldPay’s 2012 Java monolith into independently deployable services for card, UPI, ATM, and e-commerce transaction risk decisions using **rules**, **anomaly detection**, and **graph relationship analysis**. The documents and sample configurations are design artifacts.

---

## What this project is

ShieldPay processes **2.4 million transactions per day** across India, Southeast Asia, and the Middle East. In Q3 2025 fraud attempts rose **340%** (synthetic identities, a 12-million-card aggregator breach, and exploitation of a 15-minute batch scoring gap). Quarterly fraud losses moved from **₹12 crore to ₹53 crore**. The board asked for a re-architecture that:

- Scores the **critical path** (ingest → enrich → detect → decide) with a **p99 latency budget** (see latency hunter notes: the brief cites both 100 ms and 200 ms; the design treats **p99 ≤ 100 ms for gRPC detection hops** and **p99 ≤ 200 ms end-to-end**, documented as a brief inconsistency in `docs/ERROR_DETECTION.md`).
- Combines deterministic rules, ML, and graph signals into a **0–1000 risk score** with SHAP/LIME-style explanations.
- Survives individual service failure (Netflix-style fallbacks) instead of failing open or failing closed blindly.
- Meets **PCI DSS v4.0**, **RBI fraud / STR**, and **GDPR** at the same time, with jurisdiction-based retention.
- Migrates from the monolith using **Strangler Fig** plus an **anti-corruption layer**.

The platform is named **Aegis** internally (ShieldPay’s real-time decision fabric). External REST is versioned under `/api/v1`.

---

## How the system works (short)

1. Payment channels (Visa / Mastercard / RuPay, UPI, ATM switch, e-commerce gateways) post or stream a transaction.
2. **Transaction Ingestion** normalises the payload, tokenises PAN, assigns `trace_id`, and publishes `transactions.raw`.
3. Enrichment adds device, geo, BIN, MCC, and customer-profile features; publishes `transactions.enriched`.
4. **Rule Engine**, **Anomaly Detection**, and **Graph Analysis** run in parallel on the critical path (gRPC) with Kafka as the audit/event backbone.
5. **Risk Scoring** aggregates weighted signals, applies channel/market thresholds, and emits approve / step-up / review / decline.
6. **Notification**, **Case Management**, and **Audit** consume decisions. High-confidence multi-terminal malware patterns auto-correlate (Target 2013 lesson). Geographic velocity and SWIFT anomaly monitors cover Cosmos Bank 2018 patterns. Audit events are hash-chained (Wirecard 2020 lesson).

---

## Work completed in this repository

Days 1–15 have design artifacts in Markdown, YAML, JSON, Avro, Protobuf, PlantUML, and Mermaid, with a few Day 15 and deployment-format gaps tracked explicitly. A **rough prototype** under `prototype/` shows a single-process pipeline (rules + simple anomaly heuristic + in-memory graph) so the scoring path can be exercised without Kafka or Kubernetes.

| Area | What was produced |
|---|---|
| Domain | 50+ term glossary, monolith capability map, pain points |
| Architecture | 12 bounded contexts, C4 L1–L3, SLA + latency budget |
| Communication | 10 Kafka topics, Avro schemas, OpenAPI + gRPC, 3 sagas, CQRS views |
| Detection | JSON Schema rules + 20 samples, ML serving + feature store, Neo4j schema + Cypher |
| Security / ops | Istio policies, PCI mapping, rate limits, Grafana/Prometheus, logging/tracing |
| Run | CI/CD, multi-region DR, chaos experiments, cost model |
| Tracking | `DELIVERABLE_CHECKLIST.md` — required vs generated per day |


---

## Repository map

```
README.md
DELIVERABLE_CHECKLIST.md
docs/                  design documents + Master Architecture Document
diagrams/              PlantUML (.puml) and Mermaid (.mmd) sources
api-specs/             OpenAPI YAML, Protobuf, Avro
configs/               rules, Istio, Prometheus, Grafana, graph Cypher
samples/               Dockerfiles and Kubernetes manifests (2 services)
presentation/          Risk & Technology Board slide outline
daily-commits/         per-day work logs and decisions
prototype/             rough Python implementation
```

Start here after the README:

1. [Deliverable checklist](DELIVERABLE_CHECKLIST.md)
2. [Master Architecture Document](docs/463549C_Dipay_MasterArchitectureDocument.md)
3. [Board presentation deck](presentation/463549C_Dipay_BoardPresentation.pptx) and [speaker outline](presentation/463549C_Dipay_BoardPresentation.md)
4. [Embedded error findings](docs/ERROR_DETECTION.md)
5. [Rubric self-review](docs/day15/463549C_Dipay_RubricSelfReview.md)
6. [Prototype](prototype/README.md)

---

## Services (12)

| Service | Store | Role |
|---|---|---|
| Transaction Ingestion | PostgreSQL | Normalise, tokenise, publish raw events |
| Enrichment & Customer Profile | PostgreSQL + Redis | Device, geo, behavioural profile |
| Reference Data | PostgreSQL | MCC, BIN, country risk, watchlists |
| Rule Engine | Redis (compiled rules) + PostgreSQL | Deterministic YAML/JSON rules |
| Anomaly Detection | Redis feature store | Supervised + unsupervised scores |
| Graph Analysis | Neo4j | Rings, shared infrastructure, path risk |
| Risk Scoring | PostgreSQL | Composite 0–1000 score + explanation |
| Case Management | PostgreSQL | Analyst workflow, chargebacks |
| Notification | PostgreSQL | SMS, email, push, webhooks, Slack/PagerDuty |
| Audit & Compliance | Kafka (infinite) + QLDB-style hash chain | Immutable decisions and config changes |
| Alert Correlation | Redis + PostgreSQL | Target-style multi-terminal incident grouping |
| Feature Store | Redis + PostgreSQL | Batch + real-time features for ML |

---

## Decision thresholds

| Score | Action | SLA |
|---|---|---|
| 0–199 | Auto-approve | < 100 ms |
| 200–599 | Step-up authentication | < 5 s |
| 600–799 | Manual review queue | < 4 hours |
| 800–1000 | Auto-decline | < 100 ms |

---

## Prototype (rough)

```bash
cd prototype
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then `POST http://127.0.0.1:8080/api/v1/transactions` with a JSON body (see `prototype/README.md`). This is intentionally incomplete: no Kafka, Kubernetes, persistent store, authentication, or trained model. It is an educational sketch, not suitable for payment or production use.

---

## Generating diagrams

- PlantUML: paste any `diagrams/*.puml` into https://www.plantuml.com/plantuml
- Mermaid: paste any `diagrams/*.mmd` into https://mermaid.live (GitHub also renders Mermaid in Markdown)

---

## Simulation board lenses

Design choices are written so they can be defended to the CTO, CRO, VP Engineering, Head of Compliance, and CFO (see Board presentation).