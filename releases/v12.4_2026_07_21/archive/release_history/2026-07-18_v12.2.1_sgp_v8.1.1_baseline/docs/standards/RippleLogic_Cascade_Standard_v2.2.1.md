# RippleLogic Cascade Standard v2.2.1


Source-boundary rule: If this compact standard conflicts with the RippleLogic Canon, the Canon controls.

Release: MathGov Core Release 2026.09 v12.2.1 - SGP v8.1.1 Reality-Management Calibration Integration Public Research Source Release

This standard is the compact public reference for the current five-level RippleLogic cascade inside the MathGov framework. It prevents companion documents from repeating long synchronization notes.

TRC-CSV feedback rule. If CSV discovers a catastrophic, irreversible, or ruin-path scenario not represented in TRC, the run MUST reopen TRC before RLS. CSV does not absorb TRC.

TRC-CSV discriminator. TRC is the ruin veto. CSV is the viability and control test. Ordinary bounded operational risks usually route to CSV; catastrophic, irreversible, lock-in, systemic, or ruin-path risks route to TRC. Double-material evidence must be evaluated in both places and documented without double-counting it as ordinary residual welfare unless a bounded residual remains after gate treatment.


Gate-critical confidence guard. Low confidence in adverse rights-covered, catastrophe-covered, or material CSV impacts cannot by itself make an option pass RF/NCRC, TRC, or CSV. If a gate outcome could change, the run must use a governed conservative bound, collect evidence and rerun, narrow the claim, downgrade, escalate, or refuse the stronger claim.


Baseline pointer. Gate-admissibility cells and residual welfare cells may use distinct baselines where the Canon requires it; see Canon §5.1A for the floor-reference versus status-quo dual-baseline rule.


## Reproducible run interface

The cascade is easy to state but must not be implemented loosely. A conforming implementation uses the deterministic run-state and parameter-completeness rules in `docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.0.md`. In particular, an option may enter RLS only after its RG, RF/NCRC, TRC, and CSV states establish selectability; missing decision-material parameters cannot silently become zero or an undeclared default; and selection remains separate from authority and execution.

The JSON schema and validator supplied with this release check structural and semantic contradictions. They do not calculate moral truth or validate the underlying evidence.

## Public cascade

`RG -> RF -> TRC -> CSV -> RLS`

Plain language: Ground reality -> protect rights -> bound ruin -> contain/verify viability -> score the ripples.

## Two-phase interpretation

The public cascade may be taught as two phases:

1. **Qualify options:** RG -> RF -> TRC -> CSV.
2. **Rank survivors:** RLS.

This is not a new cascade and not a sixth gate. It is the teaching and implementation framing of the same method: first determine what is grounded, rights-safe, tail-safe, and structurally viable; then rank only those survivors by residual ripple impact.


## Formal shorthand

`RG/RSG -> RF/NCRC -> TRC -> CSV -> RLS`

The formal components are:

- `RG/RSG`: Reality Grounding / Reality-Surface Grounding. Claim-authority precondition, not an ordinary option-rejecting gate.
  - RG status rule: Reality Grounding is Level 1 of the public method and can force narrowing, escalation, exploratory marking, or refusal. RF/NCRC, TRC, and CSV are the option-filtering gates; RLS ranks only what survives them.
- `RF/NCRC`: Rights Floor, formally implemented by the Non-Compensatory Rights Constraint. Non-compensatory gate.
- `TRC`: Tail-Risk Constraint. Non-compensatory catastrophic-risk gate.
- `CSV`: Containment and Structural Viability. Selectability gate for containing-system integrity and execution viability.
- `RLS`: RippleLogic Score. Residual welfare-ranking layer applied only to options that remain selectable.


## Rights-specific non-attenuation rule

