#!/usr/bin/env python3
from pathlib import Path
import sys, zipfile, json, importlib.util
sys.dont_write_bytecode = True
from pypdf import PdfReader
from jsonschema import Draft202012Validator
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
 if not c: FAIL.append(m)
pairs=['docs/CORE_COMPONENT_MAP','docs/agents/RippleLogic_Agent_System_v12.2','docs/canon/RippleLogic_v12.4_Canon','docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_4','docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.2','docs/primer/RippleLogic_Foundations_Primer_v4.2','docs/sgp/SGP_v8.3','docs/standards/CSV_Gate_Standard_v2.2','docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.1','docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.1','docs/standards/RippleLogic_Cascade_Standard_v2.4','docs/standards/Source_Coupling_Integrity_Standard_v2.1','docs/standards/ripple_md_Standard_v5.3','docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.4','docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_4']
for base in pairs:
 for ext in ['.md','.docx','.pdf']: ck((ROOT/(base+ext)).is_file(),f'missing {base+ext}')
 d=ROOT/(base+'.docx')
 if d.is_file():
  try:
   with zipfile.ZipFile(d) as z:
    names=z.namelist(); xml=z.read('word/document.xml').decode('utf-8','ignore')
    ck('word/comments.xml' not in names,f'{d} comments'); ck(not __import__('re').search(r'<w:(?:ins|del)(?:\s|>)',xml),f'{d} tracked changes'); ck(not any('vbaProject' in n for n in names),f'{d} VBA')
    if '<w:tbl' in xml:
     ck('w:fill="1F4E78"' in xml,f'{d} missing blue table headers'); ck('<w:tblHeader' in xml,f'{d} missing repeating headers')
  except Exception as e: ck(False,f'{d} invalid {e}')
 p=ROOT/(base+'.pdf')
 if p.is_file():
  try:
   r=PdfReader(str(p)); ck(len(r.pages)>0,f'{p} no pages')
   for i in sorted(set([0,len(r.pages)//2,len(r.pages)-1])): ck(bool((r.pages[i].extract_text() or '').strip()),f'{p} blank text page {i+1}')
  except Exception as e: ck(False,f'{p} invalid {e}')
# run-record schema and semantic validator
spec=importlib.util.spec_from_file_location('mg',ROOT/'release/VALIDATE_MATHGOV_RUN.py'); mg=importlib.util.module_from_spec(spec); spec.loader.exec_module(mg)
passd=json.loads((ROOT/'tests/run_records/pass_reusable_cups.json').read_text()); e0,_=mg.r0(passd); e1,_=mg.r1(passd); ck(not e0 and not e1,f'positive run failed {e0+e1}')
for f in (ROOT/'tests/run_records').glob('fail_*.json'):
 d=json.loads(f.read_text()); e0,_=mg.r0(d); e1=[] if e0 else mg.r1(d)[0]; ck(bool(e0 or e1),f'negative run passed {f.name}')
# SGP schema vectors
ss=json.loads((ROOT/'schemas/sgp_rmcp_record_v8_3.schema.json').read_text()); val=Draft202012Validator(ss)
ck(not list(val.iter_errors(json.loads((ROOT/'tests/sgp_rmcp/pass_rmcp_record_v8_3.json').read_text()))),'SGP positive failed')
ck(bool(list(val.iter_errors(json.loads((ROOT/'tests/sgp_rmcp/fail_rmcp_missing_misuse_field_v8_3.json').read_text())))),'SGP negative passed')
# WDBIP validator
spec=importlib.util.spec_from_file_location('wv',ROOT/'docs/standards/wdbip/validate_wdbip_v1_4.py'); wv=importlib.util.module_from_spec(spec); spec.loader.exec_module(wv)
ws=ROOT/'docs/standards/wdbip/wdbip_record_v1_4.schema.json'; pos=ROOT/'docs/standards/wdbip/wdbip_worked_example_green_corridor_v1_4.json'
ck(not wv.validate(pos,ws),'WDBIP positive failed')
for f in (ROOT/'docs/standards/wdbip/tests').glob('fail_*.json'): ck(bool(wv.validate(f,ws)),f'WDBIP negative passed {f.name}')
if FAIL:
 print('FAIL format and reproducibility:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS DOCX/PDF formatting, schemas, vectors, and bounded replay')
