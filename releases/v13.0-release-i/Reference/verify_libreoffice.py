"""Optional named-engine check of this frozen workbook, on disposable copies.

Requires LibreOffice and a Python interpreter with UNO (often /usr/bin/python3).
Run: python -B Reference/verify_libreoffice.py --output-dir ../native-results
Does not edit the release or certify Microsoft Excel compatibility.
"""
from pathlib import Path
import subprocess,argparse,tempfile,socket,hashlib,json,math,shutil,sys
from Workbook_Verifier import inspect
ROOT=Path(__file__).resolve().parents[1]
def run(out:Path,engine:str,uno_python:str):
 out=out.resolve()
 if out==ROOT or ROOT in out.parents:raise ValueError('Output directory must be outside the release tree')
 out.mkdir(parents=True,exist_ok=True);src=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before=sha(src)
 version=subprocess.check_output([engine,'--version'],text=True).strip()
 subprocess.run([uno_python,'-c','import uno'],check=True,capture_output=True)
 with socket.socket()as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
 with tempfile.TemporaryDirectory(prefix='rl-lo-')as profile:
  proc=subprocess.Popen([engine,'-env:UserInstallation='+Path(profile).as_uri(),'--headless',f'--accept=socket,host=localhost,port={port};urp;StarOffice.ServiceManager','--norestore','--nodefault','--nofirststartwizard'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  try:
   r=subprocess.run([uno_python,str(ROOT/'Reference/_libreoffice_worker.py'),str(ROOT),str(out),str(port),version],text=True,capture_output=True,timeout=180)
   (out/'native_execution.log').write_text(r.stdout+'\n'+r.stderr)
   if r.returncode:raise RuntimeError(r.stderr[-2500:])
  finally:
   proc.terminate()
   try:proc.wait(timeout=10)
   except subprocess.TimeoutExpired:proc.kill();proc.wait()
 a=inspect(src);native=out/'native_final'/src.name;b=inspect(native);mismatch=[];checked=0
 for sn,cells in a['cells'].items():
  for addr,c in cells.items():
   if c['formula']is None:continue
   checked+=1;x=c['value'];y=b['cells'].get(sn,{}).get(addr,{}).get('value')
   same=math.isclose(x,y,rel_tol=1e-12,abs_tol=1e-12)if type(x)in(int,float)and type(y)in(int,float)else x==y
   if not same:mismatch.append({'sheet':sn,'cell':addr,'cached':x,'native':y})
 acceptance=json.loads((out/'Native_Final_Acceptance.json').read_text());unchanged=before==sha(src)
 result={'status':'PASS'if not mismatch and not b['formula_errors']and unchanged and acceptance['status']=='PASS'else'FAIL','engine':version,'input_sha256':before,'native_output_sha256':sha(native),'formula_cells_compared':checked,'native_extra_formula_cells':b['formula_count']-a['formula_count'],'formula_cache_mismatches':mismatch,'native_formula_errors':b['formula_errors'],'mutation_checks_passed':acceptance['passed'],'mutation_checks_total':acceptance['total'],'release_workbook_unchanged':unchanged,'boundary':'Engine- and build-specific calculation/cache/mutation evidence. Extra native formulas arise from the engine serialization. No Microsoft Excel parity, empirical validation, general selector or deployment authority claim.'}
 (out/'Native_Engine_Receipt.json').write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',required=True,type=Path);ap.add_argument('--engine',default='libreoffice');ap.add_argument('--uno-python',default='/usr/bin/python3');a=ap.parse_args()
 try:r=run(a.output_dir,a.engine,a.uno_python)
 except Exception as e:r={'status':'UNVERIFIED','error':str(e)}
 print(json.dumps(r,indent=2));raise SystemExit(0 if r['status']=='PASS'else 1)
