#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
files = [p for p in root.rglob('*') if p.is_file() and p.suffix.lower() in {'.md', '.txt'}]
text = '\n'.join(p.read_text(errors='ignore') for p in files)

required = [
    'RG -> RF -> TRC -> CSV -> RLS',
    'RG/RSG -> RF/NCRC -> TRC -> CSV -> RLS',
    'Rights Floor',
    'Non-Compensatory Rights Constraint',
    'Containment and Structural Viability',
    'CSV is not a purity filter',
    'RLS ranks only',
    'All-Encompassing Infinite Union (AIU)',
    'not a Tier 1-3 scoring object',
    'not ProofPack',
    'CSV_NOT_MATERIAL',
    'Appendix AI',
    'Appendix AJ',
    'Gate Boundary Discriminator',
    'least-rights-infringing',
    'Meta-Union Firewall',
    'Release Claims and Non-Claims',
    'Appendix AK',
    'Computable is not selectable',
    'Generated is not grounded',
    'Executable is not ethical',
    'v11.4 Final Core',
    'Appendix AK (Computability vs Realizability Bridge)',
    'documentation/source-completeness scores',
    'Gate-critical confidence guard',
    'low confidence in adverse gate-critical impacts',
    'Appendix AL',
    'Source-Coupling Integrity',
    'Source_Coupling_Integrity_Standard_v1.0.md',
    'SourceCouplingRecord',
    'source_coupling_status',
    'SOURCE_COUPLED',
    'SOURCE_DEBT_RISK',
]
missing = [s for s in required if s not in text]
forbidden = [
    'MathGov/RippleLogic',
    'MathGov / RippleLogic',
    'RG -> NCRC -> TRC -> CSV -> RLS',
    'RG/RSG -> NCRC -> TRC -> CSV -> RLS',
    'CSV synchronization note (v11.4 / active integration boundary)',
    'more than 500 scientists',
    'as of 2026), acknowledged a "realistic possibility"',
    'Absolute Infinite Union',
    'Source Amnesia Audit',
    'Source Amnesia Gate',
    'Source Amnesia Protocol',
]
found_forbidden = [s for s in forbidden if s in text]
if missing or found_forbidden:
    print('FAIL: semantic surface check')
    if missing:
        print('Missing:', missing)
    if found_forbidden:
        print('Forbidden:', found_forbidden)
    sys.exit(1)
print('PASS: semantic surfaces verified')
