# TEST_VECTOR_SPECS_v8.5.3_beta.1.md

This document summarizes the intent and expected governance behavior of each vector in the beta set.

## TV-0001 Simple Admissible
Baseline admissible path:
- NCRC pass
- TRC evaluated
- no containment
- RLS path reached
- explicit UCI unavailable state

## TV-0002 Rights Fail
Anti-compensation proof:
- explicit non-compensatory rights-floor violation
- immediate NCRC rejection
- no rescue by aggregate welfare gains

## TV-0003 TRC Tail Risk
Tail-risk-sensitive review escalation:
- NCRC pass
- TRC materially active
- containment not triggered
- review required due to tail-risk bounding / uncertainty

## TV-0004 Containment Trigger
Bounded restraint / safety path:
- NCRC pass
- TRC materially active
- severe uncertainty + insufficient evidence
- containment required

## TV-0005 Non-Decisive Review
Procedural humility without containment:
- NCRC pass
- TRC evaluated (not materially driving outcome)
- containment not triggered
- review required due to limited evidence / insufficient decisiveness
