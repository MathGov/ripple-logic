# TV-0002 Notes — Rights Fail (NCRC Rejection)

## Purpose
Critical anti-compensation proof vector.

## What this vector tests
- explicit non-compensatory rights-floor violation
- immediate NCRC failure
- rejection path without restoration by aggregate welfare gains

## Why this matters
This vector proves RippleLogic is not a pure utility maximizer.
A candidate implementation must reject the scenario even if some welfare metrics look positive.

## Naive implementation risk
A naive weighted-sum optimizer may produce a positive score and mark the option admissible.
That is nonconformant for this vector.

## Expected result summary
- `admissibility_status = REJECTED`
- `decision_classification = REJECTED_NCRC`
- required flags include rights failure indicators
- ordered primary path exactly:
  1. `NCRC_FAIL`
  2. `REJECT`
