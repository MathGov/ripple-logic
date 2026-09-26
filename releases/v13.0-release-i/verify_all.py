"""Run the complete supplied local test suite without modifying release files.

Use --output-dir OUTSIDE this release tree to save logs. These scoped tests do
not recalculate Excel/LibreOffice, prove empirical validity, or authorize action.
"""
from pathlib import Path
import argparse,json,subprocess,sys,time,os,hashlib,shutil,tempfile
ROOT=Path(__file__).resolve().parent

def run(output_dir:Path|None=None,skip_ledger:bool=False)->dict:
    if output_dir is not None:
        output_dir=output_dir.resolve()
        if output_dir==ROOT or ROOT in output_dir.parents:raise ValueError('Log directory must be outside the immutable release tree')
        output_dir.mkdir(parents=True,exist_ok=True)
    def snapshot():return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in ROOT.rglob('*')if p.is_file()and'.git'not in p.parts and'__pycache__'not in p.parts}
    before=snapshot();env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');py=[sys.executable,'-B'];commands=[]
    if not skip_ledger:commands.append(('release_hashes',py+['Reference/verify_release.py']))
    commands.extend([
      ('core_manifest',py+['Reference/VERIFY_CORE_FILES.py']),
      ('unit_tests',py+['-m','unittest','discover','-s','Reference','-p','test_*.py']),
      ('workbook_identity',py+['Reference/Workbook_Verifier.py','Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx']),
      ('workbook_arithmetic',py+['Reference/check_workbook_arithmetic.py']),
      ('workbook_publication',py+['Reference/check_publication_workbook.py']),
      ('workbook_mutations',py+['Reference/test_workbook_integrity.py']),
      ('stored_formula_probe',py+['Reference/workbook_probe.py']),
      ('final_corrections',py+['Reference/check_final_corrections.py']),
      ('release_c_corrections',py+['Reference/check_release_c.py']),
      ('release_d_corrections',py+['Reference/check_release_d.py']),
      ('release_e_corrections',[sys.executable,'-B','Reference/check_release_e.py']),
        ('full_formula_replay',py+['Reference/full_formula_replay.py']),
      ('release_f_corrections',py+['Reference/check_release_f.py']),
      ('final_micro_patch',py+['Reference/check_release_g.py']),
      ('release_h_feedback',py+['Reference/check_release_h.py']),
      ('release_i_errata',py+['Reference/check_release_i.py']),
      ('document_navigation',py+['Reference/document_navigation.py']),
      ('reading_integrity',py+['Reference/check_reading_integrity.py']),
      ('dashboard',['node','Reference/test_review_dashboard.js']),
    ])
    results=[]
    for name,cmd in commands:
        start=time.monotonic()
        if not shutil.which(cmd[0]):r={'name':name,'command':cmd,'status':'UNVERIFIED','error':'Required interpreter unavailable'}
        else:
            with tempfile.TemporaryFile(mode='w+t',encoding='utf-8') as stdout_file, tempfile.TemporaryFile(mode='w+t',encoding='utf-8') as stderr_file:
                completed=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=stdout_file,stderr=stderr_file,timeout=300)
                stdout_file.seek(0);stderr_file.seek(0)
                completed.stdout=stdout_file.read();completed.stderr=stderr_file.read()
            r={'name':name,'command':cmd,'exit_code':completed.returncode,'status':'PASS'if completed.returncode==0 else'FAIL','seconds':round(time.monotonic()-start,3)}
            if output_dir:(output_dir/(name+'.log')).write_text(completed.stdout+'\n'+completed.stderr,encoding='utf-8')
            try:r['result']=json.loads(completed.stdout)
            except json.JSONDecodeError:r['console_tail']=(completed.stdout+'\n'+completed.stderr)[-1400:]
        results.append(r);print(f'{name}: {r["status"]}',file=sys.stderr,flush=True)
    after=snapshot();unchanged=before==after
    result={'status':'PASS'if unchanged and all(x['status']=='PASS'for x in results)else'FAIL','tests':results,'release_files_unchanged':unchanged,'boundary':'Supplied scoped local tests only; native spreadsheet engines, full external registries, evidence truth and deployment authorization are not certified.'}
    if output_dir:(output_dir/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path);ap.add_argument('--skip-ledger',action='store_true',help='Builder-only before final checksum freeze; not a final identity pass.');a=ap.parse_args()
    try:result=run(a.output_dir,a.skip_ledger)
    except Exception as exc:result={'status':'FAIL','error':str(exc)}
    print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS'else 1)
