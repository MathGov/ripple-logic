"""Supplemental concrete record view of Canon H.10, not external v4.1 conformance.

This is one explicit, testable serialization of the semantic minimums. A result
of no structural errors neither validates evidence nor satisfies all Canon
cross-record, trigger, numerical, or domain rules. Referenced records are not
fetched here. No record or hash grants execution authority.
"""
from pathlib import Path
import json,re,math
SPECS={x['name']:x for x in json.loads(Path(__file__).with_name('record_minimums.json').read_text())['records']}

def nonempty(x):
    if isinstance(x,str):return bool(x.strip())
    if isinstance(x,(list,dict)):return bool(x)
    return x is not None

def validate_record(record:dict)->list[str]:
    if not isinstance(record,dict):return ['record must be an object']
    errors=[]
    for key in ['record_id','record_type','run_id','configuration_ref','source_clauses','applicability','review_status','result']:
        if key not in record or not nonempty(record[key]):errors.append('missing '+key)
    if record.get('record_type') not in SPECS:errors.append('unrecognized supplemental record type')
    for key in ['record_id','record_type','run_id','configuration_ref','review_status']:
        if key in record and not isinstance(record[key],str):errors.append(key+' must be text')
    source=record.get('source_clauses')
    if not isinstance(source,list)or not source or any(not isinstance(s,str)or not s.strip()for s in source):errors.append('source_clauses must be nonempty text array')
    app=record.get('applicability',{})
    if not isinstance(app,dict) or type(app.get('triggered'))is not bool or not isinstance(app.get('rationale'),str)or not app['rationale'].strip():
        errors.append('applicability requires boolean triggered and rationale');app={}
    result=record.get('result',{})
    if not isinstance(result,dict)or type(result.get('evaluated'))is not bool or not isinstance(result.get('unresolved'),list)or not isinstance(result.get('disposition'),str)or not result['disposition'].strip():errors.append('result requires evaluated, unresolved, disposition');result={}
    refs=record.get('evidence_refs')
    if not isinstance(refs,list):errors.append('evidence_refs must be an array; empty requires unresolved explanation')
    else:
        for ref in refs:
            if not isinstance(ref,dict)or not isinstance(ref.get('id'),str)or not ref['id'].strip()or not re.fullmatch('[a-f0-9]{64}',str(ref.get('sha256',''))):errors.append('invalid hash-bound evidence reference')
    content=record.get('content',{})
    if app.get('triggered')and result.get('evaluated'):
        spec=SPECS.get(record.get('record_type'))
        if not isinstance(content,dict):errors.append('content must be an object');content={}
        if spec:
            for field in spec['fields']:
                if not nonempty(content.get(field)):errors.append('missing content.'+field)
        if not refs:errors.append('evaluated triggered record needs evidence references')
    if app.get('triggered')and not result.get('evaluated')and not result.get('unresolved'):errors.append('unevaluated triggered record must disclose unresolved requirements')
    return errors

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('record',type=Path);a=ap.parse_args()
    try:errors=validate_record(json.loads(a.record.read_text()))
    except (OSError,ValueError)as e:errors=[str(e)]
    print(json.dumps({'status':'PASS'if not errors else'FAIL','errors':errors,'scope':'Supplemental record structure only; no external registry/wire conformance or evidence truth.'},indent=2));raise SystemExit(bool(errors))
