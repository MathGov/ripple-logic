"""Independent standard-library checks of the frozen worked-run arithmetic.

Reads the actual XLSX via the scoped inspector; does not edit it. This checks
named formula families and source numbers, not arbitrary Excel compatibility.
"""
from pathlib import Path
import json,math,collections,re
from Workbook_Verifier import inspect
from core_reference import contributions,tail_cvar
ROOT=Path(__file__).resolve().parents[1]
def main():
 a=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');m=a['cells'];tests=[]
 def v(s,c):return m[s][c]['value']
 def check(name,actual,expected,tol=1e-12):
  ok=math.isclose(actual,expected,rel_tol=tol,abs_tol=tol) if isinstance(actual,(int,float)) and isinstance(expected,(int,float)) else actual==expected
  tests.append({'check':name,'actual':actual,'expected':expected,'passed':ok});assert ok,(name,actual,expected)
 # Reconstruct all fourteen input effects and all ninety-eight direct cells.
 totals=collections.defaultdict(float)
 for r in range(7,21):
  mu,reach,likelihood,confidence,duration,adjust,inc=[v('Impact_Input',c+str(r)) for c in 'FGHIJKL']
  tau=min(1,math.log1p(max(duration,v('CANON','B27')))/math.log1p(v('CANON','B25')))
  welfare=mu*reach*likelihood*confidence*adjust*inc*tau;base=mu*reach*likelihood*confidence*adjust*tau
  for col,x in [('M',tau),('N',welfare),('U',base),('V',welfare)]:check(f'Impact_Input!{col}{r}',v('Impact_Input',col+str(r)),x)
  totals[(v('Impact_Input','B'+str(r)),v('Impact_Input','C'+str(r)),v('Impact_Input','D'+str(r)))]+=welfare
 for opt,start in [('A',7),('B',18)]:
  for u in range(1,8):
   for d,col in enumerate('BCDEFGH',1):check(f'I_prop!{col}{start+u-1}',v('I_prop',col+str(start+u-1)),math.tanh(v('CANON','B20')*totals[(opt,f'U{u}',f'D{d}')]))
 # Reconstruct the active local weights and all three disclosed sensitivity profiles.
 floors=[v('PLSS_Local_Scope','C'+str(r)) for r in range(12,19)];q=[v('PLSS_Local_Scope','B'+str(r)) for r in range(12,19)];res=1-math.fsum(floors)
 geom=[math.prod(v('PLSS_Local_Scope',c+str(r)) for c in 'KLMN')**.25 for r in range(12,19)];broad=[v('PLSS_Local_Scope','P'+str(r)) for r in range(12,19)]
 for i,r in enumerate(range(12,19)):
  check(f'PLSS base E{r}',v('PLSS_Local_Scope','E'+str(r)),floors[i]+res*q[i]/math.fsum(q))
  check(f'PLSS geometric Q{r}',v('PLSS_Local_Scope','Q'+str(r)),floors[i]+res*geom[i]/math.fsum(geom))
  check(f'PLSS uniform R{r}',v('PLSS_Local_Scope','R'+str(r)),floors[i]+res/7)
  check(f'PLSS broadened S{r}',v('PLSS_Local_Scope','S'+str(r)),floors[i]+res*broad[i]/math.fsum(broad))
 weights=[[v('PLSS_Local_Scope','E'+str(12+i))*v('Parameters','B'+str(48+j)) for j in range(7)] for i in range(7)]
 scores={}
 for opt,start,outstart,scorecell,marginrow in [('A',7,9,'B4',16),('B',18,22,'B5',29)]:
  impacts=[[v('I_prop',col+str(start+i)) for col in 'BCDEFGH'] for i in range(7)];c=contributions(impacts,weights);scores[opt]=c.score
  check('Contribution mass',v('Contribution_Analysis','B3'),c.mass)
  check('RLS '+opt,v('Contribution_Analysis',scorecell),c.score)
  check('Frozen RLS '+opt,v('RLS','B5' if opt=='A' else 'B6'),c.score)
  for i in range(7):
   for j,col in enumerate('BCDEFGH'):check(f'Contribution {opt} {i},{j}',v('Contribution_Analysis',col+str(outstart+i)),c.cells[i][j])
   check(f'Scope margin {opt} {i}',v('Contribution_Analysis','I'+str(outstart+i)),c.by_scope[i])
  for j,col in enumerate('BCDEFGH'):check(f'Dimension margin {opt} {j}',v('Contribution_Analysis',col+str(marginrow)),c.by_dimension[j])
  check(f'Positive/negative identity {opt}',c.positive+c.negative,c.score)
 for opt,start,dest in [('A',8,'B25'),('B',19,'B41')]:
  losses=[v('TRC','L'+str(r)) for r in range(start,start+7)];p=[v('TRC','K'+str(r)) for r in range(start,start+7)]
  check('CVaR '+opt,v('TRC',dest),tail_cvar(losses,p,v('TRC','B7')))
 # Independent populated-cell count for every whole-column edit detector.
 for addr,cell in m['Build_Integrity'].items():
  f=cell.get('formula') or '';match=re.fullmatch(r"ABS\(COUNTA\('([^']+)'!([A-Z]+):([A-Z]+)\)-(\d+)\)",f)
  if match:
   sn,lo,hi,target=match.groups()
   def num(col):
    n=0
    for x in col:n=n*26+ord(x)-64
    return n
   count=sum((c['formula'] is not None or c['type']!='blank') and num(lo)<=num(re.match('[A-Z]+',a).group())<=num(hi) for a,c in m[sn].items())
   check('Full-column counter '+addr,v('Build_Integrity',addr),abs(count-int(target)))
 # Check all subgroup lookup outputs against original option/scope/dimension records.
 for rr in range(2,72):
  u,d=v('Rights_Coverage_View','C'+str(rr)),v('Rights_Coverage_View','D'+str(rr))
  for opt,lookup,raw,dest,num,key in [('A','J','F','H','M','O'),('B','K','G','I','N','P')]:
   matches=[]
   for row in range(11,101):
    def ov(col):return m['Subgroup_Overrides'].get(col+str(row),{}).get('value')
    if [ov('B'),ov('D'),ov('E')]==[opt,u,d]:matches.append((ov('F'),ov('G')))
   if not matches:expected=''
   elif len(matches)!=1:expected='INVALID_OVERRIDE'
   else:
    x,source=matches[0]
    expected=x if isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x) and -1<=x<=1 and isinstance(source,str) and source.strip() else 'INVALID_OVERRIDE'
   check('Raw override '+opt+str(rr),v('Rights_Coverage_View',lookup+str(rr)),expected)
   direct=v('Rights_Coverage_View',raw+str(rr))
   worst=expected if isinstance(expected,(int,float)) else ('INVALID_OVERRIDE' if expected=='INVALID_OVERRIDE' else max(-1,v('Subgroup_Overrides','B7')*direct) if direct<0 else direct)
   check('Worst subgroup '+opt+str(rr),v('Rights_Coverage_View',dest+str(rr)),worst)
   numeric=worst if isinstance(worst,(int,float)) else ''
   check('Numeric subgroup '+opt+str(rr),v('Rights_Coverage_View',num+str(rr)),numeric)
   signature=v('Rights_Coverage_View','B'+str(rr))+'|'+str(round(worst*1e12)) if isinstance(worst,(int,float)) else ''
   check('Subgroup join '+opt+str(rr),v('Rights_Coverage_View',key+str(rr)),signature)
 result={'executed':len(tests),'passed':sum(t['passed'] for t in tests),'scores':scores,'scope':'Independent input, saturation, PLSS, contribution, CVaR and column-count checks of the frozen example; no evidence calibration or general spreadsheet-engine parity.','tests':tests}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':main()
