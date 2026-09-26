from component_identity import source_build_id
"""Read-only checks of this final correction set, including stored formula paths.

These verify document requirements and a bounded XLSX formula subset, not the
truth of operational evidence, a production agent, or native spreadsheet parity.
"""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E
import json,re,math
from collections import Counter
from Workbook_Verifier import inspect
from workbook_probe import WorkbookProbe
from final_review_checks import MODE4_CATEGORIES
ROOT=Path(__file__).resolve().parents[1];NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def text(el):return ''.join(x.text or ''for x in el.iter('{'+NS['w']+'}t'))
def main():
 tests=[]
 def check(name,actual,expected=True):
  ok=math.isclose(actual,expected,rel_tol=1e-12,abs_tol=1e-12)if type(actual)in(int,float)and type(expected)in(int,float)else actual==expected
  tests.append({'check':name,'actual':actual,'expected':expected,'passed':ok})
 docs={}
 for p in sorted((ROOT/'Core_15').glob('*.docx')):
  with ZipFile(p)as z:
   check(p.name+' OOXML CRC',z.testzip(),None);r=E.fromstring(z.read('word/document.xml'))
  docs[p.name]=r;check(p.name+' final build identity',source_build_id(ROOT,p) in text(r))
 agent=docs['RippleLogic_Agent_System_v13.0.docx'];at=text(agent)
 check('Removed unsupported Agent cross-check','+0.01539'not in at)
 check('Primary and conservative Agent figures preserved','+0.01492'in at and '+0.01416'in at)
 check('Privacy no infeasibility guarantee','does not guarantee anonymity'in at)
 check('Current export name','RL_Teacher_Package_v13.0_EXPORT_[DATE].zip'in at)
 tables=agent.findall('.//w:tbl',NS)
 mode4=[t for t in tables if 'MODE 4 (ACT)'in text(t)and 'Read: Public data'in text(t)]
 check('Exactly one MODE 4 supplement',len(mode4),1)
 if mode4:
  cats=[text(row.findall('w:tc',NS)[0])for row in mode4[0].findall('w:tr',NS)[1:]]
  check('MODE 4 categories match the executable fixture',cats,list(MODE4_CATEGORIES))
 paragraphs=[text(p)for p in agent.findall('w:body/w:p',NS)]
 h56=next(i for i,x in enumerate(paragraphs)if x.startswith('Section 56:'));h66=next(i for i,x in enumerate(paragraphs)if x.startswith('Section 66:'));h67=next(i for i,x in enumerate(paragraphs)if x.startswith('Section 67:'))
 check('Stable late-section IDs ordered 56 < 66 < 67',h56<h66<h67)
 sgp=text(docs['SGP_v8.8.docx'])
 check('SGP covers loss of evidence without fabricated improvement','recoding'in sgp and 'NE'in sgp and 'matched'in sgp.lower())
 check('No new canonical NE-substitution token','NE_SUBSTITUTION_INFLATION'not in sgp)
 check('SGP existing misuse signature retained','PERFORMANCE_LAUNDERING'in sgp)
 canon=text(docs['RippleLogic_v13.0_Canon.docx'])
 check('Method B explicit computability precondition','Computability precondition.'in canon)
 check('Method B no convenient net-total reconstruction','A net multi-instance cell total MUST NOT substitute'in canon)
 check('Method substitution not result-selected','MUST NOT be chosen merely to obtain a preferred result'in canon)
 check('QUICK NONE distinction retained','mode/saturation sensitivity'in canon or 'mode and saturation sensitivity'in canon)
 check('No replacement latent QUICK equation','tanh(z_dir + K'in canon,False)
 check('D6 rights non-exemption','D6'in canon and 'not an exemption from rights review'in canon)
 ripple=text(docs['ripple_md_Standard_v5.8.docx'])
 check('Wrapper cannot make nonselectable options ordinary candidates','does not convert'in ripple and 'Canon-nonselectable'in ripple)
 check('Superseded planning percentages carry inline warning',ripple.count('SUPERSEDED; do not apply')>=3 or ripple.count('SUPERSEDED — do not apply')>=3)
 obj=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');cells=obj['cells'];sc=cells['Sanity_Checklist']
 rows=sorted(int(a[1:])for a,x in sc.items()if re.fullmatch(r'A\d+',a)and isinstance(x['value'],str)and re.fullmatch(r'(SC-\d+|V127-\d+)',x['value']))
 ids=[sc['A'+str(i)]['value']for i in rows];classes=Counter(sc['G'+str(i)]['value']for i in rows);statuses=Counter(sc['E'+str(i)]['value']for i in rows)
 check('Unique checklist record IDs',len(ids),len(set(ids)))
 check('Checklist total record count',len(rows),95)
 check('Checklist classes',dict(classes),{'RECORDED_CHECK':47,'RECORDED_RECOMPUTATION':2,'DECLARED_ASSERTION':46})
 check('Checklist recorded outcomes',dict(statuses),{'RECORDED_PASS':49,'DISCLOSED_ASSERTION':46})
 p=WorkbookProbe(obj)
 for c,e in {'B38':95,'B39':49,'B40':0,'D38':0,'D39':0,'B107':47,'B108':2,'B109':46,'B111':'RECONCILED','B41':'RECONCILED RECORDS; NOT TESTS'}.items():
  value=p.get('Sanity_Checklist',c);check('Stored summary '+c,value,e);check('Cache agrees '+c,sc[c]['value'],value)
 check('Seven-scope weight display',p.get('Parameters','B42'),1.)
 check('Workbook integrity baseline',p.get('Build_Integrity','B14'),0.)
 check('Workbook formula errors',obj['formula_errors'],[])
 check('All exact guard expressions agree',all(g['match']for g in obj['formula_guards']))
 check('Retained tautology caveat',any(x['value']=='NOT INDEPENDENTLY AUDITED'for x in sc.values()))
 cases=[('wrong_total','B38',89),('unknown_class','G6','OTHER'),('recorded_failure','E6','RECORDED_FAIL'),('unclassified_pass','E114','PASS'),('missing_roster_id','A113',None)]
 for label,c,v in cases:
  q=WorkbookProbe(obj);q.set('Sanity_Checklist',c,v);check('Summary mutation '+label,q.get('Sanity_Checklist','B41'),'REVIEW RECORDS')
 result={'status':'PASS'if all(t['passed']for t in tests)else'FAIL','executed':len(tests),'passed':sum(t['passed']for t in tests),'tests':tests,'checklist_census':{'records':len(rows),'classes':dict(classes),'outcomes':dict(statuses)},'boundary':'Document/record checks and scoped evaluation of stored formulas, including five summary mutations. Existing unmodified dependency caches are used only where declared in workbook_probe; not native spreadsheet parity or external-registry conformance.'}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
