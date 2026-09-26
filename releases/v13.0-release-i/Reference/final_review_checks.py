"""Bounded executable fixtures for final-review corrections, not a runtime.

The functions validate supplied records and stipulated permission prerequisites.
They do not observe real authority, verify signatures, establish sentience,
measure capacity, or execute an action. Diagnostic strings are local test outputs,
not additions to the Canon's authoritative state/flag registries.
"""
from __future__ import annotations
from collections.abc import Mapping, Sequence
import math
from core_reference import RecordError, finite

MODE4_CATEGORIES = (
 'Read: Public data','Read: Internal docs','Read: Sensitive/Restricted',
 'Write: Draft buffer','Write: Public post','Write: DMs','Network: Open links',
 'Network: Downloads','Tools: File I/O','Tools: External actions',
 'Tools: Skills/Extensions','Memory: Public (stats)','Memory: Private (encrypted)',
 'Memory: Secrets/PII','Identity: Impersonation','Successor: authority inheritance',
)
FORBIDDEN = frozenset(('Read: Sensitive/Restricted','Network: Downloads',
 'Memory: Secrets/PII','Identity: Impersonation','Successor: authority inheritance'))
COMMON = ('mode4_activated','tier3_risk_assessment','action_allowlisted',
 'current_configuration','current_qualification','authenticated_authority',
 'applicable_signed_envelope','logging_available','within_limits','safe_state_available')

def mode4_permission_fixture(category: str, evidence: Mapping[str, object]) -> bool:
    """Return whether *stipulated* fields meet the table's permission ceiling.

    This is not signature verification or authorization. Missing and truthy-but-
    non-Boolean fields fail closed. Global invariants override all allowances.
    """
    if category not in MODE4_CATEGORIES or category in FORBIDDEN:
        return False
    if any(evidence.get(k) is not True for k in COMMON):
        return False
    extra = {
      'Read: Internal docs': ('document_allowlisted',),
      'Write: Public post': ('posting_oversight_satisfied',),
      'Write: DMs': ('thread_approved',),
      'Network: Open links': ('link_allowlisted','read_only','no_authentication','no_download'),
      'Tools: File I/O': ('file_operation_allowlisted','structural_viability_record'),
      'Tools: External actions': ('external_action_allowlisted','structural_viability_record'),
      'Tools: Skills/Extensions': ('skill_enabled','skill_pinned','skill_sandboxed'),
      'Memory: Private (encrypted)': ('private_memory_enabled','retention_controls'),
    }.get(category, ())
    return all(evidence.get(k) is True for k in extra)

def method_b_from_ledger(contributions: Sequence[float] | None, confidence: float) -> float:
    """Compute only the retained pre-saturation support proxy, not calibrated sigma.

    A net cell aggregate is not an instance ledger. Caller must establish that
    the supplied sequence is the warranted, complete pre-confidence ledger.
    """
    c=finite(confidence,'confidence',0,1)
    if contributions is None or len(contributions)==0:
        raise RecordError('Method B unavailable: complete instance ledger required')
    mass=min(1., math.fsum(abs(finite(x,'instance')) for x in contributions))
    return (1.-c)*mass

def single_instance_reconstruction(impact: float, beta: float, confidence: float) -> float:
    """Only the declared direct single-instance tanh path; no propagated inverse."""
    x=finite(impact,'impact',-1,1);b=finite(beta,'beta',0);c=finite(confidence,'confidence',0,1)
    if abs(x)>=1 or b==0 or c==0:
        raise RecordError('Single-instance inverse is undefined for these inputs')
    return math.atanh(x)/(b*c)

def rmci_coverage_fixture(levels: Sequence[float | None], weights: Sequence[float],
                          critical: Sequence[int]=(), minimum_coverage: float=1.) -> dict:
    """Compute a disclosed partial-profile number, never a capacity/authority claim."""
    if not levels or len(levels)!=len(weights):raise RecordError('Aligned nonempty profile required')
    ww=[finite(w,'weight',0) for w in weights]
    if any(w<=0 for w in ww) or not math.isclose(math.fsum(ww),1.,abs_tol=1e-12):raise RecordError('Positive normalized weights required')
    if any(type(i)is not int or i<0 or i>=len(levels) for i in critical):raise RecordError('Invalid critical index')
    cov=finite(minimum_coverage,'coverage',0,1)
    for x in levels:
        if x is not None:finite(x,'known level',0,4)
    retained=tuple(i for i,x in enumerate(levels) if x is not None)
    mass=math.fsum(ww[i]for i in retained)
    available=bool(retained) and mass+1e-12>=cov and all(levels[i]is not None for i in critical)
    summary=None
    if available:
        summary=0. if any(levels[i]==0 for i in retained) else 100.*math.exp(math.fsum((ww[i]/mass)*math.log(levels[i]/4.) for i in retained))
    return {'summary':summary,'retained':retained,'original_weight_coverage':mass,
      'weights':tuple(ww),'status':'AVAILABLE_DISPLAY_ONLY'if available else'UNAVAILABLE',
      'full_profile':tuple(levels),'authority':False,'capacity_improvement_established':False}

def compare_rmci_records(previous: dict,current: dict,*,evidence_invalidation_reason: str | None=None,
                         reviewer_confirmed: bool=False) -> dict:
    """Do not equate a changed-coverage numeric increase with improved capacity."""
    old=previous['full_profile'];new=current['full_profile']
    if len(old)!=len(new):raise RecordError('Comparison design required for changed dimension dictionary')
    removed=[i for i,(a,b)in enumerate(zip(old,new))if a is not None and b is None]
    justified=(not removed) or (isinstance(evidence_invalidation_reason,str)and bool(evidence_invalidation_reason.strip())and reviewer_confirmed is True)
    comparable=(previous['status']==current['status']=='AVAILABLE_DISPLAY_ONLY'
      and previous['retained']==current['retained'] and previous['weights']==current['weights'])
    return {'evidence_change_documented':bool(justified),'same_basis_numeric_comparison':comparable,
      'removed_dimensions':removed,'prior_profile_retained':old,
      'capacity_improvement_established':False,
      'disposition':'REVIEW_EVIDENCE_REMOVAL'if not justified else'MATCHED_DISPLAY_BASIS'if comparable else'CHANGED_COVERAGE_NOT_COMPARABLE'}
