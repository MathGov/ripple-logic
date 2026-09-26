"""Supplemental record checks only; not full Canon or physical-truth validation."""
from pathlib import Path
import sys,json,math
from jsonschema import Draft202012Validator,FormatChecker
from core_reference import strict_json_loads,RecordError,finite
BASE=Path(__file__).parent

def validate(record):
    kind=record.get('record_type')
    file={'EffectTransitionRecord':'effect_transition_1.0.schema.json','QualifiedControlRecord':'qualified_control_1.0.schema.json'}.get(kind)
    if file is None:raise RecordError('unsupported supplemental record type')
    schema=json.loads((BASE/'schemas'/file).read_text())
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema,format_checker=FormatChecker()).validate(record)
    if kind=='EffectTransitionRecord' and record['signed_impact']['status']=='KNOWN':
        p=record['signed_impact'];v=finite(p['value'],'value',-1,1);l=finite(p['lower'],'lower',-1,1);u=finite(p['upper'],'upper',-1,1)
        if not l<=v<=u:raise RecordError('impact not inside uncertainty interval')
    if kind=='QualifiedControlRecord':
        for k in ('control_time_upper','harm_time_lower','safety_margin'):finite(record[k],k,0)
    return {'schema':'PASS','supplemental_semantics':'PASS','evidence_truth':'NOT_ESTABLISHED','execution_authorized':False}
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Usage: python validate_records.py RECORD.json')
    print(json.dumps(validate(strict_json_loads(Path(sys.argv[1]).read_text())),indent=2))
