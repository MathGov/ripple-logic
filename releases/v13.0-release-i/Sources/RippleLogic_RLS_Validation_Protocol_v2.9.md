# RippleLogic RLS Validation Protocol

<table>
<tr><td>Integrity surface</td><td>Current requirement</td><td>Claim boundary</td></tr>
<tr><td>Study status</td><td>Level 1 protocol-development ready: measures, preregistration surfaces, and falsification conditions are specified.</td><td>Reliability, validity, and calibration are not established.</td></tr>
<tr><td>Latent structure</td><td>PCA, EFA, CFA, or measurement-invariance analyses require adequate samples, simulation-based planning, and preregistered interpretation criteria.</td><td>They are deferred rather than implied by a small pilot.</td></tr>
<tr><td>Workbook interface</td><td>Input validation, missingness, ranges, formulas, exclusions, and audit flags must cover the full intended data-entry region.</td><td>Workbook integrity does not validate the construct.</td></tr>
</table>

Status: protocol design, rater-study template, and validation sprint package. This document is not a governing core document, not empirical validation, not legal certification, and not deployment authorization.

Source binding: MathGov is the umbrella framework. RippleLogic is the decision architecture inside MathGov. The public cascade is RG -&gt; RF -&gt; TRC -&gt; CSV -&gt; RLS. The formal shorthand is RG/RSG -&gt; RF/NCRC -&gt; TRC -&gt; CSV -&gt; RLS. RLS ranks only selectable options after Reality Grounding, the Rights Floor, the Tail-Risk Constraint, and Containment and Structural Viability have been satisfied.

## Executive purpose

This protocol converts the next scientific need for RLS into a concrete study package. The goal is to test whether the 49-cell RLS welfare field is more than detailed. It must become defensible as structured, non-redundant, teachable, repeatable, and useful for better-justified decisions.

- Dimensional non-overlap question: do the 49 Scope x Dimension cells capture distinct decision-relevant information, or do some cells collapse into redundant clusters?

- Inter-rater reliability question: can trained analysts independently score the same cases with acceptable agreement?

- Decision-value question: does the RLS matrix reveal material harms, benefits, near-misses, or trade-patterns that a simpler single metric would hide?

- Revision question: which cells, anchors, instructions, or workbook fields need refinement before stronger operational-readiness claims are made?

## Claim boundary

A successful validation sprint does not prove universal superiority. It can support narrower claims such as: trained raters can apply the RLS scoring manual with measurable agreement on a representative case set; some cells provide distinct information not captured by a scalar score; and identified scoring ambiguities have been logged for Canon or companion refinement. Until evidence is published or registered, the correct status is: RLS is architecturally specified and audit-ready as a structured residual welfare-ranking layer, but empirical validation of dimensional independence and rater reliability remains in progress.

The protocol does not assume that cell anchors are validated interval measurements. Reliability statistics test the repeatability and decision usefulness of bounded scoring categories under the declared method; they do not convert ordinal or bounded judgment anchors into natural units of welfare.

## Canonical architecture under test

<table>
<tr><td>Layer</td><td>Role in validation</td></tr>
<tr><td>RG - Reality Grounding</td><td>Precondition for claim authority. Raters must not score claims stronger than the evidence surface permits.</td></tr>
<tr><td>RF - Rights Floor / NCRC</td><td>Non-compensatory gate. RLS cannot rescue rights-floor failure.</td></tr>
<tr><td>TRC - Tail-Risk Constraint</td><td>Non-compensatory catastrophic-risk gate. RLS cannot average ruin into ordinary benefit.</td></tr>
<tr><td>CSV - Containment and Structural Viability</td><td>Selectability gate for containing-system integrity and execution viability.</td></tr>
<tr><td>RLS - RippleLogic Score</td><td>Residual welfare-ranking layer over selectable options only.</td></tr>
</table>

Core normalized RLS formula: q(u,d)=w_u*v_d*m(u,d)*kappa(u,d), Q=sum_u sum_d q(u,d), and RLS(a)=[sum_u sum_d q(u,d)*I_prop_welfare(u,d,a)]/Q, with Q&gt;0. If a worked example has Q=1, the numerator equals the normalized score; the denominator remains part of the canonical definition and MUST NOT be omitted from general formula surfaces.

Canonical welfare impact scale: I(u,d,a) in [-1,+1], where 0 means no material change from the declared baseline, not unknown. Unknown active cells must be marked and handled under the missing-data and gate-critical unknown rules.

## Configuration Sensitivity and Profile-First Validation

Validation cases MUST freeze the evaluated configuration before first-pass scoring. Where a materially changed configuration alters capability, evidence, controls, permissions, operating envelope, or post-state effects, it is a distinct case condition rather than an unmarked repeat.

Primary reporting remains profile-first: the 7x7 field, subgroup and worst-affected slices, uncertainty, configuration sensitivity, dominance/incomparability, and rank reversals are reported before any scalar summary. Observed successful processes are partial capability evidence and do not establish untested boundaries or transfer across configurations.

## study-integrity correction (Lineage)

The initial sprint is a burden, comprehension, boundary-classification, missingness, disagreement, and preliminary reliability study. It is not adequately powered for a defensible 49-variable factor structure merely because every cell is present. PCA, EFA, CFA, or related structure claims require a preregistered simulation-based sample justification at a later validation level.

Rater work SHALL be divided into randomized or counterbalanced blocks with recorded timing, breaks, order, and fatigue measures. Repeated quality-control cases and frozen case-packet hashes are required. First-pass welfare scoring SHALL be completed and locked before gate cues are shown; gate-cue review and adjudication occur afterward to reduce priming.

The v0.3 workbook SHALL use UNASSESSED or blank review-dependent defaults, extend validation across the entire structured range, and prevent untouched rows from appearing complete. Level 1 reporting is limited to descriptive disagreement maps, missingness, cell comprehension, preliminary reliability, boundary confusion, burden, and fatigue unless a separately preregistered design supports a stronger claim.

## Additional Falsification Modules (Normative for the claims they test)

Taxonomy module: preregister plausible merges, splits and simpler alternatives; test boundary confusion, duplicated effects, omission, independent coding, subgroup visibility, explanatory value, burden and decision reversals. Do not infer statistical independence from low duplicate-effect coding, or mathematical irreducibility from a convenient seven-by-seven layout. Any combined criterion requires a disclosed measurement scale and weights.

Representation module: repeated observations, reordered keys, duplicate deliveries, alternative primary homes, conserved allocations and direct-versus-propagated endpoint estimates must be challenged. Exact duplicate transport must not change RLS. Repartitioning under nonlinear aggregation need not be invariant; detect and disclose any material reversal rather than promise invariance.

Control module: test grounded versus ungrounded effectiveness, latency on both sides of the harm deadline, ex-ante protection, late mitigation, depletion, common-cause failure, emergency authority, repeated commands, failover, stale evidence and unknown execution outcomes. Correct behavior includes refusal or restricted operation, not only successful recovery.

