# MathGov v12.5 Same-Version Carried-Obligation and Human-Compensation Hardening Report

**Integration date:** 25 July 2026  
**Version posture:** MathGov v12.5, SGP v8.4, ripple.md v5.4, Agent System v12.3, CSV v2.3, MFDI v2.2, Reproducibility v1.3, Aligners Sheet v5.5, and run-record schema v3 are retained unchanged.  
**Architectural posture:** `RG -> RF/NCRC -> TRC -> CSV -> RLS` is unchanged. No sixth gate was created.

## 1. Scientific necessity test

A change was accepted only when all of the following held:

1. it closed a concrete assurance or reproducibility gap;
2. it was compatible with the existing Canon rather than importing an external ontology;
3. it did not alter the rights floor, TRC, CSV/RLS separation, seven Union Scopes, seven Welfare Dimensions, SGP protections, equations, thresholds, or worked-run result;
4. it could be represented through inspectable records and adversarial tests; and
5. it preserved the distinction between record conformance and empirical effectiveness.

Four bounded improvements passed this test:

- **bounded reality contact:** reality constrains representations, while operational access remains mediated and revisable;
- **dependency-localized falsification:** failed dependencies reopen dependent claims without automatically destroying independently supported components;
- **carried-obligation integrity:** a declared control is not binding unless its carrier, authority/capacity, trigger, action, timing, evidence, nonperformance path, succession, change authority, and residual responsibility are inspectable;
- **hidden-human-compensation visibility:** CSV must detect when apparent resilience depends on undocumented adaptive human work before automation, scale, outsourcing, or role removal removes that work.

## 2. Exact governing-document changes

| File and retained version | Exact location | Exact change | Why it genuinely improves MathGov |
|---|---|---|---|
| `docs/canon/RippleLogic_v12.5_Canon.md/.docx/.pdf` and `core_15/RippleLogic_v12.5_Canon.docx` | §2.1B Reality Grounding | Added the **Reality-reference boundary**: reality is the final constraint, but evidence access is mediated, incomplete, and revisable; conflicting evidence reopens dependent stages. | Prevents “reality-based” from being misread as infallible or total access to reality. |
| Same Canon | §4.10A | Added **Material obligation integrity** and the minimum `MaterialObligationRecord`. | Converts governance language into inspectable, carried duties. |
| Same Canon | §4.10A | Added carrier authority/capacity, accepted handoff, backup/succession, nonperformance escalation, and control-change/requalification rules. | Closes the failure mode in which a named owner lacks power, capacity, acceptance, or replacement. |
| Same Canon | §4.10A | Separated **control performance** from **control effectiveness**. | A completed review or checklist no longer counts as evidence that the intended protection worked. |
| Same Canon | §4.10B | Added the `HumanCompensationLoadRecord` inside CSV when triggered. | Makes invisible exception handling, memory, relationships, weak-signal detection, and recovery work structurally visible before removal. |
| Same Canon | §9.8A–B | Made carried-obligation integrity and hidden-human-compensation status explicit CSV pass/pass-with-controls conditions. | Prevents promised, unowned, under-resourced, silently compensated, or freely rewritable controls from upgrading CSV. |
| Same Canon | Appendix AN.2 | Added **dependency-localized falsification**. | Avoids both framework immunity after foundation failure and indiscriminate whole-framework rejection. |
| `docs/standards/CSV_Gate_Standard_v2.3.md/.docx/.pdf` and Core mirror | Binding-control minimum | Expanded the minimum to authority, carrier, capacity, trigger, action, deadline, evidence, expiry, challenge, succession, nonperformance, change authority, residual responsibility, status, and effectiveness. | Makes `CSV_PASS_WITH_CONTROLS` operational rather than ceremonial. |
| Same CSV Standard | Control-performance boundary | Required outcome evidence when effectiveness is material. | Prevents procedural completion from laundering ineffective controls. |
| Same CSV Standard | Hidden human compensation load | Added trigger, record fields, protected evidence, and routing dispositions. | Detects resilience that is actually human overload or undocumented middleware. |
| `docs/standards/ripple_md_Standard_v5.4.md/.docx/.pdf` and Core mirror | DN-10B | Expanded the Responsibility-Continuity record requirement to material obligations and human-compensation load. | Makes the new assurance data portable across implementations. |
| Same ripple.md | Appendix L.2C | Added machine-readable `material_obligations` and `human_compensation_load` fields. | Provides a replayable interchange surface rather than prose-only guidance. |
| Same ripple.md | Appendix AB.3B–C | Added material-obligation and hidden-human-compensation rules, including no silent discharge and no self-waiver. | Connects responsibility records to execution and requalification behavior. |
| Same ripple.md | Appendix AB.6 | Added a non-overclaim boundary for obligation discharge and control effectiveness. | Prevents a complete record from being presented as proof of safety or successful control. |
| `docs/agents/RippleLogic_Agent_System_v12.3.md/.docx/.pdf` and Core mirror | §23.6 | Added runtime material-obligation records, carrier-nonperformance events, escalation/substitution/pause/safe-state routing, and no-self-waiver. | Makes responsibility failures detectable at runtime and prevents an agent from weakening its own constraints. |
| Same Agent System | §23.6 | Added pre-automation hidden-human-compensation inspection. | Prevents automation from deleting undocumented judgment or recovery capacity. |
| Same Agent System | §31.3 | Extended live-update logs to material control/carrier changes, change authority, challenger review, requalification, and rollback. | Makes control rewriting visible and configuration-bound. |
| `docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.md/.docx/.pdf` and Core mirror | New “Dependency-localized failure propagation” section | Required explicit dependency paths and rerun/withdrawal scope while preserving independently supported components. | Provides a scientifically cleaner falsification rule than monolithic “all or nothing” failure. |
| `docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.md/.docx/.pdf` and Core mirror | §5 | Corrected the minimum top-level object list from 13 to the actual 17 schema-v3 objects. | Removes a real documentation/schema mismatch. |
| Same Reproducibility Standard | §7 | Added contradiction checks for missing carried obligations, expired/ineffective obligations, unresolved human compensation, uncontrolled control changes, and unaccepted handoffs. | Makes the improvement mechanically testable. |

