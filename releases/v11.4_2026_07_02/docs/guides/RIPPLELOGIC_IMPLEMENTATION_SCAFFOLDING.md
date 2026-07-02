# RippleLogic Implementation Scaffolding

**Status:** Informative implementation guidance. This document does not override the RippleLogic Canon, SGP, Agent System, or ripple.md Standard.

**Purpose:** Provide practical scaffolding for early testing, training, pilot design, and low-to-medium-stakes use while preserving the full cascade.

## 1. Status and use boundary

This document provides implementation scaffolding for RippleLogic.

It includes:

1. provisional measurement heuristics for the seven welfare dimensions;
2. PCC profiles from lightweight to full audit;
3. minimum viable institutional requirements for Tier 3 use;
4. fast-path rules for low-stakes decisions;
5. escalation triggers;
6. validation pathway notes.

These are not validated instruments. They do not create ProofPack status. They do not certify deployment. They do not weaken the Canon.

**Evidence-status cap:** These heuristics are training scaffolding. They are not the validated instruments required by the RLS Validation Protocol. A run using only these heuristics inherits **E1-E2 evidence status at most** unless stronger independent instruments, domain evidence, or calibration are supplied and documented.

The governing cascade remains:

**RG -> RF -> TRC -> CSV -> RLS**

The teaching line remains:

**Ground reality. Protect rights. Bound ruin. Preserve the structure. Score the ripples.**

## 2. Provisional measurement heuristics for RLS

### 2.1 Measurement status

The seven welfare dimensions are defined in the Canon. The heuristics below help raters begin structured scoring.

They are provisional. They should be used for:

- training;
- worked examples;
- early validation studies;
- rater calibration;
- pilot preparation.

They should not be described as validated psychometric, ecological, legal, or social-scientific instruments.

Any use must record:

- evidence source;
- uncertainty;
- confidence;
- missing data;
- affected groups;
- reviewer notes;
- whether the indicator is direct, proxy, or qualitative.

### 2.2 General scoring discipline

For each RLS cell, reviewers should ask:

1. What is the affected union scope?
2. What welfare dimension is being affected?
3. Is the effect positive, negative, mixed, or uncertain?
4. Is the evidence direct or proxy?
5. Is the effect short-term, long-term, reversible, or irreversible?
6. Are vulnerable or worst-affected groups hidden by averages?
7. Is this issue already handled by RF/NCRC, TRC, or CSV?
8. Is this residual welfare scoring, or a gate-relevant issue?

RLS must not double-count gate failures. If the issue is rights-floor, tail-risk, or structural-viability material, it must be handled at the appropriate earlier layer.

### 2.3 D1, Material conditions

**Core question:** Does the option affect resources, livelihood, shelter, infrastructure, time, labor burden, or economic security?

Possible indicators:

- household cost burden;
- income or livelihood effect;
- access to food, housing, transport, energy, tools, or services;
- work hours gained or lost;
- care burden;
- infrastructure reliability;
- financial vulnerability;
- debt exposure;
- resilience to shocks.

Evidence examples:

- budget data;
- expenditure surveys;
- service-access data;
- cost-benefit estimates;
- labor-time estimates;
- household interviews;
- infrastructure records;
- expert review.

Scoring guidance:

- Positive scores require clear material benefit, not merely institutional savings.
- Negative scores should include hidden burden shifts.
- For vulnerable groups, use worst-affected review rather than average-only estimates.

Common errors:

- treating cost savings to an institution as automatic welfare gain;
- ignoring unpaid labor;
- missing delayed dependency costs;
- failing to identify who absorbs the burden.

### 2.4 D2, Health and safety

**Core question:** Does the option affect physical health, mental health, bodily safety, survival conditions, disease exposure, injury risk, or stress?

Possible indicators:

- mortality risk;
- morbidity risk;
- injury exposure;
- disease exposure;
- access to healthcare;
- mental-health burden;
- stress exposure;
- safety incidents;
- fatigue or burnout;
- environmental-health exposure.

Evidence examples:

- health records;
- epidemiological evidence;
- clinical literature;
- risk assessments;
- safety reports;
- exposure data;
- worker or community testimony;
- expert medical review.

Scoring guidance:

- Severe but uncertain harms require gate-critical confidence handling.
- Low confidence must not be used to minimize severe adverse gate-relevant effects.
- Residual health benefits may be scored in RLS only after rights, TRC, and CSV issues are resolved.

Common errors:

- scoring health averages while missing worst-affected groups;
- treating mental health as secondary or non-material;
- ignoring long-latency harm;
- confusing absence of evidence with evidence of absence.

### 2.5 D3, Social and relational conditions

**Core question:** Does the option affect trust, belonging, family stability, caregiving, community cohesion, exclusion, stigma, conflict, or relational burden?