Privacy and security module: test proof-of-structure versus truth claims, invalid commitments, missing freshness/replay evidence, cross-domain signatures and identity disclosure. A mock signature, multiplication-based identity relation or unexecuted circuit is not a privacy/security result.

The supplied numerical and semantic fixture results are scoped implementation evidence. Hyperinflation, infrastructure loss, supply-chain conflict and offline-operation examples are synthetic unless independently sourced and identified otherwise. Do not report invented percentages, dates, prices, geographic replication latencies or control effectiveness as observations.

## Study ladder

<table>
<tr><td>Level</td><td>Name</td><td>Minimum design</td><td>Permitted claim</td></tr>
<tr><td>L0</td><td>Internal debug</td><td>2-3 cases, 1-2 raters</td><td>Only detects obvious rubric or workbook defects.</td></tr>
<tr><td>L1</td><td>Validation sprint v0.1</td><td>10 synthetic cases, 3 options each, 3-5 raters</td><td>Exploratory evidence on clarity, disagreement, and redundancy.</td></tr>
<tr><td>L2</td><td>Calibration study v1.0</td><td>20-30 cases, 3-5 options each, 5-9 raters, mixed affiliated and non-affiliated</td><td>Preliminary IRR and dimensional-overlap evidence.</td></tr>
<tr><td>L3</td><td>External shadow-mode study</td><td>Real or historical cases, independent raters, preregistered analysis</td><td>Domain-specific evidence for operational readiness in shadow mode.</td></tr>
<tr><td>L4</td><td>Controlled pilot</td><td>Authorized institution, comparator process, outcome follow-up</td><td>Limited performance claims relative to a declared comparator.</td></tr>
</table>

## Validation sprint

This package implements the recommended first sprint. It is intentionally small enough to run quickly and rigorous enough to reveal the main weaknesses.

- Case set: 10 realistic synthetic cases across AI governance, education, health, environment, public policy, and local infrastructure.

- Options: 3 candidate options per case.

- Raters: minimum 3, preferred 5. Include at least one non-authorial reviewer when possible.

- Scoring surface: 49 RLS cells per option, with score, confidence, rationale, anchor method, evidence basis, and uncertainty flag.

- Blind posture: raters should score independently before discussion.

- Adjudication: after independent scoring, record disagreements and produce an adjudicated reference score only after preserving raw rater scores.

- Analysis: compute IRR, disagreement heatmaps, descriptive cell correlations, missingness patterns, burden, boundary confusion, and comparison to a simpler scalar or 7-dimension summary. Do not estimate or interpret PCA, EFA, CFA, or a 49-cell latent structure at Level 1; those analyses require a later preregistered study with simulation-based sample justification.

Additional experimental arms. Where resources permit, randomize or counterbalance access to the OptionClosureRecord prompt before first ranking and measure option diversity, dominance, gate passage, residual harm, and burden. Report utilitarian, leximin/prioritarian, and capability-oriented outputs as transparent comparators only; they do not override the Canon or establish moral truth.

## Rater instructions

- Score the change from the declared baseline, not the absolute goodness of the option.

- Do not treat 0 as unknown. Use 0 only for no material baseline-relative change.

- If evidence is insufficient for an active cell, mark UNKNOWN_IMPACT and explain what evidence is missing.

- Do not average away subgroup harms in rights-relevant cells. Flag rights concerns separately from residual welfare scoring.

- Do not let RLS repair an option that fails RF/NCRC, TRC, or CSV.

- Record confidence independently from magnitude. A large impact with weak evidence is not the same as a small impact with strong evidence.

- Use the cell dictionary. When two cells seem similar, explain why the impact belongs in one cell, the other, or both with redundancy handling.

- When unsure, score conservatively, mark the uncertainty, and write the reviewer challenge question.

## Scoring anchors

<table>
<tr><td>Score</td><td>Meaning</td><td>Use discipline</td></tr>
<tr><td>+1.00</td><td>Severe or maximum plausible baseline-relative benefit</td><td>Use rarely; requires strong evidence and scope-appropriate denominator.</td></tr>
<tr><td>+0.75</td><td>Major durable benefit</td><td>Large improvement with clear reach, duration, likelihood, and confidence.</td></tr>
<tr><td>+0.50</td><td>Moderate benefit</td><td>Meaningful improvement in the cell, not merely cosmetic.</td></tr>
<tr><td>+0.25</td><td>Minor benefit</td><td>Small but material benefit.</td></tr>
<tr><td>0.00</td><td>No material change from baseline</td><td>Never use as a substitute for unknown.</td></tr>
<tr><td>-0.25</td><td>Minor harm</td><td>Small but material harm.</td></tr>
<tr><td>-0.50</td><td>Moderate harm</td><td>Meaningful degradation in the cell.</td></tr>
<tr><td>-0.75</td><td>Major durable harm</td><td>Large harmful degradation, even if not gate-failing.</td></tr>
<tr><td>-1.00</td><td>Severe harm</td><td>Use rarely; often gate-relevant or escalation-worthy.</td></tr>
</table>

## Study hypotheses

<table>
<tr><td>ID</td><td>Hypothesis</td><td>Evidence that supports it</td><td>Failure or revision signal</td></tr>
<tr><td>H1</td><td>RLS cells preserve non-redundant information.</td><td>Level 1: descriptive cell patterns, boundary-confusion rates, disagreement classes, and preliminary reliability show related but non-identical information. Later levels may test factor structure only under separate preregistration and design-specific sample justification.</td><td>Multiple dimensions collapse without unique decision contribution, or later preregistered structure tests fail to support the declared distinctions.</td></tr>
<tr><td>H2</td><td>Trained raters can score cells reliably.</td><td>The primary preregistered reliability statistic meets its declared provisional target or minimum after training; disagreement is explainable and reducible.</td><td>Sustained failure of the preregistered minimum after rubric training, or an undefined primary statistic, requires review; substitute statistics cannot retrospectively establish passage.</td></tr>
<tr><td>H3</td><td>RLS improves legibility over scalar scoring.</td><td>RLS identifies localized harms, rights-adjacent near-misses, ecological burdens, or scope-level reversals missed by scalar summary.</td><td>Scalar model produces same decision and same explanation with no material loss of information.</td></tr>
<tr><td>H4</td><td>The manual is teachable.</td><td>Raters improve after calibration and can explain cell placement consistently.</td><td>Confusion clusters persist in the same cells or dimensions.</td></tr>
<tr><td>H5</td><td>A proportionate OptionClosureRecord improves the candidate set before ranking.</td><td>A randomized or counterbalanced comparison shows more non-dominated, rights-compatible, lower-tail-risk, or lower-externality alternatives when the option-generation/closure prompt is used.</td><td>The record adds burden without improving option diversity, feasibility, harm reduction, or decision justification.</td></tr>
<tr><td>H6</td><td>Ethical-theory comparator analysis improves transparency without becoming a new gate.</td><td>Utilitarian, leximin/prioritarian, and capability-oriented comparators reveal whether a result is robust or normatively sensitive while preserving the Canon decision state.</td><td>Comparator use creates false authority, obscures the rights/tail/CSV cascade, or produces no interpretable additional information.</td></tr>
</table>