## 3. Exact machine-interface changes

| File | Exact change | Why |
|---|---|---|
| `schemas/mathgov_run_record_v3.schema.json` | `responsibility_continuity` now requires `material_obligations` and `human_compensation_load`; added bounded enums and required fields. Schema version remains v3. | Existing v3 responsibility continuity was incomplete for controlled execution; the extension is backward-line hardening, not a new conceptual schema generation. |
| `release/VALIDATE_MATHGOV_RUN.py` | Rejects controlled selectability without obligations; execution under expired/suspended/escalated/ineffective obligations; unresolved hidden compensation during execution; and missing privacy protection when human compensation is material. Warns on effectiveness pending and potentially self-controlled amendment authority. | Converts prose into executable conformance behavior. |
| `docs/assurance/PARAMETER_AND_AUTHORITY_LOCK_RECORD.schema.yaml` | Added control-change, waiver, suspension, retirement, carrier-substitution, nonperformance, and challenger-review authority fields and no-self-waiver rules. | Extends configuration locking to the oversight mechanism itself. |
| `tests/run_records/pass_*.json` and existing fail vectors | Added schema-required obligation and human-compensation defaults or complete examples. | Keeps the full vector library valid under the same v3 schema. |
| Added `pass_material_obligation_integrity.json` | Positive controlled-CSV obligation record. | Demonstrates the intended valid structure. |
| Added `fail_csv_controls_without_obligation_record.json` | Rejects `CSV_PASS_WITH_CONTROLS` without a carried obligation. | Tests governance-as-furniture failure. |
| Added `fail_execution_with_expired_obligation.json` | Rejects execution relying on an expired obligation. | Tests qualification continuity. |
| Added `fail_unresolved_human_compensation_execution.json` | Rejects execution while hidden compensation requires redesign/escalation. | Tests pre-automation and structural-capacity routing. |
| `release/VERIFY_RELEASE.py`, `VERIFY_SEMANTIC_SURFACES.py`, and `VERIFY_FORMULA_INTERFACE_INTEGRITY.py` | Added release-lock checks for the new Canon, CSV, Agent, schema, and workbook surfaces. | Prevents later semantic or interface regression. |

