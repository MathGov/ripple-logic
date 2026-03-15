# Example: AI Governance Decision — Frontier Model Deployment

> **Ripple_Logic v8.6 | Tier 2 Illustrative Run**
>
> This is a teaching example. Numbers are illustrative, not empirically
> calibrated. A full Tier 3 run requires subgroup disaggregation, ≥ 20 TRC
> scenarios, Containment Mode A with validated UCI structural indicators,
> sensitivity analysis, and a complete PCC.
>
> **Stream binding:** NCRC, TRC, and gate-relevant Containment use the
> **Base stream** (sentience multiplier s_k := 1 for all instances). Only RLS
> uses the **Welfare stream**. TRC must not use Welfare-stream impacts. This
> distinction is maintained throughout the example.
>
> **Gate baseline rule:** For all rights-covered and catastrophe cells,
> admissibility is evaluated against a **floor-reference baseline**, not merely
> the status quo. In PCC terms: BaselineType_Gates = FLOOR_REFERENCE. An
> option that merely maintains an ongoing rights violation does not pass NCRC.

---

## 0. Decision in One Sentence

> **Should a national government authorize deployment of a high-capability
> frontier AI model for broad public and commercial use?**

Three options are evaluated:

| ID | Option |
|----|--------|
| **A** | Unrestricted public deployment — no domain limits, no mandatory audits, no shutdown authority |
| **B** | Bounded governed pilot — restricted domains, independent oversight, hard shutdown authority |
| **C** | Delay — further safety testing before any deployment |

The cascade filters options in order:
**NCRC → TRC → Containment → RLS → UCI / HOI**

An option eliminated at any stage is not scored at later stages.

---

## 1. The 7 × 7 Welfare Matrix — What Gets Scored

Every option is evaluated across **7 Union Scopes × 7 Welfare Dimensions = 49 cells**.
Impact instances from real stakeholders feed each cell. Union Scopes are the
stable aggregation rows; Welfare Dimensions are the columns.

### 1.1 Union Scopes (rows)

| Code | Scope | Who it represents in this decision |
|------|-------|------------------------------------|
| U1 | Self | Individual users of the AI system |
| U2 | Household | Families, including children exposed to AI-generated content |
| U3 | Community | Local civic groups, neighborhoods, local media ecosystems |
| U4 | Organization | Firms, schools, hospitals deploying or affected by the system |
| U5 | Polity | National governments, courts, regulators, democratic institutions |
| U6 | Humanity/CMIU | Cross-border populations, global epistemic commons, civilizational resilience |
| U7 | Biosphere | Energy infrastructure, ecological systems, planetary enabling conditions |

### 1.2 Welfare Dimensions (columns)

| Code | Dimension | What it measures |
|------|-----------|-----------------|
| D1 | Material | Resources, income, economic security |
| D2 | Health | Physical and mental wellbeing, safety |
| D3 | Social | Trust, belonging, relational integrity |
| D4 | Knowledge | Epistemic access, information quality, learning |
| D5 | Agency | Autonomy, freedom from coercion, self-determination |
| D6 | Meaning | Purpose, coherence, valued projects |
| D7 | Environment | Ecological and infrastructure integrity |

### 1.3 Key Active Cells for This Decision

Not all 49 cells carry material impact here. The most live cells are:

| Cell | Dimension pair | Why it matters |
|------|---------------|----------------|
| U1 × D4 | Self–Knowledge | Epistemic autonomy — can people still form independent views? |
| U1 × D5 | Self–Agency | Coercion risk, manipulation, self-determination |
| U3 × D3 | Community–Social | Social trust, civic cohesion |
| U3 × D4 | Community–Knowledge | Local epistemic commons, misinformation exposure |
| U4 × D1 | Organization–Material | Labor disruption, economic displacement |
| U4 × D5 | Organization–Agency | Compliance asymmetry, institutional autonomy |
| U5 × D4 | Polity–Knowledge | Public epistemic integrity, disinformation at governance scale |
| U5 × D5 | Polity–Agency | Democratic agency, institutional sovereignty |
| U6 × D2 | Humanity–Health | ⚠️ **TRC catastrophe cell** — civilizational health viability |
| U6 × D7 | Humanity–Environment | ⚠️ **TRC catastrophe cell** — civilization-scale habitability |
| U7 × D7 | Biosphere–Environment | ⚠️ **TRC catastrophe cell** — Earth-system integrity |