## Statistics plan

- Inter-rater reliability: use ICC(2,1) for single-rater cell scores and ICC(2,k) for averaged panel scores when the same raters score the same case-option-cell units and the declared scale and design warrant that estimator. Use a preregistered Krippendorff alpha variant when missingness or measurement level warrants it; do not switch estimators after seeing which passes. Every component requires a frozen mapping of measurement level, coding unit, rater/sample design, primary estimator and variant, provisional threshold, point-estimate or confidence-bound decision rule, missingness and undefined-statistic handling. Record the rationale for applying that threshold to that estimator; an unmapped or unsupported target cannot establish readiness.

- Gate and classification reliability: report percent agreement and the preregistered primary categorical estimator, such as Cohen or Fleiss kappa, or weighted kappa with stated weights for ordinal fields. For rare failures or imbalanced states, percent agreement MUST NOT stand alone; report prevalence, the underlying contingency counts, class-specific errors and uncertainty. An undefined primary statistic is not a pass. Diagnostic alternatives may be reported without replacing the locked primary result.

- Ranking reliability: preregister Kendall W for the declared multi-rater design or a specified Spearman comparison for the declared paired design, including tie and missing-option handling. A rank correlation is not interchangeable with categorical agreement or ICC; map the provisional threshold before confirmatory evaluation.

- Correlation analysis: build a case-option by 49-cell matrix using adjudicated or mean rater scores. Report Pearson and Spearman correlations, clustered heatmaps, and high-correlation pairs.

- Factor/PCA analysis: not part of Level 1. At later validation levels, PCA, EFA, CFA, or related latent-structure analyses MAY be run only under a separate preregistration with simulation-based sample justification, held-out checks where feasible, and explicit exploratory-versus-confirmatory labeling.

- Decision-value analysis: compare final RLS ranking and narrative justification against a simpler scalar score, a 7-dimension-only score, and a 7-scope-only score.

## Provisional protocol reliability targets (each numerical target applies only to its frozen primary preregistered reliability statistic under Canon Section 17.4A; no universal validated cutoff is implied)

<table>
<tr><td>Component</td><td>Target</td><td>Minimum acceptable</td><td>Protocol handling</td></tr>
<tr><td>Magnitude construction mu_k</td><td>Primary statistic &gt;= 0.70</td><td>Primary statistic &gt;= 0.60</td><td>Below minimum requires anchor/rubric redesign.</td></tr>
<tr><td>Rights-floor pass/fail</td><td>Primary statistic &gt;= 0.80</td><td>Primary statistic &gt;= 0.70</td><td>Below minimum requires rights mapping and subgroup guidance refinement.</td></tr>
<tr><td>TRC pass/fail</td><td>Primary statistic &gt;= 0.80</td><td>Primary statistic &gt;= 0.70</td><td>Below minimum requires scenario and probability guidance refinement.</td></tr>
<tr><td>RLS ranking order</td><td>Primary statistic &gt;= 0.70</td><td>Primary statistic &gt;= 0.60</td><td>Below minimum requires score, uncertainty, or tie-break review.</td></tr>
<tr><td>PLSS prominence classification</td><td>Primary statistic &gt;= 0.70</td><td>Primary statistic &gt;= 0.60</td><td>Below minimum requires prominence-signal guidance refinement.</td></tr>
</table>

## Correlation and factor-analysis revision rules

- If two cells correlate above 0.85 across most domains and raters cannot explain distinct causal meanings, mark the pair for overlap review.

- If a cell has persistently low variance across diverse cases, check whether it is genuinely rare, poorly defined, over-masked, or under-evidenced.

- If a dimension shows repeated cross-loading with another dimension, add boundary examples to the scoring manual before considering structural revision.

- If a cell has low reliability but high decision relevance, do not remove it prematurely. Strengthen anchors, examples, evidence requirements, and reviewer checks first.

- If simplified models produce the same winner but lose key localized risk signals, preserve RLS and report the extra legibility as decision-relevant detail.

- If simplified models produce the same winner and same explanation with no material information loss across a larger case set, consider a reduced mode or domain-specific profile.

## Disagreement taxonomy

<table>
<tr><td>Code</td><td>Meaning</td><td>Likely fix</td></tr>
<tr><td>DGT_SCOPE</td><td>Raters disagree on Union Scope mapping.</td><td>Improve stakeholder-instance and scope mapping examples.</td></tr>
<tr><td>DGT_DIMENSION</td><td>Raters disagree on welfare dimension.</td><td>Add boundary examples between dimensions.</td></tr>
<tr><td>DGT_MAGNITUDE</td><td>Raters agree direction but not size.</td><td>Improve score anchors and indicator scaling.</td></tr>
<tr><td>DGT_SIGN</td><td>Raters disagree benefit versus harm.</td><td>Clarify baseline, causal pathway, or evidence surface.</td></tr>
<tr><td>DGT_CONFIDENCE</td><td>Raters agree magnitude but not confidence.</td><td>Improve evidence-quality mapping.</td></tr>
<tr><td>DGT_GATE</td><td>Raters disagree on rights, TRC, or CSV relevance.</td><td>Strengthen gate trigger guidance.</td></tr>
<tr><td>DGT_UNKNOWN</td><td>Raters disagree whether evidence is sufficient.</td><td>Clarify unknown and phantom-instance handling.</td></tr>
<tr><td>DGT_DOUBLECOUNT</td><td>Raters place same effect in multiple cells inconsistently.</td><td>Add redundancy-handling examples.</td></tr>
</table>

## Case packet standard

- Decision boundary and baseline.

- Option set with 2-5 options.

- Stakeholder-instance map and active Union Scopes.

- Evidence packet, including what is known, unknown, contested, and assumed.

- Rights Floor, TRC, and CSV pre-screen notes.

- RLS scoring sheet for every option.

- Rater confidence and rationale fields.

- Adjudication sheet that preserves raw scores before consensus.

- Post-analysis revision notes.

## Synthetic case roster

