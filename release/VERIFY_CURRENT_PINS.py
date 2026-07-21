#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, zipfile
sys.dont_write_bytecode = True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
    if not c: FAIL.append(m)
def txt(r): return (ROOT/r).read_text(encoding='utf-8',errors='replace')
vm=yaml.safe_load(txt('VERSION_MANIFEST.yaml'))
ck(vm.get('release_line')=='v12.4','release line'); ck(vm.get('exact_release_version')=='v12.4','exact version')
expected={
'docs/canon/RippleLogic_v12.4_Canon.md':['RippleLogic Canon v12.4','RG -> RF/NCRC -> TRC -> CSV -> RLS'],
'docs/sgp/SGP_v8.3.md':['Sentience Gradient Protocol v8.3','Human FPP-100','capacity score creates standing or authority'],
'docs/standards/ripple_md_Standard_v5.3.md':['ripple.md Standard v5.3','No wrapper obligation becomes a sixth'],
'docs/agents/RippleLogic_Agent_System_v12.2.md':['Agent System v12.2','REFUSE_DETERMINISTIC_SELECTION'],
'docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.4.md':['Protocol v1.4','not an eighth welfare dimension'],
'docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_4.md':['Protocol v2.4','Reliability, validity, and calibration are not established'],
'docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_4.md':['v12.4','Eligible(a) is teaching shorthand'],
'docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.1.md':['v12-line methodological integrity discipline','retained in the current v12.4 release'],
'docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_4.md':['v12-line research ladder','retained in the current v12.4 release'],
'docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.4.md':['# Welfare Dimension Boundary and Interaction Protocol v1.4'],
}
for f,phrases in expected.items():
    ck((ROOT/f).is_file(),f'missing {f}')
    if (ROOT/f).is_file():
        s=txt(f)
        for p in phrases: ck(p.lower() in s.lower(),f'{f} missing {p}')
wp=ROOT/'docs/aligners/RippleLogic_Aligners_Sheet_v5.4.xlsx'
ck(wp.is_file(),'missing workbook')
if wp.is_file():
    with zipfile.ZipFile(wp) as z:
        blob=' '.join(z.read(n).decode('utf-8','ignore') for n in z.namelist() if n.endswith('.xml'))
    for p in ['v12.4','v8.3','v5.4','v5.3','v12.2','v1.4']:
        ck(p in blob,f'workbook missing {p}')
core=ROOT/'core_15'; artifacts=[p for p in core.iterdir() if p.is_file() and p.name!='README.md'] if core.exists() else []
ck(len(artifacts)==15,f'core_15 count {len(artifacts)}')
if FAIL:
 print('FAIL current pins:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS current v12.4 / SGP v8.3 pins and 15-artifact core')
