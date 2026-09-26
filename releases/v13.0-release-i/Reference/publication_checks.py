"""Scoped publication-build conformance arithmetic. No actuator or evidence oracle.

These functions test declared finite inputs. They do not certify the original
measurements, a whole Canon run, the external state registry, or authorization.
"""
from __future__ import annotations
from collections.abc import Mapping, Sequence
import math
from datetime import datetime, timezone
from core_reference import finite, RecordError, contributions, every_contender, tail_cvar
from recovery_checks import rmci_lower_bound


def residual_catastrophe_loss(impacts: Sequence[float], weights: Sequence[float]) -> float:
    """Post-option, safe-corridor-relative loss; NOT increment from continuation."""
    if not impacts or len(impacts)!=len(weights):raise RecordError('incomplete catastrophe profile')
    x=[finite(v,'floor-reference impact',-1,1) for v in impacts]
    w=[finite(v,'catastrophe weight',0,1) for v in weights]
    if not math.isclose(math.fsum(w),1,rel_tol=0,abs_tol=1e-12):raise RecordError('weights must sum to one')
    return math.fsum(a*max(0,-b) for a,b in zip(w,x))


def transform_interval(center: float, half_width: float, beta: float) -> dict:
    """Exact image of a stipulated interval under tanh(beta*x).

    Warrant for the input interval is external. Half-width is about the transformed
    interval midpoint, not necessarily about the transformed point estimate.
    """
    m=finite(center,'center');h=finite(half_width,'half-width',0);b=finite(beta,'beta',0)
    if b==0:raise RecordError('positive beta required')
    lo=finite(b*(m-h),'lower transformed argument');hi=finite(b*(m+h),'upper transformed argument')
    l,u=math.tanh(lo),math.tanh(hi);point=math.tanh(b*m)
    return {'lower':l,'upper':u,'midpoint':(l+u)/2,'half_width':(u-l)/2,
            'transformed_point':point,'maximum_deviation_from_point':max(point-l,u-point),
            'boundary':'Conditional interval transport only; no uncertainty calibration claim.'}


def time_weight(years: float, reference: float=25., minimum: float=.083) -> float:
    t=finite(years,'years',0);ref=finite(reference,'reference',0);mn=finite(minimum,'minimum',0)
    if t<=0 or ref<=0 or mn<=0:raise RecordError('positive temporal parameters required')
    return min(1.,math.log1p(max(t,mn))/math.log1p(ref))


def within_cluster_sigma(cell_half_widths: Sequence[float], weights: Sequence[float]) -> float:
    """Perfect positive dependence bound for one declared cluster, not a mandate."""
    if not cell_half_widths or len(cell_half_widths)!=len(weights):raise RecordError('incomplete cluster')
    s=[finite(v,'cell half-width',0,1) for v in cell_half_widths]
    w=[finite(v,'weight',0) for v in weights];q=math.fsum(w)
    if q<=0:raise RecordError('RLS_NO_ACTIVE_MASS')
    return math.fsum(a*b for a,b in zip(s,w))/q


def r38a_fixture() -> dict:
    scores={'A':.060,'B':.030,'C':.020};widths={'A':.004,'B':.004,'C':.006}
    weights=[[1/49]*7 for _ in range(7)];records={};variants=[]
    for name,score in scores.items():
        record=contributions([[score]*7 for _ in range(7)],weights)
        sigma=within_cluster_sigma([widths[name]]*49,[1/49]*49)
        records[name]={'score':record.score,'sigma':sigma,'cell_interval':[score-widths[name],score+widths[name]],'cluster_size':49}
    for scale in (.5,1.,2.):
        variants.append({n:(r['score'],scale*r['sigma']) for n,r in records.items()})
    a=every_contender(variants,list(scores))
    return {'fixture':'R.38A','evidence_kind':'SYNTHETIC_STIPULATION','records':records,'variants':variants,
            'arithmetic':a,'conditional_expected_decision':'SELECTED_DECISIVE',
            'execution_state':'NOT_AUTHORIZED','boundary':'Conditional fixture, not a real-world evidence or full-registry conformance claim.'}


