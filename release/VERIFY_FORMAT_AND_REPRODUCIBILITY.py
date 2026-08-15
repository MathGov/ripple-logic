#!/usr/bin/env python3
"""Verify current reading mirrors, PDFs, schemas, and reproducible-run surfaces."""
from __future__ import annotations
import json, sys, zipfile
from pathlib import Path
import fitz, yaml
import re

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
BASES = [
    "docs/CORE_COMPONENT_MAP", "docs/canon/RippleLogic_v12.6_Canon", "docs/sgp/SGP_v8.5",
    "docs/agents/RippleLogic_Agent_System_v12.5", "docs/standards/CSV_Gate_Standard_v2.4",
    "docs/standards/RippleLogic_Cascade_Standard_v2.6",
    "docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.4",
    "docs/primer/RippleLogic_Foundations_Primer_v4.4",
    "docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_6",
    "docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.3",
    "docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.3",
    "docs/standards/Source_Coupling_Integrity_Standard_v2.3",
    "docs/standards/ripple_md_Standard_v5.5",
    "docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6",
    "docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_6",
]
pages = 0
for base in BASES:
    md, docx, pdf = (ROOT / f"{base}{ext}" for ext in (".md", ".docx", ".pdf"))
    for path in (md, docx, pdf):
        if not path.is_file() or not path.stat().st_size:
            raise SystemExit(f"FAIL format: missing {path.relative_to(ROOT)}")
    with zipfile.ZipFile(docx) as archive:
        if archive.testzip() is not None:
            raise SystemExit(f"FAIL format: corrupt DOCX {docx.relative_to(ROOT)}")
        names = set(archive.namelist())
        if any("comments" in name.lower() or "vba" in name.lower() for name in names):
            raise SystemExit(f"FAIL format: comments or VBA in {docx.relative_to(ROOT)}")
        xml = archive.read("word/document.xml")
        if any(token in xml for token in (b"<w:ins>", b"<w:ins ", b"<w:del>", b"<w:del ")):
            raise SystemExit(f"FAIL format: tracked changes in {docx.relative_to(ROOT)}")
    document = fitz.open(pdf)
    if document.page_count < 1:
        raise SystemExit(f"FAIL format: empty PDF {pdf.relative_to(ROOT)}")
    for number, page in enumerate(document, 1):
        if len(page.get_text().strip()) < 20 and not page.get_images():
            raise SystemExit(f"FAIL format: blank PDF page {pdf.relative_to(ROOT)}:{number}")
    pages += document.page_count
    document.close()

for path in list((ROOT / "schemas").glob("*.json")) + list((ROOT / "docs/standards/wdbip").glob("*.json")):
    json.loads(path.read_text(encoding="utf-8"))
for path in (ROOT / "docs/standards/wdbip").glob("*.yaml"):
    yaml.safe_load(path.read_text(encoding="utf-8"))
print(f"PASS format and reproducibility: {len(BASES)} Markdown/DOCX/PDF triples, {pages} PDF pages, clean OOXML, and parseable machine surfaces")


# PUBLICATION_MARKUP_LEAK: narrow recurrence check for accidental literal double-backtick leakage
for rel in [
    "docs/canon/RippleLogic_v12.6_Canon.md",
    "docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_6.md",
]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if re.search(r"(?<!`)``(?!`)", text):
        fail(f"publication markup leakage: {rel} contains literal double-backticks")
