# TRC Scenario Discovery Protocol v1.0

**Status:** companion validation protocol. Canon controls if conflict occurs.

## Purpose

CVaR can only bound risks represented in the declared scenario set. This protocol strengthens TRC by requiring disciplined scenario discovery, challenge, update, and versioning.

## Scenario discovery sources

A robust TRC run SHOULD use multiple sources:

| Source | Function | Control |
|---|---|---|
| domain experts | known failure modes and plausible pathways | disclose expertise and uncertainty |
| incident and near-miss data | empirically observed precursors | cite evidence and relevance |
| red team | adversarial and neglected scenarios | independent challenger record |
| affected stakeholders | lived and local risk knowledge | prevent elite blind spots |
| AI-assisted generation | expands imagination and edge cases | discovery input only, not validity source |
| literature and standards | benchmark scenario families | cite and adapt cautiously |

## Minimum Tier 3 scenario discovery workflow

1. Define decision boundary, horizon, and catastrophe cells.
2. Generate initial scenario families from canonical categories.
3. Run red-team challenge for missing or suppressed scenarios.
4. Add stakeholder and near-miss inputs where relevant.
5. Use AI-assisted scenario generation only as a candidate discovery surface.
6. Deduplicate scenarios and map causal pathways.
7. Assign probabilities or probability bands with stated confidence.
8. Record rejected scenarios and reasons.
9. Run sensitivity with contested scenarios included and excluded.
10. Version the scenario library used for the run.

## AI-assisted scenario boundary

AI may propose scenarios. AI does not ground them. A model-generated scenario must be:

- screened for duplication;
- mapped to a plausible causal pathway;
- assigned evidence status;
- reviewed by a human or governed review process;
- included as assumption-bound if plausible but weakly evidenced.

## Rejected-scenario log

Every Tier 3 TRC run SHOULD record material rejected scenarios:

| Field | Required content |
|---|---|
| scenario_name | short label |
| proposed_by | expert, red team, stakeholder, AI-assisted, literature, other |
| reason_for_rejection | implausible, out of scope, duplicate, already covered, too weakly grounded, lower-tier only |
| challenge_status | uncontested, contested, escalated |
| sensitivity_action | excluded, included in sensitivity, included in main run |

## Update triggers

A scenario library SHOULD be reviewed after:

- incident or near miss;
- new scientific evidence;
- policy/legal change;
- challenger identifies omitted failure mode;
- repeated assumption-bound scenarios affect decisions;
- external reviewers find scenario family imbalance.

## Plain-language rule

TRC does not ask whether the modeler imagined the future perfectly. It asks whether the run searched seriously for ruin paths, recorded what it found, and refused to average away what matters most.
