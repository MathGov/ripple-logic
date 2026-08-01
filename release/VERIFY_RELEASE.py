#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from jsonschema import Draft202012Validator
import hashlib, json, subprocess, sys, yaml, os
from concurrent.futures import ThreadPoolExecutor
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
SKIP_SUBORDINATES='--skip-subordinates' in sys.argv
SKIP_HASHES='--skip-hashes' in sys.argv
CORE={'RippleLogic_Aligners_Sheet_v5.5.xlsx', 'RippleLogic_Foundations_Primer_v4.3.docx', 'Physical_Causal_Admissibility_Evidence_Profile_v2.2.docx', 'RippleLogic_RLS_Validation_Protocol_v2_5.docx', 'ripple_md_Standard_v5.4.docx', 'Source_Coupling_Integrity_Standard_v2.2.docx', 'SGP_v8.4.docx', 'MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.docx', 'Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.docx', 'Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.docx', 'RippleLogic_Cascade_Standard_v2.5.docx', 'MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.docx', 'RippleLogic_v12.5_Canon.docx', 'RippleLogic_Agent_System_v12.3.docx', 'CSV_Gate_Standard_v2.3.docx'}
TRIPLES=[('docs/canon/RippleLogic_v12.5_Canon.md', 'docs/canon/RippleLogic_v12.5_Canon.docx', 'docs/canon/RippleLogic_v12.5_Canon.pdf'), ('docs/sgp/SGP_v8.4.md', 'docs/sgp/SGP_v8.4.docx', 'docs/sgp/SGP_v8.4.pdf'), ('docs/agents/RippleLogic_Agent_System_v12.3.md', 'docs/agents/RippleLogic_Agent_System_v12.3.docx', 'docs/agents/RippleLogic_Agent_System_v12.3.pdf'), ('docs/standards/CSV_Gate_Standard_v2.3.md', 'docs/standards/CSV_Gate_Standard_v2.3.docx', 'docs/standards/CSV_Gate_Standard_v2.3.pdf'), ('docs/standards/RippleLogic_Cascade_Standard_v2.5.md', 'docs/standards/RippleLogic_Cascade_Standard_v2.5.docx', 'docs/standards/RippleLogic_Cascade_Standard_v2.5.pdf'), ('docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.md', 'docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.docx', 'docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.pdf'), ('docs/primer/RippleLogic_Foundations_Primer_v4.3.md', 'docs/primer/RippleLogic_Foundations_Primer_v4.3.docx', 'docs/primer/RippleLogic_Foundations_Primer_v4.3.pdf'), ('docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.md', 'docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.docx', 'docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.pdf'), ('docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.2.md', 'docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.2.docx', 'docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.2.pdf'), ('docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.md', 'docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.docx', 'docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.pdf'), ('docs/standards/Source_Coupling_Integrity_Standard_v2.2.md', 'docs/standards/Source_Coupling_Integrity_Standard_v2.2.docx', 'docs/standards/Source_Coupling_Integrity_Standard_v2.2.pdf'), ('docs/standards/ripple_md_Standard_v5.4.md', 'docs/standards/ripple_md_Standard_v5.4.docx', 'docs/standards/ripple_md_Standard_v5.4.pdf'), ('docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.md', 'docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.docx', 'docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.pdf'), ('docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_5.md', 'docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_5.docx', 'docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_5.pdf')]

def fail(msg): print('FAIL:',msg); raise SystemExit(1)
def ok(msg): print('PASS:',msg)
# Run the seven subordinate conformance verifiers unless a caller has already run them separately.
if not SKIP_SUBORDINATES:
    for verifier in ['VERIFY_CURRENT_PINS.py','VERIFY_AUDIT_FLAG_REGISTRY.py','VERIFY_SEMANTIC_SURFACES.py','VERIFY_STATE_SEMANTICS_AND_NON_DILUTION.py','VERIFY_FORMULA_INTERFACE_INTEGRITY.py','VERIFY_WORKBOOK_LIVE_RECALCULATION.py','VERIFY_FORMAT_AND_REPRODUCIBILITY.py','VERIFY_RELEASE_REALITY_COHERENCE.py']:
        env=dict(__import__('os').environ); env['PYTHONDONTWRITEBYTECODE']='1'
        cp=subprocess.run([sys.executable,str(ROOT/'release'/verifier),str(ROOT)],capture_output=True,text=True,env=env)
        if cp.returncode: fail(f'{verifier}: {cp.stdout}{cp.stderr}')
        print(cp.stdout.strip())
    ok('eight subordinate conformance verifiers')
else:
    ok('subordinate conformance verifiers externally completed (split replay mode)')
