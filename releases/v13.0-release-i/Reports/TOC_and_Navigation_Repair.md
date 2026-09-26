# TOC and navigation verification

Exact build: `MG-RL-13.0-20260923-RELEASE-G`.

The Canon retains its finalized static hyperlink TOC. No live PAGEREF fields or automatic field refresh was added. Three visible page labels changed because the approved text amendments affected pagination; heading/bookmark targets were preserved.

The check compares stored DOCX labels, visible PDF labels and actual PDF hyperlink destinations for 125 numbered opening entries: Canon 70, SGP 28, WDBIP 27. All passed. All 14 documents were rendered and all reading projections regenerated from the current sources. Total Core PDF pages: 686.

`Verification/Navigation_Changes.json` records the three old/new labels; `Navigation_Final_Check.json` records the matching results. `Document_Preservation.json` and `Final_G/Render_Comparison.json` distinguish semantic changes from preserved formatting. Other existing body/bookmark links are covered by `Reference/check_reading_integrity.py` and its source/index checks.

Pagination is the packaged PDF's pagination. Different host fonts or Word layout engines may repaginate editable DOCX files; the static labels are not represented as live cross-host page fields. The governing text is still the DOCX source, with PDF/HTML/Markdown as synchronized reading projections.
