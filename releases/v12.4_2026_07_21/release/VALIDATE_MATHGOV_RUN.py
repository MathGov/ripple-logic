#!/usr/bin/env python3
"""MathGov run-record v2 validator.

V0 validates the exact JSON Schema. V1 validates state and cascade semantics.
V2 is a bounded evidence/use-readiness checklist and never proves truth, safety,
legality, or moral correctness.
"""
from __future__ import annotations
import sys
sys.dont_write_bytecode=True
import argparse, json, sys
from pathlib import Path
try:
    from jsonschema import Draft202012Validator
except Exception as exc:
    Draft202012Validator = None

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'schemas/mathgov_run_record_v2.schema.json'
CSV_SELECTABLE={'CSV_PASS','CSV_PASS_WITH_CONTROLS','CSV_NOT_MATERIAL'}
FINAL_WITH_SELECTION={'SELECTED_DECISIVE','SELECTED_BY_AUTHORITY_NON_DECISIVE','PROVISIONAL_WITH_CONTROLS'}

def nonempty(v): return v not in (None,'',[],{})

def normalize_aliases(data):
    warnings=[]
    for row in data.get('gate_results',[]):
        if row.get('csv')=='CSV_REDESIGN':
            row['csv']='CSV_REDESIGN_REQUIRED'; warnings.append(f"{row.get('option_id')}: normalized deprecated CSV_REDESIGN alias")
    return warnings

def r0(data):
    if Draft202012Validator is None:
        return ['jsonschema dependency unavailable; install requirements.txt before claiming V0'],[]
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    val=Draft202012Validator(schema)
    errors=[]
    for e in sorted(val.iter_errors(data), key=lambda x:list(x.absolute_path)):
        path='.'.join(map(str,e.absolute_path)) or '<root>'
        errors.append(f'{path}: {e.message}')
    return errors,[]

