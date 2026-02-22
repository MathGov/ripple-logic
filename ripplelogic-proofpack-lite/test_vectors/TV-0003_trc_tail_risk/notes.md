# TV-0003 Notes — TRC Tail Risk (Review Required)

## Purpose
TRC-focused conformance vector.

## What this vector tests
- NCRC passes
- TRC is materially active (tail risk is not trivial)
- TRC affects the decision path
- Containment is NOT triggered
- Final result is procedural escalation (`REVIEW_REQUIRED`) rather than forced admissibility

## Why this matters
This vector proves the implementation is not a naive point-estimate optimizer.
It must surface uncertainty and tail-risk effects in the decision path.

## Naive implementation risk
A naive implementation may compute a positive weighted result and mark the case admissible.
That is nonconformant for this vector because TRC is intentionally constructed to remain decision-relevant.

## Expected result summary
- `admissibility_status = REVIEW_REQUIRED`
- `decision_classification = REVIEW_REQUIRED`
- required flags include TRC materiality and review indicators
- path must include TRC stage and review escalation
