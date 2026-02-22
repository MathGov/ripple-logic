from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List

try:
    import jsonschema
    from jsonschema import Draft202012Validator, RefResolver  # type: ignore
    JSONSCHEMA_AVAILABLE = True
except Exception:
    JSONSCHEMA_AVAILABLE = False

ROOT_REQUIRED_FILES = [
    "README.md",
    "manifest.json",
    "VERSION_PINS.json",
    "CONFORMANCE_POLICY.md",
    "SHA256SUMS.txt",
]

VECTOR_DIRS = [
    "test_vectors/TV-0001_simple_admissible",
    "test_vectors/TV-0002_rights_fail",
    "test_vectors/TV-0003_trc_tail_risk",
    "test_vectors/TV-0004_containment_trigger",
    "test_vectors/TV-0005_non_decisive_review",
]

SCHEMA_FILES = {
    "decision_input": "schemas/decision_input.schema.json",
    "decision_output": "schemas/decision_output.schema.json",
    "weights": "schemas/weights.schema.json",
    "rights_coverage": "schemas/rights_coverage.schema.json",
    "uci_structural_input": "schemas/uci_structural_input.schema.json",
    "audit_flags": "schemas/audit_flags.schema.json",
}

def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def check_exists(root: Path) -> List[str]:
    errors: List[str] = []
    for rel in ROOT_REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"Missing required root file: {rel}")
    for rel in SCHEMA_FILES.values():
        if not (root / rel).exists():
            errors.append(f"Missing schema file: {rel}")
    for vdir in VECTOR_DIRS:
        for name in ["input.json", "expected_output.json", "notes.md"]:
            if not (root / vdir / name).exists():
                errors.append(f"Missing vector file: {vdir}/{name}")
    return errors

def build_schema_store(root: Path) -> Dict[str, Any]:
    store: Dict[str, Any] = {}
    for rel in SCHEMA_FILES.values():
        p = root / rel
        if p.exists():
            schema = load_json(p)
            sid = schema.get("$id")
            if sid:
                store[sid] = schema
            store[p.name] = schema
    return store

def validate_json_schema(root: Path, data_path: Path, schema_path: Path) -> List[str]:
    if not JSONSCHEMA_AVAILABLE:
        return []
    errors: List[str] = []
    data = load_json(data_path)
    schema = load_json(schema_path)
    try:
        resolver = RefResolver.from_schema(schema, store=build_schema_store(root))
        validator = Draft202012Validator(schema, resolver=resolver)
        for err in validator.iter_errors(data):
            loc = ".".join(str(x) for x in err.absolute_path) or "<root>"
            errors.append(f"{data_path}: schema error at {loc}: {err.message}")
    except Exception as e:
        errors.append(f"{data_path}: schema validation failed to run: {e}")
    return errors

def compare_expected_vs_reference(expected: Dict[str, Any], actual: Dict[str, Any], vector_name: str) -> List[str]:
    errors: List[str] = []
    exact_fields = [
        "schema_id", "vector_id", "admissibility_status", "decision_classification",
        "primary_decision_path", "required_flags", "uci_status",
    ]
    for field in exact_fields:
        if expected.get(field) != actual.get(field):
            errors.append(
                f"{vector_name}: mismatch in '{field}'\n"
                f"  expected: {expected.get(field)!r}\n"
                f"  actual:   {actual.get(field)!r}"
            )
    exp_cp = expected.get("conformance_payload", {})
    act_cp = actual.get("conformance_payload", {})
    for k in ["proofpack_version", "comparison_profile", "numeric_mode", "rounding_policy"]:
        if exp_cp.get(k) != act_cp.get(k):
            errors.append(
                f"{vector_name}: conformance_payload mismatch in '{k}'\n"
                f"  expected: {exp_cp.get(k)!r}\n"
                f"  actual:   {act_cp.get(k)!r}"
            )
    return errors

def run_reference_compare(root: Path) -> List[str]:
    errors: List[str] = []
    vector_map = {
        "TV-0001_simple_admissible": "TV-0001",
        "TV-0002_rights_fail": "TV-0002",
        "TV-0003_trc_tail_risk": "TV-0003",
        "TV-0004_containment_trigger": "TV-0004",
        "TV-0005_non_decisive_review": "TV-0005",
    }
    for folder_name, vector_id in vector_map.items():
        expected_path = root / "test_vectors" / folder_name / "expected_output.json"
        ref_path = root / "reference_results" / vector_id / "output.json"
        if not ref_path.exists():
            errors.append(f"Missing reference result file: reference_results/{vector_id}/output.json")
            continue
        expected = load_json(expected_path)
        actual = load_json(ref_path)
        errors.extend(compare_expected_vs_reference(expected, actual, vector_id))
    return errors

def check_manifest_inventory(root: Path) -> List[str]:
    errors: List[str] = []
    man = load_json(root / "manifest.json")
    vectors = man.get("test_vectors", [])
    if len(vectors) != 5:
        errors.append(f"manifest.json expected 5 test_vectors entries, found {len(vectors)}")
    for v in vectors:
        for key in ["vector_id", "input_path", "expected_output_path", "notes_path"]:
            if key not in v:
                errors.append(f"manifest test vector missing key: {key}")
        for key in ["input_path", "expected_output_path", "notes_path"]:
            p = root / v.get(key, "")
            if not p.exists():
                errors.append(f"manifest path missing on disk: {v.get(key)}")
    return errors

def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    print(f"Validating ProofPack at: {root}")
    errors: List[str] = []
    errors.extend(check_exists(root))
    if not errors:
        errors.extend(check_manifest_inventory(root))
        for vdir in VECTOR_DIRS:
            in_path = root / vdir / "input.json"
            out_path = root / vdir / "expected_output.json"
            errors.extend(validate_json_schema(root, in_path, root / SCHEMA_FILES["decision_input"]))
            errors.extend(validate_json_schema(root, out_path, root / SCHEMA_FILES["decision_output"]))
    if (root / "reference_results").exists():
        errors.extend(run_reference_compare(root))
    else:
        print("Note: reference_results/ not found, skipping output comparison.")
    if errors:
        print("\nVALIDATION FAILED\n")
        for e in errors:
            print(f"- {e}")
        return 1
    print("\nVALIDATION PASSED")
    print(f"Schema validation: {'enabled' if JSONSCHEMA_AVAILABLE else 'skipped (install jsonschema to enable)'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