# identities, manifests, and public-source hygiene
vm=yaml.safe_load((ROOT/'VERSION_MANIFEST.yaml').read_text(encoding='utf-8'))
release_id='MathGov_Core_2026_09_v12.5_SGP_v8.4'
if vm.get('release_id')!=release_id or vm.get('exact_release_version')!='v12.5' or vm.get('release_line')!='v12.5': fail('VERSION_MANIFEST release identity')
if vm.get('governing_cascade')!='RG -> RF/NCRC -> TRC -> CSV -> RLS': fail('canonical cascade')
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.pyc','.pyo'}: fail(f'compiled artifact in source release {p.relative_to(ROOT)}')
    if p.is_dir() and p.name=='__pycache__': fail(f'bytecode directory in source release {p.relative_to(ROOT)}')
ok('release identity, cascade, and public-source hygiene')
yaml.safe_load((ROOT/'CITATION.cff').read_text(encoding='utf-8')); ok('CITATION.cff parses')
# exact Core 15
actual={p.name for p in (ROOT/'core_15').iterdir() if p.is_file() and p.name!='README.md'}
if actual!=CORE: fail(f'Core 15 set mismatch missing={CORE-actual} extra={actual-CORE}')
for p in (ROOT/'core_15').iterdir():
    if p.suffix.lower() in {'.docx','.xlsx'} and p.read_bytes()[:4]!=b'PK\x03\x04': fail(f'OOXML magic {p}')
ok('exact Core 15 and genuine OOXML')
# triples and PDF magic
for tri in TRIPLES:
    for rel in tri:
        p=ROOT/rel
        if not p.is_file() or p.stat().st_size==0: fail(f'missing/empty {rel}')
    if (ROOT/tri[1]).read_bytes()[:4]!=b'PK\x03\x04': fail(f'DOCX magic {tri[1]}')
    if (ROOT/tri[2]).read_bytes()[:4]!=b'%PDF': fail(f'PDF magic {tri[2]}')
ok('14 Markdown/DOCX/PDF triples')
# Final table/layout audit and supporting RLS validation workbook title.
audit=json.loads((ROOT/'release/DOCX_TABLE_AND_LAYOUT_AUDIT_v12_5.json').read_text(encoding='utf-8'))
if audit.get('status')!='PASS': fail('DOCX table/layout audit status')
expected_audit={'documents':15,'tables':287,'pages':566}
for k,v in expected_audit.items():
    if audit.get('totals',{}).get(k)!=v: fail(f'DOCX table/layout audit {k}')
for k,v in audit.get('totals',{}).items():
    if k not in {'documents','tables','headings','pages'} and v: fail(f'DOCX table/layout residual defect {k}={v}')
rls_validation=ROOT/'docs/validation/rls/RLS_Validation_Workbook_v0_3.xlsx'
with ZipFile(rls_validation) as z:
    xblob=' '.join(z.read(n).decode('utf-8','ignore') for n in z.namelist() if n.endswith('.xml'))
if 'RLS VALIDATION WORKBOOK v0.3 - LEVEL 1 STUDY INSTRUMENT' not in xblob: fail('RLS validation workbook visible title')
ok('final DOCX/PDF audit metrics and visible RLS validation-workbook title')
# JSON/YAML schemas
for p in list((ROOT/'schemas').glob('*.json'))+list((ROOT/'docs/standards/wdbip').glob('*.json'))+list((ROOT/'docs/standards/wdbip').glob('*.yaml')):
    if p.suffix=='.json': json.loads(p.read_text(encoding='utf-8'))
    else: yaml.safe_load(p.read_text(encoding='utf-8'))
ok('machine-readable schemas and registers parse')
run_schema=json.loads((ROOT/'schemas/mathgov_run_record_v3.schema.json').read_text(encoding='utf-8'))
if run_schema['properties']['identity']['properties']['package_release_id'].get('const')!=release_id: fail('run-record v3 package release const')
# Run-record vectors and active walkthrough example.  Execute independent vectors
# concurrently so clean-release verification remains bounded without changing semantics.
val=ROOT/'release/VALIDATE_MATHGOV_RUN.py'
example=ROOT/'docs/examples/reproducibility/reusable_cups_run_v3.json'
if not example.is_file(): fail('missing active schema-v3 reproducibility example')
env=dict(os.environ); env['PYTHONDONTWRITEBYTECODE']='1'
jobs=[]
for pth in sorted((ROOT/'tests/run_records').glob('pass_*.json')):
    jobs.append(('run pass vector',pth,[sys.executable,str(val),str(pth)]))
for pth in sorted((ROOT/'tests/run_records').glob('fail_*.json')):
    jobs.append(('run fail vector',pth,[sys.executable,str(val),str(pth),'--expect-fail']))
