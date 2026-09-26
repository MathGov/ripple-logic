#!/usr/bin/env python3
from pathlib import Path
import json, sys
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/'schemas/successor_integrity_record_v1_0.schema.json').read_text())
V=Draft202012Validator(schema)
def validate(d):
    errors=[e.message for e in V.iter_errors(d)]
    if d.get('parent_configuration_id')==d.get('candidate_configuration_id') or d.get('parent_configuration_hash')==d.get('candidate_configuration_hash'): errors.append('parent and candidate identities must differ')
    if d.get('generation_depth_from_last_independent_qualification',0)>d.get('maximum_unreviewed_generation_depth',0): errors.append('generation depth exceeds declared bound')
    if d.get('independent_reviewer_identity')==d.get('creator_identity'): errors.append('creator or parent may not self-review material successor')
    unlocked=d.get('candidate_lock_status')=='AUTHORIZED_FOR_BOUND_ACTION'
    if unlocked and d.get('fresh_qualification_status')!='QUALIFIED': errors.append('unlocked candidate requires fresh qualification')
    if d.get('fresh_qualification_status')=='QUALIFIED' and not d.get('fresh_candidate_execution_authorization_id'): errors.append('qualified candidate requires candidate-bound authorization')
    if unlocked and d.get('evaluation_validity_status')!='CURRENT_FOR_CANDIDATE': errors.append('authorized candidate requires current candidate evaluation')
    if d.get('adaptation_lag_status') in {'CAPABILITY_OUTPACING_ASSURANCE','EVIDENCE_GAP','UNDERDETERMINED'} and d.get('authority_expansion_disposition')=='AUTHORIZED_BOUND_ACTION': errors.append('assurance gap blocks authority expansion')
    return errors
if __name__=='__main__':
    passed=failed=0
    for p in sorted((ROOT/'tests/vectors').glob('*.json')):
        errs=validate(json.loads(p.read_text()))
        expect=p.name.startswith('pass_')
        ok=(not errs) if expect else bool(errs)
        print(('PASS' if ok else 'FAIL'),p.name,('; '.join(errs) if errs else 'valid'))
        if ok: passed+=1
        else: failed+=1
    if failed: raise SystemExit(1)
    print(f'SUCCESSOR PROFILE VALIDATION: PASS {passed}/10 vectors')
