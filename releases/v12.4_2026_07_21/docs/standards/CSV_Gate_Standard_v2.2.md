# CSV Gate Standard v2.2


## v2.2 Current Release Integration

**Release:** MathGov Core Release 2026.09 v12.4 / SGP v8.3 - Calculability, Type-Integrity, and Cross-Artifact Synchronization Public Research Source Release

**Exact current companion pins:** Canon v12.4; SGP v8.3; ripple.md v5.3; Agent System v12.2; CSV v2.2; Cascade v2.4; Reproducibility v1.2; WDBIP v1.4; RLS Validation v2.4; Primer v4.2; Public Introduction v12.4; PC-AEP/MFDI/Source-Coupling v2.1; Aligners Sheet v5.4.

| Integrity surface | Current requirement | Claim boundary |
|---|---|---|
| Severe-rights interface | CSV uses the Canon-owned severe-rights-hazard activation predicate and may not deactivate a hazard that has already activated in RF/NCRC review. | CSV cannot convert a rights failure into an ordinary welfare trade-off. |
| Reopening | New catastrophic or irreversible pathways discovered in CSV reopen TRC before RLS. | This feedback path is not a sixth gate. |
| Execution | Structural viability requires controls, authority, monitoring, reversibility, and any triggered domain warrant. | CSV passage is not physical-safety certification. |


Release: MathGov Core Release 2026.09 v12.4 / SGP v8.3 - Calculability, Type-Integrity, and Cross-Artifact Synchronization Public Research Source Release

Source-boundary rule: If this compact standard conflicts with the RippleLogic Canon, the Canon controls.

CSV means Containment and Structural Viability. CSV is the strengthened fourth level of the RippleLogic cascade inside the MathGov framework:

RG -> RF -> TRC -> CSV -> RLS

RF means Rights Floor, the public-facing name for the Non-Compensatory Rights Constraint (NCRC). RF names the second cascade layer; NCRC names the formal pass/fail predicate for protected rights. NCRC-style notation remains valid in equations and checklists.

CSV is not a sixth public level. It is the upgraded fourth level: Contain/Verify.

TRC-CSV feedback rule. If CSV discovers a catastrophic, irreversible, or ruin-path scenario not represented in TRC, the run MUST reopen TRC before RLS. CSV does not absorb TRC.

Gate-critical confidence guard. Low confidence in adverse rights-covered, catastrophe-covered, or material CSV impacts cannot by itself make an option pass RF/NCRC, TRC, or CSV. If a gate outcome could change, the run must use a governed conservative bound, collect evidence and rerun, narrow the claim, downgrade, escalate, or refuse the stronger claim.


Baseline pointer. Gate-admissibility cells and residual welfare cells may use distinct baselines where the Canon requires it; see Canon §5.1A for the floor-reference versus status-quo dual-baseline rule.

## Realizability interface

CSV is the main structural-realizability layer, but it does not absorb Reality Grounding or TRC. RG decides whether the claim is grounded. TRC decides whether catastrophic tail exposure is bounded. CSV decides whether the pathway can stand under containment, dependency, execution, monitoring, authority, and host-system constraints. If CSV discovers a new catastrophic or ruin-path scenario, TRC must be reopened before RLS.

Boundary discriminator: TRC is the ruin veto; CSV is the viability and control test. Do not absorb TRC into CSV. A structurally viable option may still fail TRC if its downside tail is unacceptable, and a tail-safe option may still fail CSV if it cannot execute or persist under real constraints.



RG status rule. Reality Grounding is Level 1 of the public method and a claim-authority precondition. It can force narrowing, escalation, exploratory-marking, or refusal, but it is not an option-rejecting gate; RF/NCRC, TRC, and CSV are the option-rejecting gates, and RLS ranks only what survives them.

## Two-phase selectability rule

RippleLogic first qualifies options, then ranks survivors. Phase 1 is RG -> RF -> TRC -> CSV. Phase 2 is RLS.

CSV therefore never exists to make a high-scoring option look selectable. It exists to decide whether an option that already survived RF/NCRC and TRC can structurally stand under its declared controls, dependencies, execution conditions, and monitoring. If it cannot, the option must be controlled, redesigned, escalated, refused, or treated under emergency-provisional rules before any ordinary RLS ranking.


## CSV core rule