def r1(data):
    errors=[]; warnings=normalize_aliases(data)
    ids=data['decision']['option_ids']; rows=data['gate_results']; by={r['option_id']:r for r in rows}
    if set(by)!=set(ids) or len(rows)!=len(ids): errors.append('gate_results must contain exactly one row per option')
    selectable=set(); emergency=data['profile_and_stakes']['state_transition_profile']=='TAIL_EMERGENCY'
    for oid in ids:
        r=by.get(oid)
        if not r: continue
        rg,rf,trc,csv=r['rg'],r['rf'],r['trc'],r['csv']
        if rg=='RG_REFUSED':
            req=('RF_NOT_EVALUATED_AFTER_PRIOR_FAILURE','TRC_NOT_EVALUATED_AFTER_PRIOR_FAILURE','CSV_NOT_EVALUATED_AFTER_PRIOR_FAILURE')
            if (rf,trc,csv)!=req: errors.append(f'{oid}: RG_REFUSED requires deterministic RF/TRC/CSV short-circuit states')
        elif rf in {'RF_FAIL','RF_ESCALATE'}:
            if trc!='TRC_NOT_EVALUATED_AFTER_PRIOR_FAILURE' or csv!='CSV_NOT_EVALUATED_AFTER_PRIOR_FAILURE': errors.append(f'{oid}: RF stop requires TRC/CSV not evaluated')
        elif trc in {'TRC_FAIL','TRC_ESCALATE'}:
            if csv!='CSV_NOT_EVALUATED_AFTER_PRIOR_FAILURE': errors.append(f'{oid}: TRC stop requires CSV not evaluated')
        if trc=='TRC_NOT_TRIGGERED':
            assess=r.get('trc_trigger_assessment') or {}
            if assess.get('assessed') is not True or assess.get('catastrophe_relevance_found') is not False or not nonempty(assess.get('evidence_boundary')) or not nonempty(assess.get('reviewer_status')) or not assess.get('reopen_triggers'):
                errors.append(f'{oid}: TRC_NOT_TRIGGERED requires complete negative catastrophe-relevance assessment, evidence boundary, reviewer status, and reopen triggers')
        normal=(rg in {'RG_SUPPORTED','RG_NARROWED'} and rf=='RF_PASS' and trc in {'TRC_PASS','TRC_NOT_TRIGGERED'} and csv in CSV_SELECTABLE)
        if emergency:
            if trc!='TRC_EMERGENCY_PROVISIONAL' or csv!='CSV_EMERGENCY_PROVISIONAL' or r['selectable']:
                errors.append(f'{oid}: Tail Emergency requires explicit provisional states and no ordinary selectability')
        elif bool(r['selectable'])!=normal: errors.append(f'{oid}: selectable contradicts canonical states')
        if normal: selectable.add(oid)
    ranking=data['ranking']; ranked=ranking['ranked_option_ids']
    if emergency:
        if ranking['method']!='NOT_APPLICABLE' or ranked: errors.append('Tail Emergency cannot use ordinary RLS ranking')
    else:
        if set(ranked)-selectable: errors.append('ranking includes non-selectable option')
        if ranking['method']!='NOT_APPLICABLE' and set(ranked)!=selectable: errors.append('ranking must include every and only selectable option')
    state=data['decision_state']; final=state['state']; selected=state['selected_option_id']
    if final in FINAL_WITH_SELECTION and selected not in selectable: errors.append('ordinary selected option must be selectable')
    if final=='EMERGENCY_PROVISIONAL' and not emergency: errors.append('EMERGENCY_PROVISIONAL requires TAIL_EMERGENCY profile')
    if emergency and final!='EMERGENCY_PROVISIONAL': errors.append('TAIL_EMERGENCY profile requires EMERGENCY_PROVISIONAL final state')
    if final=='SELECTED_DECISIVE' and ranking['decisive'] is not True: errors.append('SELECTED_DECISIVE requires decisive=true')
    if final=='SELECTED_BY_AUTHORITY_NON_DECISIVE' and (ranking['decisive'] is not False or not nonempty(state.get('authority_selection_rationale'))): errors.append('non-decisive authority selection requires decisive=false and rationale')
    auth=data['authority_and_execution']; executing=auth['execution_state'] in {'AUTHORIZED_WITHIN_SCOPE','EXECUTED_UNDER_MONITORING'}
    if executing and (not auth['authority_basis_present'] or not nonempty(auth.get('authority_role')) or not nonempty(auth.get('mandate_scope'))): errors.append('execution requires authority basis, role, and mandate scope')
    for p in data['parameter_lock']['parameters']:
        if p['status']=='UNKNOWN' and p.get('used_in_arithmetic'): errors.append(f"parameter {p['name']}: UNKNOWN cannot enter arithmetic")
        if p['status']=='NOT_MATERIAL' and not nonempty(p.get('not_material_rationale')): errors.append(f"parameter {p['name']}: NOT_MATERIAL requires rationale")
    if data['wdbip']['status']!='NOT_TRIGGERED' and not nonempty(data['wdbip'].get('record_hash_or_locator')): errors.append('triggered WDBIP requires immutable record reference')
    ct=data['consequence_tempo']
    if ct['status']=='RECORD_COMPLETE' and ct['tempo_disposition']=='INDETERMINATE': errors.append('complete tempo record cannot be disposition INDETERMINATE')
    rc=data['responsibility_continuity']
    if rc['status']=='COMPLETE' and any(not nonempty(rc.get(k)) for k in ['decision_authority','evidence_accountability','execution_authority','intervention_authority','appeal_owner','remedy_owner','residual_responsibility']): errors.append('complete responsibility record has unowned required role')
    if rc.get('legal_liability_determined_separately') is not True: warnings.append('responsibility record does not affirm separate legal-liability determination')
    if data['controls_monitoring_and_reopen']['material_change_requires_requalification'] is not True: errors.append('material change must require requalification')
    return errors,warnings

def r2(data):
    issues=[]
    if data['profile_and_stakes']['tier']==3 and data['audit_and_signoff'].get('independent_replay_status')=='NOT_RUN': issues.append('Tier 3 independent replay not run')
    if data['profile_and_stakes']['stakes'] in {'HIGH','CATASTROPHIC_POSSIBLE'} and not data['audit_and_signoff']['reviewers']: issues.append('high-stakes record has no reviewer')
    if data['consequence_tempo']['status']=='RECORD_INDETERMINATE': issues.append('tempo readiness indeterminate')
    if data['responsibility_continuity']['status']=='INCOMPLETE': issues.append('responsibility continuity incomplete')
    return issues

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record',type=Path); ap.add_argument('--expect-fail',action='store_true'); args=ap.parse_args()
    try: data=json.loads(args.record.read_text(encoding='utf-8'))
    except Exception as e: print('FAIL R0 parse:',e); return 0 if args.expect_fail else 1
    e0,w0=r0(data)
    if e0:
        print('FAIL V0 schema validity:'); [print('-',x) for x in e0]; return 0 if args.expect_fail else 1
    e1,w1=r1(data)
    if e1:
        print('PASS V0 schema validity'); print('FAIL V1 semantic conformance:'); [print('-',x) for x in e1]; [print('WARNING:',x) for x in w1]; return 0 if args.expect_fail else 1
    issues=r2(data)
    print('PASS V0 schema validity')
    print('PASS V1 semantic conformance')
    print('R2 USE-READINESS:', 'REVIEW_REQUIRED' if issues else 'NO_AUTOMATED_ISSUES_DETECTED')
    [print('-',x) for x in issues]; [print('WARNING:',x) for x in w1]
    return 1 if args.expect_fail else 0
if __name__=='__main__': raise SystemExit(main())
