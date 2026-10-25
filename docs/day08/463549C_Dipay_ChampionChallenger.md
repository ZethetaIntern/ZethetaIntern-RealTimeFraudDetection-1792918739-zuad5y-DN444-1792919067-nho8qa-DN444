# Champion-challenger

Champion serves decisions. Challengers get the **same features**, write `model.shadow_scores`, never change `action`.

Minimum 7 days. Promote if: detection ≥ champion, FPR ≤ champion + 0.05 pp, p99 latency within budget. Dual control: ML lead + CRO.

Canary after promote: 5% live (not shadow) with auto-rollback on FPR spike.