CSV does not demand zero harm. CSV demands that harms are visible, routed, bounded, mitigated, monitored, and not structurally degrading or unjustly externalized beyond tolerance.

## CSV status values

The canonical CSV status ladder is:

- CSV_PASS
- CSV_PASS_WITH_CONTROLS
- CSV_REDESIGN_REQUIRED
- CSV_ESCALATE
- CSV_FAIL
- CSV_NOT_MATERIAL
- CSV_EMERGENCY_PROVISIONAL


## CSV status resolver guide

The Canon controls, but this compact guide constrains routing:

| Evidence / diagnostic condition                                                                                   | CSV routing                                                               |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Any material diagnostic level 4 or uncontained / structurally degrading / unjustly externalized / non-viable harm | CSV_FAIL                                                                  |
| Material Structural Viability failure that is not controlled or redesignable                                      | CSV_FAIL                                                                  |
| Material Structural Viability failure that can plausibly be repaired                                              | CSV_REDESIGN_REQUIRED                                                     |
| Gate-material evidence missing, stale, contested, or insufficient                                                 | CSV_ESCALATE, claim narrowing, or refusal of the stronger selection claim |
| Material diagnostic level 3                                                                                       | CSV_REDESIGN_REQUIRED or CSV_ESCALATE                                     |
| Material diagnostic level 2 with binding controls                                                                 | CSV_PASS_WITH_CONTROLS                                                    |
| Material diagnostic level 2 without binding controls                                                              | CSV_REDESIGN_REQUIRED                                                     |
| All material diagnostics level 0-1 and Structural Viability passes                                                | CSV_PASS                                                                  |
| No material CSV burden under the declared claim boundary                                                          | CSV_NOT_MATERIAL                                                          |
| Necessity + no better feasible option + time limit + harm cap + monitoring + transition plan                      | CSV_EMERGENCY_PROVISIONAL                                                 |

Tier boundary. A CSV_PASS or CSV_PASS_WITH_CONTROLS in a Tier 2 worked run may be assumption-bound and must not be read as validated structural measurement. UCI/HOI remain diagnostics until separate validation evidence supports stronger claims.

## Tier-Proportional CSV Depth

| Tier | Minimum CSV obligation before ordinary ranking or selection |
| --- | --- |
| Tier 1 | A brief qualitative CSV screen or a recorded `CSV_NOT_MATERIAL` rationale. CSV is not optional when an ordinary ranking or selection claim is made. |
| Tier 2 | A proportional, assumption-bounded review issuing an explicit canonical status before RLS: `CSV_PASS`, `CSV_PASS_WITH_CONTROLS`, `CSV_NOT_MATERIAL`, `CSV_REDESIGN_REQUIRED`, `CSV_ESCALATE`, `CSV_FAIL`, or `CSV_EMERGENCY_PROVISIONAL` where the emergency protocol applies. |
| Tier 3 | Full binding CSV evidence, controls, ownership, monitoring, and review triggers sufficient for the declared claim and execution boundary. |

`REDESIGN` and `FAIL` may be used as plain-language actions, but structured records must use `CSV_REDESIGN_REQUIRED` and `CSV_FAIL`. `CSV_REFUSE` is not a canonical status; refusal is a disposition after failure, unresolved material evidence, or absent authority.


## Selectability rule

Option p is selectable for ordinary RLS ranking only if:

- RG supports the claim boundary,
- Rights Floor passes, formally NCRC(p) = PASS,
- TRC_status(p) is TRC_PASS or documented TRC_NOT_TRIGGERED,
- CSV_status(p) is CSV_PASS, CSV_PASS_WITH_CONTROLS, or CSV_NOT_MATERIAL.

If CSV_status(p) is CSV_PASS_WITH_CONTROLS, the controls are part of the option. Removing them invalidates the pass and requires rerun.

If CSV_status(p) is CSV_NOT_MATERIAL, the option is pass-equivalent for the declared claim boundary only after the PCC records why no material CSV burden is present. CSV_NOT_MATERIAL MUST NOT waive Structural Viability subchecks when execution feasibility, resource closure, dependency closure, reversibility, operational capacity, or internal coherence is material. If later evidence makes CSV material, CSV must be rerun.

If CSV_status(p) is CSV_REDESIGN_REQUIRED or CSV_FAIL, the option is not selectable as specified.

