#!/usr/bin/env python3
"""Verify MathGov / RippleLogic Core Release 2026.06 - Final Locked.

Checks, in order:
  1. SHA-256 manifest integrity (SHA256SUMS.txt) for every pinned file.
  2. OOXML container integrity (magic bytes + required parts) for every .docx/.xlsx.
  3. Absence of common workbook formula-error tokens.
  4. Presence of key Canon/SGP precision-hardening integrity tokens.
  5. Package-wide absence of the superseded SPR wording, now standardized as
     "Stewardship/Power Readiness".
  6. Presence of the required "Stewardship/Power Readiness" token in SGP,
     Agent System, and Aligners workbook surfaces.
  7. Aligners workbook internal sanity status: FAIL_COUNT = 0, OVERALL =
     "✓ ALL PASS", and SC-83 = PASS.

Run from inside the extracted release folder. A clean run prints PASS lines and exits 0.
"""
from __future__ import annotations
import hashlib
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"
DOCX_REQUIRED = ["[Content_Types].xml", "word/document.xml"]
XLSX_REQUIRED = ["[Content_Types].xml", "xl/workbook.xml"]
ERROR_TOKENS = [b"#REF!", b"#DIV/0!", b"#VALUE!", b"#NAME?", b"#N/A", b"#NULL!", b"#NUM!"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_manifest() -> list[tuple[str, str]]:
    if not MANIFEST.exists():
        raise SystemExit("FAIL: SHA256SUMS.txt missing")
    entries = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 1)
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
            raise SystemExit(f"FAIL: malformed manifest line: {line}")
        entries.append((parts[0], parts[1]))
    return entries


def verify_hashes(entries):
    for expected, name in entries:
        path = ROOT / name
        if not path.exists():
            raise SystemExit(f"FAIL: manifest file missing: {name}")
        actual = sha256(path)
        if actual != expected:
            raise SystemExit(f"FAIL: hash mismatch: {name}\n expected {expected}\n actual   {actual}")
    print(f"PASS: {len(entries)} SHA-256 manifest entries verified")


def verify_zip_office(path: Path, required: list[str]):
    b = path.read_bytes()[:4]
    if b != b"PK\x03\x04":
        raise SystemExit(f"FAIL: {path.name} is not OOXML/ZIP; magic={b.hex()}")
    try:
        with zipfile.ZipFile(path) as z:
            names = set(z.namelist())
            missing = [r for r in required if r not in names]
            if missing:
                raise SystemExit(f"FAIL: {path.name} missing required OOXML parts: {missing}")
            bad = z.testzip()
            if bad:
                raise SystemExit(f"FAIL: {path.name} corrupt ZIP member: {bad}")
    except zipfile.BadZipFile as e:
        raise SystemExit(f"FAIL: {path.name} bad ZIP: {e}")


def verify_office_files():
    for name in [
        "RippleLogic_v10.7.4_Canon.docx",
        "SGP_v5.4.4.docx",
        "ripple_md_Standard_v3.5.4.docx",
        "RippleLogic_Agent_System_v10.7.4.docx",
        "RippleLogic_Foundations_Primer_v2.5.4.docx",
    ]:
        verify_zip_office(ROOT / name, DOCX_REQUIRED)
    verify_zip_office(ROOT / "RippleLogic_Aligners_Sheet_v3.5.5.xlsx", XLSX_REQUIRED)
    print("PASS: OOXML container integrity verified for DOCX/XLSX files")


def verify_workbook_error_tokens():
    path = ROOT / "RippleLogic_Aligners_Sheet_v3.5.5.xlsx"
    hits = []
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith(".xml"):
                data = z.read(name)
                for token in ERROR_TOKENS:
                    if token in data:
                        hits.append((name, token.decode()))
    if hits:
        raise SystemExit(f"FAIL: workbook formula/error token hits: {hits[:20]}")
    print("PASS: workbook contains no common formula-error tokens")





