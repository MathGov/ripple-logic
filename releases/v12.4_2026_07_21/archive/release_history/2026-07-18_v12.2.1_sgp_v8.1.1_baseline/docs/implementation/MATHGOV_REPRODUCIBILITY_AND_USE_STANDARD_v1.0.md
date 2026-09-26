# MathGov Reproducibility and Use Standard v1.0

**Status:** Normative implementation companion for RippleLogic Canon v12.2.1. The Canon controls semantics and equations if a conflict occurs. This standard controls the minimum run record, deterministic cascade order, parameter-completeness rules, replay procedure, and proportional-use profiles for this release.

**Purpose:** Make MathGov easier to use without weakening it. A valid run should be understandable by a first-time user, reproducible by a qualified second implementer, and mechanically rejectable when required inputs, parameters, or decision states are missing or contradictory.

**Release boundary:** This standard validates record completeness and cascade conformance. It does not prove that evidence is true, measurements are valid, thresholds are justified, rights classifications are legally binding, or the selected action is safe to deploy.

## 1. The compact operating kernel

Every MathGov run follows the same twelve rules.

| Rule ID | Required rule | Failure action |
|---|---|---|
| K01 | Identify the decision, baseline, options, affected stakeholders, tier, stakes, and authority boundary. | `INCOMPLETE_RUN` |
| K02 | Freeze decision-material evidence cutoffs, parameters, weights, thresholds, masks, scenario assumptions, reviewers, and amendment rules before outcome-sensitive ranking. | `PARAMETER_LOCK_FAILURE` |
| K03 | Ground the claim. Record the reality surface, evidence trace, material unknowns, consequence pathways, and maximum claim boundary. | Narrow, test, escalate, or `REFUSE_INSUFFICIENT_GROUNDING` |
| K04 | Apply RF/NCRC before ordinary trade-off analysis. A failed rights floor cannot be repaired by welfare score. | Exclude, redesign, remedy, or emergency procedure |
| K05 | Apply TRC to catastrophic, irreversible, or ruin-relevant pathways. Ordinary gain cannot average away inadequately bounded ruin. | Exclude, redesign, control, or escalate |
| K06 | Apply CSV to containment, reversibility, monitoring, dependency health, structural viability, and execution conditions. | Exclude, redesign, control, or escalate |
| K07 | Form the selectable set only from options supported by RG and passing RF/NCRC, TRC, and CSV. | `NO_SELECTABLE_OPTION` if empty |
| K08 | Apply RLS only to the selectable set. Never score a failed option back into consideration. | `CASCADE_ORDER_VIOLATION` |
| K09 | Distinguish decisive ranking, non-decisive ranking, authority selection, refusal, delay, redesign, and emergency-provisional action. | `DECISION_STATE_AMBIGUOUS` |
| K10 | Separate selection from lawful authority and execution. A selected option is not automatically authorized or safe to execute. | `NO_EXECUTION_AUTHORITY` |
| K11 | Record controls, monitoring, review dates, appeal, shutdown, and reopen triggers proportionate to stakes. | `CONTROL_OR_MONITORING_GAP` |
| K12 | Preserve an append-only audit record and rerun affected stages after material evidence, parameter, scope, system, or distribution change. | `REQUALIFICATION_REQUIRED` |

Memory line:

> **Ground reality. Protect rights. Bound ruin. Preserve the structure. Score the ripples. Authorize and monitor separately.**

## 2. One architecture, three use profiles

The architecture remains comprehensive. The documentation burden changes with stakes.

| Profile | Typical use | Minimum burden | Numeric scoring |
|---|---|---|---|
| **Quick / Tier 1** | Personal, family, classroom, low-stakes reversible choices | Decision, options, facts/unknowns, rights screen, ruin screen, structural screen, light ripple comparison, conclusion, reopen trigger | Optional; qualitative comparison is permitted |
| **Standard / Tier 2** | Organizational, community, product, programme, or policy analysis with material but bounded consequences | Versioned run record, stakeholder map, evidence register, parameter lock, gate records, controls, uncertainty, RLS method if used, audit rationale | Permitted only with declared method and sensitivity |
| **Audit / Tier 3** | Public, institutional, high-impact, contested, or high-stakes analysis | Full schema, independent review, hashes, source and method records, scenario governance, subgroup analysis, parameter lock, replay packet, authority and execution records | Required when claiming formal RLS ranking; validation maturity must be disclosed |

A user MUST NOT choose a lower profile merely to avoid a material right, ruin, structural, evidence, or authority requirement. Any trigger in the next table escalates the run.