Possible indicators:

- family disruption;
- caregiver burden;
- social isolation;
- community trust;
- civic participation;
- conflict rate;
- stigma;
- group exclusion;
- relational dependency;
- social resilience.

Evidence examples:

- surveys;
- interviews;
- community consultation;
- social-trust indicators;
- participation records;
- conflict reports;
- ethnographic evidence;
- stakeholder mapping.

Scoring guidance:

- Consider effects on family and relational systems, not only individuals.
- Track whether benefits to one group increase social burden on another.
- Note whether affected groups had meaningful voice.

Common errors:

- treating social harm as anecdotal because it is qualitative;
- counting participation numbers without measuring trust or voice;
- ignoring stigma or exclusion effects.

### 2.6 D4, Knowledge and epistemic quality

**Core question:** Does the option affect access to truth, learning, transparency, explainability, informed consent, epistemic reliability, or ability to challenge claims?

Possible indicators:

- information access;
- transparency quality;
- explanation quality;
- error or misinformation risk;
- educational outcomes;
- source provenance;
- auditability;
- informed consent;
- appeal and challenge capacity.

Evidence examples:

- audit trails;
- educational data;
- explanation-quality review;
- source documentation;
- public communication review;
- expert challenge;
- misinformation analysis;
- user comprehension tests.

Scoring guidance:

- Strong claims require evidence proportional to claim strength.
- Generated content is not grounded evidence by itself.
- Epistemic harms can be rights-relevant where they affect consent, due process, or public accountability.

Common errors:

- treating fluency as evidence;
- hiding uncertainty;
- using opaque models for consequential claims without adequate explanation;
- failing to give affected parties a way to challenge.

### 2.7 D5, Agency and freedom

**Core question:** Does the option affect autonomy, choice, consent, control, procedural voice, appeal, exit, reversibility, or meaningful participation?

Possible indicators:

- opt-out ability;
- appeal process;
- informed consent;
- procedural voice;
- dependency lock-in;
- coercion risk;
- reversibility;
- user control;
- power asymmetry;
- ability to refuse without severe penalty.

Evidence examples:

- policy documents;
- consent forms;
- appeals records;
- legal review;
- user-interface review;
- affected-party testimony;
- governance review;
- institutional process analysis.

Scoring guidance:

- Nominal consent is weak where dependency or coercion is present.
- Agency losses may also trigger rights-floor review.
- Irreversible lock-in may require TRC or CSV escalation.

Common errors:

- treating choice as meaningful where exit is impossible;
- ignoring procedural power;
- measuring participation without measuring influence;
- treating automation as neutral when it reduces appeal or human review.

### 2.8 D6, Meaning and purpose

**Core question:** Does the option affect dignity, identity, vocation, cultural continuity, recognition, purpose, spirituality, memory, or existential orientation?

Possible indicators:

- dignity effects;
- cultural continuity;
- identity recognition;
- meaningful work;
- community memory;
- ritual or spiritual harm;
- humiliation or dehumanization;
- purpose and vocation;
- loss of valued role.

Evidence examples:

- qualitative testimony;
- cultural review;
- community consultation;
- ethnographic evidence;
- dignity-impact assessment;
- worker interviews;
- affected-party statements;
- historical or cultural analysis.

Scoring guidance:

- Meaning harms may be hard to quantify but still material.
- Do not reduce meaning to productivity.
- Cultural and dignity harms may become rights-relevant where severe.

Common errors:

- dismissing meaning because it is qualitative;
- treating cultural loss as low value because it lacks market price;
- ignoring humiliation or dehumanization;
- counting material gain while missing loss of role or dignity.

### 2.9 D7, Environmental and ecological conditions

**Core question:** Does the option affect ecological systems, habitat, climate, pollution, biodiversity, regeneration, environmental quality, or resource integrity?

Possible indicators:

- emissions;
- pollution;
- biodiversity impact;
- habitat disruption;
- land quality;
- water quality;
- air quality;
- waste;
- extraction burden;
- ecological resilience;
- resource regeneration.

Evidence examples:

- environmental impact assessments;
- climate models;
- ecological monitoring;
- pollution measurements;
- biodiversity surveys;
- hydrological data;
- land-use data;
- expert ecological review.

Scoring guidance:

- Environmental effects may appear in RLS, CSV, TRC, or rights review.
- Irreversible ecological harm may trigger TRC.
- Structural ecological dependency may trigger CSV.
- Do not treat unmeasured biosphere effects as neutral or perfect.

Common errors:

- localizing benefit while exporting ecological cost;
- ignoring delayed effects;
- using short time horizons for long ecological impacts;
- treating ecological integrity as optional.

## 3. Evidence quality levels

Use this evidence ladder for early scoring discipline.