def _xlsx_shared_strings(z: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    out: list[str] = []
    for si in root.findall("a:si", ns):
        parts = [t.text or "" for t in si.findall(".//a:t", ns)]
        out.append("".join(parts))
    return out


def _xlsx_sheet_path(z: zipfile.ZipFile, sheet_name: str) -> str:
    ns = {
        "a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    }
    wb_root = ET.fromstring(z.read("xl/workbook.xml"))
    rid = None
    for sheet in wb_root.findall(".//a:sheet", ns):
        if sheet.attrib.get("name") == sheet_name:
            rid = sheet.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            break
    if not rid:
        raise SystemExit(f"FAIL: workbook sheet missing: {sheet_name}")
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    for rel in rels.findall("rel:Relationship", ns):
        if rel.attrib.get("Id") == rid:
            target = rel.attrib.get("Target", "").lstrip("/")
            return target if target.startswith("xl/") else "xl/" + target
    raise SystemExit(f"FAIL: workbook relationship missing for sheet: {sheet_name}")


def _xlsx_cell_value(z: zipfile.ZipFile, sheet_name: str, cell_ref: str, shared: list[str]) -> str:
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    path = _xlsx_sheet_path(z, sheet_name)
    root = ET.fromstring(z.read(path))
    for cell in root.findall(".//a:c", ns):
        if cell.attrib.get("r") != cell_ref:
            continue
        v = cell.find("a:v", ns)
        if v is None or v.text is None:
            is_el = cell.find("a:is", ns)
            if is_el is not None:
                return "".join(t.text or "" for t in is_el.findall(".//a:t", ns)).strip()
            return ""
        raw = v.text
        if cell.attrib.get("t") == "s":
            try:
                return shared[int(raw)].strip()
            except Exception as exc:
                raise SystemExit(f"FAIL: bad shared string ref at {sheet_name}!{cell_ref}: {raw}") from exc
        return raw.strip()


def verify_workbook_sanity_status():
    path = ROOT / "RippleLogic_Aligners_Sheet_v3.5.5.xlsx"
    with zipfile.ZipFile(path) as z:
        shared = _xlsx_shared_strings(z)
        fail_count = _xlsx_cell_value(z, "Sanity_Checklist", "B40", shared)
        overall = _xlsx_cell_value(z, "Sanity_Checklist", "B41", shared)
        sc83_expected = _xlsx_cell_value(z, "Sanity_Checklist", "C83", shared)
        sc83_actual = _xlsx_cell_value(z, "Sanity_Checklist", "D83", shared)
        sc83_status = _xlsx_cell_value(z, "Sanity_Checklist", "E83", shared)
        canon_note = _xlsx_cell_value(z, "CANON", "C86", shared)
    if fail_count not in {"0", "0.0"}:
        raise SystemExit(f"FAIL: workbook Sanity_Checklist FAIL_COUNT is nonzero: {fail_count}")
    if overall != "✓ ALL PASS":
        raise SystemExit(f"FAIL: workbook Sanity_Checklist OVERALL is not all-pass: {overall}")
    if not (sc83_expected == sc83_actual == "Worked-run claimable" and sc83_status == "PASS"):
        raise SystemExit(
            "FAIL: workbook SC-83 publishability label mismatch: "
            f"expected={sc83_expected!r} actual={sc83_actual!r} status={sc83_status!r}"
        )
    if "Deterministic worked-run claimability predicate" in canon_note:
        raise SystemExit("FAIL: stale deterministic worked-run claimability wording remains in CANON!C86")
    print("PASS: workbook internal sanity status verified")


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", "ignore")
    # Lightweight XML text extraction sufficient for release-integrity tokens.
    xml = re.sub(r"<[^>]+>", " ", xml)
    return re.sub(r"\s+", " ", xml)


def office_package_text(path: Path) -> str:
    """Lightweight text extraction from OOXML XML parts for release-token checks."""
    chunks = []
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith((".xml", ".rels")):
                data = z.read(name).decode("utf-8", "ignore")
                chunks.append(data)
                chunks.append(re.sub(r"<[^>]+>", " ", data))
    return re.sub(r"\s+", " ", " ".join(chunks))


def verify_final_spr_terminology():
    office_files = [
        "RippleLogic_v10.7.4_Canon.docx",
        "SGP_v5.4.4.docx",
        "ripple_md_Standard_v3.5.4.docx",
        "RippleLogic_Agent_System_v10.7.4.docx",
        "RippleLogic_Foundations_Primer_v2.5.4.docx",
        "RippleLogic_Aligners_Sheet_v3.5.5.xlsx",
    ]
    forbidden = "Stewardship Participation Readiness"
    required = "Stewardship/Power Readiness"
    hits = []
    required_hits = []
    for name in office_files:
        t = office_package_text(ROOT / name)
        if forbidden in t:
            hits.append(name)
        if required in t:
            required_hits.append(name)
    if hits:
        raise SystemExit(f"FAIL: stale SPR expansion found in current Office surfaces: {hits}")
    if "SGP_v5.4.4.docx" not in required_hits or "RippleLogic_Agent_System_v10.7.4.docx" not in required_hits or "RippleLogic_Aligners_Sheet_v3.5.5.xlsx" not in required_hits:
        raise SystemExit(f"FAIL: required Stewardship/Power Readiness token missing from expected files; hits={required_hits}")
    print("PASS: final SPR terminology verified across current Office surfaces")


def verify_targeted_text_rules():
    sgp = docx_text(ROOT / "SGP_v5.4.4.docx")
    canon = docx_text(ROOT / "RippleLogic_v10.7.4_Canon.docx")
    required = [
        ("SGP_v5.4.4.docx", sgp, "Construct boundary. Union Participation"),
        ("SGP_v5.4.4.docx", sgp, "Current-release scalar boundary. In SGP v5.4.4"),
        ("SGP_v5.4.4.docx", sgp, "Stewardship/Power Readiness"),
        ("SGP_v5.4.4.docx", sgp, "O.4 v5.4.4 release delta"),
        ("RippleLogic_v10.7.4_Canon.docx", canon, "Union Participation interface note."),
        ("RippleLogic_v10.7.4_Canon.docx", canon, "Reality: For decision-making, the evaluator-independent field of constrained structures"),
    ]
    for name, text, token in required:
        if token not in text:
            raise SystemExit(f"FAIL: required text token missing in {name}: {token}")
    forbidden = [
        ("SGP_v5.4.4.docx", sgp, "O.4 v5.4.1 release delta"),
        ("SGP_v5.4.4.docx", sgp, "Release Delta (v5.4 → v5.4.1)"),
        ("SGP_v5.4.4.docx", sgp, "Stewardship Participation Readiness"),
    ]
    for name, text, token in forbidden:
        if token in text:
            raise SystemExit(f"FAIL: forbidden stale text token found in {name}: {token}")
    print("PASS: targeted Canon/SGP text-integrity rules verified")


def main():
    entries = parse_manifest()
    verify_hashes(entries)
    verify_office_files()
    verify_workbook_error_tokens()
    verify_workbook_sanity_status()
    verify_targeted_text_rules()
    verify_final_spr_terminology()
    print("PASS: MathGov / RippleLogic Core Release 2026.06 Final Locked verification complete")


if __name__ == "__main__":
    main()
