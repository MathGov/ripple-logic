# Reader guide: numerical choices, state meanings and dependencies

**Informative only.** This guide collects existing rules and the accepted September 26 clarifications. It does not create a new gate, parameter authority, state registry, emergency permission or empirical validation result. The Canon, SGP and the named companion retain their existing precedence and versions.

## 1. Read the profile before the scalar

Start with the impact/contribution matrix, affected groups and worst-affected slices, evidence, uncertainty and dependence, and the decisive or non-decisive comparison. RLS is a conditional normalized residual summary over selectable options, not a percentage of alignment or safety. A large Gap is not a p-value or calibrated statistical confidence. A point-score leader is not automatically a uniquely selected option; selection is not authority or execution approval. Sources: Canon §§10.0A, 10.1A, 10.3A–10.4B; RLS Validation Protocol, “Configuration Sensitivity and Profile-First Validation.”

## 2. Assessed zero, uncertainty and active masks

The frozen Aligners run explicitly uses all 49 active cells with demonstration-only Method C uncertainty σ_cell=.02. A has seven input-bearing cells and 42 zero point cells; B has six and 43. That is a stipulated teaching configuration, not an empirical inference that every cell has identical uncertainty.

An assessed zero point estimate is not necessarily an exactly known deterministic zero. A measured zero, model-estimated zero, offsetting effects, an assumed zero and an unassessed cell have different evidence meanings. Do not make sigma zero just because the mean is zero; do not replace unknown with zero. The synthetic exact-zero convention in Canon Appendix P/R.19 belongs to a different Method B construction and does not override the workbook's declared inputs.

For the independent-cell diagnostic, define raw weighted difference `D = Σq_i(I_Ai − I_Bi)`, active mass `Q = Σq_i`, and `V_raw = Σ(q_iσ_Ai)² + Σ(q_iσ_Bi)²`. Normalization gives the equivalent expression:

`Gap = |D| / sqrt(V_raw + εQ²)`.

A zero point-difference cell with nonzero uncertainty can increase uncertainty mass and reduce Gap. This is not a universal rule based only on the number of boxes: weights, uncertainty and dependence determine the effect. An exactly certain added zero leaves Gap unchanged when ε=0; with ε>0 its contribution to Q can still matter. Common positive rescaling of every q leaves this formula invariant. These demonstrations do not permit mask manipulation: the comparison mask is common across options, declared before result-dependent ranking, and cannot discard non-maskable gate-critical coverage. Shared evidence/cross-option dependence requires the Canon's additional treatments, not this illustration alone.

### Independently reproduced frozen results

| Quantity | Value |
| --- | ---: |
| RLS(A) | 0.0153129427168233 |
| RLS(B) | −0.0011223873850525 |
| Nominal Gap | 3.56551781265359 |
| Gap at σ×2 | 1.81508102477079 |
| Uncertainty multiplier at Gap=2 | 1.81267991954780 |
| Nominal Gap at ε=0, diagnostic only | 3.65250426432936 |
| Gap at σ×2 and ε=0, diagnostic only | 1.82625213216468 |

Epsilon=10⁻⁶ reduces the nominal Gap by about **2.3816%**. Its role is numerically meaningful and must be disclosed, as already required by Canon §10.3A. Changing it after observing a preferred outcome is prohibited. The zero-epsilon diagnostic does not rescue the doubled-sigma comparison. A scale-relative or smaller alternative may be studied prospectively under governed revision; no such replacement is silently adopted here.

The final worked result remains **REFUSE_DETERMINISTIC_SELECTION**, with authority selection separately recorded. Demonstration-only uncertainty cannot support an operational unique-selection claim even when a nominal arithmetic test passes. `Reference/feedback_sensitivity.py` reconstructs these quantities from the literal effect inputs rather than cached formula dependencies.

## 3. Parameter rationale and evidence boundaries

These are existing governance choices, not empirically discovered constants. The table summarizes the reason for each construction and relevant sensitivity; it does not invent a proof that a numerical setting is optimal.