If CSV_status(p) is CSV_EMERGENCY_PROVISIONAL, temporary action requires a time limit, harm cap, monitoring plan, review trigger, and transition/remediation plan. No unqualified alignment claim is permitted.

## Source-debt diagnostic

CSV consumes Source-Coupling Integrity evidence when an option depends on a capability whose enabling conditions, boundary conditions, or limits are weak, stale, unknown, overextended, contested, or masked by downstream compensations.

Source debt is the structural risk created when a run continues through controls, filters, waivers, monitoring, compliance, or administrative layers while the capability-generating conditions remain insufficiently grounded for the declared claim. Source debt is not automatically a CSV failure, but it is material when it affects dependency closure, resource closure, operational capacity, reversibility, monitoring adequacy, containment, or host-system integrity.

Routing rule: SOURCE_DEBT_RISK, unresolved SOURCE_UNKNOWN, or material SOURCE_CONTESTED status SHOULD route to CSV_PASS_WITH_CONTROLS, CSV_REDESIGN_REQUIRED, CSV_ESCALATE, CSV_FAIL, or emergency-provisional handling according to severity, reversibility, monitoring, and available alternatives.

## Physical/causal admissibility evidence diagnostic

CSV consumes the Physical/Causal Admissibility Evidence Profile when an option's structural viability depends on physical or causal adequacy, dependency closure, resource closure, operational capacity, reversibility, monitoring adequacy, containment, authority, or host-system integrity.

Required profile fields are: physical_or_causal_model_used; validity_domain; boundary_conditions; uncertainty_range; failure_modes; reversibility_or_irreversibility_boundary; verification_simulation_empirical_test_or_expert_warrant; monitoring_and_shutoff_path; residual_unknowns; and required_claim_action.

Routing rule: unresolved PCAE_UNKNOWN, PCAE_CONTESTED, PCAE_VERIFICATION_REQUIRED, PCAE_CONTROL_REQUIRED, or PCAE_REDESIGN_REQUIRED MAY route a non-execution or explicitly claim-narrowed option to CSV_PASS_WITH_CONTROLS, CSV_REDESIGN_REQUIRED, CSV_ESCALATE, CSV_FAIL, or emergency-provisional handling according to severity, reversibility, monitoring, authority, and available alternatives. For physical execution, CSV_PASS_WITH_CONTROLS is unavailable while admissibility remains unresolved: the evidence must first support execution inside the declared validity domain, or the action remains blocked, narrowed, redesigned, escalated, or refused. PCAE_REFUSE_OR_BLOCK is stricter and cannot issue an ordinary CSV pass or pass-with-controls for the physical execution as specified.

PC-AEP is not a sixth gate and not a claim that MathGov generates physical proof. It is an evidence discipline that prevents governance approval, model fluency, certification, monitoring, or simulation from being substituted for physical or causal admissibility.

## Consequence-tempo compatibility (Normative when material)

For rapid propagation, material irreversibility, consequential automation, delayed detectability, or material lock-in, CSV SHALL test whether the worst credible control critical path can reach a safe state before the earliest unacceptable adverse escalation threshold or irreversible stop-loss boundary. The comparison must include relevant detection, interpretation, authorization, intervention, containment, safe-state, and rollback dependencies, including parallel and automated control paths.

Where no runtime interruption window is technically possible, CSV may still pass only when stronger ex ante assurance, bounded scope/rate, fail-safe design, monitoring, lawful authority, and explicit residual-risk acceptance make the execution pathway structurally viable. The harm of delay must be compared; urgent protective action must not fail merely because its intended first effect is immediate.

A completed timing record is evidence of review, not proof that the estimates or controls are correct. Material uncertainty can require `CSV_PASS_WITH_CONTROLS`, `CSV_REDESIGN_REQUIRED`, `CSV_ESCALATE`, or refusal.

## CSV diagnostics

CSV may use internal concern levels from 0 to 4:

0 = no material concern.
1 = minor residual concern, carry to RLS.
2 = material concern, controls required.
3 = serious concern, redesign or escalation required.
4 = gate-failing concern.

Suggested diagnostic dimensions: containment integrity, structural viability, physical/causal admissibility, hollowing risk, dependency/lock-in risk, substitution pressure, mitigation adequacy, monitoring adequacy, reversibility/exit, accumulation risk, and legitimacy stress.