## 4. Exact Aligners Sheet v5.5 changes

All **2,943 formulas**, thresholds, and worked-run ranking outcomes were preserved. The final OOXML contains **2,351 explicit serialized formula results** and **592 formula cells whose recalculated result is the intentional empty string**. Every uncached cell was independently recalculated through `artifact_tool`, recorded in `release/WORKBOOK_FORMULA_CACHE_AUDIT.json`, and matched exactly by the release verifier. Zero formula errors were found, and automatic/full recalculation flags are set.

| Sheet / range | Exact change | Why |
|---|---|---|
| `Responsibility_Continuity!A18:D24` | Added the carried-obligation interface, carrier-nonperformance rule, control-change rule, and performance/effectiveness boundary. | Gives reviewers a direct operational entry point. |
| New `Material_Obligations!A1:U4` | Added the complete 21-field register with a worked-run control row, guidance row, freeze pane, and status validation lists. | Makes every selectability-material control inspectable and transferable. |
| New `Human_Comp_Load!A1:D13` | Added the hidden-human-compensation diagnostic, privacy/non-retaliation boundary, and reopen triggers. | Makes undocumented adaptive work visible without treating all human adaptation as a defect. |
| `CSV!A28:H30` | Added Material Obligation Integrity and Hidden Human Compensation subconditions while retaining the resolver as the final row. | Integrates the records inside CSV rather than creating a new gate. |
| `PCC!A242:H249` | Added Section 27 references, statuses, nonperformance path, control-change authority, effectiveness boundary, and claim boundary. | Preserves auditability and public non-overclaiming. |
| `Workflow_Navigator!B11:C11` | Routed responsibility continuity through both new registers. | Makes the workflow discoverable. |
| `How_To_Use!A19:B23` and `User_Guide!A74:C81` | Added user instructions and architecture boundaries. | Prevents misuse and overexpansion. |
| `Reproducibility_Check!B3:B4` | Corrected Reproducibility v1.2/schema v2 references to v1.3/schema v3. | Fixes a genuine stale-reference defect. |
| `Reproducibility_Check!A32:F33` | Added K13 obligation integrity and K14 human-compensation checks. | Exposes the new conformance surfaces to workbook reviewers. |
| `v12_5_Sync (2)!B4` | Corrected the duplicate sync surface from ripple.md v5.5 to the actual v5.4. | Removes a version-pin error while retaining all actual versions. |
| `Release_Notes!A105:D105` | Recorded the same-version hardening and explicit non-changes. | Preserves release provenance. |

## 5. Support-document and release-record changes

Updated without changing component versions:

- `CHANGELOG.md`
- `release/RELEASE_NOTES.md`
- `QUICKSTART.md`
- `GLOSSARY_AND_ACRONYM_INDEX.md`
- `VALIDATION_STATUS.md`
- `VERSION_MANIFEST.yaml`
- `docs/validation/V12_5_SAFETY_CONFORMANCE_VECTORS.md`
- `docs/validation/VALIDATION_INDEX.md`
- `docs/workbooks/ALIGNERS_SHEET_USER_GUIDE.md`
- `release/FINAL_VERIFICATION_REPORT.md`
- `release/WORKBOOK_FORMULA_CACHE_AUDIT.json`
- `VERIFICATION_LOG.md`
- `release/release_manifest.yml`
- `release/SHA256SUMS.txt`
- `release/SHA256SUMS_CORE15.txt`

## 6. Explicit non-changes

The patch does **not** introduce or alter:

- the five-stage cascade;
- any equation, formula, threshold, default, weight, decisiveness rule, or worked-run selection outcome;
- any Union Scope or Welfare Dimension;
- the Rights Floor, NCRC, TRC, CSV/RLS ordering, or refusal rules;
- any SGP band, MPS/FPP/P100 rule, moral-status rule, or rights protection;
- any new ontology or external primitive;
- any empirical-validation, legal-compliance, physical-safety, ProofPack, Tier 4, or deployment-certification claim.

## 7. Verification boundary

The patch establishes record, schema, semantic, workbook-interface, presentation, hash, and adversarial-vector conformance. It does not establish that a real-world carrier will act, that a control is empirically effective, that hidden human work has been completely observed, or that a deployment is safe or lawful. Those claims require external evidence and domain assurance.
## 8. Exact changed-file inventory