| Existing family | Current default / basis | Rationale and source | Test/revision boundary |
| --- | --- | --- | --- |
| Rights thresholds | LIFE −.90; BODY −.70; LBTY −.65; NEED −.50; DIGN −.55; PROC −.45; INFO −.40; ECOL −.65 | Non-compensatory versioned protection anchors; Canon §7.1 and Appendix C | Tier 3 threshold ±.05 sensitivity; retain categorical and severe-hazard channels. A floor-only table is not the full rights test. |
| Saturation | β=2; β_RF defaults to β | Bound represented impacts and separate rights-channel rules; §§5.5, 7.4.1 | Direct β sensitivity normally {1,1.5,2,2.5} for required high-stakes cases, or justified domain range; rights-channel sensitivity where material. Not empirical optimality. |
| Temporal factor | t_min=.083 years; T_ref=25 years; capped logarithm | Bounded temporal salience/persistence, not cumulative welfare or pure time discounting; §5.3–§5.3B | Suggested T_ref=15/50 sensitivity; <10 years needs charter-level justification. Preserve peak harm, recurrence and cumulative-burden review. |
| TRC context (α,τ) | Personal (.90,.30); organization (.95,.20); reversible (.95,.15); irreversible (.99,.10); existential (.999,.05) | Increasing consequence-class protection; §8.7 / Appendix D.9 | Governed defaults, not validated risk tolerances. Use applicable severity overlays, probability/scenario provenance and sensitivity. |
| Category probability floor | p_floor≥.02 for applicable mandatory categories | Anti-omission governance prior; §§8.3.1–8.3.2 | Not an observed frequency. Categories can overlap: their floors cannot automatically be added as independent mass. Context-specific implausibility requires recorded justification/review. |
| Union floors U1–U7 | (.20,.06,.06,.06,.08,.10,.10), sum .66 | Anti-erasure, proportionate attention and residual headroom; §13.1 | Normative allocation, not natural welfare exchange rates. U1 is not privileged operator self-interest. Governed alternatives/sensitivity preserve original results. |
| Dimension floors D1–D7 | (.08,.10,.08,.08,.10,.06,.10), sum .60 | Minimum residual attention; §13.1.2–§13.1.4 | Floors do not establish cardinal comparability or themselves replace protected rights. |
| Discrimination | δ=2; ε=10⁻⁶ | Conservative governance convention and numerical guard; §§10.3A–10.4 | Report guard sensitivity, every contender and required variant. Neither value creates statistical confidence. |
| Optional risk adjustment | λ=.5 when invoked | Diagnostic RLS_adj=RLS−λσ; §10.3 | Governing use requires ex-ante declaration and consistent comparison; no post-result switching. |
| UCI weights | .25 each of four applicable components, renormalized where legitimately inapplicable | Structural/process diagnostics; §11.1 | Missing applicable evidence is not “not applicable.” Framework-level measurement remains provisional; no standalone high-stakes pass or unique winner. |

Existing PCC parameter locks, uncertainty/scenario records, WeightProfileStatus and MethodologicalIntegrityRecord provide the homes for origin, authority, measurement scale, alternatives, sensitivity, reviewers and revision triggers. This guide adds no mandatory competing record and changes no numerical default.

### TRC reference and background risk

Canon §8.4 and Appendix D.6 already define **scenario-conditioned residual safe-corridor-relative Base-stream loss within the declared exposure domain**. An incremental comparison with continuation may be informative but cannot replace the gating loss or erase residual unsafe exposure. Mandatory scenario categories have applicability/exception rules and can overlap. Thus five labels with .02 floors do not universally imply .10 disjoint catastrophe probability, nor does that sum alone determine CVaR. For truly disjoint applicable categories, the floor sum does follow; risk analysis still needs the actual loss distribution, domain and governance justification.

## 4. One typed map, not one interchangeable vocabulary

