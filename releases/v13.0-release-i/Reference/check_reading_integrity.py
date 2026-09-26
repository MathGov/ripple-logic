from component_identity import source_build_id
"""Check current body-text projections, Office containers and local reading links.

Read-only. Text parity is not a visual-layout equivalence certificate. External
URLs are inventory entries, not fetched or treated as successful publications.
"""
from pathlib import Path
from zipfile import ZipFile
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as E
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[1];W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.add(a['id'])
  for k in ('href','src'):
   if k in a:self.links.append(a[k])

def main():
 checks=[]
 def add(name,ok,detail=None):checks.append({'check':name,'passed':bool(ok),'detail':detail})
 m=json.loads((ROOT/'VERSION_MANIFEST.json').read_text());index=json.loads((ROOT/'Publication/Active_Source_Index.json').read_text())
 add('15 current components',len(m['components'])==15)
 add('14 body-text projections',len(index['documents'])==14)
 norm=lambda s:re.sub(r'\s+','',s)
 canonical_matrix=None
 for record in index['documents']:
  p=ROOT/'Core_15'/record['file']
  with ZipFile(p)as z:
   add(p.name+' ZIP CRC',z.testzip()is None)
   root=E.fromstring(z.read('word/document.xml'));body=root.find(W+'body');text=''.join(x.text or ''for x in body.iter(W+'t'))
  source=ROOT/'Sources'/(p.stem+'.txt')
  matrices=[]
  for tb in root.iter(W+'tbl'):
   rows=[[''.join(x.text or ''for x in c.iter(W+'t'))for c in tr.findall(W+'tc')]for tr in tb.findall(W+'tr')]
   if rows and rows[0]==['Component','Current edition']:matrices.append(rows[1:])
  add(p.name+' one current component matrix',len(matrices)==1 and len(matrices[0])==15)
  if matrices:
   if canonical_matrix is None:canonical_matrix=matrices[0]
   add(p.name+' synchronized component matrix',matrices[0]==canonical_matrix)
  add(p.name+' current build identity',source_build_id(ROOT,p,m)in text)
  add(p.name+' source hash',hashlib.sha256(p.read_bytes()).hexdigest()==record['sha256'])
  add(p.name+' complete body text',norm(text)==norm(source.read_text()))
  add(p.name+' PDF present',(ROOT/'Reading_PDFs'/(p.stem+'.pdf')).is_file())
  add(p.name+' HTML present',(ROOT/'Reading_HTML'/(p.stem+'.html')).is_file())
  add(p.name+' historical marker',any(b.get('{'+W[1:]+'name')=='MG_HISTORICAL_RELEASE'for b in root.iter(W+'bookmarkStart')))
 # Cache all IDs before resolving anchors.
 parsed={}
 for path in list((ROOT/'Reading_HTML').glob('*.html'))+list((ROOT/'Publication').glob('*.html'))+list((ROOT/'Reports').glob('Release_[HI]_*.html'))+[ROOT/'index.html',ROOT/'Reference/review_dashboard.html']:
  h=Links();h.feed(path.read_text());parsed[path.resolve()]=h
 for path,h in parsed.items():
  for ref in h.links:
   u=urlsplit(ref)
   if u.scheme or u.netloc:continue
   dst=(path.parent/unquote(u.path)).resolve()if u.path else path
   ok=dst.is_relative_to(ROOT)and dst.is_file()
   if ok and u.fragment and dst in parsed:ok=unquote(u.fragment)in parsed[dst].ids
   add('Local link '+str(path.relative_to(ROOT))+' -> '+ref,ok)
 wb=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx'
 add('Dashboard source hash matches current workbook',hashlib.sha256(wb.read_bytes()).hexdigest()in (ROOT/'Reference/review_dashboard.js').read_text())
 add('Public root excludes raw review/baseline directories',not (ROOT/'Review_Inputs').exists()and not(ROOT/'Baseline').exists()and not(ROOT/'Private_Provenance').exists())
 result={'status':'PASS'if all(c['passed']for c in checks)else'FAIL','executed':len(checks),'passed':sum(c['passed']for c in checks),'failures':[c for c in checks if not c['passed']], 'boundary':'Office container/body-text parity and local link existence; not native spreadsheet parity, visual identity, public upload, or external-registry conformance.'}
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(0 if main()['status']=='PASS'else 1)
