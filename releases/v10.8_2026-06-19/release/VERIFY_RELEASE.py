#!/usr/bin/env python3
"""Verify MathGov / RippleLogic Core Release 2026.07."""
from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path

OOXML_SUFFIXES = {".docx", ".xlsx"}
BAD_NAME_PATTERN = re.compile(r"\(\d+\)")


def find_root() -> Path:
    here = Path(__file__).resolve()
    if here.parent.name == "release":
        return here.parent.parent
    return Path.cwd().resolve()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_ooxml(path: Path) -> str | None:
    if path.suffix.lower() not in OOXML_SUFFIXES:
        return None
    with path.open("rb") as f:
        magic = f.read(4)
    if magic != b"PK":
        return f"invalid OOXML magic bytes: {magic.hex(' ')}"
    try:
        with zipfile.ZipFile(path, "r") as zf:
            bad = zf.testzip()
            if bad:
                return f"zip integrity failure at {bad}"
    except zipfile.BadZipFile as exc:
        return f"not a valid ZIP/OOXML container: {exc}"
    return None


def main() -> int:
    root = find_root()
    manifest = root / "release" / "SHA256SUMS.txt"
    if not manifest.exists():
        print(f"ERROR: Missing {manifest}", file=sys.stderr)
        return 2

    failures: list[tuple[str, str]] = []
    checked = 0
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError:
            failures.append((line, "malformed manifest line"))
            continue
        rel = rel.strip().lstrip("*")
        if BAD_NAME_PATTERN.search(rel):
            failures.append((rel, "filename contains upload/copy suffix pattern"))
            continue
        path = root / rel
        if not path.exists():
            failures.append((rel, "missing file"))
            continue
        actual = sha256(path)
        checked += 1
        if actual.lower() != expected.lower():
            failures.append((rel, f"hash mismatch expected={expected} actual={actual}"))
        ooxml_error = check_ooxml(path)
        if ooxml_error:
            failures.append((rel, ooxml_error))

    if failures:
        print("VERIFY_RELEASE: FAIL")
        for rel, reason in failures:
            print(f"- {rel}: {reason}")
        return 1

    print(f"VERIFY_RELEASE: PASS ({checked} files checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
