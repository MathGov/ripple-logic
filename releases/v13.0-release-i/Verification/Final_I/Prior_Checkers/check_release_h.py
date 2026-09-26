"""Read-only assertions for Release H; supplemental, not a full operational validator."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,math
from component_identity import component_entry
from Workbook_Verifier import inspect,numerical_fingerprint
from feedback_sensitivity import reconstruct
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def main():
 checks=[]
 def ck(n,v):checks.append({'check':n,'passed':bool(v)})
 m=json.loads((ROOT/'VERSION_MANIFEST.json').read_text());ck('Same v13.0',m['framework']=='MathGov/RippleLogic v13.0');ck('Distinct H build',m['build_id']=='MG-RL-13.0-20260926-RELEASE-H');ck('Twelve preserved Core masters',sum(c['carried_forward_unchanged']for c in m['components'])==12)
 for c in m['components']:
  r=component_entry(ROOT,ROOT/c['path'],m);ck('Exact component '+c['path'],r==c)
  if c['carried_forward_unchanged']:ck('Original G source preserved '+c['path'],c['sha256']==c['baseline_sha256']and c['source_build_id']=='MG-RL-13.0-20260923-RELEASE-G')
 for name in ['MATHGOV_3R_1_2_PUBLIC_INTRO_v13.0.docx','RippleLogic_Cascade_Standard_v2.9.docx']:
  with ZipFile(ROOT/'Core_15'/name)as z:r=E.fromstring(z.read('word/document.xml'))
  pars=[''.join(x.xpath('.//w:t/text()',namespaces=N))for x in r.findall('.//w:body/w:p',N)];i=next(i for i,x in enumerate(pars)if x.startswith('Preserved Baseline Release Material'));legacy='docs/reproducibility/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.5.md'
  ck('Historical path outside active instructions '+name,not any(legacy in p for p in pars[:i]));ck('Historical path retained '+name,any(legacy in p for p in pars[i:]));ck('Current v1.7 source retained '+name,any('Core_15/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.7.docx'in p for p in pars[:i]));ck('Current H evidence route '+name,any('Reports/Release_H_Verification.md'in p for p in pars[:i]))
  if name.startswith('MATHGOV_3R'):ck('Public profile-first clarification',any('Read the impact and contribution profiles'in p for p in pars))
 w=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');edits=json.loads((ROOT/'Verification/Final_H/Exact_Workbook_Changes.json').read_text());ck('Eight literal-only corrections',len(edits)==8)
 for e in edits:
  c=w['cells'][e['sheet']][e['cell']];ck('Current literal '+e['sheet']+'!'+e['cell'],c['formula']is None and c['value']==e['after'])
 ck('Full formula/cache fingerprint retained',numerical_fingerprint(w)=='26c17542a44107bb80b4d24bec26c8ad59a55e76be4e05d173a449b155a9ebfb');ck('95 sheets retained',len(w['sheet_order'])==95)
 for rel in ['verify_all.py','Reports/Release_H_Verification.md','Reports/Release_H_Adjudication.md','Publication/Feedback_Clarifications.md','Verification/Workbook_Manifest.json']:ck('Current reference exists '+rel,(ROOT/rel).is_file())
 d=json.loads((ROOT/'Verification/Final_H/Document_Preservation.json').read_text());ck('336 table-preservation records',sum(x['tables_preserved']for x in d)==336 and all(x['table_content_and_format_unchanged']for x in d));ck('Section geometry retained',all(x['section_geometry_unchanged']for x in d))
 a=reconstruct();ck('Nominal arithmetic',math.isclose(a['nominal_gap'],3.56551781265359,abs_tol=1e-12));ck('Double sigma refuses',a['double_sigma_gap']<2);ck('Epsilon zero does not rescue double sigma',a['double_sigma_epsilon_zero_diagnostic']<2)
 result={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'failures':[x for x in checks if not x['passed']],'arithmetic':a,'boundary':'Targeted source/representation checks and diagnostic arithmetic, not native application, empirical or external full-registry validation.'}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