| Surface / owner | Existing terms | Interpretation and non-equivalence |
| --- | --- | --- |
| Claim grounding | RG_SUPPORTED, RG_NARROWED, RG_REFUSED | Claim support/scope, not a universal ethical rejection. |
| Ordinary option qualification | RF_PASS; TRC_PASS or justified TRC_NOT_TRIGGERED; CSV_PASS, CSV_PASS_WITH_CONTROLS or CSV_NOT_MATERIAL | Evidence and conditions govern. NOT_TRIGGERED is not a computed CVaR pass. Later `*_NOT_EVALUATED_AFTER_PRIOR_FAILURE` is not PASS. |
| Framework verdict | ALLOW_FRAMEWORK_SELECTION; REFUSE_DETERMINISTIC_SELECTION | Unique-selection claim is distinct from point leadership, governed residual preference and authority. |
| Reproducibility decision_state | SELECTED_DECISIVE; SELECTED_BY_AUTHORITY_NON_DECISIVE; PROVISIONAL_WITH_CONTROLS; EMERGENCY_PROVISIONAL; NO_SELECTABLE_OPTION; REFUSE; REDESIGN; ESCALATE; DELAY | Apply the conditional crosswalk and precedence in Reproducibility §3.1A. Authority-selected non-decisive choice does not become a framework winner. Controls alone do not select an option. Preserve actual refusal/escalation reasons. |
| Execution | NOT_AUTHORIZED; AUTHORIZED_WITHIN_SCOPE; EXECUTION_BLOCKED; EXECUTED_UNDER_MONITORING | No earlier score/state supplies authority, physical safety or successful outcome by itself. |
| Primer / public shorthand | Rights-admissible, Admissible, Selectable, Selected, Refusal; SELECT, SELECT WITH CONTROLS, NARROW, REDESIGN, ESCALATE, REFUSE, NON-DECISIVE | Teaching terms need expansion into formal fields. SELECT WITH CONTROLS is not automatically PROVISIONAL_WITH_CONTROLS or execution approval. NARROW has no universal one-token replacement. |
| Tier 1 CSV shorthand | CSV_PASS_HEURISTIC; CSV_PASS_WITH_CONTROLS_HEURISTIC | Human-only labels. Suffix removal does not establish machine conformance. CSV_REDESIGN is deprecated input; emitted token is CSV_REDESIGN_REQUIRED. |
| ripple.md wrapper | Aligned within declared scope/evidence coverage (Pass / Conditional); Not aligned | Wrapper claims follow §8.5 and the seven-test conditions, not merely the Canon verdict. Applicable FAIL/IND cannot become Pass/Conditional. Valid emergency triage does not become an aligned pass. |
| Agent capability/action | LATENT_CAPABILITY, AVAILABLE_CAPABILITY, ENABLED_CAPABILITY, AUTHORIZED_CAPABILITY, SELECTED_ACTION, EXECUTION_APPROVED, EXECUTED_TRANSITION, OBSERVED_OUTCOME | Possibility, activation, permission, selection, approval, execution and observed consequences answer separate questions. Neither capability nor execution establishes welfare, safety or authority. |

This is a navigational map, **not an exhaustive replacement for the unbundled canonical state registry or transition matrix**. Exact machine tokens and transitions require the pinned interface. Sources: Canon §§0.3, 4, 10–11 / Appendix AF.2; Reproducibility §§3–3.1A; Primer §8; Public Intro “Decision outcomes”; Cascade short-circuit rule; ripple.md §8.5; Agent capability-state extension.

## 5. Emergency pathways: shared index, distinct safeguards

| Pathway | Governing source | Keep distinct |
| --- | --- | --- |
| Rights Emergency Mode | Canon §7.5 / Appendix C | Full rights-emergency prerequisites, compound violation comparison and priority, alternatives/challenge, necessity, mitigation, authority, expiry and review. It is not ordinary RF_PASS. |
| Tail Emergency Mode | Canon §8.8 / Appendix D.11 | Rights-admissible options but none tail-passing; no automatic least-CVaR choice. Necessity, safer/no-action alternatives, independent challenge, absolute exposure cap, monitoring/shutoff, remedy and exit. Not TRC_PASS or ordinary RLS ranking. |
| CSV_EMERGENCY_PROVISIONAL | Canon Section 9 / CSV Standard | Necessity-bound time-limited structural exception, no better feasible alternative, harm cap, monitoring, authority and remediation/review. Does not erase RF/TRC or physical warrants. |
| PROVISIONAL_UNDER_REFUSAL | Canon §4.9.3 | Delay harms, conservative rights/tail screen, bounded/reversible/staged action where feasible, escalation and review, explicit provisional/refusal label. |
| ripple.md triage | §§2.19–2.20, 8.4, 11.7 | No Test 1/rights-uncertain execution through this exception; independent authority, necessity, expiry and remedy. The episode is not relabeled aligned. |
| PFAP pathway | Applicable separately supplied external protocol | Not bundled as an active protocol here. Do not invent its rules from a mention; its “Tier 1” is not Canon Tier 1. |

