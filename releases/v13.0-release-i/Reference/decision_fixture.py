"""Conditional serialization tests for Canon 11.5/AF.2 and Reproducibility 3.1A.

NOT a full run validator, evidence judge, signature verifier, or actuator. This
module deliberately accepts synthetic fixtures only. Qualification and warrants
are stipulated inputs, not measured facts. No returned record authorizes action.
"""
from __future__ import annotations
from collections.abc import Mapping, Sequence
from core_reference import RecordError, every_contender

QUALIFYING = {
    'rg': frozenset({'RG_SUPPORTED','RG_NARROWED'}),
    'rf': frozenset({'RF_PASS'}),
    'trc': frozenset({'TRC_PASS','TRC_NOT_TRIGGERED'}),
    'csv': frozenset({'CSV_PASS','CSV_PASS_WITH_CONTROLS','CSV_NOT_MATERIAL'}),
}
MODULE_STATES=frozenset({'NOT_TRIGGERED_WITH_RATIONALE','PASS_NO_REVERSAL','SENSITIVE','UNRESOLVED','REQUIRED_NOT_EVALUATED'})
GOOD_MODULE_STATES=frozenset({'NOT_TRIGGERED_WITH_RATIONALE','PASS_NO_REVERSAL'})


def serialize_fixture(record: Mapping) -> dict:
    """Evaluate a finite synthetic comparison and map its conditional outcome.

    A real implementation still needs the entire qualification evidence, a full
    independently pinned registry, and separate authenticated authorization.
    This test profile leaves sole-survivor serialization to Canon 10.4; it does
    not invent a pairwise discrimination result for an empty comparison set.
    """
    if not isinstance(record,Mapping) or record.get('synthetic') is not True:
        raise RecordError('Only explicitly synthetic fixtures are accepted')
    options=record.get('options');variants=record.get('variants');registered=record.get('registered_modules');modules=record.get('modules')
    if not isinstance(options,Mapping) or not options:raise RecordError('Option records required')
    if not isinstance(variants,Sequence) or isinstance(variants,(str,bytes)) or not variants:raise RecordError('Comparison variants required')
    if not isinstance(registered,list) or any(not isinstance(x,str)or not x for x in registered)or len(set(registered))!=len(registered):raise RecordError('Unique explicit module IDs required')
    if not isinstance(modules,Mapping) or set(modules)!=set(registered):raise RecordError('Missing or unregistered robustness module')
    for key,value in modules.items():
        if not isinstance(value,Mapping) or value.get('state') not in MODULE_STATES:raise RecordError('Invalid module state')
        if not isinstance(value.get('rationale'),str)or not value['rationale'].strip():raise RecordError('Module rationale required')
    if type(record.get('required_variants_complete')) is not bool or type(record.get('uncertainty_warrant_stipulated')) is not bool:raise RecordError('Explicit Boolean test qualifications required')
    eligible=[]
    for name,o in options.items():
        if not isinstance(name,str)or not name or not isinstance(o,Mapping):raise RecordError('Invalid option')
        if set(o)<={'rg','rf','trc','csv','qualification_complete','controls_complete'} and set(QUALIFYING)<=set(o):pass
        else:raise RecordError('Incomplete or unexpected qualification record')
        if type(o.get('qualification_complete'))is not bool or type(o.get('controls_complete'))is not bool:raise RecordError('Explicit qualification/controls Booleans required')
        passed=o['qualification_complete']and all(o[k]in allowed for k,allowed in QUALIFYING.items())
        if o['csv']=='CSV_PASS_WITH_CONTROLS'and not o['controls_complete']:passed=False
        if passed:eligible.append(name)
    for v in variants:
        if not isinstance(v,Mapping)or set(v)!=set(options):raise RecordError('Every declared option must appear in every synthetic variant')
    base={'conditional_framework_verdict':'REFUSE_DETERMINISTIC_SELECTION','conditional_decision_state':'REFUSE',
          'selected_option':None,'tie_break_preference':None,'execution_state':'NOT_AUTHORIZED',
          'evidence_kind':'SYNTHETIC_STIPULATION','boundary':'Conditional local fixture only; no actual qualification, complete-registry conformance, or authorization is established.'}
    if not eligible:return dict(base,conditional_framework_verdict=None,conditional_decision_state='NO_SELECTABLE_OPTION')
    arithmetic=every_contender([{a:v[a]for a in eligible}for v in variants],eligible,
                              delta=record.get('delta',2),epsilon=record.get('epsilon',1e-6),
                              completeness=record['required_variants_complete'])
    base['arithmetic']=arithmetic
    if len(eligible)==1:
        return dict(base,conditional_framework_verdict=None,conditional_decision_state=None,fixture_result='SOLE_SURVIVOR_OUTSIDE_THIS_TEST_PROFILE',selected_option=eligible[0])
    good=record['required_variants_complete']and record['uncertainty_warrant_stipulated']and all(v['state']in GOOD_MODULE_STATES for v in modules.values())
    if arithmetic['status']=='DECISIVE_ARITHMETIC_ONLY'and good:
        return dict(base,conditional_framework_verdict='ALLOW_FRAMEWORK_SELECTION',conditional_decision_state='SELECTED_DECISIVE',selected_option=arithmetic['leader'])
    preference=record.get('tie_break_preference')
    if preference is not None:
        if preference not in eligible:raise RecordError('Preference must be ordinarily selectable')
        base['tie_break_preference']=preference
    authority=record.get('authority_selection')
    if authority is not None:
        if not isinstance(authority,Mapping)or authority.get('option')not in eligible:raise RecordError('Invalid synthetic authority preference')
        if authority.get('valid_stipulated')is True and authority.get('record_id'):
            base.update(conditional_decision_state='SELECTED_BY_AUTHORITY_NON_DECISIVE',selected_option=authority['option'])
    return base


def r38a_serialization_fixture() -> dict:
    from publication_checks import r38a_fixture
    f=r38a_fixture()
    return {'synthetic':True,'options':{a:{'rg':'RG_SUPPORTED','rf':'RF_PASS','trc':'TRC_PASS','csv':'CSV_PASS_WITH_CONTROLS','qualification_complete':True,'controls_complete':True}for a in f['records']},
            'variants':f['variants'],'registered_modules':['fixture.dependence','fixture.sigma_stress','fixture.cross_option'],
            'modules':{'fixture.dependence':{'state':'PASS_NO_REVERSAL','rationale':'Stipulated 49-cell single-cluster interval construction, Canon R.38A.'},'fixture.sigma_stress':{'state':'PASS_NO_REVERSAL','rationale':'Explicitly computed 0.5, 1 and 2 multipliers within the stipulated dependence construction.'},'fixture.cross_option':{'state':'NOT_TRIGGERED_WITH_RATIONALE','rationale':'R.38A stipulates mutually independent option-level symmetric plus/minus half-width generators, repeated perfectly within each option. Synthetic construction only, not inferred from marginal intervals; changing or removing this premise reopens this module.'}},
            'required_variants_complete':True,'uncertainty_warrant_stipulated':True}