<table>
<tr><td>Case</td><td>Title</td><td>Purpose</td></tr>
<tr><td>C01</td><td>AI tutor in public schools</td><td>Compare mandatory deployment, opt-in teacher-supervised deployment, and no deployment for a public-school AI tutor.</td></tr>
<tr><td>C02</td><td>Flood relocation policy</td><td>Compare voluntary relocation support, mandatory relocation, and infrastructure-only flood protection for a high-risk community.</td></tr>
<tr><td>C03</td><td>Agricultural pesticide decision</td><td>Compare current pesticide use, restricted integrated pest management, and rapid ban with transition subsidy.</td></tr>
<tr><td>C04</td><td>Hospital triage support system</td><td>Compare clinician-only triage, advisory AI triage, and automated triage for non-emergency scheduling.</td></tr>
<tr><td>C05</td><td>Social-media moderation rule</td><td>Compare minimal moderation, rights-protecting graduated moderation, and aggressive automated removal.</td></tr>
<tr><td>C06</td><td>Welfare fraud detection model</td><td>Compare manual review, AI risk flagging with human appeal, and automated benefit suspension.</td></tr>
<tr><td>C07</td><td>Urban traffic redesign</td><td>Compare car-priority road widening, bus/bike corridor redesign, and congestion pricing with equity rebates.</td></tr>
<tr><td>C08</td><td>Renewable microgrid project</td><td>Compare no project, community-owned solar microgrid, and vendor-owned microgrid with long lock-in contract.</td></tr>
<tr><td>C09</td><td>School phone policy</td><td>Compare unrestricted use, blanket ban, and structured phone zones with exceptions and student voice.</td></tr>
<tr><td>C10</td><td>Local data center proposal</td><td>Compare approval as proposed, approval with water/energy/community safeguards, and rejection pending regional capacity review.</td></tr>
</table>

## 49-cell welfare dictionary - compact validation version

This compact dictionary is extracted against the Canon Appendix AD role: it supports scoring interpretation and reviewer literacy. It does not modify gates, thresholds, equations, or claim boundaries.