def fixture_decision(fixture: Mapping, *, qualification_supported: bool,
                     required_variants_complete: bool, uncertainty_warrant_stipulated: bool) -> dict:
    """Only the conditional fixture's summary contract, not a production resolver."""
    for b in (qualification_supported,required_variants_complete,uncertainty_warrant_stipulated):
        if type(b) is not bool:raise RecordError('explicit boolean fixture premise required')
    if not qualification_supported:
        return {'conditional_decision_state':'NO_SELECTABLE_OPTION','execution_state':'NOT_AUTHORIZED'}
    if not required_variants_complete or not uncertainty_warrant_stipulated:
        return {'conditional_decision_state':'REFUSE','execution_state':'NOT_AUTHORIZED'}
    a=every_contender(fixture['variants'],list(fixture['records']))
    state='SELECTED_DECISIVE' if a['status']=='DECISIVE_ARITHMETIC_ONLY' else 'REFUSE'
    return {'conditional_decision_state':state,'execution_state':'NOT_AUTHORIZED'}


def rmci_profile_record(lower_bounds: Sequence[float|None], weights: Sequence[float],
                        critical_indices: Sequence[int]) -> dict:
    """Profile-first illustrative record; missing critical evidence blocks summary."""
    if not lower_bounds or len(lower_bounds)!=len(weights):raise RecordError('incomplete profile')
    ww=[finite(v,'weight',0,1) for v in weights]
    if any(w<=0 for w in ww) or not math.isclose(math.fsum(ww),1,abs_tol=1e-12):raise RecordError('positive normalized weights required')
    if any(type(i) is not int or i<0 or i>=len(lower_bounds) for i in critical_indices):raise RecordError('invalid critical dimension')
    for v in lower_bounds:
        if v is not None:finite(v,'known lower bound',0,4)
    record={'dimension_lower_bounds':list(lower_bounds),'weights':ww,'critical_indices':list(critical_indices),
            'summary':None,'status':'UNAVAILABLE','authority':False,
            'boundary':'Arithmetic/profile completeness only. Full evidence and coding sensitivity remain external.'}
    if any(lower_bounds[i] is None for i in critical_indices):return record
    # This strict example profile requires complete coverage. It does not impute missing values.
    if any(v is None for v in lower_bounds):return record
    record.update(summary=rmci_lower_bound(lower_bounds,ww),status='PROFILE_SUMMARY_ONLY')
    return record


def oacp_metadata_check(meta: Mapping, *, audience: str, now: datetime,
                        max_validity_seconds: float, skew_seconds: float=120.) -> dict:
    """OACP-1.1 metadata check only. NO signature verification or command acceptance."""
    maxv=finite(max_validity_seconds,'max validity',0);skew=finite(skew_seconds,'skew',0)
    if maxv<=0 or not audience or now.tzinfo is None:raise RecordError('invalid verifier policy')
    required={'schema_version':'OACP-1.1','sig_alg':'Ed25519','jcs':'RFC8785','aud':audience}
    if any(meta.get(k)!=v for k,v in required.items()):raise RecordError('wrong schema, algorithm, canonicalization or audience')
    for key in ('cmd_id','nonce','kid'):
        if not isinstance(meta.get(key),str) or not meta[key]:raise RecordError('missing identity/replay metadata')
    def utc(key):
        v=meta.get(key)
        if not isinstance(v,str) or not v.endswith('Z'):raise RecordError('UTC timestamp required')
        try:return datetime.fromisoformat(v[:-1]+'+00:00')
        except ValueError as exc:raise RecordError('invalid timestamp') from exc
    issued,expiry=utc('issued_utc'),utc('expires_utc');duration=(expiry-issued).total_seconds()
    if duration<0 or duration>maxv:raise RecordError('invalid validity interval')
    age=(now-issued).total_seconds();remaining=(expiry-now).total_seconds()
    if age < -skew or remaining < -skew:raise RecordError('outside acceptance interval')
    return {'status':'METADATA_MATCH_ONLY','maximum_acceptance_span_seconds':duration+2*skew,
            'signature_verified':False,'replay_reserved':False,'execution_authorized':False}
