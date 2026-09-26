"""Scoped cross-option sensitivity, not a replacement for the canonical Gap.

Source: Canon 10.4 cross-option clarification. The caller must warrant the
final-score uncertainty interpretation and evidence. This module validates
arithmetic inputs only; it cannot establish that warrant or authorize an action.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from collections.abc import Sequence


def number(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite real number')
    return float(value)


def signed_gap(score_a: float, score_b: float, sigma_a: float, sigma_b: float,
               rho: float = 0.0, epsilon: float = 1e-6) -> float:
    """Pairwise variance identity, using a cancellation-resistant expression.

    A zero marginal implies zero covariance; rho then has no mathematical effect.
    Even in that case an invalid rho is rejected rather than silently corrected.
    """
    a,b,sa,sb,r,e = [number(x,n) for x,n in zip(
        (score_a,score_b,sigma_a,sigma_b,rho,epsilon),
        ('score_a','score_b','sigma_a','sigma_b','rho','epsilon'))]
    if sa < 0 or sb < 0 or not -1 <= r <= 1 or e <= 0:
        raise ValueError('sigma must be nonnegative, rho in [-1,1], epsilon positive')
    variance = (sa-sb)**2 + 2*sa*sb*(1-r)
    return (a-b)/math.sqrt(variance+e)


def review_pair(score_a: float, score_b: float, sigma_a: float, sigma_b: float,
                rho_lower: float | None, *, model_warranted: bool,
                epsilon: float=1e-6, delta: float=2.0) -> dict:
    """Keep nominal and adverse comparisons. Never silently certify an error model.

    None for a material unbounded rho requests the conservative pairwise -1
    stress. It is not a joint all-options equicorrelation matrix.
    """
    d=number(delta,'delta')
    if d <= 0: raise ValueError('delta must be positive')
    nominal=signed_gap(score_a,score_b,sigma_a,sigma_b,0,epsilon)
    if model_warranted is not True:
        return {'status':'UNVERIFIED_MODEL','nominal':nominal,'adverse':None,
                'comparison_survives':False,'authority':'NONE'}
    lower=-1.0 if rho_lower is None else number(rho_lower,'rho_lower')
    adverse=signed_gap(score_a,score_b,sigma_a,sigma_b,lower,epsilon)
    sensitivity=(nominal>d)!=(adverse>d)
    return {'status':'RLS_DEPENDENCE_SENSITIVE' if sensitivity else 'COMPARISON_RECORDED',
            'nominal':nominal,'adverse':adverse,'rho_lower':lower,
            'comparison_survives':min(nominal,adverse)>d,
            'authority':'NONE'}


def covariance_valid(matrix: Sequence[Sequence[float]], tolerance: float=1e-12) -> bool:
    """Small symmetric PSD check without NumPy; tolerance is numerical only.

    Zero-pivot Schur/LDL test rejects nonzero remaining covariance against a zero
    variance. This tests algebraic consistency, not empirical covariance truth.
    """
    tol=number(tolerance,'tolerance')
    if tol<0: raise ValueError('negative tolerance')
    n=len(matrix)
    if not n or any(len(row)!=n for row in matrix): return False
    try:a=[[number(x,'covariance') for x in row] for row in matrix]
    except ValueError:return False
    scale=max(1.0,max(abs(x)for row in a for x in row));bound=tol*scale
    if any(abs(a[i][j]-a[j][i])>bound for i in range(n)for j in range(n)):return False
    for k in range(n):
        pivot=a[k][k]
        if pivot < -bound:return False
        if abs(pivot)<=bound:
            if any(abs(a[k][j])>bound for j in range(k+1,n)):return False
            continue
        for i in range(k+1,n):
            for j in range(i,n):
                a[i][j]-=a[i][k]*a[k][j]/pivot;a[j][i]=a[i][j]
    return True
