# Worked Run Registry

This registry catalogs human-readable examples, schema-bound run records, and independent replay status. Inclusion does not make a run empirically validated, legally authorized, or deployment-assured.

| Run ID | Case | Domain | Tier | Framework release | Record / packet | Gate outcome | RLS / ranking outcome | Independent replay status | Notes |
|---|---|---|---:|---|---|---|---|---|---|
| MG-EXAMPLE-CUPS-001 | Reusable deposit-return cup trial | Local business operations | 1 | `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3` | `docs/examples/reproducibility/reusable_cups_run_v4.json` | A and B selectable; C escalated at RF | B directionally preferred; non-decisive authority selection | NOT_RUN | Low-stakes reversible teaching run |
| MG-REF-AI-TUTOR-001 | Bounded AI-tutor pilot | Higher education / AI governance | 2 | `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3` | `docs/examples/reference_replays/ai_tutor_pilot/` | A and C selectable; B escalated at RF | C directionally preferred; non-decisive and parameter-sensitive | NOT_RUN | Exercises Capability Claim Integrity, hidden human compensation, and selection/execution separation |
| MG-REF-CONGESTION-001 | Controlled congestion-pricing pilot | Public policy / urban transport | 2 | `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3` | `docs/examples/reference_replays/congestion_pricing_pilot/` | A and C selectable; B escalated at RF | C directionally preferred; non-decisive and hypothesis-sensitive | NOT_RUN | Exercises no-RLS-rescue, subgroup rights, public controls, appeals, and no-action comparison |

## Replay rule

A replay-status change requires a separate reviewer record and must not silently modify the frozen source packet. Allowed statuses are `REPLAY_MATCH`, `REPLAY_CONDITIONALLY_MATCHES`, `REPLAY_DIVERGES`, and `REPLAY_INADMISSIBLE`.