| Level | Name | Description | Use |
|---|---|---|---|
| E0 | Unsupported | Claim lacks usable evidence | Do not score as grounded |
| E1 | Plausible proxy | Indirect or weak evidence | Exploratory only |
| E2 | Structured qualitative | Interviews, expert review, documented reasoning | Training or early pilot |
| E3 | Indicator-supported | Relevant indicators exist and are traceable | Tier 2 to early Tier 3 |
| E4 | Calibrated | Indicators have domain support and reviewer agreement | Tier 3 stronger use |
| E5 | Validated | Independent validation and replay exist | Future mature use |

Evidence level should be recorded per material claim, not merely per document.

## 4. PCC profiles

The Provenance and Compliance Certificate, or PCC, is the audit record for a decision run.

PCC profiles reduce unnecessary administrative burden while preserving the cascade. A lower profile changes documentation depth. It does not weaken RG, RF/NCRC, TRC, CSV, or RLS.

### 4.1 PCC-Lite

Use for:

- training;
- classroom examples;
- low-stakes personal decisions;
- exploratory analysis;
- early concept testing.

Required fields:

- decision question;
- options considered;
- evidence note;
- affected scopes;
- rights-risk screen;
- tail-risk screen;
- CSV screen;
- RLS summary if used;
- uncertainty note;
- decision state.

Not allowed:

- public deployment claim;
- legal certification claim;
- institutional approval claim;
- ProofPack claim;
- automated authority claim.

### 4.2 PCC-Core

Use for:

- serious internal decisions;
- organizational analysis;
- policy drafts;
- non-deployment review;
- internal AI governance review.

Required fields:

- decision owner;
- evidence register;
- claim boundary;
- options;
- affected unions;
- RF/NCRC screen;
- TRC scenario list;
- CSV status;
- RLS matrix or summary;
- uncertainty and dissent notes;
- reviewer role;
- final decision state.

### 4.3 PCC-Audit

Use for:

- Tier 3 review;
- high-stakes decisions;
- public-facing institutional decisions;
- contested decisions;
- rights-sensitive cases;
- tail-risk-sensitive cases;
- structural-viability-sensitive cases.

Required fields:

- full evidence register;
- source provenance;
- claim boundary;
- rights coverage;
- subgroup analysis;
- TRC scenario table;
- CSV evidence and controls;
- 49-cell RLS where material;
- sensitivity analysis;
- challenger notes;
- audit flags;
- signoff record;
- preserved Decision Note.

### 4.4 PCC-Agent

Use for:

- AI agents;
- tool-enabled systems;
- runtime decision systems;
- autonomous or semi-autonomous workflows.

Required fields:

- agent mode;
- tool authority boundary;
- hard controls;
- NEI firewall status;
- runtime logs;
- redaction policy;
- override record;
- refusal record;
- human authority boundary;
- rollback path;
- containment controls.

### 4.5 PCC-Public

Use for:

- public release;
- public justification;
- published worked runs;
- policy announcement;
- GitHub or website release.

Required fields:

- public summary;
- non-claims statement;
- evidence maturity statement;
- uncertainty disclosure;
- reviewer/challenger status;
- decision state;
- source artifact links;
- limitations;
- next validation step.

## 5. Fast-path rule

Fast path is a documentation profile, not an ethical exemption.

A decision may use a lighter PCC profile only where stakes are low, reversibility is high, and no material rights, tail-risk, or CSV concerns appear.

### 5.1 Fast-path admissibility

PCC-Lite or PCC-Core may be used only when:

- no plausible rights-floor violation is present;
- no catastrophic, irreversible, or ruin-path scenario is plausible;
- CSV risk is low or not material;
- affected parties are limited;
- possible harms are reversible;
- uncertainty does not change gate outcomes;
- no vulnerable subgroup bears disproportionate risk;
- no public deployment or institutional certification is claimed;
- no agentic execution authority is being granted.

### 5.2 Fast-path stop conditions

Escalate to PCC-Audit if any of the following appear:

- rights uncertainty;
- severe but low-confidence harm;
- catastrophic scenario;
- irreversible impact;
- structural viability concern;
- governance lock-in;
- dependency lock-in;
- affected-party challenge;
- vulnerable subgroup exposure;
- public-facing decision;
- agentic or automated execution;
- high disagreement between reviewers;
- evidence conflict that changes a gate outcome.

### 5.3 Final fast-path rule

Fast path may reduce paperwork. It may not weaken:

- Reality Grounding;
- Rights Floor/NCRC;
- TRC;
- CSV;
- RLS refusal discipline;
- non-claims;
- auditability.

## 6. Minimum viable institutional requirements for Tier 3 use

RippleLogic is a socio-technical protocol. It is not a fully automated moral algorithm.

A Tier 3 use requires roles, records, and challenge pathways.

### 6.1 Minimum roles

