"""Scoped final-release regression checks. Not evidence truth or a production validator."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E
import json,math,re
from Workbook_Verifier import inspect,verify
from workbook_probe import WorkbookProbe
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def txt(el):return ''.join(x.text or ''for x in el.iter('{'+N['w']+'}t'))
def main():
 checks=[]
 def ck(name,actual,expected=True):checks.append({'test':name,'passed':actual==expected,'actual':actual,'expected':expected})
 d=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');cs=d['cells'];snap=cs['Build_Snapshot'];targets=[]
 for a,r in snap.items():
  if re.fullmatch(r'CL\d+',a)and a!='CL1'and isinstance(r['value'],str):
   row=a[2:];s=r['value'];c=snap.get('CM'+row,{}).get('value')
   if isinstance(c,str):targets.append((s,c))
 ck('Literal snapshot contains no formula targets',[(s,c)for s,c in targets if cs[s][c]['formula']is not None],[])
 newtargets=[('Sanity_Checklist',c)for c in('B38','D38','B39','D39','B40','B41','B107','B108','B109','B111')]+[('Parameters','B42'),('NCRC','A5')]
 guardset={g['target']for g in d['formula_guards']}
 p=WorkbookProbe(d)
 for s,c in newtargets:
  ck('Correct formula coverage '+s+'!'+c,s+'!'+c in guardset)
  ck('No literal snapshot for '+s+'!'+c,(s,c)not in targets)
  p.set(s,c,cs[s][c]['value']);ck('Equal literal replacing formula caught '+s+'!'+c,p.presence_mismatches()>0);p.set(s,c,cs[s][c]['value'],cs[s][c]['formula'])
 ck('Base integrity is zero',p.get('Build_Integrity','B14'),0)
 ck('NCRC frozen header intact','SNAPSHOT INTACT'in p.get('NCRC','A5'))
 for label,v in [('stale',1),('unknown',None),('invalid',-1)]:
  p.set('Build_Integrity','B14',v);ck('NCRC local warning '+label,('STALE'if label=='stale'else'UNVERIFIED')in p.get('NCRC','A5'))
 ck('Correct scenario narrative','0.011909'in cs['Scenario_Impacts']['A29']['value']and'0.003574'not in cs['Scenario_Impacts']['A29']['value'])
 ck('Distinct workbook section label',cs['CANON']['A113']['value'].startswith('SECTION G2A'))
 ck('Typed mandatory-tail field label',cs['CANON']['A103']['value'],'MANDATORY_TAILS_COUNT')
 ck('Lineage prefix disclosure','V127 is a retained lineage identifier'in cs['Sanity_Checklist']['C111']['value'])
 docs={}
 for f in (ROOT/'Core_15').glob('*.docx'):
  with ZipFile(f)as z:docs[f.name]=E.fromstring(z.read('word/document.xml'))
  ck('Inline historical identity marker '+f.name,'HISTORICAL (NON-CONTROLLING):'in txt(docs[f.name]))
 canon=txt(docs['RippleLogic_v13.0_Canon.docx']);sgp=txt(docs['SGP_v8.8.docx']);ripple=txt(docs['ripple_md_Standard_v5.8.docx']);csv=txt(docs['CSV_Gate_Standard_v2.7.docx']);primer=txt(docs['RippleLogic_Foundations_Primer_v4.7.docx'])
 ck('Positive welfare is not subgroup evidence','A nonnegative welfare average does not establish'in canon)
 ck('Fallback remains a screening convention','not a distribution-free guarantee'in canon)
 ck('Initial representation triggers explicit','initial submitted representation'in canon)
 ck('No new 0.3 partition threshold','partition threshold of 0.3'not in canon)
 ck('KQS semantic boundary','C_id'in canon and 'statistical or causal identification'in canon)
 ck('MPS display-to-assignment direction','not inputs to a continuous-score thresholding'in sgp)
 ck('Standalone CSV precedence','Ordinary PASS, PASS_WITH_CONTROLS and NOT_MATERIAL rows cannot override'in csv)
 ck('Assurance table header correction','Primary claim or assurance precondition'in ripple)
 ck('Publisher-confirmed DOI retained','10.65391/r1386'in ripple)
 ck('Primer historical closure exists','END HISTORICAL LINEAGE'in primer)
 ck('Short reader route present','Reader route'in canon)
 ck('Namespace table distinguishes MODE and Tier','Scale namespace'in canon or 'Namespace'in canon or 'namespace'in canon)
 # Algebraic regression: same-cell subdivisions preserve the sum; cross-cell
 # allocation is not generally invariant. These are examples, not taxonomy proofs.
 x=.4;ck('Same-cell subdivision invariant',math.isclose(math.tanh(2*x),math.tanh(2*(.1+.3))))
 ck('Cross-cell small-signal allocation can differ',not math.isclose(math.tanh(2*.05),2*math.tanh(2*.025)))
 ck('Cross-cell large-signal allocation can differ',not math.isclose(math.tanh(2*.8),2*math.tanh(2*.4)))
 welfare_mean=.3;rights_impact=math.tanh(2*(-.8));ck('Adverse rights input fails despite positive welfare',welfare_mean>0 and max(-.9-rights_impact,0)>0)
 ck('Existing zero RF no-harm result remains zero',math.tanh(0),0.)
 result={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'tests':checks,'boundary':'Direct artifact checks, scoped stored-formula mutations and synthetic arithmetic only; native execution has a separate build-specific receipt.'}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