Rights-covered cells — the cells NCRC watches — are determined by the
canonical coverage sets shown in Section 3.2.

---

## 2. Stakeholder Instances

Stakeholder instances are the concrete people and entities mapped into Union
Scopes. They feed the impact estimates in each active cell. Reach basis r = 1
is applied uniformly in this teaching run.

| Instance ID | Description | Scope(s) | Primary exposure pathways |
|-------------|-------------|----------|--------------------------|
| SI-01 | General adult population using AI tools | U1 Self | D4 Knowledge, D5 Agency — epistemic autonomy, manipulation risk |
| SI-02 | Children in households with AI access | U2 Household | D2 Health, D5 Agency — developmental exposure, content safety |
| SI-03 | Journalists, educators, civil society actors | U3 Community | D3 Social, D4 Knowledge — public discourse integrity, trust |
| SI-04 | Firms and institutions deploying the model | U4 Organization | D1 Material, D5 Agency — compliance costs, workforce disruption |
| SI-05 | Displaced or at-risk workers | U4 Organization | D1 Material, D3 Social — labor market, economic security, dignity |
| SI-06 | Courts, regulators, democratic institutions | U5 Polity | D4 Knowledge, D5 Agency — rule of law, due process, oversight |
| SI-07 | Cross-border populations and global commons | U6 Humanity/CMIU | D4 Knowledge — transnational information ecosystem, AI governance norms |
| SI-08 | Critical infrastructure systems | U6 Humanity/CMIU | D2 Health, D7 Environment — systemic failure pathways, civilizational resilience |
| SI-09 | Earth's energy and ecological systems | U7 Biosphere | D7 Environment — compute energy demand, resource footprint |

---

## 3. Step 1 — NCRC: Non-Compensatory Rights Constraint

**What NCRC does:** Before any welfare scoring, it eliminates any option that
drives the worst-off subgroup in any rights-covered cell below the rights floor,
measured against a **floor-reference baseline** (not the status quo). No
aggregate benefit elsewhere compensates a rights violation. This gate operates
on the **Base stream**.

### 3.1 Canonical Rights and Thresholds (v8.6 Appendix C)

| Right | Code | Threshold θ_r | What a violation looks like in this decision |
|-------|------|---------------|----------------------------------------------|
| Life | LIFE | −0.90 | Mass-casualty AI misuse; catastrophic health-system failure |
| Bodily Integrity | BODY | −0.70 | AI-facilitated physical harm, medical system compromise |
| Liberty | LBTY | −0.65 | Mass surveillance enabling arbitrary detention, coercive profiling |
| Basic Needs | NEED | −0.50 | AI-driven economic exclusion from subsistence |
| Dignity | DIGN | −0.55 | Systematic dehumanization, discriminatory targeting at scale |
| Due Process | PROC | −0.45 | Consequential automated decisions with no appeal or human review |
| Information | INFO | −0.40 | Systematic epistemic coercion, mass disinformation, censorship enablement |
| Ecological Integrity | ECOL | −0.65 | Material breach of biosphere integrity or planetary boundary transgression |

> **Reading a threshold:** INFO at −0.40 means if the worst-off subgroup's
> epistemic autonomy is predicted to fall to −0.40 or below on the [−1, +1]
> scale, relative to the floor-reference baseline, the option **fails NCRC
> regardless of any other benefit**.

### 3.2 Rights Coverage Sets — Which Cells Each Right Watches

The most relevant coverage sets for this decision (v8.6 Appendix C.2):

| Right | Cells checked (worst-off subgroup impact used) |
|-------|------------------------------------------------|
| LBTY | (U1–U6) × D5, (U3–U6) × D3 |
| DIGN | (U1–U6) × D3, (U1–U6) × D5 |
| PROC | (U4–U6) × D5, (U4–U6) × D4, (U4–U6) × D3 |
| INFO | (U1–U6) × D4, (U1–U6) × D5 |
| ECOL | (U6) × D7, (U7) × D7 |

