# CSV Measurement Maturity Note v1.0

**Status:** companion validation note. Canon controls if conflict occurs.

## Purpose

CSV is conceptually strong, but its indicators vary by domain. This note prevents overclaiming by distinguishing qualitative, indicator-supported, calibrated, and validated CSV use.

## CSV maturity ladder

| Maturity | Meaning | Public claim allowed |
|---|---|---|
| Qualitative CSV | structured judgment with evidence trace and reviewer rationale | CSV was assessed qualitatively |
| Indicator-supported CSV | measurable indicators exist but are not yet calibrated across cases | CSV was indicator-supported |
| Calibrated CSV | indicators have domain calibration, rater agreement, or pilot evidence | CSV was calibrated for this domain/scope |
| Validated CSV | independent replay and predictive or decision-improvement evidence exist | CSV validation exists for the declared domain |

## Required declaration

Any Tier 3 or public claim-bearing Tier 2 run SHOULD declare CSV maturity status for each material CSV domain, such as:

- institutional capacity;
- ecological support;
- infrastructure dependency;
- public legitimacy;
- labor burden;
- data governance;
- operational executability;
- system resilience.

## UCI/HOI boundary

UCI and HOI-style diagnostics are structural signals, not magical measurements. They require domain grounding. A run MUST NOT present UCI or HOI as empirically validated in a domain unless the validation evidence exists.

## CSV calibration plan

Future CSV validation should test:

- whether independent reviewers identify the same structural failures;
- whether CSV flags predict implementation failures, hidden burdens, or institutional degradation;
- whether controls convert CSV_REDESIGN_REQUIRED into CSV_PASS_WITH_CONTROLS;
- whether CSV_PASS_WITH_CONTROLS outcomes remain stable after controls expire;
- whether UCI/HOI thresholds are too strict, too weak, or domain-specific.

## Plain-language rule

CSV is a structural integrity gate. Until domain validation exists, say how strong the evidence is and do not pretend the structure has been proven safe beyond the declared surface.
