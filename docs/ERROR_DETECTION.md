# Embedded error findings in the project brief

The source brief calls for five embedded errors, but the available PDF text does not identify their locations. The following are the five most material internal inconsistencies found while reviewing the brief and the existing design pack. They are recorded as findings to verify with the project owner; they should not be treated as a definitive answer key.

| # | Finding | Evidence / effect | Recommended resolution |
|---|---|---|---|
| 1 | Conflicting latency targets | The brief refers to 100 ms and 200 ms p99 objectives in different places. | Define 100 ms for detection fan-out and 200 ms for end-to-end authorization, and label scope consistently. |
| 2 | Mixed Kafka topic naming convention | The stated convention is `domain.entity.action`, while examples omit the `fraud` domain prefix (for example `transactions.raw`). | Adopt one canonical namespace (for example `fraud.transactions.raw`) or explicitly document the shorter aliases. |
| 3 | Requirements versus deliverable summary mismatch | The infrastructure guidance requires Kubernetes Deployment, Service, HPA, PDB, and NetworkPolicy samples for two or more services, while the daily summary mentions only broad deployment samples. | Track each manifest type explicitly; the current samples are incomplete for some resources. |
| 4 | Deliverables versus repository transfer | The Day 15 list includes repository ownership transfer, which is an external Git-host action and cannot be represented by a local file. | Keep transfer as a candidate-owned submission step and report it as not generated locally. |
| 5 | Submission format versus source-centric deliverables | The brief asks for UML code / design artifacts while also recommending one or two consolidated PDFs; the existing source pack contains no rendered bundle. | Preserve editable source as canonical and create a final readable export only when a PDF packaging tool and approval are available. |

## Existing pack conflict

The architecture documents also mix a 100 ms detection-hop/fan-out limit with a 100 ms risk-scoring SLA and a 200 ms end-to-end target. The scope-based interpretation above is the safest design, but service-level values should be recalculated to ensure the component budgets sum to the total budget.