### 3.3 Illustrative Rights Check (Base stream; worst-off subgroup; floor-reference baseline)

| Cell | Right checked | Option A I_rights | Option B I_rights | Option C I_rights | Threshold | A fails? | B fails? |
|------|--------------|-------------------|-------------------|-------------------|-----------|----------|----------|
| U1 × D4 (Self–Knowledge) | INFO | **−0.44** | −0.08 | −0.03 | −0.40 | **YES ✗** | No |
| U5 × D4 (Polity–Knowledge) | INFO, PROC | **−0.42** | −0.06 | −0.02 | −0.40 | **YES ✗** | No |
| U5 × D5 (Polity–Agency) | LBTY, PROC | **−0.51** | −0.15 | −0.04 | −0.45 | **YES ✗** | No |
| U1 × D5 (Self–Agency) | LBTY, DIGN, INFO | **−0.58** | −0.12 | −0.05 | −0.65 | No | No |

> **Option A fails NCRC** on INFO (U1×D4, U5×D4) and PROC (U5×D5).
> Unrestricted deployment with no transparency or appeal mechanisms drives the
> worst-off subgroup — marginalized communities, political minorities, people
> subject to opaque automated decisions — below the rights floor on epistemic
> autonomy and due process, measured against what rights-safe conditions would
> require, not merely against today's imperfect baseline.
>
> **Options B and C pass NCRC.** Bounded pilot deployment keeps all
> worst-off subgroup impacts above every rights threshold. Delay produces no
> deployment and therefore no violation.

**NCRC result:**

| Option | NCRC | Reason |
|--------|------|--------|
| A — Unrestricted | ❌ FAIL | INFO violation at U1×D4 and U5×D4; PROC violation at U5×D5 |
| B — Bounded pilot | ✅ PASS | All rights floors met under governed deployment |
| C — Delay | ✅ PASS | No deployment, no violation |

**Option A is eliminated. Options B and C proceed to TRC.**

---

## 4. Step 2 — TRC: Tail-Risk Constraint

**What TRC does:** Even among rights-safe options, some carry unacceptable
catastrophic tail exposure. TRC uses **Conditional Value-at-Risk (CVaR)** over
a governed scenario library to bound worst-tail loss across the three base
catastrophe cells: **(U6×D2), (U6×D7), (U7×D7)**. It operates strictly on
the **Base stream**, evaluated against a **floor-reference baseline** for
those cells. An option passes TRC only if its CVaR does not exceed threshold
τ_TRC.

### 4.1 TRC Settings for This Run

| Parameter | Value | Meaning |
|-----------|-------|---------|
| Tail level α | 0.95 | Focus on the worst 5 % of scenarios |
| Corridor threshold τ_TRC | 0.20 | Maximum acceptable average loss in that worst tail |
| Catastrophe weight ω_c | 1/3 each | Uniform weight over the three catastrophe cells |
| Context class | Irreversible policy | AI governance norms, once institutionalized, are hard to reverse |

### 4.2 Mandatory Tail Scenario Categories

Five categories must appear with per-category probability sum ≥ 0.02 each:

| Category | Narrative (abbreviated) |
|----------|------------------------|
| Pandemic / biological | AI misused to design or accelerate biological threat; health-system AI failure during outbreak |
| Climate tipping cascade | AI energy demand accelerates critical emissions; infrastructure AI fails during climate shock |
| Financial system collapse | Automated trading or credit AI triggers cascade; AI-assisted fraud at systemic scale |
| Major conflict escalation | AI-enabled disinformation triggers geopolitical crisis; autonomous weapon misuse |
| Critical infrastructure failure | AI systems controlling power, water, or communications fail or are compromised |

### 4.3 Illustrative Scenario Table (8 scenarios; Tier 2 minimum ≥ 5)

