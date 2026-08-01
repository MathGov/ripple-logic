# State Transition Matrix v1.0

This human-readable surface mirrors `STATE_TRANSITION_MATRIX_v1.0.json`. It controls deterministic short-circuit behavior for run-record v3.

| Trigger | Required later states | Selectable |
|---|---|---|
| `RG_REFUSED` | RF/TRC/CSV all `NOT_EVALUATED_AFTER_PRIOR_FAILURE` | No |
| `RF_FAIL` or `RF_ESCALATE` | TRC/CSV `NOT_EVALUATED_AFTER_PRIOR_FAILURE` | No |
| `TRC_FAIL` or `TRC_ESCALATE` | CSV `NOT_EVALUATED_AFTER_PRIOR_FAILURE` | No |
| RG supported/narrowed + RF pass + `TRC_PASS` or documented `TRC_NOT_TRIGGERED` + selectable CSV state | Normal | Yes |
| Tail Emergency | Explicit emergency provisional states; no ordinary ranking | No ordinary selectability |