RF/NCRC is not a welfare-duration calculation. For adverse rights-covered instances, short duration and low analyst confidence cannot by themselves weaken the floor. The run must apply the Canon's rights-floor impact channel, categorical-prohibition screen, and severe-hazard risk-tolerance test. Missing severe-hazard evidence prevents an ordinary pass.

## Tail Emergency Mode rule

When rights-safe options exist but every option fails TRC, the ordinary selectable set is empty. The default is redesign, delay, escalation, no-action review, or refusal. A provisional least-CVaR action may be used only when delay/no-action is evidenced to be unavailable or worse, an independent challenger has reviewed alternatives, a hard maximum exposure is respected, and time limits, monitoring, shutoff, remedy, and return-to-normal criteria are binding. The state is TAIL_EMERGENCY_PROVISIONAL_ACTION, not SELECT or TRC_PASS.

## Normalized residual ranking rule

RLS divides the weighted impact numerator by the active effective weight mass after masks and cell multipliers. Define `q(u,d)=w_u*v_d*m(u,d)*kappa(u,d)`, `Q=sum_u sum_d q(u,d)`, and `RLS(a)=[sum_u sum_d q(u,d)*I_prop_welfare(u,d,a)]/Q`, with `Q>0`. This preserves the [-1,+1] interpretation and prevents masks or κ multipliers from changing score scale. A worked example with `Q=1` may report the numerator as the score, but the denominator remains part of the canonical definition. If active mass is zero, ranking is undefined and must be repaired or refused.

NCRC three-channel rule. An option passes RF/NCRC only when, for every right, `v_r^floor=0`, `v_r^cat=0`, `v_r^risk=0`, and no required categorical-prohibition or severe-hazard evidence field is unresolved. A compact table displaying only the floor channel must label it as such and record the other two channels separately.

## Computability vs realizability rule

A computed, simulated, generated, or model-fluent option is not automatically grounded, selectable, executable, or ethical. RG supplies claim authority; RF/NCRC supplies rights admissibility; TRC supplies ruin bounding; CSV supplies structural and execution viability; RLS ranks only the surviving selectable set.

## Source-coupling rule

A downstream output, interface result, benchmark success, compliance status, institutional permission, inherited procedure, or model-fluent answer is not proof of grounded capability. When material, Reality Grounding must record the claimed capability, enabling conditions, boundary conditions, source evidence, inherited assumptions, downstream compensations, and required claim action. CSV consumes this evidence when weak source coupling creates dependency, containment, or structural-viability risk.

Source-Coupling Integrity is not a sixth gate. It is a Reality Grounding subdiscipline and a CSV diagnostic where material.

## Physical/causal admissibility evidence rule

A consequence-bearing physical or causal action is not selectable merely because it was computed, simulated, generated, approved, certified, monitored, or made compliant. When material, Reality Grounding must link a Physical/Causal Admissibility Evidence Profile with the candidate-generation source, physical or causal model used, validity domain, boundary conditions, uncertainty range, failure modes, reversibility/irreversibility boundary, verification/simulation/empirical test/expert warrant, admissibility-warrant source, monitoring and shutoff path, residual unknowns, and claim action. CSV consumes this profile when structural viability depends on physical or causal adequacy.

Generated candidate is not verified transition. The cascade treats the source that generated a candidate and the source that warrants admissibility as separate record fields. Orchestration, filtering, guardrails, policy routing, monitoring, and approval can govern candidate handling, but they do not by themselves establish physical or causal safety.

The profile is not a sixth gate. It is a Reality Grounding subdiscipline and a CSV diagnostic where material.

## Non-overlap rule

RG determines what claim may be made. RF/NCRC, TRC, and CSV determine whether an option remains selectable. RLS ranks only selectable options. RLS cannot rescue rights-floor failure, tail-risk failure, or CSV failure.

## CSV non-purity rule

CSV does not reject every negative ripple. Negative ripples must be made visible and routed. Bounded residual harms may enter RLS. Uncontained, structurally degrading, unjustly externalized, non-viable, hidden, lock-in-producing, unmonitored, or beyond-tolerance harms require controls, redesign, escalation, emergency-provisional handling, or failure.