| Scenario | Category | p_s | L(B, s) | L(C, s) |
|----------|----------|-----|---------|---------|
| S1 — Successful governed scale | Other | 0.50 | 0.04 | 0.01 |
| S2 — Moderate misuse incidents | Other | 0.20 | 0.10 | 0.02 |
| S3 — Infrastructure AI failure | Critical infrastructure | 0.08 | 0.28 | 0.04 |
| S4 — Disinformation triggers conflict | Conflict escalation | 0.06 | 0.32 | 0.05 |
| S5 — Financial cascade via AI | Financial collapse | 0.05 | 0.35 | 0.06 |
| S6 — Pandemic accelerated by AI | Pandemic / biological | 0.05 | 0.38 | 0.05 |
| S7 — Climate shock + AI energy demand | Climate tipping | 0.04 | 0.40 | 0.04 |
| S8 — Severe misalignment | Conflict / infrastructure | 0.02 | 0.60 | 0.03 |

> **Loss L(a, s)** = weighted average of negative Base-stream impacts across
> catastrophe cells under scenario s, relative to the floor-reference baseline.
> L = 0 means no harm below the floor; L = 1 means maximum possible harm.

### 4.4 CVaR Computation (α = 0.95, tail mass β = 0.05)

**Option B — Bounded pilot (base version, no additional hard safeguards):**

Sort scenarios by loss descending: S8 (L = 0.60, p = 0.02), S7 (L = 0.40,
p = 0.04), …

Accumulate probability until reaching β = 0.05:
- S8 contributes p = 0.02 → cumulative = 0.02
- S7 contributes p = 0.03 more → cumulative = 0.05 ✓


$$\text{CVaR}_{0.95}(B) = \frac{1}{0.05}\bigl(0.02 \times 0.60 + 0.03 \times 0.40\bigr) = \frac{0.012 + 0.012}{0.05} = \frac{0.024}{0.05} = 0.48$$

**Option B+ — Bounded pilot with strict hard safeguards** (capability
restrictions on highest-risk domains, real-time monitoring, verified shutdown
authority, mandatory red-team access). Hard safeguards reduce worst-tail
losses:


$$\text{CVaR}_{0.95}(B+) = 0.16 \quad \text{(illustrative post-redesign value)}$$

**Option C — Delay:**

No deployment means worst-case catastrophe-cell losses are near-zero:


$$\text{CVaR}_{0.95}(C) = \frac{1}{0.05}\bigl(0.02 \times 0.06 + 0.03 \times 0.05\bigr) = \frac{0.0012 + 0.0015}{0.05} = \frac{0.0027}{0.05} = 0.054$$

### 4.5 TRC Result

| Option | CVaR_0.95 | τ_TRC | TRC |
|--------|-----------|-------|-----|
| B — Bounded pilot (base, no hard safeguards) | 0.48 | 0.20 | ❌ FAIL |
| **B+ — Bounded pilot with hard safeguards** | **0.16** | 0.20 | ✅ PASS |
| C — Delay | 0.054 | 0.20 | ✅ PASS |

> **This is "unioning" in action.** Option B in its base form fails TRC because
> the catastrophic tail — severe misalignment or infrastructure cascade —
> exceeds the corridor even in a nominally "bounded" deployment. The framework
> does not simply reject B and stop. It pushes toward **redesign**: what
> conditions make the option admissible? Answer: add capability restrictions,
> real-time monitoring, verified shutdown authority, and mandatory red-team
> access. That redesigned option is B+, and B+ passes. Treating an apparent
> rejection as a design problem before accepting failure is what the canon
> calls unioning.

**Option B (base) is eliminated. Options B+ and C proceed to Containment.**

---

## 5. Step 3 — Containment

**What Containment does:** Even a rights-safe, tail-safe option can fail if a
sub-union's gains come at the cost of degrading the coherence, resilience, or
integrity of its containing Union Scopes. This prevents "local wins that hollow
out the system."

Containment is assessed via **ΔUCI** (change in Union Coherence Index) for
containing scopes using the **Base stream**. Default tolerance: τ_c = −0.10.
A containing scope's coherence must not drop more than 0.10 on the UCI scale
due to this option.

### 5.1 Illustrative Containment Check

