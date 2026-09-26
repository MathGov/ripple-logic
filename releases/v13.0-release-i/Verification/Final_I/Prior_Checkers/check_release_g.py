from component_identity import source_build_id
"""Independent current-source assertions for the approved final micro-patch.

Reads actual DOCX/XLSX; exercises the recorded numerical construction and scoped
mutation checks. It does not certify arbitrary implementations or evidence truth.
"""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from fractions import Fraction as F
import hashlib,json,math,re
from Workbook_Verifier import inspect,numerical_fingerprint
from full_formula_replay import Evaluator
from final_patch_checks import crossed_pair,recovery_mode,RECOVERY_CHECKS
from decision_fixture import r38a_serialization_fixture,serialize_fixture
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def text(p):return ''.join(p.xpath('.//w:t/text()',namespaces=N))
def main():
 checks=[]
 def ck(label,value):checks.append({'check':label,'passed':bool(value)})
 docs={}
 for f in(ROOT/'Core_15').glob('*.docx'):
  with ZipFile(f)as z:
   ck('Genuine OOXML '+f.name,z.testzip()is None and '[Content_Types].xml'in z.namelist());docs[f.name]=E.fromstring(z.read('word/document.xml'))
  t=text(docs[f.name]);ck('Same current build '+f.name,source_build_id(ROOT,f)in t)
  ck('Workbook corrected build disclosed '+f.name,'label, runtime-token and integrity-snapshot corrections'in t)
 c=docs['RippleLogic_v13.0_Canon.docx'];a=docs['RippleLogic_Agent_System_v13.0.docx'];ct=text(c);at=text(a)
 cp=[text(p)for p in c.xpath('//w:body//w:p',namespaces=N)];ap=[text(p)for p in a.xpath('//w:body//w:p',namespaces=N)]
 for prefix in['43.1 LLM Backend Unavailable:','43.4 Network Connectivity Loss:']:
  par=next(p for p in ap if p.startswith(prefix))
  ck(prefix+' no automatic prior-mode resume','resume in prior mode'not in par.lower()and'resume when backend returns'not in par.lower())
  ck(prefix+' explicit MODE 0 and operator approval','MODE 0'in par and'operator approval'in par and'Section 8'in par and'Section 23.7'in par)
 ck('Joint scaling under each dependence treatment','Required uncertainty-scale variants SHALL be evaluated within each required dependence treatment'in ct)
 ck('Joint construction excludes incompatible/double-counted sources','Do not double-count the same uncertainty source or combine logically incompatible models'in ct)
 fixture=next(p for p in cp if p.startswith('Synthetic fixture, not empirical calibration:'))
 ck('Cross-option disposition explicit','Cross-option disposition for this fixture is NOT_TRIGGERED_WITH_RATIONALE'in fixture)
 ck('Independent generators explicitly stipulated','stipulated mutually independent'in fixture and'not inferred from marginal intervals'in fixture)
 ck('Changed fixture reopens claim','removing this premise reopens the dependence module'in fixture)
 ck('P.8 reference repaired','Table P-8'not in ct and'The nonzero weighted numerator from Table P-4'in ct)
 ck('P.3 forward confidence included','Î_dir(u,d,a) = τ · ℓ · c_k · μ'in ct)
 ck('P.3 inverse confidence included','μ = atanh(I_prop) / (β_sat · τ · ℓ · c_k)'in ct)
 ck('Zero means exact only in the synthetic vector','Synthetic-zero uncertainty boundary.'in ct and'An empirical zero estimate retains any material'in ct)
 ck('General Method B equation unchanged','σ(u,d,a) = (1 − c(u,d,a)) × A_cell(u,d,a)'in ct)
 ck('Tier and final-weight basis explicit','For Tier 3 HDW runs, where a ballot-derived proposal'in ct and'Evaluate the final proposed weight after the declared HDW combination'in ct)
 ck('No obsolete skipped state','NOT_EVALUATED_AFTER_PRIOR_ELIMINATION'not in ct)
 ck('CSV skipped state used',ct.count('CSV_NOT_EVALUATED_AFTER_PRIOR_FAILURE')>=2)
 ck('P prior failure not double-counted','TRC audit-only'in ct)
 # Full-precision equations independently rebuilt from rational floor constructions.
 w0=list(map(F,['.2','.06','.06','.06','.08','.1','.1']));v0=list(map(F,['.08','.1','.08','.08','.1','.06','.1']))
 w=[x+(1-sum(w0))/7 for x in w0];v=[x+(1-sum(v0))/7 for x in v0]
 start=cp.index('Table P-4. I_prop(u,d,a) for the 33 active cells');vals=[]
 for p in cp[start+1:start+38]:
  m=re.fullmatch(r'U(\d)×D(\d)\s+([+\-]?[0-9.]+)\s+([+\-]?[0-9.]+)\s+([+\-]?[0-9.]+)',p)
  if m:vals.append((int(m[1])-1,int(m[2])-1,float(m[4])))
 ck('P has 33 active rows',len(vals)==33)
 q=sum(w[u]*v[d]for u,d,_ in vals);n=sum(float(w[u]*v[d])*i for u,d,i in vals)
 ck('Exact P Q in source',q==F(20886,30625)and'20886/30625'in ct)
 ck('P normalized result unchanged',math.isclose(n/float(q),.0066483769031887375,abs_tol=1e-15))
 r19=[(0,4,.05),(3,0,.3),(3,4,.12),(4,4,.08),(5,4,.03)]
 sig=math.sqrt(sum((float(w[u]*v[d])*.15*abs(math.atanh(i)/(2*.85)))**2 for u,d,i in r19))
 ck('R19 precise sigma in source','0.000502303633'in ct and math.isclose(sig,.0005023036327425277,abs_tol=1e-15))
 ck('R19 final-digit value repaired','0.017653'not in ct and'0.017652'in ct)
 # Actual workbook surfaces; no cached formula values used for the mutations.
 d=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');cs=d['cells'];ev=Evaluator(d)
 expected={('RLS','A35'):'ΔRLS (raw)',('RLS','F67'):'Nominal demo only; see final verdict',('Config','C22'):'SignedGap > δ in every required comparison',('Audit_Flags','C29'):'RUNTIME_BLOCK',('Audit_Flags','C30'):'RUNTIME_BLOCK',('Audit_Flags','C31'):'RUNTIME_INVALID'}
 for (s,a),v in expected.items():ck(s+'!'+a+' corrected label',cs[s][a]['value']==v)
 ck('Runtime severities not PCC','do not extend the PCC vocabulary'in cs['Audit_Flags']['A39']['value'])
 ck('All 95 sheets preserved',len(d['sheet_order'])==95)
 fp=json.loads((ROOT/'Verification/Baseline_Numerical_Fingerprint.json').read_text())
 ck('All 20212 formulas and their caches unchanged',d['formula_count']==20212 and numerical_fingerprint(d)==fp['formula_and_cache_sha256'])
 ck('Current integrity intact',ev.get('Build_Integrity','B14')==0)
 for (s,a),v in expected.items():
  qev=ev.clone_with(s,a,v+' CHANGED');ck('Changed literal is detected '+s+'!'+a,qev.get('Build_Integrity','B14')>0)
 ck('Original result A',math.isclose(ev.get('RLS','B5'),.0153129427168233,abs_tol=1e-14))
 ck('Original result B',math.isclose(ev.get('RLS','B6'),-.00112238738505248,abs_tol=1e-14))
 for k in RECOVERY_CHECKS:
  m=dict.fromkeys(RECOVERY_CHECKS,True);m[k]=False;ck('Missing '+k+' blocks reentry',recovery_mode(4,m)['permitted_mode_ceiling']==0)
 r=crossed_pair(.06,.03,.004,.004,[1,2],[0,-1],model_warranted=True)
 ck('Joint negative case refuses',not r['comparison_survives'])
 ck('Stipulated positive case still selects',serialize_fixture(r38a_serialization_fixture())['conditional_decision_state']=='SELECTED_DECISIVE')
 out={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'failures':[x for x in checks if not x['passed']],'scope':'Actual artifact assertions, independent finite arithmetic and synthetic predicates; native-engine evidence is separately recorded.'}
 print(json.dumps(out,indent=2));return out
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