## UCI/HOI placement

UCI and HOI are not public cascade stages. They are first evaluated inside CSV when material to structural integrity. Residual UCI/HOI may be used only as tie-break, monitoring, or hollowing-risk documentation after RLS is tied, close, or non-decisive.

## CSV graduated verdict logic

CSV is a routing and selectability layer, not a purity filter. Its job is to distinguish ordinary bounded residual harm from uncontained or structurally non-viable harm.

- `CSV_PASS`: contained and structurally viable; residuals may enter RLS.
- `CSV_PASS_WITH_CONTROLS`: selectable only if specified controls become binding conditions.
- `CSV_REDESIGN_REQUIRED`: not selectable as specified, but a revised option may be evaluated.
- `CSV_ESCALATE`: stakes, uncertainty, or authority gaps require deeper review before selection.
- `CSV_FAIL`: uncontained, structurally degrading, unjustly externalized, non-viable, hidden, lock-in-producing, unmonitored, or beyond-tolerance harm.
- `CSV_EMERGENCY_PROVISIONAL`: temporary necessity-bounded action with time limit, harm cap, review trigger, and transition plan; not a full alignment certification.
- `CSV_NOT_MATERIAL`: no material CSV burden found for the declared claim boundary; pass-equivalent for selectability only after rationale is recorded. This status does not waive Structural Viability where execution feasibility is material.

## CSV diagnostic channels

CSV may use diagnostic ratings for containment integrity, structural viability, physical/causal admissibility, hollowing risk, dependency/lock-in risk, substitution pressure, mitigation adequacy, monitoring adequacy, reversibility, and accumulation risk. UCI/HOI-style diagnostics are evaluated inside CSV when material and are not independent public gates by default.


Formal selectability rule: `A_sel = {a in A_adm : CSV_status(a) in {CSV_PASS, CSV_PASS_WITH_CONTROLS, CSV_NOT_MATERIAL}}`. `CSV_NOT_MATERIAL` is pass-equivalent only for the declared claim boundary after the PCC records the rationale. It does not waive Structural Viability where execution feasibility is material. If later evidence makes CSV material, CSV MUST be rerun. Emergency provisional options are handled through emergency protocol, not ordinary RLS selection.


## Methodological dependency rule

CSV_PASS, CSV_PASS_WITH_CONTROLS, and CSV_NOT_MATERIAL are valid only within the declared dependency chain. If a starting assumption, physical/causal model, source-coupling condition, threshold, operator, or evidence surface materially changes, the affected CSV conclusion MUST be rerun, narrowed, escalated, controlled, redesigned, or refused. Silent model tuning after failure is not CSV integrity.
## Physical execution support rule

CSV may evaluate controls, dependencies, sequencing, reversibility, monitoring, containment, and host-system integrity, but CSV does not itself compute physical safety. When physical execution is material, CSV must consume PC-AEP and distinguish three states: physical admissibility supported within declared validity domain; governance permission only; or physical admissibility not established.

If PC-AEP is `PCAE_UNKNOWN`, `PCAE_VERIFICATION_REQUIRED`, `PCAE_REDESIGN_REQUIRED`, or `PCAE_REFUSE_OR_BLOCK`, CSV must not issue an ordinary physical-execution pass. It must narrow, control, redesign, escalate, or refuse according to the evidence and risk state.


## Binding-control minimum

A control counts as binding only if the run identifies an owner, trigger condition, verification surface, failure consequence, and review date. A control that is merely promised, unowned, unmonitored, or consequence-free must not be used to upgrade CSV status.


## UCI/HOI measurement-maturity warning

UCI/HOI may support CSV reasoning only within declared measurement maturity. Current v12.4 does not claim cross-domain validated UCI/HOI. Where UCI/HOI are material and unavailable, the run must narrow, escalate, collect evidence, or refuse stronger selectability claims. A provisional UCI result must not be the sole basis of a high-stakes `CSV_FAIL`; the fail requires a structured CSV evidence case identifying the concrete mechanism, affected containing scope, evidence and uncertainty, threshold or failure condition, reviewer status, and available controls or redesign path. Otherwise route to `ASSUMPTION_BOUND`, `CSV_ESCALATE`, or `CSV_REDESIGN_REQUIRED` as appropriate.