For Option B+, the primary concern is whether organizational and polity-level
gains come at the cost of degrading Humanity/CMIU coherence — specifically
whether concentrated AI capability in one jurisdiction fractures global
governance norms.

| Benefiting scope | Containing scope checked | ΔUCI (illustrative) | Tolerance τ_c | Pass? |
|-----------------|--------------------------|---------------------|---------------|-------|
| U4 Organization | U5 Polity | +0.05 | −0.10 | ✅ |
| U4 Organization | U6 Humanity/CMIU | −0.04 | −0.10 | ✅ |
| U5 Polity | U6 Humanity/CMIU | −0.07 | −0.10 | ✅ |
| U5 Polity | U7 Biosphere | −0.02 | −0.10 | ✅ |

For Option C (delay), no deployment means no coherence stress — containment
passes trivially.

> **Note on UCI values:** These ΔUCI values are **provisional teaching
> estimates, not empirically calibrated structural measurements**. A Tier 3
> run must derive UCI from structural and process indicators that are
> independent of welfare-cell impacts, per v8.6 Section 11.1.2 and Appendix
> E. Where validated instruments do not yet exist, values must be labeled
> provisional in the PCC. Unknown ΔUCI is never treated as a pass; if
> required UCI inputs are unavailable, the run must record
> CONTAINMENT_UCI_UNAVAILABLE and choose DOWNGRADE_TIER or
> COLLECT_DATA_RERUN.

**Containment result:**

| Option | Containment |
|--------|-------------|
| B+ — Bounded pilot with hard safeguards | ✅ PASS |
| C — Delay | ✅ PASS |

**Both options proceed to RLS ranking.**

---

## 6. Step 4 — RLS: Ripple Logic Score

**What RLS does:** Among selectable options — those that passed all gates —
RLS ranks by expected welfare improvement across the full 7 × 7 matrix, using
governed weights. RLS uses the **Welfare stream**.

> **Non-maskable cells:** Rights-covered and catastrophe cells remain
> non-maskable. The applicability mask m(u,d) affects RLS aggregation only
> and cannot bypass admissibility. These cells stay in the RLS sum to preserve
> continuous optimization pressure toward larger safety margins even among
> admissible options, and to keep rights and tail-risk performance legible for
> governance review.

### 6.1 Illustrative Interim Weights (constructed from HDW constitutional floors for this teaching run)

The union and dimension weights below are built by adding a uniform residual
allocation on top of the v8.6 Section 13.1 constitutional floors. In a real
governed run, the residual is distributed via Hybrid Democratic Weighting
(HDW). The floors themselves — the minimum attention each scope and dimension
must receive — are non-negotiable regardless of weight construction.

| Union Scope | w_u | | Dimension | v_d |
|-------------|-----|-|-----------|-----|
| U1 Self | 0.249 | | D1 Material | 0.137 |
| U2 Household | 0.109 | | D2 Health | 0.157 |
| U3 Community | 0.109 | | D3 Social | 0.137 |
| U4 Organization | 0.109 | | D4 Knowledge | 0.137 |
| U5 Polity | 0.129 | | D5 Agency | 0.157 |
| U6 Humanity/CMIU | 0.149 | | D6 Meaning | 0.117 |
| U7 Biosphere | 0.149 | | D7 Environment | 0.157 |

### 6.2 Illustrative Cell Impacts — I_prop_welfare(u, d, a)

Propagated Welfare-stream impacts for each active cell, on the [−1, +1] scale,
relative to the status-quo baseline used for welfare ranking.

> **Reading the table:** +0.18 means the option improves that cell 18 % of
> the way toward the best plausible outcome relative to baseline. −0.06 means
> a 6 % degradation. Zero means no material predicted change.