## All-Encompassing Infinite Union (AIU) and SGP boundary

All-Encompassing Infinite Union (AIU) is a horizon/meta-union orientation, not a Tier 1-3 scoring object or override. SGP is a moral-status and protection evidence interface; it informs protected-stakeholder modeling where permitted but does not replace RG, RF/NCRC, TRC, CSV, RLS, lawful authority, or governance-role requirements.


## Methodological integrity rule

For Tier 3 and high-stakes Tier 2 runs, material gate claims MUST identify claim type, dependency position, evidence or test surface, falsification or revision trigger, alternative-explanation status, and re-derivation scope if a foundation changes. This does not add a public gate. It strengthens Reality Grounding and prevents downstream scoring from inheriting hidden assumption authority.
## Carried-forward v12.1 physical execution and rights/ruin hardening boundary

For consequence-bearing physical systems, the cascade must not confuse governance permission with physical admissibility. A run may say that authority, documentation, certification, or procedure is complete, but that is not the same as showing that a robot movement, vehicle maneuver, industrial action, medical intervention, infrastructure operation, or other physical execution is safe inside the relevant physical regime.

When PC-AEP is triggered, RLS cannot treat an option as selectable for physical execution unless the run identifies a domain-appropriate physical or causal warrant and the claim remains inside its declared validity domain. If that warrant is missing, contested, out of domain, or insufficient, the option must be narrowed, controlled, redesigned, escalated, or refused before selection.


## Carried-forward v12.1 Reality Grounding hardening note

Reality Grounding is the first claim-authority layer. For high-consequence domains, a claim is not adequately grounded merely because it is fluent, computed, authorized, compliant, simulated, or institutionally convenient. The claim must be testable or otherwise warranted, bounded, auditable, correctable, and refusible before it can support rights, TRC, CSV, or RLS conclusions.

Operational admissibility sequence: ground the claim; protect the right; bound the ruin; verify the system; make exit and correction real; rank only what survives qualification.

### Diagnostic routing rule (Normative clarification)

Use Category Grounding when the name, boundary, or class of a material term is weak. Use Source-Coupling Integrity when a claimed capability may be detached from the source conditions that make it possible. Use PC-AEP when a physical or causal execution claim is material. Use MFDI when a claim's testability, dependency chain, or revision trigger is material. These are RG/CSV diagnostics, not extra public gates.


## Layer-failure response quick table

| Failure at layer | Permitted response |
|---|---|
| RG insufficient | Narrow the claim, collect evidence, escalate, mark sensitivity-only, or refuse the stronger claim. |
| RF/NCRC fail | Redesign, choose least-rights-infringing emergency handling where allowed, or refuse. No score rescue. |
| TRC fail | Redesign, delay, escalate, review no-action, or refuse. Tail Emergency Mode is permitted only under necessity evidence, an absolute exposure cap, independent challenge, binding controls, and exit criteria. No ordinary RLS rescue. |
| CSV fail | Add binding controls, redesign, escalate, or refuse. Do not move structural failure into a tie-break. |
| RLS non-decisive | Use declared tie-break, authority selection, additional evidence, or refusal of deterministic selection. |
**SGP welfare-interface rule (Normative).** MPS bands and intervals are not cardinal welfare multipliers. They determine protection posture and the governed welfare-inclusion hypotheses that must be tested in residual RLS sensitivity. Human persons and FPP entities use full inclusion. Hypothesis-sensitive rankings return `MPS_HYPOTHESIS_SENSITIVE`.

**Gate-critical evidence rule (Normative).** Low confidence cannot establish a gate pass by shrinking adverse severity. Use the Canon `GateAdverseBound` operator or return UNKNOWN, ESCALATE, NARROW, or REFUSE.


