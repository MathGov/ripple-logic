# Source-Coupling Integrity Standard v1.0

Release: MathGov Core Release 2026.09 v11.4.6 Final GitHub Readiness Patch

Source-boundary rule: If this compact standard conflicts with the RippleLogic Canon, the Canon controls.

## Purpose

Source-Coupling Integrity is a MathGov-native diagnostic inside Reality Grounding and CSV. It prevents a RippleLogic run from treating downstream output, model fluency, institutional permission, benchmark performance, compliance status, inherited procedure, or interface success as proof that the claimed capability is grounded in the enabling conditions that make it possible and define its limits.

It is not a new public gate. It does not alter the public cascade:

`RG -> RF -> TRC -> CSV -> RLS`

It strengthens the existing rule that Reality Grounding comes before claims, and that CSV must verify whether an option can structurally stand.

## Core rule

A claim-bearing run MUST NOT rely on a capability, output, procedure, model, metric, or institution as decision-relevant unless the run records, at the required tier, enough source-coupling information to support the claim boundary.

Plain-language rule: before MathGov trusts a capability, it asks what makes the capability possible, what boundary conditions limit it, and what evidence shows that the run has not mistaken downstream performance for grounded understanding.

## Trigger

Source-Coupling Review is REQUIRED for Tier 3 runs and high-stakes Tier 2 runs when any of the following materially affects claim authority, RF/NCRC, TRC, CSV, RLS, SGP interpretation, execution authority, or public conformance:

- a model-generated output, simulation, benchmark, dashboard value, or interface result is used as evidence;
- an inherited institutional procedure, legal category, standard, dataset, metric, or compliance label is used as if it settled the underlying claim;
- a claimed capability is extrapolated beyond the context in which it was demonstrated;
- downstream controls, filters, waivers, compensations, or monitoring layers are used to manage a limitation whose source is not understood;
- the system is being scaled, automated, delegated, or made agentic;
- a challenger plausibly alleges that performance, permission, compliance, or fluency is being substituted for grounded capability.

For low-stakes Tier 1 and ordinary Tier 2 runs, Source-Coupling Review is recommended when any trigger is plausible but may be satisfied with a short rationale.

## Required record fields

When triggered, the Source-Coupling Record SHOULD include the following fields, and MUST include them for Tier 3 public or institutional claim-bearing runs:

| Field | Required content |
|---|---|
| `claimed_capability` | The capability, output, procedure, or system state being relied on. |
| `enabling_conditions` | The physical, institutional, computational, evidentiary, legal, ecological, social, or operational conditions that make the claimed capability possible. |
| `boundary_conditions` | Known limits, failure ranges, assumptions, context restrictions, and conditions under which the claim no longer holds. |
| `source_evidence` | Evidence that the enabling conditions and boundaries are known enough for the declared claim boundary. |
| `generator_output_distinction` | How the run distinguishes the process that produced an output from the output itself. |
| `inherited_assumptions` | Assumptions, standards, procedures, datasets, or categories inherited from prior use rather than re-derived in this run. |
| `downstream_compensations` | Filters, controls, monitors, compliance checks, waivers, manual reviews, redundancies, or governance layers used to compensate for uncertainty or limitation. |
| `source_coupling_status` | One of the status values below. |
| `source_debt_flag` | Whether the run is accumulating structural risk because source understanding is weak, stale, unknown, or overextended. |
| `falsification_or_recheck_trigger` | What evidence would force narrowing, rerun, redesign, escalation, refusal, or stronger controls. |
| `required_claim_action` | The claim action: proceed within boundary, narrow, mark assumption-bound, require controls, rerun, escalate, redesign, or refuse. |

## Status values

- `SOURCE_COUPLED`: enabling conditions and boundary conditions are sufficiently evidenced for the declared claim. Default routing: proceed within claim boundary.
- `SOURCE_PARTIAL`: some source-coupling evidence exists, but the claim must be narrowed or controls must be added. Default routing: narrow, add controls, or route into CSV.
- `SOURCE_INFERRED`: source coupling is inferred from indirect evidence and must not support strong conformance or deployment claims. Default routing: assumption-bound or sensitivity-only unless corroborated.
- `SOURCE_UNKNOWN`: the enabling conditions or limits are not known enough for the requested claim. Default routing: escalate, narrow, collect evidence, or refuse stronger claim.
- `SOURCE_CONTESTED`: relevant experts, affected parties, data, or reviewers materially dispute the source account. Default routing: escalate and preserve challenger evidence.
- `SOURCE_DEBT_RISK`: downstream controls are compensating for weak source understanding. Default routing: route to CSV and require controls, monitoring, and recheck triggers.
- `SOURCE_COUPLING_FAILURE`: the run substitutes output, fluency, compliance, permission, or procedure for source-coupled evidence. Default routing: refuse or redesign the claim as specified.

## Relationship to Reality Grounding

Source-Coupling Integrity is a subdiscipline of Reality Grounding. It extends Category Grounding and Term Discrimination by asking whether the claimed capability itself remains traceable to the enabling conditions and limits that make it possible.

A weak Source-Coupling Record does not automatically make every option fail. It does constrain what may be claimed. The correct action may be claim narrowing, assumption-bound use, sensitivity-only treatment, stronger evidence collection, escalation, redesigned controls, or refusal of deterministic selection.

## Relationship to CSV

CSV consumes source-coupling evidence when source weakness creates structural fragility. CSV SHOULD treat `SOURCE_DEBT_RISK`, unresolved `SOURCE_UNKNOWN`, or `SOURCE_CONTESTED` as material when the option's structural viability, dependency closure, operational capacity, reversibility, monitoring, or containment depends on the claimed capability.

Source-debt diagnostic. Source debt is the structural risk created when a run continues through compensatory controls while the enabling conditions, boundary conditions, or limits of a claimed capability remain weak, stale, unknown, overextended, or contested.

Source debt is different from semantic debt. Semantic debt concerns weak terms or categories. Source debt concerns weak understanding of the capability-generating conditions themselves.

## Agent and AI-output rule

Model fluency, benchmark performance, agentic tool use, chain-of-action success, or policy-filter compliance does not establish source-coupled admissibility. Agent outputs remain downstream claims until Reality Grounding and, where material, Source-Coupling Review establish the supported claim boundary.

## Related external work

Related external scholarship: Strüver, Alexander Wolfgang. (2026). *Source Amnesia: How Civilizations Lose Their Understanding of Generative Structures*. Science of Stability. CC BY-NC-ND 4.0. MathGov cites that work as related external scholarship only. MathGov does not adopt the term as a MathGov module, does not reproduce or adapt that text, and does not bundle that work into this Apache-licensed release.