| Escalation trigger | Minimum response |
|---|---|
| Plausible rights-floor violation or severe protected-interest uncertainty | Tier 2 or 3 rights review |
| Catastrophic, irreversible, systemic, lock-in, or ruin-relevant pathway | TRC with governed scenario set; normally Tier 3 |
| Physical, cyber-physical, medical, weapons, critical infrastructure, or irreversible execution | PC-AEP and qualified domain warrant |
| Materially affected vulnerable subgroup | Explicit subgroup mapping and distributional review |
| AI or agent with consequential autonomy or delegation | Agent System, authority boundary, monitoring, revocation, and security acceptance evidence |
| Public conformance, scientific, legal, safety, or deployment claim | Tier 3 evidence and claim-boundary review |
| Result changes under admissible assumptions or welfare-inclusion hypotheses | Sensitivity record and non-decisive handling |

## 3. Deterministic run state machine

A conforming implementation processes each option in this order:

1. `DECLARED`
2. `RG_SUPPORTED`, `RG_NARROWED`, or `RG_REFUSED`
3. `RF_PASS`, `RF_FAIL`, or `RF_ESCALATE`
4. `TRC_PASS`, `TRC_FAIL`, or `TRC_ESCALATE`
5. `CSV_PASS`, `CSV_PASS_WITH_CONTROLS`, `CSV_NOT_MATERIAL`, `CSV_FAIL`, `CSV_REDESIGN`, or `CSV_ESCALATE`
6. `SELECTABLE` only when the declared RG/RF/TRC/CSV conditions are satisfied
7. `RLS_RANKED` only for selectable options
8. Final decision state: `SELECTED_DECISIVE`, `SELECTED_BY_AUTHORITY_NON_DECISIVE`, `PROVISIONAL_WITH_CONTROLS`, `DELAY`, `REDESIGN`, `ESCALATE`, `REFUSE`, `NO_SELECTABLE_OPTION`, or `EMERGENCY_PROVISIONAL`
9. Separate execution state: `NOT_AUTHORIZED`, `AUTHORIZED_WITHIN_SCOPE`, `EXECUTION_BLOCKED`, or `EXECUTED_UNDER_MONITORING`

### 3.1 Selectable-set rule

For option `a`:

```text
SELECTABLE(a) =
  RG supports the claim boundary
  AND RF/NCRC passes
  AND TRC passes
  AND CSV is one of:
      CSV_PASS
      CSV_PASS_WITH_CONTROLS
      CSV_NOT_MATERIAL
```

No RLS value, benefit claim, popularity, urgency, institutional permission, or superior capability may change a non-selectable option into a selectable option.

### 3.2 Refusal and unknowns

Missing evidence is not zero. Missing parameters are not defaults unless the controlling source explicitly declares a default. A required unknown produces one of four actions:

- narrow the claim;
- collect or verify evidence;
- apply a governed conservative bound;
- refuse or escalate the stronger decision.

## 4. Parameter completeness and lock

A calculation-bearing run MUST declare every decision-material parameter before outcome-sensitive ranking. At minimum:

- component and package versions;
- evidence cutoff;
- options and baseline;
- stakeholder and subgroup boundaries;
- Union Scope and welfare-dimension mappings;
- rights floors and categorical prohibitions;
- TRC scenario families, probabilities or bounds, dependence assumptions, severity model, alpha, and tolerance;
- CSV materiality, controls, monitoring, reversibility, dependency, and tolerance assumptions;
- RLS active cells, masks, weights, propagation method, saturation method, uncertainty method, and decisiveness threshold where RLS is used;
- SGP records and welfare-inclusion hypotheses where moral-patient uncertainty is material;
- authority role, mandate, limits, appeal, and revocation;
- permitted amendments and rerun triggers.

A value is valid only when it has a declared source, status, and scope. The allowed status vocabulary is:

- `CANON_DEFAULT`
- `DOMAIN_STANDARD`
- `EMPIRICALLY_ESTIMATED`
- `EXPERT_JUDGMENT`
- `PARTICIPATORY_CHOICE`
- `CONSERVATIVE_BOUND`
- `ASSUMPTION_BOUND`
- `UNKNOWN`
- `NOT_MATERIAL`

`UNKNOWN` cannot enter arithmetic as zero. `NOT_MATERIAL` requires a rationale and a reopen trigger.

Any material post-outcome amendment creates a new run version and requires replay of every affected downstream stage.

## 5. Minimum reproducible run record

The machine-readable minimum is defined by `schemas/mathgov_run_record_v1.schema.json`. A human-readable run MUST expose the same logical fields even when it uses prose or a workbook.

Required top-level objects:

1. `identity`
2. `decision`
3. `profile_and_stakes`
4. `evidence_and_claim_boundary`
5. `parameter_lock`
6. `stakeholders`
7. `options`
8. `gate_results`
9. `ranking`
10. `decision_state`
11. `authority_and_execution`
12. `controls_monitoring_and_reopen`
13. `audit_and_signoff`

## 6. Two-implementer reproducibility protocol

A run is **replay-ready** when another qualified implementer receives:

