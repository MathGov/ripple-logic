"""Literal-input reconstruction and illustrative zero-cell/epsilon sensitivity.
Not a replacement selector, empirical calibration or native spreadsheet engine.
"""
from pathlib import Path
from collections import defaultdict
import math,json
from Workbook_Verifier import inspect
ROOT=Path(__file__).resolve().parents[1]

def independent_gap(a,b,q,sa,sb,epsilon=1e-6):
 vs=[list(x)for x in (a,b,q,sa,sb)]
 if not vs[0]or len({len(v)for v in vs})!=1:raise ValueError('Equal nonempty vectors required')
 if any(type(x)not in(int,float)or not math.isfinite(x)for v in vs for x in v):raise ValueError('Finite numeric inputs required')
 a,b,q,sa,sb=vs
 if any(x<0 for v in(q,sa,sb)for x in v)or not math.isfinite(epsilon)or epsilon<0:raise ValueError('Negative weight/uncertainty/guard')
 Q=math.fsum(q)
 if Q<=0:raise ValueError('No active mass')
 D=math.fsum(w*(x-y)for w,x,y in zip(q,a,b));V=math.fsum((w*x)**2+(w*y)**2 for w,x,y in zip(q,sa,sb));den=math.sqrt(V+epsilon*Q*Q)
 if den==0:raise ValueError('Zero diagnostic denominator, not invented infinity')
 return abs(D)/den

def reconstruct(root=ROOT):
 w=inspect(root/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx')['cells']
 def v(s,a):
  c=w[s][a]
  if c['formula']is not None:raise ValueError('No formula cache may enter raw reconstruction')
  return c['value']
 totals=defaultdict(float)
 for r in range(7,21):
  mu,reach,prob,conf,dur,adj,inc=[v('Impact_Input',c+str(r))for c in'FGHIJKL'];tau=min(1,math.log1p(max(dur,v('CANON','B27')))/math.log1p(v('CANON','B25')))
  totals[tuple(v('Impact_Input',c+str(r))for c in'BCD')]+=mu*reach*prob*conf*adj*inc*tau
 floors=[v('PLSS_Local_Scope','C'+str(r))for r in range(12,19)];p=[v('PLSS_Local_Scope','B'+str(r))for r in range(12,19)]
 weights=[f+(1-math.fsum(floors))*x/math.fsum(p)for f,x in zip(floors,p)];dims=[v('Parameters','B'+str(r))for r in range(48,55)];q=[x*y for x in weights for y in dims];Q=math.fsum(q)
 fields={o:[math.tanh(v('CANON','B20')*totals[(o,'U'+str(u),'D'+str(d))])for u in range(1,8)for d in range(1,8)]for o in'AB'}
 sigma=v('RLS','B36');sigopt=sigma*math.sqrt(math.fsum(x*x for x in q))/Q;delta=v('Config','B22');eps=1e-6
 scores={o:math.fsum(x*y for x,y in zip(q,fields[o]))/Q for o in'AB'}
 f=lambda e,k:independent_gap(fields['A'],fields['B'],q,[k*sigma]*49,[k*sigma]*49,e)
 return {'scores':scores,'active_mass':Q,'assessed_zero_cells':{o:fields[o].count(0.0)for o in'AB'},'sigma_cell':sigma,'sigma_option':sigopt,'epsilon':eps,'delta':delta,'nominal_gap':f(eps,1),'double_sigma_gap':f(eps,2),'epsilon_zero_diagnostic':f(0,1),'double_sigma_epsilon_zero_diagnostic':f(0,2),'epsilon_gap_reduction_percent':100*(1-f(eps,1)/f(0,1)),'flip_multiplier':math.sqrt((((scores['A']-scores['B'])/delta)**2-eps)/(2*sigopt**2)),'verdict':'REFUSE_DETERMINISTIC_SELECTION','boundary':'Demonstration arithmetic only; no calibration, statistical confidence, full operational selector or native application certification.'}
if __name__=='__main__':print(json.dumps(reconstruct(),indent=2))