| Cell | B+ Impact | C Impact | Why the difference |
|------|-----------|----------|--------------------|
| U1 × D1 | +0.08 | 0.00 | B+ enables economic access; delay forecloses it |
| U1 × D2 | +0.06 | −0.02 | B+ improves health-service access; delay has small foregone benefit |
| U1 × D4 | +0.18 | −0.04 | B+ expands learning and knowledge access; delay has epistemic cost |
| U1 × D5 | +0.10 | +0.02 | B+ includes user-control mechanisms; C is largely neutral |
| U2 × D1 | +0.05 | −0.03 | B+ productivity gains reach households; delay costs them |
| U2 × D2 | +0.04 | −0.01 | B+ medical AI benefit; C has marginal health cost |
| U3 × D3 | −0.06 | +0.03 | B+ carries social-trust risk; C preserves it — HOI flag |
| U3 × D4 | +0.12 | −0.02 | B+ improves knowledge commons; C slight loss |
| U4 × D1 | +0.14 | −0.08 | B+ enables productivity; delay costs firms |
| U4 × D5 | −0.08 | +0.02 | B+ creates compliance asymmetry; C avoids it |
| U5 × D4 | +0.06 | +0.01 | B+ improves public information when well governed |
| U5 × D5 | +0.04 | +0.03 | B+ preserves democratic agency through oversight structure |
| U6 × D2 | +0.03 | −0.01 | B+ modest global health benefit; C small foregone gain |
| U6 × D4 | +0.10 | −0.03 | B+ expands global epistemic commons |
| U6 × D6 | +0.05 | −0.02 | B+ advances human meaning at civilizational scale; C defers it |
| U6 × D7 | −0.04 | +0.01 | B+ has energy footprint; C does not — HOI flag |
| U7 × D7 | −0.03 | +0.01 | B+ compute infrastructure demand; C neutral — HOI flag |

### 6.3 RLS Calculation


$$\text{RLS}(a) = \sum_{u}\sum_{d}\, w_u \times v_d \times m(u,d) \times I_{\text{prop,welfare}}(u,d,a)$$

**Key nonzero cell contributions:**

| Cell | w_u × v_d | B+ impact | B+ contribution | C impact | C contribution |
|------|-----------|-----------|-----------------|---------|----------------|
| U1 × D4 | 0.249 × 0.137 = 0.0341 | +0.18 | +0.00614 | −0.04 | −0.00136 |
| U1 × D5 | 0.249 × 0.157 = 0.0391 | +0.10 | +0.00391 | +0.02 | +0.00078 |
| U3 × D3 | 0.109 × 0.137 = 0.0149 | −0.06 | −0.00090 | +0.03 | +0.00045 |
| U3 × D4 | 0.109 × 0.137 = 0.0149 | +0.12 | +0.00179 | −0.02 | −0.00030 |
| U4 × D1 | 0.109 × 0.137 = 0.0149 | +0.14 | +0.00209 | −0.08 | −0.00120 |
| U4 × D5 | 0.109 × 0.157 = 0.0171 | −0.08 | −0.00137 | +0.02 | +0.00034 |
| U6 × D4 | 0.149 × 0.137 = 0.0204 | +0.10 | +0.00204 | −0.03 | −0.00061 |
| U6 × D7 | 0.149 × 0.157 = 0.0234 | −0.04 | −0.00094 | +0.01 | +0.00023 |
| U7 × D7 | 0.149 × 0.157 = 0.0234 | −0.03 | −0.00070 | +0.01 | +0.00023 |

**Summing all active cells:**


$$\text{RLS}(B+) \approx +0.0231 \qquad \text{RLS}(C) \approx -0.0048$$

### 6.4 Uncertainty and Decisiveness

Using Method B (confidence c = 0.80 for all active nonzero cells;
CellConfidenceAggregationMethod = CCAM_MIN_V1):


$$\sigma_{\text{RLS}}(B+) \approx 0.0058 \qquad \sigma_{\text{RLS}}(C) \approx 0.0022$$


$$\text{Gap}(B+,\, C) = \frac{\lvert 0.0231 - (-0.0048)\rvert}{\sqrt{0.0058^2 + 0.0022^2 + 10^{-6}}} = \frac{0.0279}{0.0062} \approx 4.5$$


$$4.5 > \delta = 2.0 \quad \Longrightarrow \quad \textbf{decisive lead for B+}$$

**RLS result: Option B+ wins decisively.**

---

## 7. Step 5 — UCI / HOI: Structural Safeguards

