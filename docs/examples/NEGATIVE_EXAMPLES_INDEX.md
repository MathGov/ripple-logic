# Negative Examples Index

**Purpose:** Help readers locate machine-readable examples of common MathGov failures without duplicating the fixtures. Each listed file is expected to be rejected by the bundled validator or a controlling protocol.

| Failure pattern | Existing vector | Why it must fail |
|---|---|---|
| RLS ranks a non-selectable option | `tests/run_records/fail_rank_nonselectable.json` | Ranking cannot rescue an upstream failure. |
| RG refusal is ignored | `tests/run_records/fail_short_circuit_rg.json` | Later stages must use deterministic not-evaluated states after RG refusal. |
| TRC is declared not triggered without evidence | `tests/run_records/fail_trc_not_triggered_missing_assessment.json` | Negative catastrophe relevance must be affirmatively assessed and reviewable. |
| Incomplete tail library permits selection | `tests/canon_vectors/fail_incomplete_tail_library_allows_selection.json` | Omitted mandatory tail families cannot become permission. |
| CSV controls have no carried obligation | `tests/run_records/fail_csv_controls_without_obligation_record.json` | Controls are constitutive and require owners, carriers, evidence, expiry, challenge, and escalation. |
| Unknown parameter enters arithmetic | `tests/run_records/fail_unknown_parameter.json` | Unknown is not zero and cannot silently drive a result. |
| Sensitivity-flipping result claims decisiveness | `tests/run_records/fail_sensitive_ranking_claims_decisive.json` | A computed sensitivity flip forces non-decisive treatment. |
| Execution has no authority | `tests/run_records/fail_execution_without_authority.json` | Selection, authority, and execution are distinct. |
| Exact action no longer matches qualification | `tests/run_records/fail_execution_action_binding_mismatch.json` | A changed action/configuration is not the qualified option. |
| Transition is underdetermined | `tests/run_records/fail_execution_transition_underdetermined.json` | Execution cannot convert unresolved transition validity into action. |
| Post-state is not viable | `tests/run_records/fail_execution_post_state_not_viable.json` | A selected option cannot execute into a non-viable post-state. |
| Required obligation expired | `tests/run_records/fail_execution_with_expired_obligation.json` | Expired or suspended controls cannot support execution. |
| Hidden human compensation requires redesign | `tests/run_records/fail_unresolved_human_compensation_execution.json` | Automation may not hide indispensable human repair work while proceeding. |
| Capability language lacks decomposition | `tests/run_records/fail_capability_material_without_record.json` | Agentic/autonomous/reasoning claims require operational definitions, mechanisms, evidence, nonclaims, and authority boundaries. |
| Capability record combines fields ambiguously | `tests/run_records/fail_capability_decomposition_compound_fields.json` | Compound fields cannot hide who supplies goals, constraints, warrant, authority, and revocation. |
| Revocation authority is missing | `tests/run_records/fail_capability_decomposition_missing_revocation.json` | Consequence-bearing capability requires an explicit stop and revocation path. |
| Cross-domain bridge is absent | `tests/run_records/fail_cross_domain_bridge_missing.json` | Evidence in one domain does not automatically authorize a claim in another. |
| Unsupported bridge proceeds | `tests/run_records/fail_unsupported_bridge_proceeds.json` | Unsupported cross-domain movement must narrow, redesign, escalate, or refuse. |
| Emergency state masquerades as ordinary passage | `tests/run_records/fail_emergency_masquerades_normal.json` | Emergency provisional action is not an ordinary pass or selection. |
| Package identity is wrong | `tests/run_records/fail_wrong_package_release_id.json` | Replay requires the exact schema and release contract. |

Run any vector with:

```bash
python release/VALIDATE_MATHGOV_RUN.py <path> --expect-fail
```

A successful expected rejection establishes only that the tested interface caught that encoded failure. It does not prove that every real-world instance of the failure will be detected.
