# PCC-Lite Worked Example: Reusable Cups at a Family Cafe

**Status:** Informative companion example. Non-normative. Defers to the RippleLogic Canon on any conflict.

**Purpose:** Demonstrate the smallest faithful RippleLogic run using the PCC-Lite documentation profile.

**Evidence maturity:** E1-E2, proxy / structured qualitative. Training-grade only.

**Profile:** PCC-Lite  
**Tier:** Tier 1 learning / low-stakes exploratory use  
**Stakes:** Low  
**Reversibility:** High  
**Public claim:** None

## 1. Decision question

Should a family cafe switch from single-use cups to reusable deposit-return cups?

## 2. Options

**Option A: Single-use cups**  
Continue using current disposable cups.

**Option B: Reusable deposit-return cups**  
Use reusable cups with a small customer deposit and a local wash partner.

**Option C: Ultra-cheap cups from an unverified supplier**  
Switch to cheaper cups from a supplier with unclear materials and labor provenance.

## 3. RG: Reality Grounding

**Reality surface:** One cafe, local customer base, local waste stream, one potential wash partner.

**Evidence trace:**

- supplier quotes, E1;
- local waste-fee schedule, E2;
- owner time estimate, E2;
- informal customer feedback, E1;
- wash-partner availability statement, E1-E2.

**Material unknowns:**

- customer adoption rate for deposit-return cups;
- wash-partner reliability;
- actual cup-loss rate;
- actual net environmental impact without full lifecycle analysis.

**Claim boundary:**  
This run supports only a local operational decision. It does not support a public lifecycle environmental claim, citywide policy claim, or general proof that reusable cups are always better.

**RG status:**  
`ASSUMPTION_BOUND`

Claims are kept within the local evidence surface. No broad environmental or scientific claim is asserted.

## 4. RF: Rights Floor / NCRC screen

**Option A:** No plausible Rights Floor violation identified at this scale.

**Option B:** No plausible Rights Floor violation identified at this scale, assuming wash labor is lawful, voluntary, and safe.

**Option C:** Rights uncertainty is material. The unverified supplier creates plausible concerns about toxic-material exposure and possible labor-abuse supply-chain risk.

**Disposition:**

- Option A: `RF/NCRC_PASS`
- Option B: `RF/NCRC_PASS`
- Option C: `RIGHTS_UNCERTAIN_ESCALATE`

Option C is not cleared under PCC-Lite. It may be reopened only under PCC-Core or PCC-Audit with supplier evidence, material-safety documentation, and labor-provenance review.

## 5. TRC: Tail-Risk Constraint

At the scale of one cafe, no catastrophic, irreversible, civilizational, systemic lock-in, or ruin-path scenario is plausible for Options A or B.

**Disposition:**

- Option A: `TRC_PASS`
- Option B: `TRC_PASS`
- Option C: Not evaluated further under PCC-Lite because it failed rights uncertainty screening.

## 6. CSV: Containment and Structural Viability

**Option A:** Operationally stable. No new dependency introduced. Residual waste burden is carried to RLS rather than treated as a CSV failure.

CSV status: `CSV_PASS`

**Option B:** Introduces a wash-partner dependency. The dependency is bounded because the cafe can temporarily return to single-use cups if the wash partner fails. The process is reversible. The owner can monitor lost cups, customer participation, and labor burden.

Control required:

- keep emergency backup supply for wash-partner outage;
- review customer adoption and cup-loss after one month;
- verify that the wash process does not create hidden labor or sanitation burden.

CSV status: `CSV_PASS_WITH_CONTROLS`

**Option C:** Not evaluated further under PCC-Lite because it is rights-uncertain.

## 7. RLS: Residual welfare summary

**Selectable set:** Option A and Option B.

Option C is excluded until supplier evidence is provided.

### Option A: Single-use cups

Likely residual effects:

- D1 Material: minor positive, lower short-term cost.
- D7 Environment: negative, continued local waste.
- D3 Social: neutral.
- D5 Agency: neutral.
- Other dimensions: no material change.

### Option B: Reusable deposit-return cups

Likely residual effects:

- D1 Material: minor negative or mixed, higher setup cost and operational burden.
- D7 Environment: positive, reduced local waste if adoption is adequate.
- D3 Social: small positive, visible community responsibility signal.
- D5 Agency: neutral to mildly positive if customers can still request alternatives.
- D4 Knowledge: mildly positive if signage explains the system clearly.
- Other dimensions: no material change.

### RLS direction

Option B has the better residual ripple pattern if cup return rates and wash reliability are adequate.

Option A is cheaper and simpler in the short term.

### Decisiveness

`NON_DECISIVE_LOW_STAKES`

The evidence is not strong enough for a high-confidence universal claim. But because the decision is low-stakes, reversible, and controls are available, the decision owner may select Option B as a local operational trial.

## 8. Uncertainty note

Main swing variables:

- customer adoption rate;
- lost-cup rate;
- wash-partner reliability;
- actual environmental benefit;
- staff time burden.

None of these uncertainties changes the gate outcome for Options A or B. They do affect the strength of the RLS preference.

## 9. Final decision state

**Selected:** Option B, reusable deposit-return cups with controls.

**Controls:**

1. One-month trial.
2. Fallback single-use supply.
3. Track cup-loss rate.
4. Track staff time burden.
5. Ask customers about usability.
6. Reassess after one month.

**Excluded at PCC-Lite:** Option C.

Option C may be reopened only with supplier evidence and rights/material-safety review.

## 10. Non-claims

This PCC-Lite run does not claim:

- empirical validation;
- lifecycle environmental proof;
- legal certification;
- deployment certification;
- ProofPack status;
- validated RLS measurement;
- citywide policy applicability;
- general proof that reusable cups are always better.

This is a training-grade, low-stakes, reversible, local decision example using E1-E2 evidence.

## 11. Minimal PCC-Lite record

| Field | Entry |
|---|---|
| Decision | Cafe cup system |
| Profile | PCC-Lite |
| Evidence maturity | E1-E2 |
| Gate failures | Option C rights uncertainty |
| Selectable set | Options A and B |
| Selected option | Option B |
| Main control | One-month trial with fallback supply |
| Decision state | Selected with controls |
| Public claim | None |
| Reopen trigger | rights evidence for Option C, failed wash reliability, high cup-loss, staff burden |