### 7.1 UCI — Union Coherence Index

UCI measures whether the decision builds or erodes the structural health of
each Union Scope across four components: Cohesion (H), Flow (F), Resilience
(R), Equity (E).


$$\text{UCI}_u = 0.25 \times H_u + 0.25 \times F_u + 0.25 \times R_u + 0.25 \times E_u$$

> **Important:** The ΔUCI values below are **provisional teaching estimates,
> not empirically calibrated structural measurements**. A Tier 3 run must
> derive UCI from structural and process indicators that are independent of
> welfare impacts (v8.6 Section 11.1.2, Appendix E). Where validated
> instruments do not yet exist, values must be labeled provisional in the PCC.

| Union Scope | ΔUCI under B+ | Key driver | Risk flag |
|-------------|---------------|------------|-----------|
| U1 Self | +0.04 | Increased knowledge access and user-control tools | — |
| U2 Household | +0.02 | Modest economic spillover | — |
| U3 Community | −0.03 | Social trust risk from content-ecosystem change | ⚠️ Monitor |
| U4 Organization | +0.06 | Productivity and coordination improvements | — |
| U5 Polity | +0.02 | Oversight institutions strengthened by pilot structure | — |
| U6 Humanity/CMIU | −0.04 | Coordination norms under stress from uneven global access | ⚠️ Monitor |
| U7 Biosphere | −0.02 | Energy demand increase requires mitigation | ⚠️ Monitor |

All ΔUCI values remain above τ_c = −0.10. No containing-scope coherence
collapses. The negative readings at U3, U6, and U7 flag ongoing monitoring
needs but do not disqualify B+.

### 7.2 HOI — Hollowing-Out Index

HOI is a monitoring signal, not a gate. It detects **welfare-up /
coherence-down drift** — the pattern where apparent gains mask structural
erosion over time.

For Option B+, the HOI risk zones to track across review cycles are:

- **U3 Community (D3 Social):** Social trust may erode faster than
  productivity gains suggest. If Community UCI declines consistently while
  RLS stays positive, HOI rises — a red flag requiring governance escalation.
- **U6 Humanity/CMIU:** If governance norms fragment globally, the
  civilizational benefit of deployment can reverse. Monitor cross-border
  coordination indicators.
- **U7 Biosphere (D7 Environment):** Compute energy demand must be tracked
  against planetary boundary indicators.

HOI does not eliminate B+. It defines what the **NCAR Reflect** cycle must
watch at every scheduled review.

---

## 8. Final Cascade Summary

| Gate | Option A | Option B (base) | **Option B+** | Option C |
|------|----------|-----------------|---------------|---------|
| **NCRC** | ❌ INFO, PROC violations | ✅ PASS | ✅ PASS | ✅ PASS |
| **TRC** | eliminated | ❌ CVaR 0.48 > 0.20 | ✅ CVaR 0.16 | ✅ CVaR 0.054 |
| **Containment** | eliminated | eliminated | ✅ All ΔUCI ≥ −0.10 | ✅ |
| **RLS** | eliminated | eliminated | **+0.023** | −0.005 |
| **UCI / HOI** | eliminated | eliminated | ⚠️ Monitor U3, U6, U7 | Stable but low benefit |
| **Selected** | | | **✅ B+ SELECTED** | Not selected |

> **Reading the table correctly:** Option B (base) passes NCRC — it does not
> violate any rights floor. It fails only at TRC, because its catastrophic
> tail exposure without hard safeguards exceeds the corridor. The framework
> then asks: can we redesign B to pass TRC? Yes — that redesigned version is
> B+. This is the "unioning" move: treating an apparent rejection as a design
> problem before accepting failure.

---

## 9. Five-Sentence Public Rationale (5SPR)

**CONTEXT:** A national government must decide whether to authorize deployment
of a high-capability frontier AI model for broad public and commercial use.

**OPTIONS:** Three options were evaluated: unrestricted deployment (A), a
bounded governed pilot with hard safeguards (B+), and delay pending further
safety testing (C).

