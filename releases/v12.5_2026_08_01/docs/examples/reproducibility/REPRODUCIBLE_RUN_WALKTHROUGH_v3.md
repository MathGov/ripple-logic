# Reproducible MathGov Run Walkthrough v3

**Purpose:** Show how a small decision can be recorded under run-record schema v3 so that another person can reproduce the gate states and decision state without reading the entire Canon.

**Files:**

- Human-readable walkthrough: this file
- Machine-readable record: `reusable_cups_run_v3.json`
- Schema: `schemas/mathgov_run_record_v3.schema.json`
- Validator: `release/VALIDATE_MATHGOV_RUN.py`

## 1. Decision

A family cafe is choosing among:

- A: continue single-use cups;
- B: run a 30-day reusable deposit-return trial;
- C: buy ultra-cheap cups from an unverified supplier.

This is a low-stakes, reversible Tier 1 run. It does not support general environmental, scientific, or policy claims.

## 2. Qualification

| Option | RG | RF/NCRC | TRC | CSV | Selectable? |
|---|---|---|---|---|---|
| A | Supported | Pass | Pass | Pass | Yes |
| B | Narrowed to a local trial | Pass | Pass | Pass with controls | Yes |
| C | Narrowed | Escalate because supplier rights/safety evidence is missing | Not evaluated after prior failure | Not evaluated after prior failure | No |

The selectable set is `{A, B}`. Option C is not ranked.

## 3. Ranking

The run uses a qualitative Tier 1 comparison, not a formal validated RLS score. B has the stronger expected residual ripple if return rate and wash reliability are adequate. A is the fallback.

The comparison is **non-decisive** because several swing variables remain uncertain.

## 4. Decision state

The cafe owner uses bounded operational authority to select B as a reversible trial with controls. The correct state is:

`SELECTED_BY_AUTHORITY_NON_DECISIVE`

This does not pretend the evidence proved B universally superior.

## 5. Controls and continuity

- 30-day limit;
- fallback supply;
- sanitation check;
- staff workload check;
- monitoring of cup loss, wash reliability, and customer feedback;
- explicit material-obligation and hidden-human-compensation records;
- pause/reopen if a trigger becomes material;
- configuration-assurance fields binding evaluation to the reviewed configuration.

## 6. Replay

Run:

```bash
python release/VALIDATE_MATHGOV_RUN.py docs/examples/reproducibility/reusable_cups_run_v3.json
```

Expected result:

```text
PASS V0 schema validity
PASS V1 semantic conformance
V2 USE-READINESS: NO_AUTOMATED_ISSUES_DETECTED
```

The validator confirms that the record is structurally complete for schema v3 and that its gate, ranking, authority, execution, responsibility-continuity, and configuration-assurance states do not contradict one another. It does not verify evidence truth, legal correctness, empirical instrument validity, physical safety, or decision superiority.