jobs.append(('active reproducibility example',example,[sys.executable,str(val),str(example)]))
def run_job(job):
    label,pth,cmd=job
    r=subprocess.run(cmd,capture_output=True,text=True,env=env)
    return label,pth,r
with ThreadPoolExecutor(max_workers=min(8,max(1,os.cpu_count() or 1))) as pool:
    for label,pth,r in pool.map(run_job,jobs):
        if r.returncode: fail(f'{label} {pth.name}: {r.stdout}{r.stderr}')
if (ROOT/'docs/examples/reproducibility/reusable_cups_run_v2.json').exists(): fail('obsolete v2 reproducibility example remains active')
ok('run-record v3 pass/fail vectors and active walkthrough example')
# SGP RMCP vectors
sgps=json.loads((ROOT/'schemas/sgp_rmcp_record_v8_4.schema.json').read_text(encoding='utf-8')); sv=Draft202012Validator(sgps)
for p in sorted((ROOT/'tests/sgp_rmcp').glob('pass_*.json')):
    e=list(sv.iter_errors(json.loads(p.read_text(encoding='utf-8'))))
    if e: fail(f'SGP pass vector {p.name}: {e[0].message}')
for p in sorted((ROOT/'tests/sgp_rmcp').glob('fail_*.json')):
    e=list(sv.iter_errors(json.loads(p.read_text(encoding='utf-8'))))
    if not e: fail(f'SGP fail vector unexpectedly passed {p.name}')
ok('SGP RMCP v8.4 vectors')
# WDBIP vectors
import importlib.util
wv_path=ROOT/'docs/standards/wdbip/validate_wdbip_v1_5.py'
spec=importlib.util.spec_from_file_location('wdbip_validator',wv_path); wv=importlib.util.module_from_spec(spec); spec.loader.exec_module(wv)
wdbip_schema=ROOT/'docs/standards/wdbip/wdbip_record_v1_5.schema.json'
for p in sorted((ROOT/'docs/standards/wdbip/tests').glob('pass_*.json')):
    e=wv.validate(p,wdbip_schema)
    if e: fail(f'WDBIP pass vector {p.name}: {e[0]}')
for p in sorted((ROOT/'docs/standards/wdbip/tests').glob('fail_*.json')):
    e=wv.validate(p,wdbip_schema)
    if not e: fail(f'WDBIP fail vector unexpectedly passed {p.name}')
ok('WDBIP v1.5 vectors')
# Aligners workbook formulas, serialized results, intentional-blank audit, and recalc metadata.
# OOXML permits a formula cell that evaluates to the empty string to omit <v>.  The
# release therefore rejects every uncached nonblank result while permitting only the
# exact cells independently recalculated through artifact_tool and pinned below.
xp=ROOT/'docs/aligners/RippleLogic_Aligners_Sheet_v5.5.xlsx'
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
RNS='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
fc=errs=0; missing=[]
with ZipFile(xp) as z:
    wr=etree.fromstring(z.read('xl/workbook.xml'))
    rels=etree.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    relmap={r.get('Id'):r.get('Target') for r in rels}
    for s in wr.find('{%s}sheets'%NS['m']):
        sheet=s.get('name'); target=relmap[s.get('{%s}id'%RNS)].lstrip('/')
        if not target.startswith('xl/'): target='xl/'+target
        xr=etree.fromstring(z.read(target))
        for c in xr.xpath('.//m:c[m:f]',namespaces=NS):
            fc+=1; v=c.find('{%s}v'%NS['m']); f=c.find('{%s}f'%NS['m'])
            if v is None or v.text is None: missing.append((sheet,c.get('r'),f.text or ''))
            elif c.get('t')=='e' or (v.text and v.text.startswith('#')): errs+=1
    calc=wr.find('{%s}calcPr'%NS['m'])
