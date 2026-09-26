# Distribution Shift and Requalification Protocol

**Status:** Informative implementation companion for MathGov Core v12.5.

A prior pass is not permanent. A material change can invalidate the evidence, scenario, structural, or authority surface on which the run depended.

## Requalification triggers

- model, weights, tools, memory, data, prompt, policy, or deployment-context change;
- new stakeholder, subgroup, jurisdiction, ecosystem, or dependency;
- evidence beyond the declared cutoff or evidence-age limit;
- incident, near miss, audit finding, appeal, or credible whistleblower report;
- change in law, authority, standards, professional guidance, or domain practice;
- scenario-library expiry, new catastrophe pathway, or revised dependence evidence;
- capacity, resource, containment, monitoring, rollback, or shutoff degradation;
- observed outcome outside preregistered validity or uncertainty bounds;
- material drift in welfare, rights, tail-risk, or structural indicators.

## Gate reopening map

| Change | Minimum reopening |
|---|---|
| Source, evidence, category, target, or validity-domain change | RG |
| New protected group, right, categorical prohibition, or severe hazard | RG + RF/NCRC |
| New catastrophe pathway, probability, dependence, or horizon | RG + TRC |
| New dependency, capacity, control, legitimacy, physical-admissibility, or rollback issue | RG + CSV |
| Weight, mask, residual evidence, or MPS hypothesis change after gates remain valid | RLS plus parameter-lock versioning |
| Model/system identity or deployment-context change with cross-gate effects | Full requalification |

## Required states

- `REQUALIFICATION_NOT_TRIGGERED`
- `REQUALIFICATION_REQUIRED`
- `REQUALIFICATION_IN_PROGRESS`
- `PRIOR_VERDICT_SUSPENDED`
- `REQUALIFIED_PASS`
- `REQUALIFIED_WITH_CONTROLS`
- `REQUALIFIED_REDESIGN`
- `REQUALIFIED_REFUSE`

## Rules

1. A material trigger suspends the affected prior claim until requalification is complete.
2. Monitoring is not requalification and does not preserve a stale pass.
3. A new run version must preserve the prior record and identify the triggering change.
4. Emergency action remains governed by Rights Emergency or Tail Emergency requirements and cannot be normalized into ordinary selection.
5. Post-incident review must update scenario libraries, domain profiles, controls, and test fixtures where warranted.
