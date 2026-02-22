# TV-0004 Notes — Containment Trigger

## Purpose
Containment conformance vector.

## What this vector tests
- NCRC passes
- TRC is materially active
- containment trigger conditions are met
- containment becomes the primary result instead of normal admissibility scoring

## Why this matters
This vector proves the system can choose restraint and bounded action when evidence/risk conditions make a normal decision unsafe or premature.

## Naive implementation risk
A naive implementation may still output an admissible ranked option from partial or low-quality evidence.
That is nonconformant for this vector.

## Expected result summary
- `admissibility_status = CONTAINMENT_REQUIRED`
- `decision_classification = CONTAINMENT_REQUIRED`
- required flags include containment and evidence-insufficiency indicators
- path must include `CONTAINMENT_TRIGGERED`