An optional **cover index over existing records** can link episode/option/configuration, invoked pathways and source versions, original failures, necessity/alternatives, authority, controls, expiry, review, remedy and return-to-normal. Each pathway retains every additional prerequisite. This is not a common permit or weaker shared denominator. Where both Canon and wrapper duties apply, satisfy both or refuse the stronger claim.

Canon run tiers, wrapper conformance L0–L3, empirical-study L0–L4, Reproducibility V0–V2/R0–R4 and SGP bands are separate ladders.

## 6. What the package does and does not contain

**Bundled:** all 15 Core Office masters; complete 14-document PDF/HTML/MD/TXT/structured-block mirrors; manifest and ledger; scoped equation/record/reference code and selected synthetic Appendix R fixtures; workbook identity and cache-independent formula replay; supplemental schemas; dashboard; verification evidence. These are real executable subsets, not a full production runtime or complete external validator.

**Not claimed as bundled/verified:** exact canonical state/transition/audit registries, normative kernel index, full `mathgov_run_record_v4_1` interface and `VALIDATE_MATHGOV_RUN.py`, complete machine-readable Appendix R corpus, active governed scenario library, active RPAP/PFAP protocols, exact WDBIP external v1_7 interfaces/study companions, and `RLS_Validation_Workbook_v0.3` with a complete L1 case/rater execution kit. The latter is distinct from frozen Aligners 5.9. See `Dependency_Status.json` for individual artifacts and consequences.

ripple.md already places the current bundle boundary on page 2 before its abstract: self-contained L0/L1 wrapper learning and basic Decision Notes; stronger paths requiring recourse/redaction/coercion/emergency companions need those applicable protocols separately supplied, hash-pinned and recorded. “L2/L3 unavailable from this package alone on those paths” must not become a claim that every imaginable stronger path has identical companion requirements.

The L1 research design is specified, not an executed study or complete data-entry kit. Prepare and freeze the case packets, workbook, rater instructions, preregistration, blocking/randomization and analysis before recruiting/scoring; preserve independent raw scores before adjudication. Its first sprint tests clarity, burden, missingness, disagreements and preliminary reliability, not an adequately powered 49-variable latent factor structure. RLS Validation Protocol H3 concerns legibility; H5 concerns OptionClosureRecord improvement. Hypothesis numbers must not be borrowed from another document.

MHIOS, Auditable Flourishing and AIAP lie outside this Core 15 release and inherit no assurance from it.

## 7. Historical labels and exact release identity

Sheet names and “SECTION G2A: v12.0” remain lineage/reference labels; renaming them would risk reference damage without improving the current computation. The active counterpart of Config!B27 is Build_Snapshot!CN1466, not the old archived B27. The invalid command is repaired only at the actual current surface and its typed mirror.

Publication build **MG-RL-13.0-20260926-RELEASE-I**, with all component editions unchanged. Eleven untouched Core masters retain their exact G/H source IDs; the Primer, wrapper, WDBIP and workbook have I identities. The manifest binds every hash. The existing numerical defaults and Canon gates are unchanged. See the current Release I adjudication for the eight scoped errata.

**Native application limit:** no new I LibreOffice Calc/Microsoft Excel recalculation/save/reopen is claimed. Older native receipts retain their original input hashes. The reviewer reports native H parity, not a native I result. Current I tests check the recorded text/print-scope corrections, formula/cache preservation and cache-independent arithmetic. Hosted publication and empirical validation remain separate evidence-generating tasks.
