# RippleLogic

**Canonical decision operating system for rights-constrained, ripple-aware ethical governance**

| | |
|---|---|
| **Version** | v9.0 |
| **Status** | Freeze-ready core canon line, with a synced document/workbook set and release manifest/hash package |
| **License** | CC BY-ND 4.0 (spec text) · MIT (code) · CC BY 4.0 (examples) |
| **Canonical sites** | ripplelogic.org · mathgov.org |
| **Repository** | github.com/MathGov/ripple-logic |
| **Author** | James McGaughran · ORCID: 0009-0005-3324-7290 |

---

## What RippleLogic Is

RippleLogic is a general-purpose ethical operating system that evaluates decisions across nested stakeholder scopes while enforcing:

- **Non-compensatory rights floors** so rights violations cannot be traded away for aggregate benefit elsewhere
- **Catastrophic tail-risk control** using Conditional Value-at-Risk (CVaR) over a governed scenario library rather than expected value
- **Containment** so local gains may not degrade the coherence of containing union scopes beyond governed tolerance
- **Welfare ranking** only among options that pass the admissibility gates, scored across a 7 × 7 welfare matrix of union scopes × welfare dimensions
- **Structural diagnostics** through Union Coherence Index (UCI) and Hollowing-Out Index (HOI) for long-run integrity monitoring and tie-breaking

It is designed for governance and public policy analysis, AI alignment and safety evaluation, institutional and organizational decision-making, and other high-stakes environments requiring auditable, rights-respecting reasoning under uncertainty.

**Canonical naming:** RippleLogic is the canonical release-line name. MathGov remains the historical umbrella term for the broader lineage and ecosystem.

**Single source of truth:** The Foundation Canon (`RippleLogic_v9.0_Canon.docx`) is the governing artifact for the v9.0 core release line. If any companion artifact conflicts with the Canon, the Canon governs.

---

## Current Canonical Release

**Current release:** v9.0  
**Release folder:** `releases/v9.0_2026-03-24`  
**Release type:** Freeze-ready core canon line  
**Core package:** `RippleLogic_v9.0_Core_Freeze_Package.zip`

The v9.0 line contains five synced core artifacts:

- `RippleLogic_v9.0_Canon.docx`
- `SGP_4.3.docx`
- `ripple_md_Standard_v2.0.docx`
- `RippleLogic_Agent_System_v9.0.docx`
- `RippleLogic_Aligners_Sheet_v2.3.xlsx`

The release package also includes:

- SHA-256 checksums
- machine-readable release manifests
- release notes
- ProofPack release-integrity documentation

---

## The Core Decision Cascade

RippleLogic filters and ranks options in a fixed lexicographic order:

```text
NCRC → TRC → Containment → RLS → UCI / HOI
```

- **NCRC** removes rights-violating options.
- **TRC** removes options with unacceptable catastrophic tail risk.
- **Containment** blocks local optimization that degrades containing scopes.
- **RLS** ranks the remaining selectable options by weighted welfare improvement.
- **UCI / HOI** provide structural diagnostics, tie-breaking support, and longitudinal monitoring.

Later-stage gains cannot compensate for earlier-stage failure.

---

## The 7 × 7 Welfare Matrix

Every decision is evaluated across **49 cells**, formed by **7 union scopes × 7 welfare dimensions**.

### Union Scopes

| Code | Scope |
|------|-------|
| U1 | Self |
| U2 | Household |
| U3 | Community |
| U4 | Organization |
| U5 | Polity |
| U6 | Humanity / CMIU |
| U7 | Biosphere |

### Welfare Dimensions

| Code | Dimension |
|------|-----------|
| D1 | Material |
| D2 | Health |
| D3 | Social |
| D4 | Knowledge |
| D5 | Agency |
| D6 | Meaning |
| D7 | Environment |

All normative computation is performed on the canonical **[-1, +1]** scale.

---

## Companion Artifacts

The Canon is the normative source of truth. The following companion artifacts extend or operationalize the v9.0 core line:

| Artifact | Version | Role |
|----------|---------|------|
| Sentience Gradient Protocol (SGP) | v4.3 | Sentience scoring and rights-of-protection interface consumed by RippleLogic |
| ripple.md Standard | v2.0 | Portable alignment contract and wrapper/interface standard |
| RippleLogic Agent System | v9.0 | Operational agent controls, evaluation harness expectations, stewardship, and deployment mode governance |
| RippleLogic Aligners Sheet | v2.3 | Worked-run and audit-ready workbook companion |

---

## Validation Status

RippleLogic v9.0 is **freeze-ready as the core synced document/workbook set**.

This means the v9.0 release line now provides:

- a synced canonical document stack
- a calculable and publication-clean workbook companion
- release hashes and manifest surfaces suitable for GitHub and website publication

This does **not** mean the system is fully empirically validated or that Tier 4 replay claims are open.

### Claim boundary

- **Core synced canon line:** ready
- **Tier 1–3 specification/use as a documented framework:** claimable within the stated boundaries of the canon and companion documents
- **Tier 4 independent replay claim:** still prohibited until validator/schema surfaces and any optional executable companion assets are separately published and pinned

---

## Repository Structure

```text
releases/
  v7.4.5_2026-01-25/
  v8.1_2026-02-14/
  v8.5.3_2026-02-20/
  v8.6_2026_03_15/
  v9.0_2026-03-24/
examples/
ripplelogic-proofpack-lite/
README.md
RELEASE_HISTORY.md
VALIDATION_STATUS.md
RELEASE_MANIFEST.json
```

---

## Relationship to MathGov

MathGov is the historical umbrella lineage from which RippleLogic emerged. RippleLogic is the canonical name of the formal release line and specification stack. MathGov remains a valid lineage, ecosystem, and narrative reference.

---

## Citation

McGaughran, J. (2026). *RippleLogic Framework v9.0* [Specification package]. MathGov Institute for Ethical Systems Design.

Canonical artifacts:
- `RippleLogic_v9.0_Canon.docx`
- `SGP_4.3.docx`
- `ripple_md_Standard_v2.0.docx`
- `RippleLogic_Agent_System_v9.0.docx`
- `RippleLogic_Aligners_Sheet_v2.3.xlsx`

Pin downstream references to the canonical filenames and SHA-256 values in the release manifest and checksum files.

---

## License

RippleLogic uses a three-layer license structure:

- **Specification text**: CC BY-ND 4.0
- **Reference implementations, schemas, code, templates, and test fixtures**: MIT
- **Worked examples, teaching materials, and translations**: CC BY 4.0

See `LICENSE` for full terms.

---

## Author

**James McGaughran**  
Creator and system architect of RippleLogic and the MathGov lineage.  
ORCID: 0009-0005-3324-7290

---

*RippleLogic v9.0 · ripplelogic.org · mathgov.org*  
*github.com/MathGov/ripple-logic*
