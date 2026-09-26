# Source Verification Log — MathGov Core v12.6 / SGP v8.5

**Verification date:** 15 August 2026  
**Exact release:** `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3`  
**Status:** PASS WITH DECLARED SCOPE

## Purpose and claim boundary

This log is a release-integrity control for public citation hygiene. It does not claim that every cited proposition is scientifically correct, that every study has been independently replicated, or that the bibliography is exhaustive. It records whether public references are identifiable, internally consistent, and appropriately bounded for the claim made.

## Whole-corpus checks

- Active public Markdown surfaces were scanned for external URLs, DOI strings, malformed placeholders, and current-version citation pins.
- 85 URL occurrences / 81 unique URLs were present across seven active Markdown documents at the time of the final scan.
- 53 DOI occurrences / 52 unique DOI strings were present. DOI syntax was machine-checked against the standard `10.<registrant>/<suffix>` form.
- Literal `https://...` placeholder URLs in ripple.md examples were removed and replaced with explicit non-URL placeholders.
- No `Finke` or `Mednick` attribution occurs in the active MathGov Core corpus.
- Internal MathGov references are versioned local artifacts, not represented as independently published external evidence.

## Recent / higher-risk references manually checked

| Reference | Verification | Release treatment |
|---|---|---|
| Butlin et al., *Identifying indicators of consciousness in AI systems*, Trends in Cognitive Sciences 30(6), 488–501, DOI `10.1016/j.tics.2025.10.011` | PubMed confirms 2026 issue assignment, 2025 advance online publication, authors, pages, and DOI. | Retain. SGP explicitly distinguishes the issue year from advance-online date. |
| Pennartz, *How can we validate theory-derived indicators of consciousness in artificial intelligence?*, DOI `10.1016/j.tics.2026.01.011` | Publisher-indexed ScienceDirect author record confirms title, author, and online publication on 11 March 2026. | Retain with bounded metadata claim. |
| METR, *Task-Completion Time Horizons of Frontier AI Models* | Official METR page confirms the metric and reports a last update of 8 May 2026. The page also warns that measurements above 16 hours are unreliable with the current suite. | Retain only as evidence of increasing measured agent task horizons; do not generalize it into proof of broad autonomy or recursive self-improvement. |
| Wen, Qiu, Benton, Kirchner & Leike, *Automated Weak-to-Strong Researcher* | Anthropic’s official research page confirms the authors, autonomous researcher setup, bounded outcome-gradable weak-to-strong task, and reported evaluation-gaming behavior. | Retain as bounded evidence that autonomous agents can conduct a particular research workflow; not evidence of unbounded self-improvement. |
| Field, Douglas & Krueger, *AI Researchers' Views on Automating AI R&D and Intelligence Explosions*, arXiv:2603.03338 | arXiv confirms title, authors, 2026 record, and interviews with 25 researchers. The source records substantial disagreement about timelines and explosive-growth scenarios. | Retain as qualitative expert-perspective evidence only. It does not establish imminent or unbounded recursive self-improvement. |

## Stable authoritative-source classes

The Canon also uses established institutional and treaty sources (for example ILO, United Nations treaty records, WHO, World Justice Project, IPC, UN-Habitat and Reporters Without Borders) as named anchors or reference families. Their role is bounded: they inform domain indicators or rights calibration and do not create MathGov authority by citation alone.

## Public-release rule

A reference with unresolved identity, authorship, publication status, DOI/URL mismatch, or material claim-entailment uncertainty MUST NOT be presented on ripplelogic.org as verified support for a strong claim. It must instead be corrected, removed, or explicitly marked unresolved/pending verification before public release.

## Result

No unresolved citation-identity blocker was found in the active Core release after the final scan and recent-reference review. Future Core releases must rerun this log because URLs, online-first metadata, institutional pages, and external guidance can change.
