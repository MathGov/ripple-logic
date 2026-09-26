from component_identity import source_build_id
"""Verify targeted Release-F corrections and reproducible evidence boundaries.
No full canonical-registry or external deployment conformance is asserted.
"""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import hashlib,json,re
from Workbook_Verifier import inspect,numerical_fingerprint
from full_formula_replay import Evaluator
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def tx(e):return ''.join(e.xpath('.//w:t/text()',namespaces=N))
def main():
 checks=[]
 def ck(n,v):checks.append({'check':n,'passed':bool(v)})
 docs={}
 build=json.loads((ROOT/'VERSION_MANIFEST.json').read_text())['build_id']
 for p in (ROOT/'Core_15').glob('*.docx'):
  with ZipFile(p)as z:
   ck('Genuine OOXML '+p.name,z.testzip() is None and '[Content_Types].xml'in z.namelist())
   docs[p.name]=E.fromstring(z.read('word/document.xml'))
  ck('Current identity '+p.name,source_build_id(ROOT,p) in tx(docs[p.name]))
  ck('Bounded engine claim '+p.name, ('rejected compatibility experiment' in tx(docs[p.name])) or ('Prior-build receipts do not certify changed bytes' in tx(docs[p.name])))
 c=docs['RippleLogic_v13.0_Canon.docx'];sg=docs['SGP_v8.8.docx'];pr=docs['RippleLogic_Foundations_Primer_v4.7.docx'];wd=docs['Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.9.docx'];ag=docs['RippleLogic_Agent_System_v13.0.docx'];mf=docs['Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.6.docx'];rp=docs['ripple_md_Standard_v5.8.docx']
 cp=[tx(p)for p in c.xpath('//w:body/w:p',namespaces=N)];sp=[tx(p)for p in sg.xpath('//w:body/w:p',namespaces=N)]
 for key in ['B.4 Missing Data','B.10 TRC Loss','SECTION 19: LIMITATIONS','R.20','R.34','R.35','R.36','R.37','R.38A']:
  ck('Canon governing body present '+key,any(x.startswith(key)for x in cp))
 ck('One B.10 equation heading',sum(x.startswith('B.10 ')for x in cp)==1)
 for key in ['Appendix G: Responsible Sentience Research Protocol','Appendix I: Interface Conformance Test Vectors','Appendix J: References']:
  ck('SGP appendix actual body '+key,key in sp)
 for key in ['Appendix A: Minimal','Appendix B: Decision','Appendix C: Rights','Appendix D: 7-Test','Appendix E: Drift','Appendix F: Compact','Appendix G: Assurance','Appendix H: Material','Appendix I: Minimum','Appendix J: Registry']:
  body=[p for p in rp.xpath('//w:body/w:p',namespaces=N)if tx(p).startswith(key) and p.xpath('./w:pPr/w:outlineLvl',namespaces=N)]
  ck('ripple.md appendix heading '+key,bool(body))
 pt=tx(pr);wt=tx(wd);at=tx(ag);mt=tx(mf);ct=tx(c)
 for key in ['Define and Reality-Ground the decision','floor, categorical-prohibition and severe-hazard','Apply CSV: Containment and Structural Viability','ex-ante locked union','14.1 Specified now']:
  ck('Primer correction '+key,key in pt)
 ck('Stale Primer cascade gone','The cascade architecture is specified: rights floors first'not in pt)
 pp=[tx(p)for p in pr.xpath('//w:body/w:p',namespaces=N)]
 ck('Primer lineage relocated',pp.index('Version 4.3 (Informative lineage; not the current release)')>pp.index('Preserved Baseline Release Material (Historical; Non-Controlling)'))
 ck('No categorical controller assignment','the data controller is the Human Operator'not in at)
 ck('Official role guidance bound','EDPB Guidelines 07/2020, v2.1'in at and 'controllerprocessor_final_en.pdf'in at)
 ck('MFDI field reuse explicit','Reuses the general falsification_or_revision_trigger field'in mt)
 ck('Allocation no parent duplication','Do not add the parent’s full value again to the allocated entries'in wt)
 ck('No fabricated 1.8 final','not a claim of a separately published v1.8 final'in wt)
 ck('Current history change classes','No new machine schema or proven v1_7 parity'in wt)
 ck('WDBIP external compatibility explicit','field-by-field and rule-by-rule compatibility record against v1.9'in wt)
 for key in ['schemas/mathgov_run_record_v4_1.schema.json','docs/implementation/NORMATIVE_KERNEL_INDEX_v1.1.yaml','release/VALIDATE_MATHGOV_RUN.py','CANONICAL_STATE_REGISTRY_v1.1.yaml','STATE_TRANSITION_MATRIX_v1.1.json']:
  ck('Canon exact external pointer '+key,key in ct)
 for key in ['b_tail','X_{u,j}','s_RLS, s_UCI','I_RF(u,d,a|g,r)']:ck('Existing symbol exposed '+key,key in ct)
 ck('Upstream identifier retained without live claim','Retained upstream repository identifier: ripplelogic/ripple-md-standard'in tx(rp))
 outline_index={}
 for par in c.xpath('//w:body//w:p',namespaces=N):
  outline_index.setdefault(tx(par),[]).append(par.xpath('./w:pPr/w:outlineLvl/@w:val',namespaces=N))
 restored=json.loads((ROOT/'Verification/Uploaded_Canon_Outline_Recovery.json').read_text())
 for item in restored:
  roles=outline_index.get(item['text'],[])
  # Exact headings are stable; duplicate identical heading labels may exist.
  ck('Uploaded heading role '+item['text'],[str(item['outline_level']-1)] in roles)
 data=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');ev=Evaluator(data)
 ck('Original formula text and cached results preserved',numerical_fingerprint(data)==json.loads((ROOT/'Verification/Baseline_Numerical_Fingerprint.json').read_text())['formula_and_cache_sha256'])
 ck('Full current formula count',data['formula_count']==20212)
 for sn,cl in [('RLS','B5'),('RLS','B6'),('Build_Integrity','B14')]:ck('Fresh recursive value '+sn+'!'+cl,ev.get(sn,cl)==data['cells'][sn][cl]['value'])
 # Full dependency evaluation rather than the former limited probe/cache mixture.
 miss=ev.clone_with('Impact_Input','F7',None)
 ck('Missing input propagated',miss.get('Impact_Input','M7')=='UNKNOWN_INPUT')
 ck('Missing input flags integrity',miss.get('Build_Integrity','B14')>0)
 invalid=ev.clone_with('Impact_Input','F7','invalid')
 ck('Invalid input distinguished',invalid.get('Impact_Input','M7')=='INVALID_INPUT')
 # The registry correctly distinguishes formula presence from identity.
 guard=ev.clone_with('Sanity_Checklist','B38',data['cells']['Sanity_Checklist']['B38']['value'])
 ck('Summary formula removed is detected',guard.get('Build_Integrity','B6')>0)
 d=json.loads((ROOT/'Publication/Dependency_Status.json').read_text())
 ck('No invented schema verification',all('VERIFIED'not in x.get('status','') or 'NOT_VERIFIED'in x.get('status','') for x in d['dependencies']))
 result={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'failures':[x for x in checks if not x['passed']],'scope':'Artifact assertions and cache-independent formula-path mutations, not native spreadsheet parity or complete external-registry conformance.'}
 print(json.dumps(result,ensure_ascii=False,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
