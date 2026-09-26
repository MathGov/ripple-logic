# WDBIP Validation Study Protocol v1.0

## Status and purpose

This companion converts the WDBIP v1.4 validation and falsification program into a runnable preregistration template. It does not claim that the seven welfare dimensions, instruments, pathways, or decision effects are already validated.

**Owner:** WDBIP  
**Applies to:** WDBIP v1.4 and `WELFARE_DIMENSION_SET_7D_V1`  
**Controlling conflict rule:** RippleLogic Canon controls admissibility, RLS, Union Scopes, weights, and authority. WDBIP controls only the measurement and conformance surfaces it owns.

## 1. Study questions

A study SHALL identify which questions it tests:

1. Can trained raters classify bounded effect tokens into the seven primary dimensions reproducibly?
2. Can raters distinguish pathway types, evidence statuses, and scope treatments?
3. Do the dimensions show adequate content and discriminant validity for the intended domain?
4. Do instruments retain sufficiently comparable meaning across relevant groups, languages, cultures, ages, or substrates?
5. Do preregistered pathways predict later outcomes or respond to targeted interventions?
6. Does WDBIP detect material omissions, subgroup harms, and interaction effects that comparator models miss?
7. Does WDBIP improve decisions enough to justify its cost and complexity?
8. Can the system resist indicator gaming, scope inflation, weight gaming, and forced positive reporting?

## 2. Study phases

| Phase | Purpose | Minimum outputs |
|---|---|---|
| 0. Construct and content review | Clarify definitions, bearer/state boundaries, cultural meaning, and foreseeable harms | Expert and affected-party review; cognitive interviews; item and token map; ethics approval where required |
| 1. Coding and record reliability | Test primary-dimension, pathway, evidence, and scope classifications | Annotated case set; rater training; agreement estimates with confidence intervals; disagreement taxonomy |
| 2. Construct and measurement validity | Test dimension structure and instrument performance | Alternative factor/network models; convergent/discriminant evidence; invariance/DIF results; measurement limitations |
| 3. Longitudinal and intervention validation | Test temporal ordering, prediction, and causal claims | Preregistered longitudinal/intervention models; out-of-sample performance; calibration; alternative explanations |
| 4. Decision utility and adversarial validation | Compare decisions, burden, and gaming resistance | Comparator analysis; ablations; subgroup detection; weight sensitivity; red-team results; revision recommendation |

A study may complete only some phases, but its claims SHALL be limited accordingly.

## 3. Decision domains, cases, and populations

Preregister:

- decision domain and stakes;
- deployment context;
- target population and affected subgroups;
- sampling frame and inclusion/exclusion rules;
- case selection and enrichment for ambiguous or high-risk cases;
- baseline and observation windows;
- expected distribution shift;
- ethical and privacy constraints.

The study SHOULD include straightforward, ambiguous, cross-cultural, subgroup-sensitive, time-lagged, and adversarial cases rather than only clean examples.

## 4. Units of analysis

Declare each unit separately:

- effect token;
- welfare profile;
- token-level pathway;
- Union Scope treatment;
- full option/run;
- decision outcome;
- affected-party assessment.

Agreement on an option-level score does not prove agreement on the underlying tokens or pathways.

## 5. Raters and annotation

Preregister:

- number and expertise of raters;
- independence and conflicts;
- training materials and examples;
- whether raters are blinded to option labels, outcomes, or one another;
- permitted supporting evidence;
- adjudication process;
- treatment of `BOUNDARY_CONTESTED`;
- repeat-rating or drift checks.

### 5.1 Provisional reliability review triggers

These are governance review triggers, not universal validation constants.

| Classification surface | Development target | High-stakes target | Mandatory review trigger |
|---|---:|---:|---|
| Primary dimension | coefficient >= 0.70 | >= 0.80 | lower confidence bound < 0.60 or persistent domain cluster |
| Pathway type | >= 0.70 | >= 0.80 | materially lower after training |
| Evidence status | >= 0.70 | >= 0.80 | systematic UNKNOWN/CONTESTED disagreement |
| Scope treatment | >= 0.70 | >= 0.80 | allocation/deduplication disagreement affects totals |
| `BOUNDARY_CONTESTED` rate | ordinarily < 20% | ordinarily < 10% for decision-critical tokens | exceedance triggers partition/anchor review |

Select a statistic suitable to the scale and prevalence, such as Krippendorff's alpha, Gwet's AC1/AC2, weighted kappa, or ICC. Report uncertainty and prevalence. Do not select the statistic after seeing which produces the strongest result.

## 6. Construct and psychometric analysis

No one model is universally controlling. Preregister the primary model and credible alternatives. Depending on the instrument and theory, analyses may include:

- content validity and cognitive interviewing;
- exploratory and confirmatory factor analysis;
- ESEM;
- bifactor or bifactor-ESEM;
- network psychometrics;
- multitrait-multimethod analysis;
- item-response models;
- differential item functioning;
- known-groups and criterion validity;
- test-retest and longitudinal stability.

