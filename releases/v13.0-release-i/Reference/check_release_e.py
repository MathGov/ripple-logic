from component_identity import source_build_id
"""Current-artifact assertions for Release E. Not full external conformance."""
from pathlib import Path
from zipfile import ZipFile
from lxml import etree as E
from html.parser import HTMLParser
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1];N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def txt(e):return ''.join(e.xpath('.//w:t/text()',namespaces=N))
def main():
 checks=[]
 def ck(name,ok):checks.append({'check':name,'passed':bool(ok)})
 docs={p.name:E.fromstring(ZipFile(p).read('word/document.xml'))for p in (ROOT/'Core_15').glob('*.docx')}
 c=docs['RippleLogic_v13.0_Canon.docx'];ct=txt(c);rp=docs['ripple_md_Standard_v5.8.docx'];rt=txt(rp)
 for name,x in docs.items():
  text=txt(x)
  ck(name+' synchronized package identity',source_build_id(ROOT,ROOT/'Core_15'/name) in text)
  ck(name+' corrected workbook build disclosed',('Aligners Sheet v5.9 retains its component edition but carries this correction build'in text or ('Aligners Sheet v5.9 keeps its numerical inputs, formulas, cached results and worked verdict'in text and 'Verification/Final_I/Exact_Workbook_Changes.json'in text)))
  starts=x.xpath('//w:bookmarkStart/@w:name',namespaces=N);anchors=x.xpath('//w:hyperlink/@w:anchor',namespaces=N)
  ck(name+' bookmarks resolve',not (set(anchors)-set(starts)))
  ck(name+' no PAGEREF',not any('PAGEREF'in s for s in x.xpath('//w:instrText/text()',namespaces=N)))
 tb=next(t for t in c.xpath('//w:body/w:tbl',namespaces=N)if txt(t).startswith('Token / typeTrigger'))
 for r in json.loads((ROOT/'Reference/token_completion.json').read_text())['entries']:
  ck('Token source completion '+r['token'],r['token']in txt(tb) and r['action']in txt(tb))
 ck('Reason not invented severity','NonDecisiveReason / not a severity'in txt(tb))
 ck('No obsolete F.3 duplicate claim','duplicated verbatim in Appendix H.3'not in ct)
 ck('External conformance boundary explicit','registry-conformant machine interchange remains blocked'in ct)
 ck('H.10 token mirror removed',not any('Key audit tokensRIGHTS_PARTITION_SENSITIVE'in txt(t)for t in c.xpath('//w:tbl',namespaces=N)))
 tb=next(t for t in c.xpath('//w:body/w:tbl',namespaces=N)if txt(t).startswith('Existing record familyMinimum content'))
 for r in json.loads((ROOT/'Reference/record_minimums.json').read_text())['records']:
  ck('Minimum record source '+r['name'],r['name']in txt(tb) and r['meaning']in txt(tb))
 ck('Common minimum binding','A record required by H.10 SHALL provide'in ct)
 ck('No purported new EffectTokenRecord','EffectTokenRecord'not in [r['name']for r in json.loads((ROOT/'Reference/record_minimums.json').read_text())['records']])
 ck('Kernel labels disambiguated','κ_raw'not in ct and 'κ_shrunk'not in ct and 'k_raw'in ct and 'k_shrunk'in ct)
 ck('Alpha meanings explicit','alpha_H/alpha_F/alpha_R/alpha_E'in ct and 'alpha_u in a conserved-allocation'in ct)
 ck('Cross option covariance identity','sigma_a^2+sigma_b^2-2*Cov(error_a,error_b)'in ct)
 ck('Nominal retained','The nominal Gap above is retained.'in ct)
 ck('No positive-covariance rescue','Favorable covariance cannot be used alone to rescue failed nominal'in ct)
 ck('PSD and proxy safeguards','positive semidefinite'in ct and 'Non-statistical interval or heuristic proxies'in ct)
 ck('No global impossible anticorrelation assumption','not a claim that all pairs jointly have correlation -1'in ct)
 repair=json.loads((ROOT/'Verification/Heading_Repairs.json').read_text())
 for item in repair:
  x=docs[item['file']]
  p=next(p for p in x.xpath('//w:body/w:p',namespaces=N)if item['bookmark']in p.xpath('./w:bookmarkStart/@w:name',namespaces=N))
  ck('Outline '+item['file']+' '+item['text'],p.xpath('./w:pPr/w:outlineLvl/@w:val',namespaces=N)==[str(item['outline_level']-1)])
 ck('Run family pin explicit','v4 family, with the v4.1 external schema pin'in rt)
 ck('Workbook current component identity',hashlib.sha256((ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx').read_bytes()).hexdigest()==next(c['sha256']for c in json.loads((ROOT/'VERSION_MANIFEST.json').read_text())['components']if c['path'].endswith('.xlsx')))
 ck('Exact verifier present',(ROOT/'Reference/Workbook_Verifier.py').is_file()and(ROOT/'Verification/Workbook_Manifest.json').is_file())
 html=(ROOT/'Reading_HTML/ripple_md_Standard_v5.8.html').read_text()
 ck('ripple normative sections promoted in projection','>2.15 Qualifying Episode</h2>'in html and '>6.3 Gate 3' in html)
 wd=(ROOT/'Sources/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.9.md').read_text()
 ck('WDBIP literal tuples not raw tags','&lt;S, F, C, X, L, G, U&gt;'in wd)
 ck('No fragmented Markdown bold',all('****'not in p.read_text()for p in(ROOT/'Sources').glob('*.md')))
 result={'status':'PASS'if all(x['passed']for x in checks)else'FAIL','executed':len(checks),'passed':sum(x['passed']for x in checks),'failures':[x for x in checks if not x['passed']],'scope':'Current-artifact assertions and structural/schema/numerical tests; not evidence truth, empirical validation or full external machine conformance.'}
 print(json.dumps(result,ensure_ascii=False,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
