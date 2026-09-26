# Citation Verification Report — MathGov v12.6 / SGP v8.5

**Original bibliographic review:** 25 July 2026  
**Current-pin review:** 15 August 2026  
**Status:** PASS WITH DECLARED SCOPE

**Current exact release:** `MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3`

## Scope

This release-hygiene pass reviewed the active Markdown reference surfaces in the fourteen-document core for DOI syntax, exact current-version citation pins, recent/advance-online publication metadata, and obvious title/year/identifier conflicts. It is a bibliographic-integrity check, not a systematic literature review, endorsement of cited claims, or proof that the reference set is complete.

## Machine checks

- Fourteen active Markdown core surfaces scanned.
- Eighteen DOI links detected in the angle-bracket reference surfaces; all eighteen are unique and match the standard `10.<registrant>/<suffix>` DOI syntax.
- No malformed DOI token was detected in the scanned active reference surfaces.
- The controlling current surfaces point to **Sentience Gradient Protocol v8.5** and **WDBIP v1.6**; earlier pins remain historical lineage only.

## Current and advance-online references checked

| Reference | Verification result | Current release treatment |
|---|---|---|
| Andrews, Birch, and Sebo, *Evaluating animal consciousness*, Science, DOI `10.1126/science.adp4990` | Title, authors, 2025 year, volume/issue, pages, and DOI agree with PubMed and the LSE repository record. | Retain as cited. |
| Butlin et al., *Identifying indicators of consciousness in AI systems*, DOI `10.1016/j.tics.2025.10.011` | Published online in 2025 and assigned to Trends in Cognitive Sciences 30(6), 488-501 in 2026. | The SGP citation correctly states 2026 and notes advance online publication in 2025. |
| Butlin and Lappas, *Principles for responsible AI consciousness research*, DOI `10.1613/jair.1.17310` | Title, authors, 2025 year, JAIR volume 82, and pages 1673-1690 are consistent across indexed records. | Retain as cited. |
| Pennartz, *How can we validate theory-derived indicators of consciousness in artificial intelligence?*, DOI `10.1016/j.tics.2026.01.011` | Title, author, DOI, and 2026 online-publication status are consistent with the publisher-indexed author record. | Retain as cited. |

## Source records used for the current-reference check

- PubMed record for Andrews, Birch, and Sebo: `https://pubmed.ncbi.nlm.nih.gov/39977511/`
- LSE Research Online record for Andrews, Birch, and Sebo: `https://researchonline.lse.ac.uk/127514/`
- PubMed record for Butlin et al.: `https://pubmed.ncbi.nlm.nih.gov/41219038/`
- ScienceDirect record for Butlin et al.: `https://www.sciencedirect.com/science/article/pii/S1364661325002864`
- Indexed JAIR metadata for Butlin and Lappas: DOI `10.1613/jair.1.17310`
- ScienceDirect author record listing the Pennartz correspondence and online date: `https://www.sciencedirect.com/author/7003645919/cyriel-m-a-pennartz`


## Agent-system external security references checked

| Reference | Verification result | Current release treatment |
|---|---|---|
| OWASP, *Top 10 for Agentic Applications for 2026* | The official OWASP GenAI Security Project resource identifies the title, date **9 December 2025**, and ASI01-ASI10 risk family used by the Agent System. | Retain the Agent System mapping as a supporting threat-model crosswalk. It does not create certification or normative authority over MathGov. |
| NIST, Center for AI Standards and Innovation (CAISI) | The official NIST CAISI site confirms the current center name and its work on AI-system testing, security measurement, voluntary guidelines, and agent standards. | Retain CAISI as a supporting external comparator. Exact current guidance must still be checked at each public release. |

Official records checked:

- `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/`
- `https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/`
- `https://www.nist.gov/caisi`

## Boundary

This PASS establishes that the scanned DOI strings, selected recent-reference metadata, and current internal version pins are consistent within the declared review scope. It does not establish that every URL will remain permanently available, that every cited proposition is correct, that the bibliography is exhaustive, or that MathGov has been empirically validated.


## Final 15 August 2026 source-integrity closure

The complete active public-source scan and the higher-risk recent-reference review are recorded in `release/SOURCE_VERIFICATION_LOG.md`. The final pass additionally verified the current Agent System references to METR task horizons, Anthropic's Automated Weak-to-Strong Researcher, and Field, Douglas, and Krueger (arXiv:2603.03338); removed literal placeholder URLs from ripple.md examples; and found no unresolved `Finke` or `Mednick` attribution in the active Core corpus. No unresolved citation-identity blocker remains within the declared review scope.
