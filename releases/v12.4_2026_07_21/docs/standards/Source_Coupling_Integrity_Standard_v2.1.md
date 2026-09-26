# Source-Coupling Integrity Standard v2.1


## v2.1 Current Release Integration

**Release:** MathGov Core Release 2026.09 v12.4 / SGP v8.3 - Calculability, Type-Integrity, and Cross-Artifact Synchronization Public Research Source Release

**Exact current companion pins:** Canon v12.4; SGP v8.3; ripple.md v5.3; Agent System v12.2; CSV v2.2; Cascade v2.4; Reproducibility v1.2; WDBIP v1.4; RLS Validation v2.4; Primer v4.2; Public Introduction v12.4; PC-AEP/MFDI/Source-Coupling v2.1; Aligners Sheet v5.4.

| Integrity surface | Current requirement | Claim boundary |
|---|---|---|
| Source map | Capabilities remain traceable to enabling conditions, boundary conditions, provenance, inherited assumptions, scaffolding, and source debt. | Output performance is not source-coupling evidence. |
| Interface boundary | Models, optimizers, procedures, benchmarks, and institutions may route or generate candidates without proving the underlying claim. | Downstream success cannot launder upstream uncertainty. |
| Placement | Source-Coupling Review operates inside RG and CSV where material. | It is not a new public cascade stage. |


Release: MathGov Core Release 2026.09 v12.4 / SGP v8.3 - Calculability, Type-Integrity, and Cross-Artifact Synchronization Public Research Source Release

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

When triggered, the Source-Coupling Record MUST include the following minimum fields for Tier 3 runs, high-stakes Tier 2 runs, and any public conformance claim. Low-stakes Tier 1 and ordinary Tier 2 reviews may use a shorter rationale only when the trigger is non-material and the claim boundary is correspondingly narrow:

| Field                              | Required content                                                                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `claimed_capability`               | The capability, output, procedure, or system state being relied on.                                                                                           |
| `enabling_conditions`              | The physical, institutional, computational, evidentiary, legal, ecological, social, or operational conditions that make the claimed capability possible.      |
| `boundary_conditions`              | Known limits, failure ranges, assumptions, context restrictions, and conditions under which the claim no longer holds.                                        |
| `source_evidence`                  | Evidence that the enabling conditions and boundaries are known enough for the declared claim boundary.                                                        |
| `generator_output_distinction`     | How the run distinguishes the process that produced an output from the output itself.                                                                         |
| `inherited_assumptions`            | Assumptions, standards, procedures, datasets, or categories inherited from prior use rather than re-derived in this run.                                      |
| `downstream_compensations`         | Filters, controls, monitors, compliance checks, waivers, manual reviews, redundancies, or governance layers used to compensate for uncertainty or limitation. |
| `source_coupling_status`           | One of the status values below.                                                                                                                               |
| `source_debt_flag`                 | Whether the run is accumulating structural risk because source understanding is weak, stale, unknown, or overextended.                                        |
| `falsification_or_recheck_trigger` | What evidence would force narrowing, rerun, redesign, escalation, refusal, or stronger controls.                                                              |
| `required_claim_action`            | The claim action: proceed within boundary, narrow, mark assumption-bound, require controls, rerun, escalate, redesign, or refuse.                             |

Machine-readable PCC and validator-facing records MUST use the canonical SourceCouplingStatus enum: `SOURCE_COUPLED`, `SOURCE_PARTIAL`, `SOURCE_INFERRED`, `SOURCE_UNKNOWN`, `SOURCE_CONTESTED`, `SOURCE_DEBT_RISK`, and `SOURCE_COUPLING_FAILURE`. Human-readable labels may describe these states, but labels such as `GROUNDED` do not replace the canonical tokens.

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

## Relationship to Physical/Causal Admissibility Evidence

Source-Coupling Integrity asks whether a claimed capability remains traceable to the enabling conditions and limits that make it possible. The Physical/Causal Admissibility Evidence Profile asks whether a material physical or causal action has a declared model basis, validity domain, boundary conditions, uncertainty range, failure modes, reversibility boundary, verification or warrant, monitoring/shutoff path, residual unknowns, and claim action.

