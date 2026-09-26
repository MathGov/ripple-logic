#!/usr/bin/env python3
"""Verify release-availability claims against the active reality register."""
from __future__ import annotations
import hashlib, sys
from pathlib import Path
import yaml

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
REG = ROOT / "docs/assurance/RELEASE_REALITY_REGISTER_v1.0.yaml"
data = yaml.safe_load(REG.read_text(encoding="utf-8"))
if data.get("status") != "ACTIVE_RELEASE_REGISTRY":
    raise SystemExit("FAIL release reality: inactive registry")
if data.get("release_id") != "MathGov_Core_2026_09_v12.6_SGP_v8.5+2026.08.15.3":
    raise SystemExit("FAIL release reality: release identity")
if data.get("build_id") != "2026.08.15.3":
    raise SystemExit("FAIL release reality: build identity")
artifacts = {item["artifact_id"]: item for item in data.get("artifacts", [])}
if set(artifacts) != {"WDBIP_v1_6", "MPMR_v1_0", "ProofPack_Tier4"}:
    raise SystemExit(f"FAIL release reality: artifact inventory {set(artifacts)}")
if artifacts["ProofPack_Tier4"].get("status") != "UNAVAILABLE_DESIGN_TARGET" or artifacts["ProofPack_Tier4"].get("files"):
    raise SystemExit("FAIL release reality: ProofPack/Tier4 boundary")
for artifact in artifacts.values():
    for item in artifact.get("files", []):
        path = ROOT / item["path"]
        if not path.is_file():
            raise SystemExit(f"FAIL release reality: missing {item['path']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item.get("sha256"):
            raise SystemExit(f"FAIL release reality: hash mismatch {item['path']}")
print("PASS release-reality availability, WDBIP v1.6 binding, and unavailable-target claim boundary")