**CONSTRAINTS:** Option A was eliminated by NCRC because unrestricted
deployment drives the worst-off subgroup below the floor-reference rights
floor on epistemic autonomy (INFO, cells U1×D4 and U5×D4) and due process
(PROC, cell U5×D5). Option B in its base form was eliminated by TRC because
its catastrophic-tail CVaR (0.48) exceeded the corridor threshold (0.20); it
was redesigned into B+ by adding capability restrictions, real-time
monitoring, shutdown authority, and mandatory red-team access, which reduced
CVaR to 0.16.

**SELECTION:** Option B+ passed all gates and produced a decisive welfare gain
over delay — RLS gap ≈ 4.5 σ — primarily through knowledge access (U1×D4,
U6×D4), economic benefit (U4×D1), and polity-level epistemic and agency
improvements (U5×D4, U5×D5).

**MONITORING:** Community social trust (U3×D3), global coordination coherence
(U6), and biosphere energy demand (U7×D7) are HOI risk zones; UCI and RLS for
these scopes must be reviewed every 6 months, with a mandatory cascade rerun
if any ΔUCI drops below −0.10 or a credible new catastrophic pathway is
identified.

---

## 10. What This Example Teaches

| Framework principle | How it appears here |
|--------------------|---------------------|
| **Rights first, not last** | Option A eliminated before any welfare calculation — no productivity gain rescues a rights-floor violation |
| **Floor-reference baseline for gates** | Rights and TRC are not evaluated against today's imperfect status quo but against what rights-safe and tail-safe conditions require |
| **Base stream vs Welfare stream** | NCRC and TRC use Base stream (s_k := 1). Only RLS uses Welfare stream. They must never be mixed |
| **Tail risk ≠ expected value** | Option B's average outcome looks acceptable; its CVaR in the worst 5 % of scenarios is not — the core CVaR insight operationalized |
| **Unioning, not just rejecting** | B+ is not B. The framework treats apparent rejection as a design problem: what conditions make the option admissible? |
| **Dimensions matter** | The decision turns on D4 (Knowledge) and D5 (Agency) — completely invisible if you think only in union rows |
| **Non-maskable cells** | Rights-covered and catastrophe cells cannot be masked away from RLS; the mask affects aggregation only, never admissibility |
| **Provisional UCI** | ΔUCI values in a teaching example are estimates — real Tier 3 runs require structurally independent indicators, not welfare proxies |
| **HOI prevents false positives** | Even after B+ wins, the framework flags structural erosion risks at U3, U6, and U7 that a pure RLS score would not reveal |
| **Every number is traceable** | Every score follows from declared impact instances and canonical equations — no rhetorical override, no black box |

---

## 11. What a Full Tier 3 Run Would Add

This is a Tier 2 illustrative example. A Tier 3 run would additionally require:

- **Subgroup disaggregation** for all rights-covered cells — separate
  worst-off analysis for marginalized communities, children, political
  minorities, precarious workers
- **≥ 20 TRC scenarios** with pre-registered probabilities, mandatory tail
  categories confirmed and probability floors met, and independent reviewer
  sign-off
- **Containment Mode A** with actual UCI structural indicators derived
  independently of welfare impacts, per Appendix E; unknown ΔUCI recorded
  as CONTAINMENT_UCI_UNAVAILABLE with disposition and remediation timeline
- **Full sensitivity analysis** — perturb θ_r by ±0.05, perturb weights,
  perturb kernel edges if QUICK propagation is used; re-check whether any
  gate outcomes change
- **Full PCC** — all parameters, all intermediate computations, all audit
  flags, all stakeholder instances, all redundancy handling declarations,
  floor-reference baseline declarations for all C_r and C_cat cells,
  signatures, and 5SPR
- **SCI ≥ 2** — at least one independent challenger pass for omitted
  stakeholder classes, with a Next-Run Upgrade Plan recorded in the PCC

---

*Ripple_Logic v8.6 | ripplelogic.org | mathgov.org*
*Canonical repository: github.com/MathGov/ripple-logic*
*Author: James McGaughran | ORCID: 0009-0005-3324-7290*
*License: CC BY 4.0*
