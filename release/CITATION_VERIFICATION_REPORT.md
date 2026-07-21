# Citation Verification Report - MathGov v12.4 / SGP v8.3

**Date:** 21 July 2026  
**Status:** PASS WITH DECLARED SCOPE

## Scope

This release-hygiene pass reviewed the active Markdown reference surfaces in the fourteen-document core for DOI syntax, exact current-version citation pins, recent/advance-online publication metadata, and obvious title/year/identifier conflicts. It is a bibliographic-integrity check, not a systematic literature review, endorsement of cited claims, or proof that the reference set is complete.

## Machine checks

- Fourteen active Markdown core surfaces scanned.
- Eighteen DOI links detected in the angle-bracket reference surfaces; all eighteen are unique and match the standard `10.<registrant>/<suffix>` DOI syntax.
- No malformed DOI token was detected in the scanned active reference surfaces.
- The controlling WDBIP citation now points to **Sentience Gradient Protocol v8.3**; v8.1.1 remains lineage only where explicitly historical.

## Current and advance-online references checked

| Reference | Verification result | Current release treatment |
|---|---|---|
| Andrews, Birch, and Sebo, *Evaluating animal consciousness*, Science, DOI `10.1126/science.adp4990` | Title, authors, 2025 year, volume/issue, pages, and DOI agree with PubMed and the LSE repository record. | Retain as cited. |
| Butlin et al., *Identifying indicators of consciousness in AI systems*, DOI `10.1016/j.tics.2025.10.011` | Published online in 2025 and assigned to Trends in Cognitive Sciences 30(6), 488-501 in 2026. | The SGP citation correctly states 2026 and notes advance online publication in 2025. |
| Butlin and Lappas, *Principles for responsible AI consciousness research*, DOI `10.1613/jair.1.17310` | Title, authors, 2025 year, JAIR volume 82, and pages 1673-1690 are consistent across indexed records. | Retain as cited. |
| Pennartz, *How can we validate theory-derived indicators of consciousness in artificial intelligence?*, DOI `10.1016/j.tics.2026.01.011` | Title, author, DOI, and 2026 online-publication status are consistent with the publisher's indexed author record. | Retain as cited. |

## Source records used for the current-reference check

- PubMed record for Andrews, Birch, and Sebo: `https://pubmed.ncbi.nlm.nih.gov/39977511/`
- LSE Research Online record for Andrews, Birch, and Sebo: `https://researchonline.lse.ac.uk/127514/`
- PubMed record for Butlin et al.: `https://pubmed.ncbi.nlm.nih.gov/41219038/`
- ScienceDirect record for Butlin et al.: `https://www.sciencedirect.com/science/article/pii/S1364661325002864`
- Indexed JAIR metadata for Butlin and Lappas: DOI `10.1613/jair.1.17310`
- ScienceDirect author record listing the Pennartz correspondence and online date: `https://www.sciencedirect.com/author/7003645919/cyriel-m-a-pennartz`

## Boundary

This PASS establishes that the scanned DOI strings and selected recent-reference metadata are internally and externally consistent at the time of review. It does not establish that every URL will remain permanently available, that every cited proposition is correct, that the bibliography is exhaustive, or that MathGov has been empirically validated.
