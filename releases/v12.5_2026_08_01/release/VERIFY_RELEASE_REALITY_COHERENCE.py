#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys, yaml
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
REG=ROOT/'docs/assurance/RELEASE_REALITY_REGISTER_v1.0.yaml'

def fail(msg):
    print('FAIL:',msg)
    raise SystemExit(1)

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

data=yaml.safe_load(REG.read_text(encoding='utf-8'))
if data.get('status')!='ACTIVE_RELEASE_REGISTRY': fail('release-reality registry is not active')
if data.get('release_id')!='MathGov_Core_2026_09_v12.5_SGP_v8.4': fail('release-reality release_id')
arts={x.get('artifact_id'):x for x in data.get('artifacts',[])}
required={'WDBIP_v1_5','MPMR_v1_0','ProofPack_Tier4'}
if set(arts)!=required: fail(f'artifact set mismatch: {set(arts)}')
if arts['WDBIP_v1_5'].get('status')!='AVAILABLE_IN_CORE': fail('WDBIP availability')
if arts['MPMR_v1_0'].get('status')!='AVAILABLE_IN_CORE': fail('MPMR availability')
if arts['MPMR_v1_0'].get('authority')!='INFORMATIVE_CANON_MIRROR': fail('MPMR authority')
if arts['ProofPack_Tier4'].get('status')!='UNAVAILABLE_DESIGN_TARGET' or arts['ProofPack_Tier4'].get('files')!=[]: fail('ProofPack availability boundary')
for aid,a in arts.items():
    for item in a.get('files',[]):
        p=ROOT/item['path']
        if not p.is_file(): fail(f'{aid} missing {item["path"]}')
        if digest(p)!=item.get('sha256'): fail(f'{aid} hash mismatch {item["path"]}')
mp=(ROOT/'docs/assurance/MEASUREMENT_AND_PARAMETER_MATURITY_REGISTER_v1.0.md').read_text(encoding='utf-8')
for forbidden in ['Candidate Canon-owned registry for the next synchronized','This file does not alter an already released Canon until listed']:
    if forbidden in mp: fail('stale MPMR candidate status remains')
blob=REG.read_text(encoding='utf-8')
for forbidden in ['WDBIP_v1_2','CANDIDATE_NOT_CORE_INTEGRATED','COMPUTE_AT_RELEASE','CANDIDATE_TEMPLATE_REQUIRES_HASH_LAST_POPULATION']:
    if forbidden in blob: fail(f'stale release-reality token {forbidden}')
print('PASS release-reality availability, hash binding, and assurance-authority coherence')
