"""Repeat native Calc recalculation, save, cold reopen and comparison on test copies.
Run from the publication root:
python -B Native_Verification/verify_native_roundtrip.py --output-dir ../native-acceptance
Requires LibreOffice and a Python interpreter with UNO. Never edits Core_15.
"""
from pathlib import Path
import sys,subprocess,socket,tempfile,argparse,json,os,math,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'Reference'))
from Workbook_Verifier import inspect

def main(out,engine,uno_python):
    out=out.resolve()
    if out==ROOT or ROOT in out.parents:raise ValueError('Output must be outside the immutable publication root')
    out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    cmd=[sys.executable,'-B',str(ROOT/'Reference/verify_libreoffice.py'),'--output-dir',str(out/'native'),'--engine',engine,'--uno-python',uno_python]
    run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True,timeout=240)
    (out/'native_console.log').write_text(run.stdout+'\n'+run.stderr)
    if run.returncode:raise RuntimeError('Native recalculation did not pass; see native_console.log')
    base=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx';data=inspect(base)
    requests={sn:[a for a,c in cells.items() if c['formula'] is not None]for sn,cells in data['cells'].items()}
    (out/'formula_cells.json').write_text(json.dumps(requests))
    saved=out/'native/native_final'/base.name
    with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    with tempfile.TemporaryDirectory(prefix='mathgov-cold-reopen-')as profile:
        proc=subprocess.Popen([engine,'-env:UserInstallation='+Path(profile).as_uri(),'--headless',f'--accept=socket,host=localhost,port={port};urp;StarOffice.ServiceManager','--norestore','--nodefault','--nofirststartwizard'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        try:
            worker=subprocess.run([uno_python,'-B',str(ROOT/'Native_Verification/native_reopen_worker.py'),str(port),str(saved),str(out/'formula_cells.json'),str(out/'cold_reopen.json')],capture_output=True,text=True,timeout=180)
            (out/'cold_reopen.log').write_text(worker.stdout+'\n'+worker.stderr)
            if worker.returncode:raise RuntimeError('Cold reopen failed; see cold_reopen.log')
        finally:
            proc.terminate()
            try:proc.wait(timeout=10)
            except subprocess.TimeoutExpired:proc.kill();proc.wait()
    native=json.loads((out/'cold_reopen.json').read_text()); differences=[]; count=0
    for sn,cells in native['formula_results'].items():
        for addr,record in cells.items():
            count+=1;x=data['cells'][sn][addr]['value'];y=record['value']
            same=math.isclose(x,y,rel_tol=1e-12,abs_tol=1e-12)if type(x)in(int,float)and type(y)in(int,float)else x==y
            if not same:differences.append({'sheet':sn,'cell':addr,'original':x,'native':y})
    unchanged=hashlib.sha256(base.read_bytes()).hexdigest()==data['sha256']
    old=json.loads((out/'native/Native_Engine_Receipt.json').read_text())
    result={'status':'PASS'if not differences and not native['errors']and unchanged else'FAIL','engine':old['engine'],'input_sha256':data['sha256'],'calculation_comparisons':old['formula_cells_compared'],'mutation_checks_passed':old['mutation_checks_passed'],'mutation_checks_total':old['mutation_checks_total'],'cold_reopen_formula_comparisons':count,'cold_reopen_differences':differences,'cold_reopen_errors':native['errors'],'core_workbook_unchanged':unchanged,'boundary':'Build-specific Calc calculation and saved/reopened test-copy evidence. The native reserialization is not substituted for the immutable Core master; not Microsoft Excel parity or a general operational-selector certificate.'}
    (out/'Native_Roundtrip_Receipt.json').write_text(json.dumps(result,indent=2))
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',required=True,type=Path);ap.add_argument('--engine',default='libreoffice');ap.add_argument('--uno-python',default='/usr/bin/python3');a=ap.parse_args()
    try:r=main(a.output_dir,a.engine,a.uno_python)
    except Exception as e:r={'status':'UNVERIFIED','error':str(e)}
    print(json.dumps(r,indent=2));sys.exit(0 if r['status']=='PASS'else 1)