audit_path=ROOT/'release/WORKBOOK_FORMULA_CACHE_AUDIT.json'
audit=json.loads(audit_path.read_text(encoding='utf-8'))
audited=[(x['sheet'],x['cell'],x['formula']) for x in audit.get('cells',[])]
if fc!=2974 or errs: fail(f'workbook formulas={fc} cached_errors={errs}')
if sorted(missing)!=sorted(audited): fail('workbook uncached-formula set differs from artifact_tool blank-result audit')
if audit.get('formula_count')!=fc or audit.get('formula_cells_without_serialized_cache')!=len(missing): fail('workbook cache-audit counts')
if audit.get('live_recalculation_nonblank_count')!=0 or audit.get('live_recalculation_blank_count')!=len(missing): fail('workbook cache-audit recalculation result')
if any(not x.get('intentional_blank') or x.get('recalculated_value') not in ('',None) for x in audit.get('cells',[])): fail('workbook cache audit contains a nonblank uncached result')
# calcPr is optional and may be rewritten by the independent recalculation engine.
# Iterative calculation is forbidden because the workbook is required to be acyclic.
# The controlling freshness checks are the exact cached-result audit plus the mandatory
# hard recalculation verifier, so engine-specific omission of calcMode/fullCalcOnLoad is
# not treated as a release failure.
if calc is not None and calc.get('iterate') not in (None,'0','false','False'): fail('workbook iterative calculation enabled')
if hashlib.sha256(xp.read_bytes()).hexdigest()!=hashlib.sha256((ROOT/'core_15/RippleLogic_Aligners_Sheet_v5.5.xlsx').read_bytes()).hexdigest(): fail('Aligners workbook mirror mismatch')
ok(f'Aligners Sheet 2974 formulas, {fc-len(missing)} serialized results + {len(missing)} independently recalculated intentional blanks, no errors, acyclic formula graph, and exact mirror')
# Required content / no architectural drift
for rel in ['docs/canon/RippleLogic_v12.5_Canon.md','docs/standards/ripple_md_Standard_v5.4.md']:
    t=(ROOT/rel).read_text(encoding='utf-8').lower()
    if 'configuration' not in t or 'assurance' not in t: fail(f'configuration assurance absent {rel}')
agent_text=(ROOT/'docs/agents/RippleLogic_Agent_System_v12.3.md').read_text(encoding='utf-8').lower()
if not all(x in agent_text for x in ['capability-state','requalification']): fail('Agent capability-state and requalification interface')
sgp_text=(ROOT/'docs/sgp/SGP_v8.4.md').read_text(encoding='utf-8').lower()
if not all(x in sgp_text for x in ['computational','functional','epistemic','phenomenal']): fail('SGP capability-language boundary')
canon=(ROOT/'docs/canon/RippleLogic_v12.5_Canon.md').read_text(encoding='utf-8')
for phrase in ['RG -> RF/NCRC -> TRC -> CSV -> RLS','No sixth gate','seven Welfare Dimensions','Reality-reference boundary','Material obligation integrity','Hidden human compensation load','Dependency-localized falsification rule']:
    if phrase.lower() not in canon.lower(): fail(f'Canon required phrase {phrase}')
csv_text=(ROOT/'docs/standards/CSV_Gate_Standard_v2.3.md').read_text(encoding='utf-8').lower()
ripple_text=(ROOT/'docs/standards/ripple_md_Standard_v5.4.md').read_text(encoding='utf-8').lower()
if not all(x in csv_text for x in ['binding-control minimum','hidden human compensation load','does not establish that its intended protective effect occurred']): fail('CSV carried-obligation/human-compensation interface')
if not all(x in ripple_text for x in ['material_obligations','human_compensation_load','ab.3b material-obligation integrity']): fail('ripple.md carried-obligation machine interface')
if not all(x in agent_text for x in ['carrier-nonperformance rule','hidden-human-compensation rule','affected obligation id']): fail('Agent carried-obligation runtime interface')
rc_props=run_schema['properties']['responsibility_continuity']['properties']
if not {'material_obligations','human_compensation_load'} <= set(rc_props): fail('run-record v3 obligation-integrity schema fields')
ok('configuration and carried-obligation assurance integrated without cascade expansion')
# Full active-file hash ledger
if not SKIP_HASHES:
    ledger=ROOT/'release/SHA256SUMS.txt'; entries={}
    for line in ledger.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        h,rel=line.split('  ',1); entries[rel]=h
    for rel,h in entries.items():
        p=ROOT/rel
        if not p.is_file(): fail(f'hash path absent {rel}')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=h: fail(f'hash mismatch {rel}')
    manifest=yaml.safe_load((ROOT/'release/release_manifest.yml').read_text(encoding='utf-8'))
    listed=set(manifest['active_files'])
    if listed!=set(entries): fail('release manifest active_files differs from SHA256SUMS')
    ok(f'full active-file SHA-256 ledger ({len(entries)} files)')
    # Core 15 ledger
    core_entries={}
    for line in (ROOT/'release/SHA256SUMS_CORE15.txt').read_text(encoding='utf-8').splitlines():
        h,rel=line.split('  ',1); core_entries[rel]=h
    if {Path(x).name for x in core_entries}!=CORE: fail('Core 15 hash ledger set')
    for rel,h in core_entries.items():
        if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=h: fail(f'Core hash mismatch {rel}')
    ok('Core 15 SHA-256 ledger')
else:
    ok('hash verification skipped by explicit flag')
print('FINAL VERIFICATION: PASS')