- the exact source package and hashes;
- the locked run record;
- the evidence registry or accessible evidence bundle;
- the option definitions and baseline;
- parameter sources and statuses;
- scenario and uncertainty records;
- formulas or scoring rules actually used;
- reviewer conflicts and authority boundary;
- expected intermediate statuses, not only the final answer.

The independent implementer reruns the decision without seeing the original final selection where practical. Differences are classified as:

| Difference class | Meaning | Required action |
|---|---|---|
| `DATA_DIFFERENCE` | Different evidence or extraction | Resolve source and cutoff |
| `DEFINITION_DIFFERENCE` | Different category or boundary | Apply Category Grounding |
| `PARAMETER_DIFFERENCE` | Different threshold, weight, mask, scenario, or assumption | Return to lock record |
| `OPERATOR_DIFFERENCE` | Different formula or gate interpretation | Canon controls; fix implementation |
| `JUDGMENT_DIFFERENCE` | Same inputs, different governed judgment | Record panel disagreement and sensitivity |
| `AUTHORITY_DIFFERENCE` | Different lawful or governed mandate | Separate analysis from execution authority |
| `IMPLEMENTATION_ERROR` | Formula, reference, transcription, or software defect | Correct and rerun affected stages |

### 6.1 Reproducibility outcomes

- `REPLAY_MATCH`: selectable set, gate states, ranking state, and final decision state agree within declared tolerances.
- `REPLAY_CONDITIONALLY_MATCHES`: final state agrees but one or more material intermediate judgments differ and are disclosed.
- `REPLAY_DIVERGES`: selectable set or decision state differs.
- `REPLAY_INADMISSIBLE`: record or evidence bundle is incomplete.

A replay match demonstrates procedural reproducibility for the supplied record. It does not establish empirical validity or moral truth.

## 7. Mechanical contradiction checks

The release validator MUST reject at least these contradictions:

1. an option has an RLS rank but is not selectable;
2. an RF, TRC, or CSV failure is selected through aggregate benefit;
3. a selected option is marked both authorized and outside mandate;
4. a required parameter is missing or `UNKNOWN` but enters arithmetic;
5. the final state claims decisiveness while the declared decisiveness test failed;
6. a non-decisive result lacks an authority-selection or refusal rationale;
7. execution is authorized without an authority basis;
8. material distribution shift is recorded but requalification is not triggered;
9. FPP, MPS, ICP, RMCP, P100, GPR, SPR, or CMIU status is used as a substitute for another type;
10. a public validation or certification claim exceeds the declared evidence maturity.

## 8. Burden-proportional documentation

The framework is not intended to make ordinary life bureaucratic. The smallest faithful record is:

```text
Decision:
Options:
Known / unknown:
Rights concern:
Ruin concern:
Structural concern:
Best remaining ripple:
Decision and reason:
Controls / reopen trigger:
```

The full Tier 3 record is required only when the stakes, irreversibility, public claim, contestability, or system coupling justify it.

## 9. Conformance levels

| Level | Claim permitted | Required evidence |
|---|---|---|
| `R0_RECORD_COMPLETE` | The run record contains the required fields and valid status values. | Schema and semantic validator pass |
| `R1_CASCADE_CONFORMANT` | The run followed the five-stage ordering and non-compensation rules. | R0 plus gate/ranking consistency checks |
| `R2_INDEPENDENTLY_REPLAYED` | A second implementer reproduced the declared decision state within tolerance. | R1 plus independent replay record |
| `R3_EMPIRICALLY_SUPPORTED` | The instruments used have relevant reliability/validity evidence for the domain. | External study evidence; not established by this release alone |
| `R4_DEPLOYMENT_ASSURED` | The action has domain-specific engineering, legal, operational, and monitoring assurance. | External domain assurance; not established by this release alone |

Do not shorten these to a single word such as “validated.” State the exact level.

## 10. Source hierarchy and conflict rule

1. RippleLogic Canon v12.2.1 controls decision semantics and equations.
2. SGP v8.1.1 controls MPS/FPP/GPR/SPR/ICP/RMCP/P100 semantics.
3. Named companion standards control their bounded interface unless they conflict with the Canon.
4. This standard controls run-record completeness, replay procedure, and proportional-use profiles.
5. Markdown is the governing semantic source where a reading mirror differs.
6. Examples and workbooks are informative unless explicitly designated otherwise.

A conflict MUST be logged, not silently harmonized. Use `SOURCE_HIERARCHY.md` and the normative kernel index to identify the controlling rule.

## 11. Required release artifacts

This release provides:

- this standard;
- `schemas/mathgov_run_record_v1.schema.json`;
- `docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml`;
- `release/VALIDATE_MATHGOV_RUN.py`;
- a passing worked example;
- intentionally failing test vectors;
- release verification that checks the files and example results.

These artifacts make basic contradictions and missing fields mechanically detectable. They are not a complete reference calculator and do not automate ethical judgment.
