"""Actual-artifact assertions for the final scoped errata pass; not external registry certification."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json
from lxml import etree as E
from component_identity import component_entry
from Workbook_Verifier import inspect,numerical_fingerprint
from full_formula_replay import Evaluator
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def main():
 out=[]
 def ck(name,value):out.append({'check':name,'passed':bool(value)})
 m=json.loads((ROOT/'VERSION_MANIFEST.json').read_text());parent=json.loads((ROOT/'Verification/Final_I/Prior_VERSION_MANIFEST.json').read_text());pr={x['path']:x for x in parent['components']}
 ck('Exact I source identity',m['build_id']=='MG-RL-13.0-20260926-RELEASE-I');ck('Four changed masters only',sum(not x['carried_forward_unchanged']for x in m['components'])==4)
 for c in m['components']:
  ck('Current exact component '+c['path'],component_entry(ROOT,ROOT/c['path'],m)==c);ck('Edition unchanged '+c['path'],c['version']==pr[c['path']]['version'])
  if c['carried_forward_unchanged']:ck('Untouched exact source '+c['path'],c['sha256']==pr[c['path']]['sha256'])
  if c['path'].endswith('.docx'):
   with ZipFile(ROOT/c['path'])as z:r=E.fromstring(z.read('word/document.xml'))
   ck('Internal source ID '+c['path'],c['source_build_id']in ''.join(r.xpath('.//w:t/text()',namespaces=N)))
 w=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');fp=json.loads((ROOT/'Verification/Baseline_Numerical_Fingerprint.json').read_text())
 ck('Every original formula and cache retained',numerical_fingerprint(w)==fp['formula_and_cache_sha256']);ck('Original formula count',w['formula_count']==20212);ck('95 sheets',len(w['sheet_order'])==95)
 edits=json.loads((ROOT/'Verification/Final_I/Exact_Workbook_Changes.json').read_text())
 for e in edits:
  c=w['cells'][e['sheet']][e['cell']];ck('Recorded text patch '+e['sheet']+'!'+e['cell'],c['formula']is None and c['value']==e['after'])
 ev=Evaluator(w);ck('Current integrity record passes',ev.get('Build_Integrity','B14')==0)
 for s,c in [('Sensitivity_Analysis','E13'),('Audit_Flags','F12'),('Audit_Flags','A46'),('Dashboard','I5')]:ck('Retained literal edit detected '+s+'!'+c,ev.clone_with(s,c,'CHANGED').get('Build_Integrity','B14')>0)
 guard=ev.clone_with('RLS','B40','SELECTED_DECISIVE');ck('Disclosed verdict-display exclusion reproduced',guard.get('Build_Integrity','B14')==0)
 result={'status':'PASS'if all(x['passed']for x in out)else'FAIL','executed':len(out),'passed':sum(x['passed']for x in out),'failures':[x for x in out if not x['passed']],'scope':'Source identities, retained formula/cache fingerprint, recorded errata and actual formula-path mutations. Not empirical validation or native application certification.'}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
