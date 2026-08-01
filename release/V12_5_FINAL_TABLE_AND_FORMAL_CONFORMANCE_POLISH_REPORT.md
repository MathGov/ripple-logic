# MathGov v12.5 Final Table and Formal-Conformance Polish Report

## Scope

This same-version finalization preserves MathGov Core v12.5, SGP v8.4, all companion versions, the RG -> RF/NCRC -> TRC -> CSV -> RLS cascade, the seven Union Scopes, the seven Welfare Dimensions, all numerical defaults, and all established authority boundaries.

## Table defect confirmed

The prior publication candidate had applied `cantSplit` to every row of every table in the 14 Core DOCX files and centered every table. In the Canon this affected 1,050 rows across 130 tables. The supplied known-good Canon had zero `cantSplit` rows and left-aligned table geometry. The global no-split rule caused excessive white space, unstable pagination, and severe compression risk in long registries. Section 14.3 was especially vulnerable because the current release adds a five-column ownership registry before the canonical audit-flag registry.

## Repairs

- Replaced 121 Canon tables with the exact OOXML table objects from the supplied formatting reference where and only where the complete cell text was identical.
- Preserved every current v12.5 table whose content differs from the reference; applied only stable table-level, header, alternating-row, border, and width geometry.
- Repaired the Section 14.3A.1 five-column ownership registry with proportional full-page widths: Token 2500, Trigger 2350, Required action 2650, Severity 1500, Owner 1280 twips.
- Removed unintended `cantSplit` from body rows in all active DOCX source surfaces, allowing long rows to continue naturally across pages.
- Restored left-aligned, zero-indent table placement consistent with the supplied stable Canon.
- Preserved repeating header rows and removed any exact-height clipping risk.
- Synchronized all canonical DOCX sources to their `core_15` mirrors.

## Scientific audit of “AI Is Quietly Rediscovering Classical Control Engineering”

### Ideas accepted and integrated

1. **Candidate generation is not execution warrant.** A generated proposal, trajectory, or plan does not become physically admissible merely because a model produced it.
2. **Governance permission is not physical admissibility.** Organizational approval, policy compliance, or legal authority cannot substitute for evidence that a physical transition is safe inside a declared operating envelope.
3. **Formal conformance is not reality correspondence.** Formal verification establishes that an implementation satisfies a specification under stated assumptions. It does not by itself establish that the specification accurately represents the physical regime.
4. **Authority must be layered.** Candidate generation, formal conformance, domain qualification, rights/ruin/viability qualification, lawful authorization, and controlled execution are distinct warrant surfaces.

The third point was the one genuine gap in the current wording. It is now stated explicitly in the Canon, PC-AEP v2.2, and MFDI v2.2. The PC-AEP warrant field now requires the verified specification, assumptions, and separate specification-to-reality evidence when formal verification supports a physical claim.

### Claims not imported

1. **“AI only produces statistical correlations.”** Too broad. AI systems may include symbolic, causal, search, optimization, control, retrieval, formal, and hybrid components. Output authority must be judged by the actual architecture and evidence, not by a blanket substrate label.
2. **“Deterministic engineering decides.”** Too narrow. Safety-relevant engineering may use deterministic, stochastic, robust, adaptive, probabilistic, or hybrid control. The scientifically relevant requirement is qualified constraints and bounded warrant, not determinism as such.
3. **“Every permissible action must already exist in predefined knowledge.”** Overstated. Novel actions can be evaluated against invariants, envelopes, tests, simulations, monitors, and staged experimental authorization without being enumerated in advance.
4. **“Engineering knowledge is the final authority.”** Engineering evidence governs physical feasibility and safety claims, but it does not create rights compatibility, legitimate public authority, distributive justice, or ethical authorization.
5. **“Formal verification cannot resolve this.”** Too categorical. Formal verification is indispensable for formal-conformance questions; it is insufficient only when used alone to establish empirical correspondence.
6. **“Autonomy is absent unless the system intrinsically establishes reality.”** Autonomy is multidimensional and graded. Operational independence, policy discretion, learning, authority, moral agency, and physical self-validation are different properties and must not be collapsed.

## Result

The release now preserves the article’s valid scientific warning without importing its categorical overreach. The integrated rule is original MathGov language and remains bounded, inspectable, falsifiable or revision-triggered, and compatible with domain engineering and empirical testing.

## Final rendering and verification

- Added an explicit paragraph boundary between the Section 14.3 five-column ownership registry and the four-column audit-flag registry so Word/LibreOffice cannot merge their continuation semantics.
- Normalized explicit dark-blue terminal borders across all tables after the strict source verifier identified border properties missing from several restored table objects.
- Freshly rendered all 15 DOCX source surfaces to 559 PDF pages.
- Audited 286 tables and 1,626 styled headings.
- Confirmed zero comments, tracked changes, VBA parts, vertical text, exact-height rows, collapsed columns, non-full-width tables, missing repeat headers, style defects, terminal-border defects, blank pages, page-boundary breaches, or stacked-text pages.
- All five subordinate conformance verifiers pass. The master verifier passes after hash and manifest regeneration and clean-extraction replay.
