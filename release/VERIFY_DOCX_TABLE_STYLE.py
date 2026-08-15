#!/usr/bin/env python3
"""Verify the restrained MathGov light-blue table system in all primary DOCX artifacts."""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path
from lxml import etree

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
HEADER_FILL = 'D9EAF7'
PRIMARY_NAMES = {
    'RippleLogic_v12.6_Canon.docx', 'SGP_v8.5.docx', 'ripple_md_Standard_v5.5.docx',
    'RippleLogic_Agent_System_v12.5.docx', 'CSV_Gate_Standard_v2.4.docx',
    'RippleLogic_Cascade_Standard_v2.6.docx', 'MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.4.docx',
    'Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.6.docx',
    'RippleLogic_RLS_Validation_Protocol_v2_6.docx', 'RippleLogic_Foundations_Primer_v4.4.docx',
    'MATHGOV_3R_1_2_PUBLIC_INTRO_v12_6.docx',
    'Physical_Causal_Admissibility_Evidence_Profile_v2.3.docx',
    'Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.3.docx',
    'Source_Coupling_Integrity_Standard_v2.3.docx',
}

def fail(msg: str) -> None:
    raise SystemExit(f'FAIL DOCX table style: {msg}')

main_docs = {}
for path in ROOT.rglob('*.docx'):
    if 'core_15' not in path.parts and path.name in PRIMARY_NAMES:
        if path.name in main_docs:
            fail(f'duplicate primary {path.name}')
        main_docs[path.name] = path
if set(main_docs) != PRIMARY_NAMES:
    fail(f'primary inventory missing={PRIMARY_NAMES-set(main_docs)} extra={set(main_docs)-PRIMARY_NAMES}')

table_count = 0
for name, path in sorted(main_docs.items()):
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:
            fail(f'OOXML ZIP integrity {name}')
        root = etree.fromstring(z.read('word/document.xml'))
    tables = root.xpath('.//w:tbl', namespaces=NS)
    if not tables:
        fail(f'no tables {name}')
    for index, table in enumerate(tables, 1):
        table_count += 1
        if not table.xpath('./w:tblPr/w:tblBorders', namespaces=NS):
            fail(f'missing borders {name} table {index}')
        rows = table.xpath('./w:tr', namespaces=NS)
        if len(rows) >= 2:
            first = rows[0]
            if not first.xpath('./w:trPr/w:tblHeader', namespaces=NS):
                fail(f'nonrepeating header {name} table {index}')
            cells = first.xpath('./w:tc', namespaces=NS)
            if not cells:
                fail(f'header has no cells {name} table {index}')
            for cell in cells:
                fills = cell.xpath('./w:tcPr/w:shd/@w:fill', namespaces=NS)
                if not fills or fills[-1].upper() != HEADER_FILL:
                    fail(f'header fill {name} table {index}')

    mirror = ROOT / 'core_15' / name
    if not mirror.is_file() or hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256(mirror.read_bytes()).digest():
        fail(f'Core 15 mirror mismatch {name}')

print(f'PASS professional table style: 14 primary DOCX artifacts, {table_count} tables, exact Core 15 mirrors')