Report model assumptions, identification, fit criteria, cross-validation, local dependence, item redundancy, and substantive interpretability. A statistically better model does not by itself prove the ontology of welfare.

## 7. Invariance and comparability

Preregister the comparison claims and required evidence:

| Claim | Normally required evidence |
|---|---|
| Same broad construct organization | Configural invariance or equivalent qualitative evidence |
| Compare associations/slopes | Metric invariance or justified alternative |
| Compare latent means or rank groups | Scalar or defensible partial-scalar/approximate invariance |
| Compare observed scores with strong equivalence assumptions | Residual/strict evidence where material |

Where invariance fails, report group-specific results, qualitative evidence, DIF, and narrowed claims. Do not rank populations using a scale known to function differently across them.

## 8. Named comparators

Use only comparators relevant to the domain. Candidate comparators include:

- health-only or narrow outcome model;
- OECD Well-being Framework/dashboard;
- WHOQOL or WHOQOL-SRPB;
- VanderWeele-style flourishing measure;
- Alkire-Foster-style multidimensional deprivation/counting method;
- domain-specific capability or quality-of-life instrument;
- WDBIP ablation models removing one dimension at a time.

The study SHALL explain differences in purpose. A dashboard, deprivation measure, clinical scale, and governance protocol are not interchangeable merely because all are multidimensional.

## 9. Outcome metrics

Preregister direction, scale, practical importance, and uncertainty for each primary and secondary metric:

- material-effect omission and false-positive rates;
- primary-location and pathway reliability;
- predictive discrimination and calibration;
- incremental out-of-sample value;
- severe subgroup-harm detection;
- rights/TRC/CSV issue discovery;
- realized adverse events;
- decision reversals after later evidence;
- affected-party evaluation;
- analyst and reviewer burden;
- rank and decisiveness stability across weights;
- gaming and red-team success rates.

No single metric defines decision value. A favorable average cannot compensate for hidden severe harm in a protected subgroup.

## 10. Power, precision, and sample size

Use design-specific justification. Acceptable methods include:

- simulation-based power for factor, network, longitudinal, or causal models;
- precision targets for agreement coefficients and calibration estimates;
- minimum-events logic for outcome prediction;
- sequential or adaptive designs with preregistered stopping rules;
- saturation criteria for qualitative components.

Do not copy one universal participant-to-item ratio or one fixed sample threshold. Report sensitivity to model complexity, missingness, clustering, and subgroup comparisons.

## 11. Time and causality

Preregister:

- exposure, mediator, outcome, and follow-up windows;
- expected lags and feedback;
- baseline adjustment;
- confounders and alternative explanations;
- intervention assignment or natural-experiment assumptions;
- missingness and attrition;
- distribution shift;
- causal estimand, if any.

A cross-sectional association does not validate a directed pathway.

## 12. Weight sensitivity

Test a governed family of plausible floor-preserving weights. Report:

- score ranges;
- rank stability;
- decisiveness stability;
- selected-option changes;
- subgroup conclusion changes;
- which weights are normative, empirical, participatory, or exploratory.

When plausible weights change the selection or a material subgroup conclusion, classify the run `WEIGHT_SENSITIVE` and use the Canon's authority-selection discipline.

## 13. Anti-Goodhart and adversarial tests

At minimum, test foreseeable attempts to improve the metric without improving welfare:

- coached or forced self-report;
- selective subgroup exclusion;
- duplicated effect tokens;
- scope multiplication;
- unexplained allocation residual;
- proxy multiplication;
- short-window gains hiding long-window harm;
- instrument choice after results are known;
- weight choice after results are known;
- spiritual or cultural conformity presented as meaning;
- offsets masking local environmental harm.

## 14. Analysis and publication rules

Preregister:

- confirmatory and exploratory analyses;
- multiplicity treatment;
- missing-data rules;
- model and coding changes;
- adverse-result publication;
- data/code access and privacy limits;
- independent replay plan;
- revision triggers.

Negative or ambiguous findings are part of the validation result and must not be omitted.

## 15. Decision and maturity output

Each study SHALL conclude with one or more bounded outputs:

- `WDBIP_EVIDENCE_INSUFFICIENT`;
- `WDBIP_RELIABILITY_SUPPORTED_IN_DOMAIN`;
- `WDBIP_CONSTRUCT_VALIDITY_PARTIAL`;
- `WDBIP_INVARIANCE_LIMITED`;
- `WDBIP_PATHWAY_SUPPORTED_IN_DOMAIN`;
- `WDBIP_DECISION_UTILITY_SUPPORTED_IN_DOMAIN`;
- `WDBIP_REVISION_REQUIRED`;
- `WDBIP_DIMENSION_SET_REVIEW_REQUIRED`.

No phase result permits a universal validation claim beyond the tested populations, domains, versions, and use conditions.
