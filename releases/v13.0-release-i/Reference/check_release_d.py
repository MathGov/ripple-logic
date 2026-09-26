"""Release-D regression checks over actual Core files, not reviewer assertions.

Targets source authority, RMCP mirror fidelity, scoped lint mutations, preserved
unknown/zero distinction and metadata. This is not an empirical validity test.
"""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
import json,re
from Workbook_Verifier import inspect
from workbook_probe import WorkbookProbe
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def text(e):return ''.join(e.xpath('.//w:t/text()',namespaces=N))
def main():
 checks=[]
 def ck(name,condition):checks.append({'test':name,'passed':bool(condition)})
 docs={}
 for p in (ROOT/'Core_15').glob('*.docx'):
  with ZipFile(p)as z:
   ck('OOXML ZIP '+p.name,z.testzip()is None)
   docs[p.name]=E.fromstring(z.read('word/document.xml'))
   app=E.fromstring(z.read('docProps/app.xml'))
   ns='{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}'
   ck('Realistic app metadata '+p.name,int(app.findtext(ns+'Pages','0'))>1 and int(app.findtext(ns+'Words','0'))>100)
 canon=text(docs['RippleLogic_v13.0_Canon.docx']);sgp=text(docs['SGP_v8.8.docx']);primer=text(docs['RippleLogic_Foundations_Primer_v4.7.docx'])
 paras=[text(p)for p in docs['RippleLogic_v13.0_Canon.docx'].xpath('//w:body/w:p',namespaces=N)]
 start=next(i for i,p in enumerate(paras)if p.startswith('0.1 Normative hierarchy'))
 end=next(i for i in range(start+1,len(paras))if paras[i].startswith('0.1A'))
 hier='\n'.join(paras[start:end])
 for key in ['Appendix AQ (Current Canonical','Appendix AX (Normative and Claim-Authority','Appendix AQ-1 (Configuration-Bound','Release-authority scope']:
  ck('Precedence contains '+key,key in hier)
 ck('Hierarchy does not grant metadata semantic override','does not change substantive decision semantics'in hier)
 ck('SGP current bibliography','Sentience Gradient Protocol (SGP) v8.8 [Specification]'in canon)
 ck('SGP v8.5 history retained','Historical lineage: SGP v8.5 [Specification]'in canon)
 ck('SGP current delivered master','Core_15/SGP_v8.8.docx is the controlling SGP prose/table master'in sgp)
 ck('SGP old external source explicitly historical','Historical external-source reference (NON-CONTROLLING for this package): docs/sgp/SGP_v8.6.md'in sgp)
 ck('Remote publication remains separate','this package does not assert that those actions occurred'in sgp)
 ck('Primer ambiguity removed','with the human plateau treated as absolute'not in primer)
 ck('Primer constitutional protection retained','while every human person retains non-downgradable FPP-100 protection'in primer)
 table=next(t for t in docs['SGP_v8.8.docx'].xpath('//w:tbl',namespaces=N)if'Integrated transfer and robustness'in text(t)and'Reality-grounded modelling and correction'in text(t))
 rows=table.xpath('./w:tr',namespaces=N);labels=[]
 for row in rows:
  cells=row.xpath('./w:tc',namespaces=N)
  if cells and re.match(r'^R(?:10|[1-9])\. ',text(cells[0])):labels.append(re.sub(r'^R(?:10|[1-9])\. ','',text(cells[0])))
 ck('Ten controlling RMCP rows',len(labels)==10)
 data=inspect(ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx');cells=data['cells'];rm=cells['SGP_v8_3_RMCP'];p=WorkbookProbe(data)
 for i,label in enumerate(labels,7):ck('RMCP mirror R'+str(i-6),rm['B'+str(i)]['value']==label)
 ck('Current RMCP pins',rm['B26']['value']=='Canon v13.0 / SGP v8.8 / Aligners Sheet v5.9')
 ck('No validator fabricated','no standalone SGP validator'in rm['B25']['value'])
 ck('No-evidence not zero','missing or inadequate evidence = NE'in rm['D7']['value'] and '0 = observed absence/contrary capacity evidence'in rm['D7']['value'])
 ck('Legacy release notes locally historical','HISTORICAL'in cells['Release_Notes']['A1']['value'])
 ck('History pins locally historical','historical snapshot'in cells['v10_7_History']['B2']['value'])
 ck('Separate confidence channel retained','Separate adverse gate-confidence rules'in cells['SGP_Integration']['B24']['value'])
 ck('All frozen formulas retain cached nonerror values',not data['formula_errors'])
 for c in ['C5','C6']:
  ck('Stored lint cache equals executed '+c,p.get('Release_Lint',c)==cells['Release_Lint'][c]['value']=='PASS')
 for address,value,label,lintcell in [('B16','Reflective correction and restraint','old R10 label','C6'),('B7','Legacy R1','other RMCP label','C6'),('B26','Canon v12.6 / SGP v8.5 / Aligners Sheet v5.6','old pins','C5'),('B2','Historical sheet','missing current-use boundary','C6'),('B25','Standalone validator certified','invented validator','C6')]:
  q=WorkbookProbe(data);q.set('SGP_v8_3_RMCP',address,value);ck('Lint rejects '+label,q.get('Release_Lint',lintcell)=='FAIL')
  ck('Integrity rejects changed '+label,q.get('Build_Integrity','B14')>0)
 for row in [2,3,7,16]:
  attrs=next(a for a in data['structure']['SGP_v8_3_RMCP']['row_attributes']if a['r']==str(row))
  ck('Revised RMCP row has readable height '+str(row),float(attrs['ht'])>={2:72,3:60,7:60,16:36}[row])
 result={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'checks':checks,'boundary':'Direct artifact assertions and scoped execution of stored lint/integrity formulas. Native spreadsheet-engine parity, external publication, empirical validity and production authorization are not established.'}
 print(json.dumps(result,ensure_ascii=False,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
