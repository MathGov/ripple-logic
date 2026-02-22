# TV-0001 Notes — Simple Admissible

## Purpose
Baseline conformance vector for the standard admissible path.

## What this vector tests
- NCRC pass
- TRC evaluation present
- No containment trigger
- RLS computation path is reached
- UCI explicitly declared unavailable (not silently omitted)

## Why this matters
This is the first parity vector between:
- spreadsheet-assisted evaluation
- future deterministic reference engine
- third-party implementations

## Naive implementation risk
A naive implementation might skip explicit path tracking and still output "admissible."
This vector requires the path labels, not just the final classification.

## Expected result summary
- `admissibility_status = ADMISSIBLE`
- `decision_classification = ADMISSIBLE`
- no required flags
- ordered primary path exactly as specified in `expected_output.json`