Compared with the user-supplied v12.5 ZIP: **6 files added, 58 existing files changed, and 0 files deleted.** No file was removed.

### Added files

- `release/V12_5_CARRIED_OBLIGATION_AND_HUMAN_COMPENSATION_HARDENING_REPORT.md`
- `release/WORKBOOK_FORMULA_CACHE_AUDIT.json`
- `tests/run_records/fail_csv_controls_without_obligation_record.json`
- `tests/run_records/fail_execution_with_expired_obligation.json`
- `tests/run_records/fail_unresolved_human_compensation_execution.json`
- `tests/run_records/pass_material_obligation_integrity.json`

### Changed files

- `CHANGELOG.md`
- `GLOSSARY_AND_ACRONYM_INDEX.md`
- `QUICKSTART.md`
- `VALIDATION_STATUS.md`
- `VERIFICATION_LOG.md`
- `VERSION_MANIFEST.yaml`
- `core_15/CSV_Gate_Standard_v2.3.docx`
- `core_15/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.docx`
- `core_15/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.docx`
- `core_15/RippleLogic_Agent_System_v12.3.docx`
- `core_15/RippleLogic_Aligners_Sheet_v5.5.xlsx`
- `core_15/RippleLogic_v12.5_Canon.docx`
- `core_15/ripple_md_Standard_v5.4.docx`
- `docs/agents/RippleLogic_Agent_System_v12.3.docx`
- `docs/agents/RippleLogic_Agent_System_v12.3.md`
- `docs/agents/RippleLogic_Agent_System_v12.3.pdf`
- `docs/aligners/RippleLogic_Aligners_Sheet_v5.5.xlsx`
- `docs/assurance/PARAMETER_AND_AUTHORITY_LOCK_RECORD.schema.yaml`
- `docs/canon/RippleLogic_v12.5_Canon.docx`
- `docs/canon/RippleLogic_v12.5_Canon.md`
- `docs/canon/RippleLogic_v12.5_Canon.pdf`
- `docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.docx`
- `docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.md`
- `docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.pdf`
- `docs/standards/CSV_Gate_Standard_v2.3.docx`
- `docs/standards/CSV_Gate_Standard_v2.3.md`
- `docs/standards/CSV_Gate_Standard_v2.3.pdf`
- `docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.docx`
- `docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.md`
- `docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.pdf`
- `docs/standards/ripple_md_Standard_v5.4.docx`
- `docs/standards/ripple_md_Standard_v5.4.md`
- `docs/standards/ripple_md_Standard_v5.4.pdf`
- `docs/validation/V12_5_SAFETY_CONFORMANCE_VECTORS.md`
- `docs/validation/VALIDATION_INDEX.md`
- `docs/workbooks/ALIGNERS_SHEET_USER_GUIDE.md`
- `release/FINAL_VERIFICATION_REPORT.md`
- `release/RELEASE_NOTES.md`
- `release/SHA256SUMS.txt`
- `release/SHA256SUMS_CORE15.txt`
- `release/VALIDATE_MATHGOV_RUN.py`
- `release/VERIFY_FORMULA_INTERFACE_INTEGRITY.py`
- `release/VERIFY_RELEASE.py`
- `release/VERIFY_SEMANTIC_SURFACES.py`
- `release/release_manifest.yml`
- `schemas/mathgov_run_record_v3.schema.json`
- `tests/run_records/fail_decisive_contradiction.json`
- `tests/run_records/fail_emergency_masquerades_normal.json`
- `tests/run_records/fail_execution_without_authority.json`
- `tests/run_records/fail_rank_nonselectable.json`
- `tests/run_records/fail_schema_additional_property.json`
- `tests/run_records/fail_schema_invalid_stakes.json`
- `tests/run_records/fail_schema_missing_reversibility.json`
- `tests/run_records/fail_short_circuit_rg.json`
- `tests/run_records/fail_trc_not_triggered_missing_assessment.json`
- `tests/run_records/fail_unknown_parameter.json`
- `tests/run_records/pass_reusable_cups.json`
- `tests/run_records/pass_trc_not_triggered.json`

### Deleted files

- None.
