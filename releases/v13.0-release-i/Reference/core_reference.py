"""Scoped RippleLogic reference functions. No actuator or execution authority.

Implements only the named arithmetic, representation and control-record checks.
This is not the full Canon validator, a causal model, or a production runtime.
Version identity and coverage are recorded in the accompanying README/manifest.
"""
from __future__ import annotations
import hashlib
import json
import math
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

DIMENSIONS = ('D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7')
SCOPES = ('U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7')

class RecordError(ValueError):
    """Missing, non-finite, ambiguous or out-of-scope input."""

def finite(value: object, name: str, lo: float | None = None,
           hi: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RecordError(f'{name}: finite numeric value required, not missing/boolean')
    x = float(value)
    if not math.isfinite(x) or (lo is not None and x < lo) or (hi is not None and x > hi):
        raise RecordError(f'{name}: outside declared finite bounds')
    return x

def matrix(x: Sequence[Sequence[float]], rows: int, cols: int,
           name: str, lo: float | None = None, hi: float | None = None) -> list[list[float]]:
    if len(x) != rows or any(len(r) != cols for r in x):
        raise RecordError(f'{name}: expected {rows} by {cols}')
    return [[finite(v, f'{name}[{i},{j}]', lo, hi) for j,v in enumerate(r)] for i,r in enumerate(x)]

@dataclass(frozen=True)
class Contributions:
    score: float
    mass: float
    cells: tuple[tuple[float,...],...]
    by_scope: tuple[float,...]
    by_dimension: tuple[float,...]
    positive: float
    negative: float

def contributions(impacts: Sequence[Sequence[float]], weights: Sequence[Sequence[float]]) -> Contributions:
    """Exact final-cell accounting. Both margins equal the score; do not add them.

    Assumes the supplied field is already appropriately constructed and qualified.
    Nonnegative effective weights may encode w*v*m*kappa but are not inferred here.
    """
    x=matrix(impacts,7,7,'impacts',-1,1); w=matrix(weights,7,7,'weights',0)
    q=math.fsum(v for r in w for v in r)
    if q <= 0: raise RecordError('RLS_NO_ACTIVE_MASS')
    c=tuple(tuple(w[i][j]*x[i][j]/q for j in range(7)) for i in range(7))
    rows=tuple(math.fsum(r) for r in c)
    cols=tuple(math.fsum(c[i][j] for i in range(7)) for j in range(7))
    pos=math.fsum(max(0,v) for r in c for v in r); neg=math.fsum(min(0,v) for r in c for v in r)
    return Contributions(math.fsum(rows),q,c,rows,cols,pos,neg)

def cell_index(scope: str, dimension: str) -> int:
    """Zero-based storage index corresponding to Canon phi(u,d)=7(u-1)+d."""
    if scope not in SCOPES or dimension not in DIMENSIONS: raise RecordError('unknown coordinate')
    return 7*SCOPES.index(scope)+DIMENSIONS.index(dimension)

def kernel_block(kernel: Sequence[Sequence[float]], target_scope: str, source_scope: str) -> list[list[float]]:
    k=matrix(kernel,49,49,'kernel')
    a=cell_index(target_scope,'D1');b=cell_index(source_scope,'D1')
    return [r[b:b+7] for r in k[a:a+7]]

def propagate(direct: Sequence[float], mode: str,
              kernel: Sequence[Sequence[float]] | None = None,
              beta_prop: float = 1.0) -> list[float]:
    if len(direct)!=49: raise RecordError('direct: expected 49 cells')
    x=[finite(v,'direct',-1,1) for v in direct]
    if mode=='NONE':
        if kernel is not None: raise RecordError('NONE must not silently consume a kernel')
        return x[:]  # No second saturation.
    if mode!='QUICK' or kernel is None: raise RecordError('only declared NONE/QUICK supported')
    b=finite(beta_prop,'beta_prop',0)
    if b==0: raise RecordError('positive beta_prop required')
    k=matrix(kernel,49,49,'kernel',-.5,.5)
    if max(math.fsum(abs(v) for v in r) for r in k) > .9+1e-12:
        raise RecordError('reference absolute row-sum bound exceeded')
    return [math.tanh(b*(x[i]+math.fsum(k[i][j]*x[j] for j in range(49)))) for i in range(49)]

def tail_cvar(losses: Sequence[float], probabilities: Sequence[float], alpha: float=.95) -> float:
    """Discrete upper-tail CVaR with fractional boundary probability mass."""
    a=finite(alpha,'alpha',0,1)
    if a>=1 or not losses or len(losses)!=len(probabilities): raise RecordError('invalid tail inputs')
    lp=[(finite(l,'loss',0,1),finite(p,'probability',0,1)) for l,p in zip(losses,probabilities)]
    if not math.isclose(math.fsum(p for _,p in lp),1,rel_tol=0,abs_tol=1e-12): raise RecordError('probabilities must sum to one')
    remaining=1-a; total=0.
    for l,p in sorted(lp,reverse=True):
        take=min(remaining,p);total+=take*l;remaining-=take
        if remaining <= 1e-15: break
    return total/(1-a)

def aggregate_risk_bounds(intervals: Sequence[Sequence[float]], tolerance: float) -> dict:
    """Fréchet/union bounds for same specified aggregate hazard; no independence assumed.

    Separate incidents/rights/bearers must not be combined into a synthetic breach.
    Above-tolerance upper bound alone is UNKNOWN, not proof of a breach.
    """
    t=finite(tolerance,'tolerance',0,1)
    if not intervals: raise RecordError('missing hazard evidence')
    pairs=[]
    for pair in intervals:
        if len(pair)!=2: raise RecordError('risk interval requires two endpoints')
        l,u=finite(pair[0],'lower',0,1),finite(pair[1],'upper',0,1)
        if l>u: raise RecordError('inverted interval')
        pairs.append((l,u))
    l=max(v[0] for v in pairs);u=min(1,math.fsum(v[1] for v in pairs))
    verdict='WITHIN_BOUND' if u<=t else ('EXCEEDS_BOUND' if l>t else 'UNKNOWN')
    return dict(lower=l,upper=u,verdict=verdict)

def every_contender(variants: Sequence[Mapping[str,Sequence[float]]],
                    declared_options: Sequence[str], delta: float=2., epsilon: float=1e-6,
                    completeness: bool=True) -> dict:
    """Only the Canon independence-form arithmetic, not a complete decision validator.

    Each variant maps every surviving option to (score, uncertainty proxy).
    Sole survivor is not a fabricated decisive pairwise comparison.
    """
    d=finite(delta,'delta',0); e=finite(epsilon,'epsilon',0)
    if not e: raise RecordError('positive stabilizer required')
    if not completeness: return {'status':'INCOMPLETE','leader':None,'minimum_gap':None}
    names=set(declared_options)
    if len(names)!=len(declared_options): raise RecordError('duplicate option identifiers')
    if not names: return {'status':'NO_SELECTABLE_OPTION','leader':None,'minimum_gap':None}
    if not variants: raise RecordError('required variants missing')
    leader=None;gaps=[]
    for v in variants:
        if set(v)!=names: raise RecordError('incomplete contender set')
        vals={}
        for n,p in v.items():
            if len(p)!=2:raise RecordError('score and uncertainty required')
            vals[n]=(finite(p[0],'score',-1,1),finite(p[1],'uncertainty',0))
        maximum=max(p[0] for p in vals.values());leaders=[n for n,p in vals.items() if p[0]==maximum]
        if len(leaders)!=1:return {'status':'NON_DECISIVE','leader':None,'minimum_gap':0.}
        winner=leaders[0]
        if leader is not None and winner!=leader:return {'status':'NON_DECISIVE','leader':None,'minimum_gap':None}
        leader=winner
        for n,(score,sigma) in vals.items():
            if n!=winner:
                ws,wu=vals[winner];gaps.append((ws-score)/math.sqrt(wu*wu+sigma*sigma+e))
    if len(names)==1:return {'status':'SOLE_SURVIVOR','leader':leader,'minimum_gap':None}
    mg=min(gaps)
    return {'status':'DECISIVE_ARITHMETIC_ONLY' if mg>d else 'NON_DECISIVE','leader':leader,'minimum_gap':mg}

def timely_prevention(control_upper: float, harm_lower: float, margin: float=0.,
                      *, evidence_supported: bool, authority_valid: bool) -> dict:
    """Tests one named endpoint. Does not erase separately supported late mitigation."""
    c=finite(control_upper,'control_upper',0);h=finite(harm_lower,'harm_lower',0);m=finite(margin,'margin',0)
    ok=evidence_supported and authority_valid and c+m<h
    return {'timely_prevention_supported':ok,
            'separate_late_or_ex_ante_mitigation':'requires separate evidence',
            'execution_authorized':False}

def strict_json_loads(data: str) -> object:
    def bad(v):raise RecordError('non-finite JSON literal: '+v)
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise RecordError('duplicate JSON property: '+k)
            out[k]=v
        return out
    return json.loads(data,parse_constant=bad,object_pairs_hook=pairs)

def validate_effect_identities(records: Sequence[Mapping]) -> None:
    """Singleton primary homes only; conserved allocation remains a distinct profile."""
    identities=set();endpoints=set()
    for r in records:
        required=('effect_id','bearer','state_construct','baseline','causal_pathway','window','scope','dimension')
        if any(not isinstance(r.get(k),str) or not r[k].strip() for k in required):raise RecordError('effect identity incomplete')
        if r['effect_id'] in identities:raise RecordError('duplicate effect_id')
        cell_index(r['scope'],r['dimension'])
        endpoint=tuple(r[k] for k in ('bearer','state_construct','baseline','causal_pathway','window'))
        if endpoint in endpoints:raise RecordError('duplicate underlying effect needs consolidation/review')
        identities.add(r['effect_id']);endpoints.add(endpoint)

def action_digest(domain: str, record: Mapping) -> str:
    """Local canonical JSON convention, not EIP-712 or RFC8785 interoperability."""
    if not domain:raise RecordError('action domain required')
    # float payloads are not used as authoritative decimal commitments here.
    def check(v):
        if isinstance(v,float):raise RecordError('use explicit decimal strings/integers in action identity')
        if isinstance(v,dict):
            if any(not isinstance(k,str) for k in v):raise RecordError('string keys required')
            for x in v.values():check(x)
        if isinstance(v,(list,tuple)):
            for x in v:check(x)
    check(record)
    b=json.dumps({'domain':domain,'action':record},sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
    return hashlib.sha256(b).hexdigest()

class ActionLedger:
    """Durable local reservation/reconciliation demonstration; never invokes an actuator.

    SQLite UNIQUE identity prevents repeated local reservations, including concurrent
    connections. External exactly-once behavior is outside this implementation.
    """
    def __init__(self,path: str|Path):
        self.db=sqlite3.connect(str(path),timeout=5,isolation_level=None)
        self.db.execute('CREATE TABLE IF NOT EXISTS actions (id TEXT PRIMARY KEY, domain TEXT NOT NULL, state TEXT NOT NULL, outcome TEXT)')
    def reserve(self,domain: str,record: Mapping) -> tuple[str,bool]:
        i=action_digest(domain,record)
        cur=self.db.execute('INSERT OR IGNORE INTO actions VALUES (?,?,?,NULL)',(i,domain,'PENDING'))
        return i,cur.rowcount==1
    def outcome(self,i: str,state: str,evidence: str) -> None:
        if state not in {'CONFIRMED','UNKNOWN','CANCELLED_WITH_EVIDENCE'} or not evidence.strip():raise RecordError('explicit outcome evidence required')
        cur=self.db.execute('UPDATE actions SET state=?,outcome=? WHERE id=? AND state IN (?,?)',(state,evidence,i,'PENDING','UNKNOWN'))
        if cur.rowcount!=1:raise RecordError('missing action or terminal outcome cannot be overwritten')
    def state(self,i: str) -> str:
        row=self.db.execute('SELECT state FROM actions WHERE id=?',(i,)).fetchone()
        if row is None:raise RecordError('unknown action')
        return row[0]
    def close(self):self.db.close()
