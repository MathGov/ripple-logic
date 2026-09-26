"""Read-only checks of the publication changes; not native spreadsheet recalculation."""
from pathlib import Path
import json, math
from Workbook_Verifier import inspect
ROOT=Path(__file__).resolve().parents[1]

def main():
    obj=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');cells=obj['cells'];tests=[]
    def v(s,a):return cells[s][a]['value']
    def check(label,a,b):
        ok=math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12) if type(a) in (float,int) and type(b) in (float,int) else a==b
        tests.append({'check':label,'actual':a,'expected':b,'passed':ok})
    # Reconstruct the adverse-bound instance independently, rather than accepting its cache.
    mu,reach,exposure,t,adjust=[v('Impact_Input',c+'18')for c in ('F','G','H','J','K')]
    tau=min(1,math.log1p(max(t,v('CANON','B27')))/math.log1p(v('CANON','B25')))
    impact=math.tanh(v('CANON','B20')*mu*reach*exposure*tau*adjust)
    loss=.35*max(0,-impact)
    check('S01 adverse-bound impact',v('Scenario_Impacts','H21'),impact)
    for s,a in [('Scenario_Impacts','D21'),('Scenario_Impacts','I21'),('TRC','L19')]:check(s+'!'+a,v(s,a),loss)
    # Full seven-row sorted trace: all fields are a declared frozen example.
    rows=[(v('TRC','J'+str(r)),v('TRC','K'+str(r)),v('TRC','L'+str(r)))for r in range(19,26)]
    ordered=sorted(rows,key=lambda z:z[2],reverse=True);cum=0.;used=0.;tail=1-v('TRC','B7');contrib=0.
    for r,(sid,p,l) in zip(range(31,38),ordered):
        cum+=p;take=max(0.,min(p,tail-used));used+=take;contrib+=take*l
        expected={'B':sid,'C':l,'D':p,'E':cum,'G':take,'H':take*l}
        for col,x in expected.items():check('Sorted trace '+col+str(r),v('TRC',col+str(r)),x)
    check('CVaR unaffected by non-tail correction',v('TRC','B41'),contrib/tail)
    guards=obj['formula_guards']
    check('All protected references still contain formulas',all(g['formula_present']for g in guards),True)
    check('Exact protected formula identity verified externally',all(g['match']for g in guards),True)
    check('Guard caches match XML-derived presence',all(g['presence_cache_matches']for g in guards),True)
    check('No engine-rendered formula strings in internal predicate',all('FORMULATEXT'not in c['formula'] and 'ISFORMULA'in c['formula'] for a,c in cells['Workbook_Formula_Guard'].items()if a.startswith('D')and c['formula']),True)
    check('Snapshot/presence aggregate cache',v('Build_Integrity','B14'),0.)
    check('Guard label does not claim exact identity','not formula identity'in v('Build_Integrity','A6'),True)
    check('Core sheets unchanged in number',len(obj['sheet_order']),95)
    check('No cached spreadsheet errors',obj['formula_errors'],[])
    result={'status':'PASS'if all(t['passed']for t in tests)else'FAIL','executed':len(tests),'passed':sum(t['passed']for t in tests),'tests':tests,'boundary':'Read-only XML/formula inspection and independent frozen arithmetic; no native Excel/LibreOffice recalculation.'}
    print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