When both triggers hold, the records SHOULD cross-reference each other. Source coupling may show what makes a capability possible, while PC-AEP shows whether a specific action is admissible under the relevant physical or causal constraints. Neither record is a sixth gate. Both are consumed inside RG and CSV where material.

## Relationship to CSV

CSV consumes source-coupling evidence when source weakness creates structural fragility. CSV SHOULD treat `SOURCE_DEBT_RISK`, unresolved `SOURCE_UNKNOWN`, or `SOURCE_CONTESTED` as material when the option's structural viability, dependency closure, operational capacity, reversibility, monitoring, or containment depends on the claimed capability.

Source-debt diagnostic. Source debt is the structural risk created when a run continues through compensatory controls while the enabling conditions, boundary conditions, or limits of a claimed capability remain weak, stale, unknown, overextended, or contested.

Source debt is different from semantic debt. Semantic debt concerns weak terms or categories. Source debt concerns weak understanding of the capability-generating conditions themselves.

## Computational-source boundary

Source-Coupling Integrity distinguishes the source that generates a candidate from the source that warrants the candidate. For AI, optimization, robotics, industrial control, medical, infrastructure, or other consequence-bearing workflows, the run SHOULD record `candidate_generation_source` and, where PC-AEP is triggered, `admissibility_warrant_source`. A model, orchestration layer, guardrail, policy engine, monitor, approval workflow, or application layer may route or constrain a candidate, but it MUST NOT be treated as the physical or causal warrant unless it is itself a domain-valid verification method inside a declared validity domain.

## Agent and AI-output rule

Model fluency, benchmark performance, agentic tool use, chain-of-action success, or policy-filter compliance does not establish source-coupled admissibility. Agent outputs remain downstream claims until Reality Grounding and, where material, Source-Coupling Review establish the supported claim boundary.

## Related external work

Framework boundary: Source-Coupling Integrity is a MathGov-native Reality Grounding and CSV diagnostic. It does not import any external ontology, protected framework, or third-party text, and it does not create a sixth gate.


## Methodological integrity linkage

Source-coupling claims MUST declare the claim type, source dependency, evidence surface, alternative explanations, falsification or recheck trigger, and downstream dependencies where material. A capability claim that survives through inherited procedure, benchmark success, compliance, or model fluency alone is not METHOD_SUPPORTED. Weak source coupling constrains claim strength and may require re-derivation of downstream CSV or public conformance statements.
## Short-form boundary

The short form for Source-Coupling Integrity is `SC-Int`. Do not abbreviate Source-Coupling Integrity as `SCI`, because `SCI` is reserved in the Canon for Stakeholder Coverage Index.

## Physical-source coupling

For consequence-bearing physical systems, SC-Int asks where the claimed physical capability obtains its authority: a physical model, controller envelope, validated simulator, empirical test, standards-based warrant, certified engineering basis, clinical warrant, or other domain-specific method. If the claimed capability is sourced only to governance permission, compliance status, documentation, authority, monitoring, or model fluency, the source coupling is insufficient for physical-execution safety claims.


## Concrete source-coupling examples

| Situation | Source-coupling interpretation | Required boundary |
|---|---|---|
| A model gives a fluent legal answer without cited jurisdiction, statute, or qualified review. | Output fluency is not legal grounding. | Mark `SOURCE_INFERRED` or `SOURCE_UNKNOWN`; narrow to exploratory analysis or require legal warrant. |
| A benchmark score is used to justify deployment in a new clinical, military, or infrastructure domain. | Benchmark performance is not domain deployment capability. | Mark `SOURCE_PARTIAL`; require domain testing, PC-AEP where physical/causal action is material, and CSV controls. |
| A certification or organizational approval is used as proof of physical safety. | Permission is not physical admissibility. | Trigger PC-AEP; source-coupling may support governance evidence but not physical proof by itself. |
