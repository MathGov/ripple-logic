"""Validate or rebuild generated static TOC labels from actual rendered PDF links.

Does not recreate Word PAGEREF/TOC fields. --write is an explicit authoring action
on a working copy, never used by the read-only release verification suite.
Page labels describe the packaged fixed-layout PDF; another application/font
substitution may repaginate an editable DOCX.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import argparse,json,re,sys
from lxml import etree as E
import fitz
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'; N={'w':W}
ROOT=Path(__file__).resolve().parents[1]
def text(e):return ''.join(e.xpath('.//w:t/text()',namespaces=N))
def norm(s):return re.sub(r'[^\w]','',s).casefold()
def annotation_text(page,rect):
 chars=[]
 for b in page.get_text('rawdict')['blocks']:
  for line in b.get('lines',[]):
   for sp in line['spans']:
    for ch in sp['chars']:
     x0,y0,x1,y1=ch['bbox'];cx=(x0+x1)/2;cy=(y0+y1)/2
     if rect.x0-.3<=cx<=rect.x1+.3 and rect.y0-.3<=cy<=rect.y1+.3:chars.append(ch['c'])
 return ''.join(chars).strip()
def entries(doc):
 out=[]
 for p in doc.xpath('//w:p[w:hyperlink[@w:anchor]]',namespaces=N):
  hs=p.xpath('./w:hyperlink[@w:anchor]',namespaces=N)
  if not hs:continue
  h=hs[0];anchor=h.get('{'+W+'}anchor')
  if not anchor.startswith(('mg_toc_','mg_sgp_toc_','mg_wdbip_')):continue
  ts=p.xpath('.//w:t',namespaces=N)
  if not ts or not (ts[-1].text or '').strip().isdigit():continue
  out.append({'anchor':anchor,'label':text(h),'shown':int(ts[-1].text.strip()),'node':ts[-1]})
 return out

def inspect_one(docx,pdf,write=False):
 with ZipFile(docx)as z:infos=z.infolist();parts={i.filename:z.read(i)for i in infos}
 x=E.fromstring(parts['word/document.xml']);es=entries(x)
 bookmarks=x.xpath('//w:bookmarkStart/@w:name',namespaces=N)
 anchors=x.xpath('//w:hyperlink/@w:anchor',namespaces=N)
 broken=sorted(set(anchors)-set(bookmarks));fields=x.xpath('//w:instrText/text()|//w:fldSimple/@w:instr',namespaces=N)
 pd=fitz.open(pdf);matches=[];changes=[]
 annotations=[]
 for i in range(min(10,len(pd))):
  pg=pd[i]
  for lk in pg.get_links():
   if lk['kind']!=fitz.LINK_GOTO:continue
   if lk.get('page',-1)<0:continue
   s=annotation_text(pg,lk['from'])
   if s and not s.isdigit():annotations.append({'page':i+1,'text':s,'to':lk['page']+1,'point':[round(lk['to'].x,2),round(lk['to'].y,2)],'rect':list(lk['from'])})
 for en in es:
  key=norm(en['label']);found=[a for a in annotations if len(norm(a['text']))>=min(16,len(key))and(norm(a['text'])in key or key in norm(a['text']))]
  if found:
   longest=max(len(norm(a['text']))for a in found)
   found=[a for a in found if len(norm(a['text']))==longest]
  dest={(a['to'],tuple(a['point']))for a in found}
  if len(dest)!=1:raise ValueError((docx.name,en['label'],'ambiguous or absent PDF link',found))
  actual=next(iter(dest))[0];matched=en['shown']==actual
  # Check visible rendered labels, independently of the DOCX text cache.
  # PDF extractors can join a number to the dot leaders and heading into one
  # word, so word-level numeric matching is deliberately not used.
  visible=[]
  for source_page in sorted({a['page']for a in found}):
   pg=pd[source_page-1]
   linked_digits=[]
   for lk in pg.get_links():
    if lk['kind']!=fitz.LINK_GOTO or lk.get('page',-1)<0:continue
    lk_dest=(lk['page']+1,(round(lk['to'].x,2),round(lk['to'].y,2)))
    if lk_dest not in dest:continue
    rendered=annotation_text(pg,lk['from'])
    if rendered.isdigit():linked_digits.append(int(rendered))
   if linked_digits:
    visible.extend(linked_digits)
   else:
    # SGP and WDBIP link the heading, while the page number is ordinary text
    # on the same row. Read complete character lines over that exact row.
    relevant=[a for a in annotations if a['page']==source_page and
              (a['to'],tuple(a['point'])) in dest]
    y0=min(a['rect'][1]for a in relevant);y1=max(a['rect'][3]for a in relevant)
    for block in pg.get_text('rawdict')['blocks']:
     for line in block.get('lines',[]):
      cy=(line['bbox'][1]+line['bbox'][3])/2
      chars=[ch for span in line['spans']for ch in span['chars']]
      line_text=''.join(ch['c']for ch in chars).strip()
      tail=re.search(r'(\d+)$',line_text)
      if y0-.3<=cy<=y1+.3 and line['bbox'][2]>500 and tail:
       visible.append(int(tail.group(1)))
  rendered_match=(len(set(visible))==1 and visible[0]==actual)
  matched=matched and rendered_match
  rec={k:v for k,v in en.items()if k!='node'};rec.update(destination_page=actual,rendered_page_labels=visible,rendered_label_matches=rendered_match,matched=matched,source_pages=sorted({a['page']for a in found}))
  if write and en['shown']!=actual:
   changes.append({'file':docx.name,'anchor':en['anchor'],'label':en['label'],'before':en['shown'],'after':actual,'operation':'static_TOC_page_label_only'})
   en['node'].text=str(actual)
  matches.append(rec)
 if write and changes:
  parts['word/document.xml']=E.tostring(x,encoding='UTF-8',xml_declaration=True,standalone=True)
  with ZipFile(docx,'w',ZIP_DEFLATED)as z:
   for inf in infos:z.writestr(inf,parts[inf.filename])
 app=E.fromstring(parts['docProps/app.xml'])if'docProps/app.xml'in parts else None
 appns='{http://schemas.openxmlformats.org/officeDocument/2006/extended-properties}'
 pages=int(app.findtext(appns+'Pages','0'))if app is not None else 0
 return {'file':docx.name,'pdf_pages':len(pd),'app_pages':pages,'page_metadata_matches':pages==len(pd),'toc_entries':len(es),'toc':matches,'broken_anchors':broken,'pageref_fields':[f for f in fields if'PAGEREF'in f.upper()],'changes':changes,'scope':'DOCX TOC labels and visible rendered PDF labels each checked against actual PDF hyperlink destinations; internal bookmark existence is checked separately. DOCX pagination in untested Word configurations is not certified.'}

def run(root=ROOT,pdf_root=None,write=False):
 pdf_root=pdf_root or root/'Reading_PDFs';out=[]
 for p in sorted((root/'Core_15').glob('*.docx')):
  pdf=pdf_root/(p.stem+'.pdf')
  if not pdf.exists():pdf=pdf_root/p.stem/(p.stem+'.pdf')
  out.append(inspect_one(p,pdf,write))
 okay=all(x['page_metadata_matches'] and not x['broken_anchors'] and not x['pageref_fields'] and all(t['matched']for t in x['toc'])for x in out)
 return {'status':'PASS'if okay else'NEEDS_TOC_REFRESH','documents':out,'toc_entries':sum(x['toc_entries']for x in out),'changes':[c for x in out for c in x['changes']]}
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=ROOT);ap.add_argument('--pdf-root',type=Path);ap.add_argument('--write',action='store_true');ap.add_argument('--output',type=Path);a=ap.parse_args()
 result=run(a.root,a.pdf_root,a.write)
 s=json.dumps(result,ensure_ascii=False,indent=2)
 if a.output:a.output.write_text(s)
 print(json.dumps({'status':result['status'],'toc_entries':result['toc_entries'],'changed':len(result['changes'])}))
 raise SystemExit(0 if a.write or result['status']=='PASS'else 1)
