#!/usr/bin/env python3
from pathlib import Path
import sys, zipfile, json, importlib.util, re
sys.dont_write_bytecode=True
from pypdf import PdfReader
from jsonschema import Draft202012Validator
from lxml import etree
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
    if not c: FAIL.append(m)
pairs=['docs/CORE_COMPONENT_MAP','docs/agents/RippleLogic_Agent_System_v12.3','docs/canon/RippleLogic_v12.5_Canon','docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5','docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3','docs/primer/RippleLogic_Foundations_Primer_v4.3','docs/sgp/SGP_v8.4','docs/standards/CSV_Gate_Standard_v2.3','docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2','docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.2','docs/standards/RippleLogic_Cascade_Standard_v2.5','docs/standards/Source_Coupling_Integrity_Standard_v2.2','docs/standards/ripple_md_Standard_v5.4','docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5','docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_5']
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; ns={'w':W}
for base in pairs:
    for ext in ['.md','.docx','.pdf']: ck((ROOT/(base+ext)).is_file(),f'missing {base+ext}')
    d=ROOT/(base+'.docx')
    if d.is_file():
        try:
            with zipfile.ZipFile(d) as z:
                names=z.namelist(); doc=etree.fromstring(z.read('word/document.xml')); settings=etree.fromstring(z.read('word/settings.xml'))
                xml=z.read('word/document.xml').decode('utf-8','ignore')
                ck('word/comments.xml' not in names,f'{d} comments'); ck(not re.search(r'<w:(?:ins|del)(?:\s|>)',xml),f'{d} tracked changes'); ck(not any('vbaProject' in n for n in names),f'{d} VBA')
                cm=settings.xpath('.//w:compatSetting[@w:name="compatibilityMode"]',namespaces=ns)
                ck(bool(cm) and cm[-1].get('{%s}val'%W)=='15',f'{d} not Word compatibilityMode 15')
                tables=doc.xpath('.//w:tbl',namespaces=ns)
                ck(not doc.xpath('.//w:textDirection',namespaces=ns),f'{d} contains unintended vertical text')
                ck(not doc.xpath('.//w:trHeight[@w:hRule="exact"]',namespaces=ns),f'{d} contains exact-height rows')
                for ti,t in enumerate(tables,1):
                    grid=t.xpath('./w:tblGrid/w:gridCol',namespaces=ns)
                    for gi,col in enumerate(grid,1):
                        try: gw=int(col.get('{%s}w'%W,'0'))
                        except ValueError: gw=0
                        ck(gw>=900,f'{d} table {ti} grid column {gi} collapsed width {gw}')
                    ck(not t.xpath('.//w:tcPr/w:textDirection',namespaces=ns),f'{d} table {ti} contains vertical cell text')
                    rows=t.xpath('./w:tr',namespaces=ns); ck(bool(rows),f'{d} table {ti} no rows')
                    if not rows: continue
                    tw=t.xpath('./w:tblPr/w:tblW',namespaces=ns)
                    ck(bool(tw) and tw[-1].get('{%s}type'%W)=='pct' and tw[-1].get('{%s}w'%W)=='5000',f'{d} table {ti} not full preferred width')
                    ck(bool(rows[0].xpath('./w:trPr/w:tblHeader',namespaces=ns)),f'{d} table {ti} missing repeating header')
                    for ci,cell in enumerate(rows[0].xpath('./w:tc',namespaces=ns),1):
                        sh=cell.xpath('./w:tcPr/w:shd',namespaces=ns)
                        ck(bool(sh) and sh[-1].get('{%s}fill'%W,'').upper()=='1F4E78',f'{d} table {ti} header cell {ci} fill')
                        for run in cell.xpath('.//w:r[w:t[string-length(normalize-space(.))>0]]',namespaces=ns):
                            ck(bool(run.xpath('./w:rPr/w:b',namespaces=ns)),f'{d} table {ti} header cell {ci} not bold')
                            co=run.xpath('./w:rPr/w:color',namespaces=ns)
                            ck(bool(co) and co[-1].get('{%s}val'%W,'').upper()=='FFFFFF',f'{d} table {ti} header cell {ci} not white')
                    for ri,row in enumerate(rows[1:],1):
                        expected='F7FBFF' if ri%2==1 else 'D9EAF7'
                        for ci,cell in enumerate(row.xpath('./w:tc',namespaces=ns),1):
                            sh=cell.xpath('./w:tcPr/w:shd',namespaces=ns)
                            ck(bool(sh) and sh[-1].get('{%s}fill'%W,'').upper()==expected,f'{d} table {ti} row {ri+1} cell {ci} body fill')
                    for ci,cell in enumerate(rows[-1].xpath('./w:tc',namespaces=ns),1):
                        b=cell.xpath('./w:tcPr/w:tcBorders/w:bottom',namespaces=ns)
                        ok=bool(b) and b[-1].get('{%s}val'%W)=='single' and b[-1].get('{%s}color'%W,'').upper()=='1F4E78' and int(b[-1].get('{%s}sz'%W,'0'))>=6
                        ck(ok,f'{d} table {ti} last-row cell {ci} missing terminal bottom border')
                if tables:
                    ck('w:fill="1F4E78"' in xml,f'{d} missing blue table headers')
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
ss=json.loads((ROOT/'schemas/sgp_rmcp_record_v8_4.schema.json').read_text()); val=Draft202012Validator(ss)
for f in (ROOT/'tests/sgp_rmcp').glob('pass_*.json'): ck(not list(val.iter_errors(json.loads(f.read_text()))),f'SGP positive failed {f.name}')
for f in (ROOT/'tests/sgp_rmcp').glob('fail_*.json'): ck(bool(list(val.iter_errors(json.loads(f.read_text())))),f'SGP negative passed {f.name}')
# WDBIP validator
spec=importlib.util.spec_from_file_location('wv',ROOT/'docs/standards/wdbip/validate_wdbip_v1_5.py'); wv=importlib.util.module_from_spec(spec); spec.loader.exec_module(wv)
ws=ROOT/'docs/standards/wdbip/wdbip_record_v1_5.schema.json'; pos=ROOT/'docs/standards/wdbip/wdbip_worked_example_green_corridor_v1_5.json'
ck(not wv.validate(pos,ws),'WDBIP positive failed')
for f in (ROOT/'docs/standards/wdbip/tests').glob('fail_*.json'): ck(bool(wv.validate(f,ws)),f'WDBIP negative passed {f.name}')
if FAIL:
    print('FAIL format and reproducibility:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS full-width readable DOCX tables, no vertical text/collapsed columns/exact-height clipping, bold repeating headers, terminal borders, Word compatibility mode, PDF mirrors, schemas, vectors, and bounded replay')
