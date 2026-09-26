"""Negative controls: bad static TOC caches or metadata must not pass review."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import tempfile, unittest
from document_navigation import inspect_one,entries,annotation_text
import fitz
ROOT=Path(__file__).resolve().parents[1]
class NavigationRegression(unittest.TestCase):
 def mutate(self,kind):
  source=ROOT/'Core_15/RippleLogic_v13.0_Canon.docx';pdf=ROOT/'Reading_PDFs/RippleLogic_v13.0_Canon.pdf'
  with ZipFile(source)as z:parts={n:z.read(n)for n in z.namelist()}
  x=E.fromstring(parts['word/document.xml']);es=entries(x)
  if kind=='page':es[0]['node'].text='1'
  elif kind=='anchor':
   N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
   h=x.xpath('//w:hyperlink[@w:anchor="mg_toc_001"]',namespaces=N)[0];h.set('{'+N['w']+'}anchor','nonexistent_toc_target')
  else:
   a=E.fromstring(parts['docProps/app.xml']);a.find('{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}Pages').text='1';parts['docProps/app.xml']=E.tostring(a)
  parts['word/document.xml']=E.tostring(x)
  with tempfile.TemporaryDirectory()as td:
   p=Path(td)/source.name
   with ZipFile(p,'w',ZIP_DEFLATED)as z:
    for n,b in parts.items():z.writestr(n,b)
   return inspect_one(p,pdf)
 def test_page_one_regression_is_detected(self):self.assertTrue(any(not t['matched']for t in self.mutate('page')['toc']))
 def test_broken_anchor_is_detected(self):self.assertIn('nonexistent_toc_target',self.mutate('anchor')['broken_anchors'])
 def test_stale_page_metadata_is_detected(self):self.assertFalse(self.mutate('metadata')['page_metadata_matches'])
 def test_stale_rendered_pdf_label_is_detected(self):
  source=ROOT/'Core_15/RippleLogic_v13.0_Canon.docx'
  pdf=ROOT/'Reading_PDFs/RippleLogic_v13.0_Canon.pdf'
  with tempfile.TemporaryDirectory()as td:
   doc=fitz.open(pdf)
   changed=False
   for pg in doc:
    for lk in pg.get_links():
     if lk['kind']==fitz.LINK_GOTO and annotation_text(pg,lk['from'])=='5':
      rect=lk['from'];pg.draw_rect(rect,color=None,fill=(1,1,1),overlay=True)
      pg.insert_text((rect.x0,rect.y1-2),'1',fontsize=10,overlay=True)
      changed=True;break
    if changed:break
   self.assertTrue(changed)
   out=Path(td)/'stale-rendered-label.pdf';doc.save(out);doc.close()
   result=inspect_one(source,out)
   self.assertTrue(any(not t['rendered_label_matches']for t in result['toc']))
if __name__=='__main__':unittest.main()
