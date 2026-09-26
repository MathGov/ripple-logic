"""Read-only, scoped models for the Release-G recovery and stress clarifications.

No result authorizes a real action or warrants empirical error distributions.
The joint model, applicability and admissible variant set are caller evidence.
"""
from __future__ import annotations
from collections.abc import Mapping, Sequence
import itertools, math
from dependence_sensitivity import number, signed_gap

RECOVERY_CHECKS=('logs_reconciled','configuration_reconciled','authority_current',
                 'affected_qualification_complete','reentry_gate_complete','operator_approved')

def recovery_mode(requested_mode:int, checks:Mapping[str,bool]) -> dict:
    """Synthetic gated-reentry predicate: connectivity itself is not an input."""
    if type(requested_mode)is not int or not 0<=requested_mode<=4:
        raise ValueError('requested mode must be an integer from 0 to 4')
    if not isinstance(checks,Mapping)or any(type(v)is not bool for v in checks.values()):
        raise ValueError('recovery checks must be explicit Booleans')
    complete=all(checks.get(k)is True for k in RECOVERY_CHECKS)
    return {'permitted_mode_ceiling':requested_mode if complete else 0,
            'reentry_supported_by_stipulated_checks':complete,
            'execution_authorized':False,'scope':'Synthetic recovery predicate only'}

def crossed_pair(score_a:float,score_b:float,sigma_a:float,sigma_b:float,
                 scales:Sequence[float],rhos:Sequence[float],*,model_warranted:bool,
                 comparisons_complete:bool=True,delta:float=2.,epsilon:float=1e-6)->dict:
    """Cross all declared compatible scale/dependence inputs for one pair.

    Accepts only an explicitly warranted final-score error model. It is not a
    covariance interpretation for arbitrary interval or heuristic half-widths.
    A pairwise adverse bound does not assert joint all-options anticorrelation.
    """
    d=number(delta,'delta')
    if d<=0 or type(model_warranted)is not bool or type(comparisons_complete)is not bool:
        raise ValueError('positive delta and Boolean claims required')
    if not scales or not rhos:raise ValueError('nonempty declared variant sets required')
    ks=[number(k,'scale')for k in scales];rs=[number(r,'rho')for r in rhos]
    if any(k<=0 for k in ks)or any(not -1<=r<=1 for r in rs):raise ValueError('invalid variant')
    nominal=signed_gap(score_a,score_b,sigma_a,sigma_b,0,epsilon)
    if not model_warranted:
        return {'status':'UNVERIFIED_MODEL','comparisons':[],'comparison_survives':False,'authority':'NONE'}
    rows=[{'scale':k,'rho':r,'signed_gap':signed_gap(score_a,score_b,k*sigma_a,k*sigma_b,r,epsilon)}
          for k,r in itertools.product(ks,rs)]
    survives=comparisons_complete and nominal>d and all(x['signed_gap']>d for x in rows)
    return {'status':'COMPARISON_RECORDED'if survives else'NON_DECISIVE',
            'nominal':nominal,'comparisons':rows,'comparison_survives':survives,'authority':'NONE'}
