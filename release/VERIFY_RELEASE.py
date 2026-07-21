#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,subprocess,sys,yaml
ROOT0=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default=str(ROOT0)); ap.add_argument('--skip-hashes',action='store_true'); a=ap.parse_args(); ROOT=Path(a.root).resolve()
FAIL=[]
def ck(c,m):
 if not c: FAIL.append(m)
manifest=yaml.safe_load((ROOT/'release/release_manifest.yml').read_text())
ck(manifest.get('package')=='MathGov_Core_2026_09_GitHub_Release_v12_4_SGP_V8_3_FINAL_WORLD_INTRODUCTION_GITHUB_PILOT_READY','package name')
ck('v12.4 / SGP v8.3' in manifest.get('release_line',''),'release line')
for row in manifest.get('active_files',[]):
 rel=row['file'] if isinstance(row,dict) else row; ck((ROOT/rel).is_file(),f'manifest active file missing {rel}')
for sc in ['VERIFY_CURRENT_PINS.py','VERIFY_SEMANTIC_SURFACES.py','VERIFY_FORMULA_INTERFACE_INTEGRITY.py','VERIFY_FORMAT_AND_REPRODUCIBILITY.py','VERIFY_STATE_SEMANTICS_AND_NON_DILUTION.py']:
 print(f'RUN {sc}', flush=True)
 try:
  cp=subprocess.run([sys.executable,str(ROOT/'release'/sc),str(ROOT)],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env={**__import__('os').environ,'PYTHONDONTWRITEBYTECODE':'1'},timeout=300)
  print(cp.stdout,end='',flush=True); ck(cp.returncode==0,f'{sc} failed')
 except subprocess.TimeoutExpired as e:
  print((e.stdout or ''),end='',flush=True); ck(False,f'{sc} timed out')
if not a.skip_hashes:
 ledger=ROOT/'release/SHA256SUMS.txt'; ck(ledger.is_file(),'missing hash ledger')
 if ledger.is_file():
  for line in ledger.read_text().splitlines():
   if not line.strip(): continue
   h,rel=line.split('  ',1); p=ROOT/rel; ck(p.is_file(),f'hash path missing {rel}')
   if p.is_file(): ck(hashlib.sha256(p.read_bytes()).hexdigest()==h,f'hash mismatch {rel}')
if FAIL:
 print('FAIL complete v12.4 release verification:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS complete MathGov v12.4 / SGP v8.3 release verification')