1. **Decision owner**  
   Holds lawful, organizational, or legitimate authority for the decision.

2. **Evidence steward**  
   Maintains evidence register, provenance, claim boundary, and uncertainty notes.

3. **Rights reviewer**  
   Reviews RF/NCRC, affected rights, worst-affected groups, and threshold risks.

4. **Tail-risk reviewer**  
   Reviews catastrophic, irreversible, lock-in, and ruin-path scenarios.

5. **CSV reviewer**  
   Reviews containment, execution feasibility, structural viability, dependency closure, reversibility, and controls.

6. **RLS scorer or scoring team**  
   Scores residual welfare only after prior layers survive.

7. **Independent challenger**  
   Searches for missing evidence, hidden harms, subgroup omissions, tail scenarios, and structural failure.

8. **Record custodian**  
   Preserves PCC, Decision Notes, audit flags, signoffs, and final decision state.

### 6.2 Minimum process

A Tier 3 run should:

1. define the decision;
2. define options;
3. declare scope and claim boundary;
4. ground evidence through RG;
5. screen rights through RF/NCRC;
6. conduct subgroup review;
7. run TRC scenario analysis;
8. run CSV and structural viability review;
9. score RLS only for surviving options;
10. check uncertainty and decisiveness;
11. record refusal, redesign, selection, or authority selection;
12. preserve PCC and audit record;
13. define monitoring and update triggers.

### 6.3 Minimum anti-capture safeguards

A Tier 3 run should include:

- affected-party representation where appropriate;
- independent challenger rights;
- dissent record;
- no single actor controls evidence, scoring, and final authority;
- no hidden threshold modification;
- no private override of RF/NCRC or TRC failure;
- public non-claims where public-facing;
- emergency use with sunset, redress, and post-event review;
- source retention or traceability proportionate to stakes.

### 6.4 Minimum maturity statement

Any Tier 3 use should include:

**This is a structured, auditable decision protocol. It is not empirical validation, legal certification, deployment certification, ProofPack status, reference-calculator status, or automated moral truth.**

## 7. Institutional dependency clarification

RippleLogic is computable in parts, but it is not merely an algorithm.

It requires human and institutional processes for:

- evidence selection;
- claim boundary setting;
- affected-party recognition;
- rights interpretation;
- scenario discovery;
- structural-viability review;
- uncertainty judgment;
- challenger review;
- authority selection;
- monitoring and update.

This is not a weakness. It is a realistic design feature.

A purely automatic system cannot legitimately decide every value, right, evidence boundary, subgroup status, and governance authority question without institutional grounding.

RippleLogic should therefore be described as:

**a socio-technical decision protocol with computable components, not a fully automated moral machine.**

## 8. Pilot readiness levels

Use the following ladder to describe practical readiness.

| Level | Name | Meaning |
|---|---|---|
| P0 | Concept review | Documents reviewed, no run conducted |
| P1 | Training run | Low-stakes classroom or internal exercise |
| P2 | Synthetic replay | Hypothetical cases scored by raters |
| P3 | Shadow-mode pilot | Real decision context, no binding authority |
| P4 | Advisory pilot | Used to inform decisions, human authority retained |
| P5 | Governed operational use | Institutional controls, monitoring, and audit in place |
| P6 | Validated operational use | External replay, reliability, and outcome evidence established |

Current core status should be described as source-ready for P1 to P3 preparation, not as validated P5 or P6.

## 9. Validation path

The next scientific work should include:

1. RLS rater training.
2. Ten to thirty scored cases.
3. Three to five independent raters minimum.
4. Inter-rater reliability analysis.
5. Dimensional separability and non-redundancy analysis.
6. Correlation and factor analysis as secondary diagnostics.
7. Disagreement heatmaps.
8. Workbook formula audit.
9. SGP rater study.
10. UCI measurement annex.
11. Biological and artificial-entity SGP annexes.
12. Reference calculator.
13. Shadow-mode pilots.

The goal is to move from:

**coherent architecture**

to:

**repeatable instrument**

to:

**externally replayable decision method**

to:

**validated governance practice.**

## 10. Implementation summary

The practical implementation rule is:

1. Use PCC-Lite for learning.
2. Use PCC-Core for serious internal analysis.
3. Use PCC-Audit for high-stakes or public-facing decisions.
4. Use PCC-Agent for agentic systems.
5. Use PCC-Public for public explanation.
6. Escalate whenever rights, tail risk, structural viability, vulnerable groups, automation, or public authority are material.
7. Never treat fast path as a waiver.
8. Never treat RLS as a rescue layer.
9. Never claim validation before validation is done.

## 11. Final operating sentence

**RippleLogic is usable now as a structured Tier 1-3 source specification, but its next maturity step is disciplined validation, not additional theoretical expansion.**
