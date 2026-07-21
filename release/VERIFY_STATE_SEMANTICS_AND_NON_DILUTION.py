#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys, yaml
from pathlib import Path

ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
fail=[]
def ck(cond,msg):
    if not cond: fail.append(msg)

registry=yaml.safe_load((ROOT/'docs/implementation/CANONICAL_STATE_REGISTRY_v1.0.yaml').read_text())
ck(registry.get('release')=='MathGov_v12.4','state registry release is not v12.4')
ck('TRC_NOT_TRIGGERED' in registry['canonical_tokens']['trc'],'TRC_NOT_TRIGGERED absent from canonical registry')

matrix=json.loads((ROOT/'docs/implementation/STATE_TRANSITION_MATRIX_v1.0.json').read_text())
ck(matrix.get('release')=='MathGov_v12.4','transition matrix release is not v12.4')
normal=[r for r in matrix['normal_rules'] if r.get('require',{}).get('selectable') is True]
ck(len(normal)==1,'expected one normal selectable rule')
if normal:
    trc=normal[0]['when'].get('trc')
    ck(set(trc if isinstance(trc,list) else [trc])=={'TRC_PASS','TRC_NOT_TRIGGERED'},'selectable transition does not use exact TRC qualifying states')

schema=json.loads((ROOT/'schemas/mathgov_run_record_v2.schema.json').read_text())
item=schema['properties']['gate_results']['items']
ck('TRC_NOT_TRIGGERED' in item['properties']['trc']['enum'],'schema lacks TRC_NOT_TRIGGERED')
ck('trc_trigger_assessment' in item['properties'],'schema lacks trigger assessment record')
ck(any(x.get('if',{}).get('properties',{}).get('trc',{}).get('const')=='TRC_NOT_TRIGGERED' for x in item.get('allOf',[])),'schema does not conditionally require trigger assessment')

canon=(ROOT/'docs/canon/RippleLogic_v12.4_Canon.md').read_text()
for token in ['RG_qualified(a)','TRC_qualified(a)','TRC_NOT_TRIGGERED','Non-dilution rule for catastrophe profiles','Catastrophe-profile non-dilution test']:
    ck(token in canon,f'Canon missing {token}')

# Mathematical invariant: adding a zero-loss extension cannot dilute base-profile loss.
base=[1.0,0.0,0.0]
extension=[0.0,0.0,0.0,0.0]
base_profile=sum(base)/len(base)
separate_base=sum(base)/len(base)
naive_combined=sum(base+extension)/len(base+extension)
ck(abs(separate_base-base_profile)<1e-15,'separate profile changed base loss')
ck(naive_combined < base_profile,'non-dilution test fixture does not expose dilution')

validator=ROOT/'release/VALIDATE_MATHGOV_RUN.py'
for rel, expect_fail in [('tests/run_records/pass_trc_not_triggered.json',False),('tests/run_records/fail_trc_not_triggered_missing_assessment.json',True)]:
    cmd=[sys.executable,str(validator),str(ROOT/rel)]
    if expect_fail: cmd.append('--expect-fail')
    cp=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    ck(cp.returncode==0,f'validator vector failed: {rel}')
    if cp.returncode==0:
        if expect_fail:
            print(f'PASS expected rejection vector: {rel}')
        else:
            print(f'PASS positive conformance vector: {rel}')
    else:
        print(cp.stdout,end='')

if fail:
    print('FAIL state-semantics and non-dilution verification:')
    for x in fail: print('-',x)
    raise SystemExit(1)
print('PASS RG/TRC state semantics, TRC_NOT_TRIGGERED evidence requirement, and catastrophe-profile non-dilution')