<table>
<tr><td>Cell</td><td>Label</td><td>Plain meaning</td><td>Reviewer check</td></tr>
<tr><td>U1/D1</td><td>Personal Resources</td><td>An individual&#x27;s economic security: income, savings, housing stability, and access to the material means of a decent life.</td><td>A reviewer checks whether the income/housing change is measured against a declared baseline cohort, not anecdote.</td></tr>
<tr><td>U1/D2</td><td>Personal Health</td><td>The individual&#x27;s physical and mental health, safety, and bodily integrity.</td><td>A reviewer asks whether a claimed health gain rests on outcome data or only on inputs (e.g. clinics built ≠ health improved).</td></tr>
<tr><td>U1/D3</td><td>Relationships</td><td>The quality and stability of a person&#x27;s close personal relationships and social connection.</td><td>A reviewer challenges whether a relationship claim is evidenced or inferred from a proxy like attendance.</td></tr>
<tr><td>U1/D4</td><td>Learning</td><td>The individual&#x27;s access to education, skills, and the capacity to learn and develop.</td><td>A reviewer asks whether learning outcomes are demonstrated or only opportunity offered.</td></tr>
<tr><td>U1/D5</td><td>Personal Agency</td><td>The person&#x27;s real ability to choose, refuse, consent, act, and shape their own life path.</td><td>A reviewer tests whether consent was genuine and revocable, or merely formal.</td></tr>
<tr><td>U1/D6</td><td>Purpose</td><td>The individual&#x27;s sense of meaning, dignity, and worth in their life and work.</td><td>A reviewer distinguishes a genuine dignity effect from sentiment unsupported by experience data.</td></tr>
<tr><td>U1/D7</td><td>Local Conditions</td><td>The immediate physical environment a person lives in: air, noise, water, hazards, and surroundings.</td><td>A reviewer checks measured exposure change against the affected location, not a city-wide average.</td></tr>
<tr><td>U2/D1</td><td>Household Resources</td><td>The economic security of the household unit: shared income, assets, housing, and ability to meet needs.</td><td>A reviewer asks whether the household, not just the earner, is the measured unit.</td></tr>
<tr><td>U2/D2</td><td>Household Health</td><td>The collective physical and mental health and safety of household members, including dependents.</td><td>A reviewer checks that dependents and caregivers are scored separately, not blended into one household figure.</td></tr>
<tr><td>U2/D3</td><td>Family Cohesion</td><td>The strength, stability, and supportive quality of relationships within the household.</td><td>A reviewer asks whether a cohesion claim rests on outcomes or on assumed effects of a program.</td></tr>
<tr><td>U2/D4</td><td>Shared Learning</td><td>The household&#x27;s collective access to information, education, and learning capacity.</td><td>A reviewer checks access actually reaches the household, not just the area.</td></tr>
<tr><td>U2/D5</td><td>Household Agency</td><td>The household&#x27;s collective ability to make decisions, plan, and control its own circumstances.</td><td>A reviewer tests whether household choice is real or constrained by conditions.</td></tr>
<tr><td>U2/D6</td><td>Family Meaning</td><td>The household&#x27;s shared sense of identity, belonging, dignity, and purpose.</td><td>A reviewer separates a real meaning effect from program rhetoric.</td></tr>
<tr><td>U2/D7</td><td>Home Environment</td><td>The physical environmental quality of the home and its immediate setting.</td><td>A reviewer checks measured home conditions, not self-report alone.</td></tr>
<tr><td>U3/D1</td><td>Local Resources</td><td>The shared economic resources, infrastructure, and services available to a local community.</td><td>A reviewer asks whether the benefit is genuinely shared or captured by a subgroup.</td></tr>
<tr><td>U3/D2</td><td>Community Health</td><td>The collective physical and mental health and safety of the local population.</td><td>A reviewer checks whether subgroup harms are masked by a favourable community average.</td></tr>
<tr><td>U3/D3</td><td>Community Cohesion</td><td>The quality of trust, cooperation, belonging, safety, and relational fabric within a community.</td><td>A reviewer asks whether cohesion gains for some came via exclusion of others.</td></tr>
<tr><td>U3/D4</td><td>Local Knowledge</td><td>The community&#x27;s shared knowledge, information access, and local expertise.</td><td>A reviewer checks consent and ownership of the knowledge claimed as preserved.</td></tr>
<tr><td>U3/D5</td><td>Community Agency</td><td>The community&#x27;s collective capacity to organise, participate, and influence decisions affecting it.</td><td>A reviewer tests whether participation was substantive or a procedural formality.</td></tr>
<tr><td>U3/D6</td><td>Shared Meaning</td><td>The community&#x27;s shared identity, culture, dignity, and sense of collective purpose.</td><td>A reviewer separates a genuine cultural effect from a symbolic gesture.</td></tr>
<tr><td>U3/D7</td><td>Local Ecology</td><td>The ecological condition of the community&#x27;s local environment: green space, biodiversity, water, land.</td><td>A reviewer asks whether &#x27;no local effect&#x27; was measured or merely assumed.</td></tr>
<tr><td>U4/D1</td><td>Organizational Resources</td><td>An organization&#x27;s operating means: finances, capital, staffing, and capacity to function and deliver.</td><td>A reviewer checks whether the organizational gain creates uncosted externalities in other cells (the classic &#x27;operating resources up, U7 down&#x27; trap).</td></tr>
<tr><td>U4/D2</td><td>Organizational Safety</td><td>The safety of people within and affected by the organization: workers, users, and the public.</td><td>A reviewer checks whether reported safety reflects outcomes or only paperwork compliance.</td></tr>
<tr><td>U4/D3</td><td>Organizational Culture</td><td>The internal relational health of the organization: trust, fairness, inclusion, and cooperation.</td><td>A reviewer asks whether culture data is independent or self-reported by leadership.</td></tr>
<tr><td>U4/D4</td><td>Knowledge Systems</td><td>The organization&#x27;s knowledge, data integrity, institutional memory, and learning systems.</td><td>A reviewer tests whether claimed integrity is verifiable or asserted.</td></tr>
<tr><td>U4/D5</td><td>Role Agency</td><td>The meaningful autonomy, voice, and fair treatment of individuals in their organizational roles.</td><td>A reviewer checks whether voice mechanisms produce outcomes or are decorative.</td></tr>
<tr><td>U4/D6</td><td>Mission Coherence</td><td>The alignment between the organization&#x27;s stated purpose and its actual conduct and effects.</td><td>A reviewer asks whether coherence is evidenced by conduct or only by restated values.</td></tr>
<tr><td>U4/D7</td><td>Operational Footprint</td><td>The environmental impact of the organization&#x27;s operations: emissions, waste, resource use, land.</td><td>A reviewer checks footprint against measured externalities, not offset claims alone.</td></tr>
<tr><td>U5/D1</td><td>Public Resources</td><td>The polity&#x27;s fiscal and material capacity: public finances, infrastructure, and provisioning.</td><td>A reviewer checks whether gains are sustainable or borrowed from the future.</td></tr>
<tr><td>U5/D2</td><td>Population Health</td><td>The health, safety, and mortality outcomes of the whole population within a polity.</td><td>A reviewer checks whether worst-case scenarios were bounded with a tail measure, not averaged away.</td></tr>
<tr><td>U5/D3</td><td>Legitimacy</td><td>The rule of law, due process, accountability, and perceived legitimacy of public institutions.</td><td>A reviewer tests whether legitimacy is measured independently or claimed by the institution being assessed.</td></tr>
<tr><td>U5/D4</td><td>Information Access</td><td>The polity&#x27;s information environment: access, transparency, free expression, and epistemic integrity.</td><td>A reviewer checks whether transparency is real and usable or nominal.</td></tr>
<tr><td>U5/D5</td><td>Civil Agency</td><td>People&#x27;s ability to participate in public life, exercise rights, contest authority, and influence governance.</td><td>A reviewer tests whether civic participation is enforceable or merely nominal, and whether any group is selectively excluded.</td></tr>
<tr><td>U5/D6</td><td>Public Meaning</td><td>Shared civic identity, dignity, social contract, and non-domination across the polity.</td><td>A reviewer separates symbolic recognition from changes people actually experience.</td></tr>
<tr><td>U5/D7</td><td>Public Environment</td><td>The environmental quality and ecological sustainability managed at the polity scale.</td><td>A reviewer checks whether environmental-justice distribution was assessed, not just regional totals.</td></tr>
<tr><td>U6/D1</td><td>Global Resources</td><td>Humanity&#x27;s shared material base: global resource stocks, critical supply chains, and common infrastructure.</td><td>A reviewer checks whether &#x27;global&#x27; claims rest on global data or extrapolated local figures.</td></tr>
<tr><td>U6/D2</td><td>Human Safety</td><td>The safety and survival of humanity at large, including existential and catastrophic risk.</td><td>A reviewer checks that tail risk was bounded with a worst-case measure and not diluted by expected-value framing.</td></tr>
<tr><td>U6/D3</td><td>Cooperation</td><td>The capacity of humanity to coordinate, cooperate, and maintain peaceful, stable relations at scale.</td><td>A reviewer asks whether cooperation is durable or a fragile short-term arrangement.</td></tr>
<tr><td>U6/D4</td><td>Civilizational Knowledge</td><td>Humanity&#x27;s accumulated knowledge, science, and the integrity and safety of its knowledge systems.</td><td>A reviewer checks whether knowledge benefits were weighed against misuse and proliferation pathways.</td></tr>
<tr><td>U6/D5</td><td>Collective Agency</td><td>Humanity&#x27;s capacity for self-determination and legitimate collective decision-making at the species scale.</td><td>A reviewer tests whether &#x27;collective&#x27; agency includes the marginalised or only powerful actors.</td></tr>
<tr><td>U6/D6</td><td>Shared Purpose</td><td>Humanity&#x27;s shared sense of meaning, moral direction, and long-term orientation toward flourishing.</td><td>A reviewer flags this cell as especially prone to rhetoric and demands concrete mechanisms.</td></tr>
<tr><td>U6/D7</td><td>Planetary Conditions</td><td>The condition of planetary systems that support human civilisation and coordinated managing intelligence.</td><td>A reviewer checks whether irreversibility and worst-case bounds were modelled, not just expected outcomes.</td></tr>
<tr><td>U7/D1</td><td>Life-Support Resources</td><td>The biosphere&#x27;s foundational resources that sustain life: soil, fresh water, clean air, fertility.</td><td>A reviewer checks whether renewal rates, not just current stocks, were assessed.</td></tr>
<tr><td>U7/D2</td><td>Ecosystem Health</td><td>The health, function, and viability of ecosystems and the species within them.</td><td>A reviewer checks whether ecosystem-function evidence exists or only a single charismatic indicator.</td></tr>
<tr><td>U7/D3</td><td>Biotic Relations</td><td>The integrity of relationships and interdependencies among living systems and between humans and nature.</td><td>A reviewer asks whether relational/cascade effects were modelled or ignored as &#x27;no direct effect&#x27;.</td></tr>
<tr><td>U7/D4</td><td>Ecological Knowledge</td><td>Ecological information-bearing/enabling-condition view only under the Canon U7 construct rule; human understanding and monitoring have primary human or institutional D4 homes and no duplicate U7 RLS mass.</td><td>A reviewer checks that absent ecological data is marked unknown, not scored as 0 (&#x27;no effect&#x27;).</td></tr>
<tr><td>U7/D5</td><td>Resilience Capacity</td><td>The biosphere&#x27;s capacity to absorb shocks, adapt, and recover from disturbance.</td><td>A reviewer asks whether proximity to thresholds was assessed, not just current condition.</td></tr>
<tr><td>U7/D6</td><td>Life Continuity</td><td>The continuity and persistence of life and biodiversity over time, including irreversibility of loss.</td><td>A reviewer checks whether irreversibility was treated as a tail constraint, not a discountable cost.</td></tr>
<tr><td>U7/D7</td><td>Ecological Integrity</td><td>The overall health, resilience, diversity, and continuity of ecosystems as living support systems.</td><td>A reviewer checks whether integrity is evidenced by ecosystem-level data or inferred from a single metric.</td></tr>
</table>

## Recommended additions to the release ecosystem

Add the following as companion, non-governing materials. They should be versioned separately from the core canon unless a future release explicitly promotes part of them into normative core.

<table>
<tr><td>Artifact</td><td>Role</td></tr>
<tr><td>RippleLogic_RLS_Validation_Protocol_v2.9</td><td>Study protocol, rater instructions, hypotheses, analysis plan, and revision rules.</td></tr>
<tr><td>RLS_Validation_Workbook_v0.3</td><td>Rater-entry and analysis-prep workbook.</td></tr>
<tr><td>RLS_Calibration_Note_v1.0</td><td>Future results document after the first scoring sprint.</td></tr>
<tr><td>Case_Packets/</td><td>Folder for frozen synthetic and real shadow-mode case packets.</td></tr>
</table>

## Proposed README wording

Current status: RLS is specification-ready and audit-ready as a structured residual welfare-ranking specification and audit method. Empirical validation of dimensional independence, inter-rater reliability, and decision-performance advantage is a next-stage research priority. The RLS Validation Protocol provides the study design for testing these claims through scored cases, independent raters, reliability statistics, and correlation/factor analysis of the 49-cell welfare field.

## Completion definition for the first sprint

- At least 10 cases scored independently by at least 3 raters.

- All raw rater scores preserved.

- Completion, missingness, and disagreement statistics produced.

- IRR reported for score, ranking, and key classifications where applicable.

- Correlation or redundancy heatmap produced over the 49 cells.

- At least one scalar or reduced-matrix comparator run.

- Revision log produced with exact cells, anchors, or instructions needing repair.

- Public claim boundary updated: exploratory, preliminary, validated for limited domain, or not validated.

## Physical-admissibility validation extension

The v12-line research ladder, introduced at v12.0 and retained in the current v13.0 candidate, treats physical admissibility claims as a separate validation surface from governance mandate and authorization. Future validation runs should measure whether reviewers can reliably distinguish: governance authorization only, physical admissibility supported within the declared validity domain, physical admissibility not established, and physical admissibility contraindicated.

This extension does not test whether MathGov computes physics. It tests whether MathGov records the correct evidence boundary and refuses to overclaim physical safety when the domain evidence is missing or insufficient.

## Minimum successful first validation report

A first RLS validation report should publish, at minimum:

<table>
<tr><td>Required output</td><td>Purpose</td></tr>
<tr><td>Raw rater score CSV</td><td>Allows independent review of cell-level ratings and missingness.</td></tr>
<tr><td>Adjudication log</td><td>Shows how disagreements, uncertainty, and gate-relevant disputes were handled.</td></tr>
<tr><td>ICC / alpha results</td><td>Reports the preregistered reliability estimators and variants, uncertainty, missingness, contingency counts where relevant, and any separately justified internal-consistency analysis; these are distinct claims.</td></tr>
<tr><td>Disagreement heatmaps</td><td>Reveals unstable cells, dimensions, or union scopes.</td></tr>
<tr><td>Revision register</td><td>Records proposed changes to definitions, examples, thresholds, or training material.</td></tr>
<tr><td>Claim-boundary update</td><td>States what the results do and do not validate.</td></tr>
</table>

## mandatory conformance vectors

### Single-source and vector mapping rule (Normative for protocol conformance).

<table>
<tr><td>RLSV extension family</td><td>Canon control / mapping</td><td>Purpose</td></tr>
<tr><td>RLSV-IRR-*</td><td>Canon §17.4A</td><td>Reliability and disagreement studies.</td></tr>
<tr><td>RLSV-RANK-*</td><td>Appendix R decisiveness, masking, and non-selectability vectors</td><td>Ranking and refusal behavior.</td></tr>
<tr><td>RLSV-DEP-*</td><td>Appendix R.20 dependence-sensitivity stress</td><td>Dependence-cluster robustness.</td></tr>
<tr><td>RLSV-BOUNDARY-*</td><td>Appendix R category, rights, tail, CSV, and claim-boundary vectors</td><td>Construct and interface discrimination.</td></tr>
</table>

Canon §17.4A controls IRR targets and Canon Appendix R controls framework conformance vectors. This protocol operationalizes those targets. Protocol-specific extensions use the RLSV- prefix and MUST state the Appendix R vector or invariant they extend; they do not create an independent framework-conformance authority.

The validation suite must include at least the following deterministic conformance cases before empirical claims are considered:

- one-month categorical bodily-integrity violation: RF/NCRC must fail regardless of short duration;

- one-year arbitrary detention: RF/NCRC must fail or return unknown/escalate if the categorical profile is unresolved;

- low-probability lethal exposure: a severe-hazard probability bound and governed tolerance are required; missing fields cannot pass;

- every option fails TRC while safe delay is available: Tail Emergency Mode must not activate;

- every option fails TRC in a demonstrated emergency: only a below-absolute-cap provisional least-CVaR option may proceed, with no ordinary RLS;

- non-default κ values that would produce an unnormalized raw score above 1: normalized RLS must remain within [-1,+1];

- active masks that change effective weight mass: score scale must remain invariant under normalization;

- uncertain equal-and-opposite impact instances: Method B uncertainty must remain positive through pre-cancellation contribution mass; a leader that clears the second-ranked option but fails discrimination against another selectable contender must not receive a unique-selection claim.

## Current-package Tier-Integrity Conformance Vectors (Normative for protocol conformance)

The validation package MUST include the following cases:

- TIER2_CSV_REQUIRED_BEFORE_RLS: an option passes NCRC and TRC but has no CSV status. Expected: no ordinary RLS selection claim; route to CSV review or refusal.

- TIER2_CSV_NOT_MATERIAL_WITH_RATIONALE: a low-structural-materiality option records the rationale and may enter RLS.

- TIER2_CSV_REDESIGN_REQUIRED_BLOCKS_RLS: an option with CSV_REDESIGN_REQUIRED is excluded before scoring.

- TRC_ALL_FAIL_SAFE_DELAY: expected redesign/delay/refusal; minimum CVaR does not create selection.

- TAIL_EMERGENCY_PREREQUISITE_MISSING: expected TAIL_EMERGENCY_REFUSED or escalation.

- TAIL_EMERGENCY_FULL_PREREQUISITES: minimum-CVaR provisional action is allowed only inside Tail Emergency Mode, with ordinary RLS disabled.

- RIGHTS_UNKNOWN_NOT_ZERO: missing material rights evidence returns an unknown/refusal posture rather than a zero impact.

- RLS_ZERO_ACTIVE_MASS: returns RLS_NO_ACTIVE_MASS, not zero.

## Formal-Integrity and Selection-Claim Validation Programme

Supplemental synthetic regression: adverse-confidence reversal (implements Canon R.25). Stipulate all qualification and evidence conditions separately; use one active ordinary-welfare cell, q/Q=1, NONE, beta=2. Option A has pre-confidence contributions +0.20 at c=1 and -0.18 at c=0.1; option B has +0.10 at c=1. Other instance multipliers are 1. Declared scores are tanh(0.364)=0.3487324660 for A and tanh(0.2)=0.1973753202 for B. The required adverse-confidence counterfactual yields tanh(0.04)=0.0399786803 for A; B is unchanged. The leader reverses. Expected: CONFIDENCE_RANK_SENSITIVE and no unique framework selection. NOT_TRIGGERED_WITH_RATIONALE is not valid merely because the run is Tier 2 or the nominal leader is convenient. This fixture is a test of the existing trigger/refusal rule, not measured welfare or an assertion of a real gate pass.

Supplemental synthetic regression: cross-option adverse dependence (implements the existing dependence module). Hold scores at A=0.032, B=0, final-score sigma_A=sigma_B=0.010, epsilon=0.000001 and delta=2. Nominal SignedGap is 0.032/sqrt(0.000201), above 2. With a supported pairwise rho=-1, SignedGap is 0.032/sqrt(0.000401), below 2. Expected: RLS_DEPENDENCE_SENSITIVE, non-decisive framework result and full disclosure of the nominal and adverse variants. An independent-error fixture with non-material cross-option dependence retains the nominal calculation. Test zero-sigma covariance handling, invalid rho, non-finite input, inconsistent joint covariance and unsupported proxy interpretation separately. These are stipulated regression inputs, not empirical error estimates.

This candidate retains the v2.7 specification tests for RightsEffectToken non-dilution; token and temporal partitioning; probability operator order; adverse confidence; distributional/subgroup washout; reference and baseline families; comparison-mask symmetry; uncertainty dependence and numerical guards; weight-profile disagreement; option-set closure; and robustness completeness.

Formal vectors establish whether an implementation follows the Canon. They do not establish construct validity, inter-rater reliability, predictive validity, external validity, decision superiority, legal authority, physical safety, deployment readiness, or moral truth.

The reliability programme SHALL separately measure effect-token individuation, primary dimension assignment, subgroup discovery, likelihood-semantics classification, reference/baseline selection, robustness-trigger status, and final ranking. Agreement on a final score without agreement on these upstream constructions is insufficient.

Comparative pilots SHOULD test the full Core against a qualify-first equal-weight matrix and a qualify-first profile-only comparator, plus a documented constrained MCDA method where a claim about MCDA is made. Match the information, option set, noncompensatory constraints and analyst resources fairly. Incremental decision value must be earned rather than presumed. A causal superiority claim additionally requires the claim-specific identification plan specified by MFDI and PC-AEP; pre/post change alone is not a treatment-effect estimate.

<table>
<tr><td>Study family</td><td>Minimum v2.9 output</td></tr>
<tr><td>Formal invariance</td><td>Reproduce all retained regression vectors plus Canon Appendix R.34–R.37 (every-contender/sole-survivor, aggregate protected-event risk bound, Tier 1 tail-screen completeness, and scenario-discovery completeness), including the expected refusal or escalation states.</td></tr>
<tr><td>Inter-rater reliability</td><td>Token identity, dimension, subgroup, likelihood, reference/baseline, CSV, RLS ranking</td></tr>
<tr><td>Construct validity</td><td>Convergent/discriminant tests; cross-cultural/substrate limitations</td></tr>
<tr><td>Predictive validity</td><td>Pre-registered sign, magnitude and ranking forecasts versus outcomes. ExactSignAccuracy = exact predicted/observed sign matches divided by evaluated cells; the v12.8 SignAcc alias denotes this exact metric. PartialSignScore retains the former half-credit treatment of unmatched zeros as a separately labelled diagnostic, with no acceptance target. Freeze the zero/deadband rule, evaluation set, no-change and majority baselines, adverse/beneficial class measures, case dependence and uncertainty. The legacy 0.70 number is retained only as a provisional research target; acceptance requires metric-specific justification and preregistered adoption, with no automatic transfer from the former partial-credit metric. Neither that target nor an exact-match score alone establishes predictive skill.</td></tr>
<tr><td>Anti-gaming</td><td>Adversarial split/merge, omission, masking, reference, confidence and option-set attacks</td></tr>
<tr><td>Comparator study</td><td>Error, burden, reconstructability and decision utility versus simpler alternatives</td></tr>
</table>

Also reproduce Canon R.38A alongside the retained R.38, including its cell-level interval and dependence construction, correct conditional decisive outcome, and blocked variants. This is a synthetic conformance test, not evidence of empirical uncertainty calibration, improved real-world decisions or execution authorization. Method B selection claims must additionally satisfy the Canon Section 10.3.2 transformation-consistency rule.

## Appendix: Current-package source-integrity vectors

<table>
<tr><td>ID</td><td>Input</td><td>Required result</td></tr>
<tr><td>MPS-HYPOTHESIS-01</td><td>RLS ranking changes between h=0 and h=1 for a non-FPP stakeholder with decision-material MPS evidence.</td><td>MPS_HYPOTHESIS_SENSITIVE; no convenient intermediate coefficient; preserve multiple options, seek evidence, apply precaution, narrow, or refuse.</td></tr>
<tr><td>MPS-NE-01</td><td>Target boundary is valid but admissible evidence is insufficient or observability is poor.</td><td>MPS-NE; no conversion to MPS-0, zero, or a scalar multiplier.</td></tr>
<tr><td>UCI-NA-01</td><td>U1 Equity is inapplicable; H=F=R=0.</td><td>E is NA, remaining weights renormalize, UCI=0; no fixed perfect equity value.</td></tr>
<tr><td>UCI-UNKNOWN-01</td><td>A governed within-self equity instrument is applicable but evidence is missing.</td><td>E is UNKNOWN and the claim is narrowed/escalated; it is not NA or 1.</td></tr>
<tr><td>RIGHTS-HAZARD-01</td><td>Credible fatality pathway with intrinsic severity 0.80 and non-negligible exposure.</td><td>Severe-rights-hazard channel activates independently of LIFE floor threshold 0.90.</td></tr>
<tr><td>GATE-BOUND-01</td><td>Low-confidence adverse catastrophe or material CSV instance could change a gate.</td><td>Apply the deterministic adverse bound; if not reproducible, return UNKNOWN/ESCALATE/NARROW/REFUSE, never a confidence-discounted pass.</td></tr>
<tr><td>RLS-FULL-MASK-01</td><td>Eight nonzero cells, all 49 cells active with explicit evidence-backed zeros.</td><td>Q=1 and normalized RLS equals the contribution sum.</td></tr>
</table>

# APPENDIX RELEASE: Identity, Source Authority and Revision Record

Framework release: MathGov/RippleLogic v13.0. Component: RLS Validation Protocol v2.9. Edition-origin preparation: 10 September 2026; the separately identified correction build is dated below. Two-part major.minor component versions are used; preserved historic identifiers are not renumbered.

Status: integrated research and teaching specification with a bounded worked-example and scoped reference implementation. Readiness is limited to the checks in Reports/Verification_and_Readiness.md. No empirical validation, independent human validation, full production runtime, physical-safety certification, legal authority, deployment authorization or Tier-4 ProofPack status is implied by the edition number.

Delivery identity: MathGov/RippleLogic v13.0, build MG-RL-13.0-20260923-RELEASE-G. Prepared 23 September 2026 from the supplied frozen publication archive. Only reproduced defects and approved clarifications were patched; component editions are unchanged. The manifest identifies the exact current bytes and the preserved baseline. This is a new correction build, not a silent replacement of the earlier frozen artifact. Live publication is not asserted.

Component/build identity. Aligners Sheet v5.9 retains its component edition but carries this correction build’s identifier. Its numerical inputs, calculation formulas and worked verdict are unchanged; label, runtime-token and integrity-snapshot corrections are itemized in Verification/Exact_Workbook_Changes.json. Exact hashes, rather than filenames or edition labels alone, distinguish the new bytes from Release D and the previous frozen publication.

Verification boundary: Reports/Verification_and_Readiness.md and Verification/Final_G/ contain the current build’s executed checks and limitations. Earlier verification and the rejected compatibility experiment belong to the preserved baseline and do not certify changed bytes. Cache-independent replay, stored-formula and native-engine results are separate evidence surfaces. Microsoft Excel parity, full external-registry conformance, empirical validation and production authorization are not asserted.

Package source authority: Core_15 contains 14 DOCX specification masters and one XLSX Aligners frozen worked-run workbook. DOCX files control prose, equations and tables subject to Canon and SGP ownership. The workbook controls only its disclosed exemplar surfaces. Sources, Reading_HTML and Reading_PDFs are generated reading projections, not competing normative masters. The manifest and hashes identify exact bytes; supplemental code and schemas govern only their documented subset. Conflicts require recorded correction against the controlling source.

License and reuse: consult the package-level LICENSE and NOTICE and retain applicable component-specific and third-party notices. This pointer does not override a valid exception or grant rights over separately supplied private or third-party review material.

External repository publication and any absent legacy schema/validator/registry are separate authorities/evidence surfaces. The local package does not claim to update a remote repository or reproduce unavailable implementations. Current source pointers in this appendix replace prior front-matter edition pointers for this package; accurate historical source references below are retained as lineage only.

Preserved invariants: RG -&gt; RF/NCRC -&gt; TRC -&gt; CSV -&gt; RLS; rights non-compensation and unallocated rights effects; existing seven rows and seven dimensions; existing SGP MPS/FPP/GPR/SPR/ICP/RMCP separation; probability ownership, uncertainty, stability and every-contender rules; selection, authority and execution separation.

<table>
<tr><td>Component</td><td>Current edition</td></tr>
<tr><td>RippleLogic Canon</td><td>v13.0</td></tr>
<tr><td>Sentience Gradient Protocol</td><td>v8.8</td></tr>
<tr><td>ripple.md Standard</td><td>v5.8</td></tr>
<tr><td>RippleLogic Agent System</td><td>v13.0</td></tr>
<tr><td>CSV Gate Standard</td><td>v2.7</td></tr>
<tr><td>RippleLogic Cascade Standard</td><td>v2.9</td></tr>
<tr><td>MathGov Reproducibility and Use Standard</td><td>v1.7</td></tr>
<tr><td>Welfare Dimension Boundary and Interaction Protocol</td><td>v1.9</td></tr>
<tr><td>RLS Validation Protocol</td><td>v2.9</td></tr>
<tr><td>RippleLogic Foundations Primer</td><td>v4.7</td></tr>
<tr><td>MathGov Public Introduction</td><td>v13.0</td></tr>
<tr><td>Physical/Causal Admissibility Evidence Profile</td><td>v2.6</td></tr>
<tr><td>Methodological Falsifiability and Dependency Integrity Standard</td><td>v2.6</td></tr>
<tr><td>Source-Coupling Integrity Standard</td><td>v2.6</td></tr>
<tr><td>RippleLogic Aligners Sheet</td><td>v5.9</td></tr>
</table>

Change locations and rationales: Reports/Audit_Adjudication_and_Changes.md; exact edits: Verification/Exact_Document_Changes.json and Exact_Workbook_Changes.json. Navigation and metadata records are separate. Prior releases and feedback are preserved in the complete provenance archive.

Current proposals are not universal truths. Taxonomy maximality, continuous-time propagation, cross-substrate cardinal welfare, generic susceptibility/shield formulas, autonomous recovery, vendor infrastructure, zero-knowledge circuits and hardware meshes remain unvalidated unless independently demonstrated under a scoped implementation profile.

<!-- HISTORICAL_RELEASE_START: non-controlling -->

## Preserved Baseline Release Material (Historical; Non-Controlling)

The following blocks are relocated intact from the recovered baseline. Their edition numbers, release-readiness wording and external-source limitations describe that historical candidate, not current component identity or newly executed verification. Governing current metadata is the matrix above.

## v2.8-rc2 Historical Release Integration

HISTORICAL (NON-CONTROLLING): Release: MathGov Core Release 2026.09 — RippleLogic Canon v12.8-rc2 / SGP v8.7-rc2 — Controlled Adversarial-Audit Correction Candidate

<table>
<tr><td>Release control</td><td>Historical value</td></tr>
<tr><td>Component</td><td>RLS Validation Protocol v2.8-rc2</td></tr>
<tr><td>Release</td><td>HISTORICAL (NON-CONTROLLING): MathGov Core Release 2026.09 — RippleLogic Canon v12.8-rc2 / SGP v8.7-rc2</td></tr>
<tr><td>Architecture</td><td>RG → RF/NCRC → TRC → CSV → RLS</td></tr>
<tr><td>Role</td><td>Formal, reliability, validity, anti-gaming, and comparative study protocol for RLS and its retained v12.7 integrity controls and v12.8-rc2 corrections.</td></tr>
<tr><td>Claim boundary</td><td>Controlled Tier 1–3 research specification candidate; not empirical validation, legal authority, physical-safety certification, deployment authorization, Tier 4, or moral truth.</td></tr>
<tr><td>Source/render parity</td><td>Versioned semantic source and DOCX/PDF mirrors must agree. Filename, internal version, active pins, manifest, and hashes must agree; mismatch is release-integrity failure.</td></tr>
</table>

## Historical Release Integration (v2.8-rc2)

HISTORICAL (NON-CONTROLLING): This controlled candidate advances RippleLogic RLS Validation Protocol from v2.7 to v2.8-rc2 and binds it to MathGov Core Release 2026.09 — RippleLogic Canon v12.8-rc2 / SGP v8.7-rc2. The original release is preserved. Historical references remain lineage only; active references use the candidate component-version map. Publication, semantic-source parity and implementation conformance are not established by this reading-copy candidate.

Historical companion pins: Canon v12.8-rc2; SGP v8.7-rc2; ripple.md v5.7-rc2; Agent System v12.7-rc2; CSV v2.6-rc2; Cascade v2.8-rc2; Reproducibility v1.6-rc2; WDBIP v1.8-rc2; RLS Validation v2.8-rc2; Primer v4.6-rc2; Public Introduction v12.8-rc2; PC-AEP/MFDI/Source-Coupling v2.5-rc2; Aligners Sheet v5.8-rc1.

## Historical Patch Note (non-controlling)

v2.4 synchronizes normative vector headings and package references. The study design, claim boundaries, and validation hypotheses remain unchanged.

Companion validation protocol for MathGov Core Release 2026.09 and the RippleLogic Canon.

<!-- HISTORICAL_RELEASE_END -->
