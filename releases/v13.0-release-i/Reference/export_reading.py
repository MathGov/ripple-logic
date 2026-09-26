"""Rebuild complete read-only Markdown/text/HTML projections from Core DOCX.

The Office masters remain authoritative. This preserves textual block order,
inline emphasis, links and table spans in HTML; it is not a Word layout engine.
Only the explicitly marked terminal historical-release zone is collapsed. Other
origin-stamped active provisions remain visible and are not labelled obsolete.
Uses Python standard-library XML; does not alter any master file.
"""
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E
import hashlib,html,json,re
from urllib.parse import quote

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';N={'w':W}
ROOT=Path(__file__).resolve().parents[1]
def t(e):
 return ''.join((x.text or '')if x.tag=='{'+W+'}t'else'\t'if x.tag=='{'+W+'}tab'else'\n'if x.tag in('{'+W+'}br','{'+W+'}cr')else''for x in e.iter())
def val(e,name,default=None):return e.get('{'+W+'}'+name,default)if e is not None else default
CSS='''body{font:17px/1.6 system-ui,-apple-system,Segoe UI,sans-serif;margin:0;background:#f5f7fa;color:#15293a}main{max-width:1080px;margin:auto;padding:30px 24px 70px;background:white}h1,h2,h3,h4,h5,h6{line-height:1.25;color:#133b53;scroll-margin-top:20px}h1{font-size:2rem;border-bottom:3px solid #167d8d;padding-bottom:12px}h2{font-size:1.55rem;margin-top:2.3em}h3{font-size:1.22rem;margin-top:1.8em}p{margin:.7em 0}a{color:#08677e;overflow-wrap:anywhere}code{font-family:ui-monospace,monospace;font-size:.9em}.notice{padding:15px 18px;background:#edf5f8;border-left:4px solid #167d8d}.table-wrap{overflow-x:auto;margin:1.2em 0;border:1px solid #bccbd4}table{border-collapse:collapse;width:100%;font-size:.91em;line-height:1.45}td,th{border:1px solid #c9d4dc;padding:10px 12px;vertical-align:top;overflow-wrap:anywhere}th{background:#e7f0f5;text-align:left}td p,th p{margin:.35em 0}details{margin:1.8em 0;padding:16px;border:1px solid #afc4d0}summary{cursor:pointer;font-weight:700;color:#17465d}.list-item{padding-left:1.35em;text-indent:-1em}.table-wrap h1,.table-wrap h2,.table-wrap h3{font-size:1.05em}.toc-list{columns:2;column-gap:35px;font-size:.88em}.toc-list a{display:block;margin:4px 0;break-inside:avoid}.meta{font-size:.87em;color:#526573}nav{padding:12px 0}footer{margin-top:40px;padding-top:20px;border-top:1px solid #ccd5dc;font-size:.86em}.bookmark{scroll-margin-top:20px}@media(max-width:700px){main{padding:18px 14px}.toc-list{columns:1}body{font-size:16px}td,th{padding:7px}}@media print{body{background:white}main{padding:0}.notice,nav,.toc-list{display:none}details{display:block}table{font-size:9pt}.table-wrap{overflow:visible}a{color:inherit}}'''

def export_one(path:Path)->dict:
 with ZipFile(path)as z:
  d=E.fromstring(z.read('word/document.xml'));rels={}
  if 'word/_rels/document.xml.rels'in z.namelist():
   rels={x.get('Id'):x.get('Target')for x in E.fromstring(z.read('word/_rels/document.xml.rels'))if x.get('TargetMode')=='External'}
 body=d.find('w:body',N);blocks=[];history=False;heading_entries=[];counter=0
 def inline(e):
  tag=e.tag.rsplit('}',1)[-1]
  if tag=='t':return html.escape(e.text or '')
  if tag in ('tab','br','cr'):return '<br>'if tag!='tab'else ' &emsp; '
  if tag=='bookmarkStart':
   name=val(e,'name','');return '<span class="bookmark" id="'+html.escape(name,quote=True)+'"></span>'if name else ''
  if tag in ('pPr','rPr','bookmarkEnd','sectPr'):return ''
  content=''.join(inline(x)for x in e)
  if tag=='hyperlink':
   anchor=val(e,'anchor');target=('#'+anchor)if anchor else rels.get(e.get('{'+R+'}id'),'')
   if target.startswith(('#','https://','http://','mailto:')):return '<a href="'+html.escape(target,quote=True)+'">'+content+'</a>'
  if tag=='r':
   pr=e.find('w:rPr',N)
   if pr is not None:
    if pr.find('w:b',N)is not None and val(pr.find('w:b',N),'val','1')not in('0','false'):content='<strong>'+content+'</strong>'
    if pr.find('w:i',N)is not None and val(pr.find('w:i',N),'val','1')not in('0','false'):content='<em>'+content+'</em>'
    va=val(pr.find('w:vertAlign',N),'val')
    if va in('superscript','subscript'):content=('<sup>'+content+'</sup>')if va=='superscript'else('<sub>'+content+'</sub>')
  return content
 def paragraph(e):
  nonlocal counter
  counter+=1;txt=t(e);style=val(e.find('w:pPr/w:pStyle',N),'val','');num=e.find('w:pPr/w:numPr',N)
  m=re.fullmatch(r'Heading(\d)',style);level=int(m.group(1))if m else (1 if style=='Title'else 0)
  outline=val(e.find('w:pPr/w:outlineLvl',N),'val')
  if not level and outline is not None and outline.isdigit() and int(outline)<6:level=int(outline)+1
  pid='p-'+str(counter);rec={'kind':'paragraph','id':pid,'style':style,'level':level,'text':txt,'list':num is not None,'historical_release_zone':history,'bookmarks':[val(x,'name')for x in e.findall('w:bookmarkStart',N)]}
  content=inline(e)
  if level:
   heading_entries.append({'id':pid,'level':min(level,6),'text':txt,'historical_release_zone':history})
   frag=f'<h{min(level,6)} id="{pid}">{content}</h{min(level,6)}>'
  else:frag=f'<p id="{pid}"'+(' class="list-item">• 'if num is not None else '>')+content+'</p>'
  return rec,frag
 def table(e):
  rows=[];fragments=[];active={}
  for ri,tr in enumerate(e.findall('w:tr',N)):
   rr=[];cells=[];col=0;ishead=tr.find('w:trPr/w:tblHeader',N)is not None or ri==0
   for tc in tr.findall('w:tc',N):
    span=int(val(tc.find('w:tcPr/w:gridSpan',N),'val','1'));vm=tc.find('w:tcPr/w:vMerge',N);vmerge=val(vm,'val','continue')if vm is not None else None
    cellblocks=[];subhtml=[]
    for child in tc:
     if child.tag=='{'+W+'}p':a,b=paragraph(child);cellblocks.append(a);subhtml.append(b)
     elif child.tag=='{'+W+'}tbl':a,b=table(child);cellblocks.append(a);subhtml.append(b)
    obj={'col':col,'colspan':span,'vmerge':vmerge,'blocks':cellblocks};rr.append(obj)
    if vmerge=='continue'and col in active:
     owner=active[col];owner['rowspan']+=1
     # Continuation cells should be empty; preserve any exceptional text rather than drop it.
     if any(x.get('text','')for x in cellblocks):owner['html']+=''.join(subhtml)
    else:
     owner={'colspan':span,'rowspan':1,'html':''.join(subhtml),'tag':'th'if ishead else'td'};cells.append(owner)
     if vmerge=='restart':active[col]=owner
     else:active.pop(col,None)
    col+=span
   rows.append(rr);fragments.append(cells)
  out=[]
  for cells in fragments:
   out.append('<tr>'+''.join(f'<{c["tag"]} colspan="{c["colspan"]}" rowspan="{c["rowspan"]}">{c["html"]}</{c["tag"]}>'for c in cells)+'</tr>')
  return {'kind':'table','rows':rows,'historical_release_zone':history},'<div class="table-wrap"><table>'+''.join(out)+'</table></div>'
 pieces=[]
 for el in body:
  if el.tag=='{'+W+'}p':
   current=t(el)
   if current.startswith('Preserved Baseline Release Material'):
    history=True;pieces.append('<details class="historical"><summary>Preserved historical release material (non-controlling)</summary>')
   a,b=paragraph(el);blocks.append(a);pieces.append(b)
  elif el.tag=='{'+W+'}tbl':a,b=table(el);blocks.append(a);pieces.append(b)
  elif el.tag=='{'+W+'}bookmarkStart':pieces.append(inline(el))
 if history:pieces.append('</details>')
 def plain(block):
  if block['kind']=='paragraph':return block['text']
  return '\n'.join('\t'.join('\n'.join(plain(b)for b in c['blocks'])for c in row)for row in block['rows'])
 def md(block):
  if block['kind']=='paragraph':
   # Escape literal angle brackets: a DOCX tuple is text, not an HTML tag in Markdown.
   value=block['text'].replace('<','&lt;').replace('>','&gt;')
   return ('#'*block['level']+' 'if block['level']else'- 'if block['list']else'')+value
  # HTML table preserves irregular cell spans; paragraphs have complete text.
  return '<table>\n'+'\n'.join('<tr>'+''.join('<td'+(f' colspan="{c["colspan"]}"'if c['colspan']!=1 else'')+'>'+html.escape('\n'.join(plain(b)for b in c['blocks'])).replace('\n','<br>')+'</td>'for c in row)+'</tr>'for row in block['rows'])+'\n</table>'
 stem=path.stem;sp=ROOT/'Sources';rp=ROOT/'Reading_HTML';sp.mkdir(exist_ok=True);rp.mkdir(exist_ok=True)
 txt='\n\n'.join(plain(b)for b in blocks)+'\n'
 (sp/(stem+'.txt')).write_text(txt,encoding='utf-8')
 mdparts=[];past=False
 for b in blocks:
  if b['historical_release_zone']and not past:mdparts.append('<!-- HISTORICAL_RELEASE_START: non-controlling -->');past=True
  mdparts.append(md(b))
 if past:mdparts.append('<!-- HISTORICAL_RELEASE_END -->')
 (sp/(stem+'.md')).write_text('\n\n'.join(mdparts)+'\n',encoding='utf-8')
 (sp/(stem+'.blocks.json')).write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
 title=next((b['text']for b in blocks if b['kind']=='paragraph'and b['text'].strip()),stem)
 nav=''.join('<a href="#'+x['id']+'">'+html.escape(x['text'])+'</a>'for x in heading_entries if x['level']==1 and not x['historical_release_zone'])
 page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="reading.css"></head><body><main><nav><a href="../index.html">Core reading room</a> · <a href="../Core_15/'+quote(path.name)+'">Word master</a> · <a href="../Reading_PDFs/'+quote(stem+'.pdf')+'">PDF</a></nav><aside class="notice">Complete reading projection of the supplied Word master. Canon/SGP precedence and Appendix RELEASE govern. This page adds navigation, not normative rules. Historical release material is collapsed at the end, not deleted.</aside><details><summary>Navigate principal headings</summary><div class="toc-list">'+nav+'</div></details>'+''.join(pieces)+'<footer>Source: '+html.escape(path.name)+' · SHA-256 '+hashlib.sha256(path.read_bytes()).hexdigest()+'<br>Release identity: see Appendix RELEASE. <a href="../LICENSE">License</a> · <a href="../Publication/Dependency_Status.json">Implementation boundaries</a></footer></main></body></html>'
 (rp/(stem+'.html')).write_text(page,encoding='utf-8')
 # Lossless body-text check, independent of Markdown/HTML styling.
 raw=''.join(el.text or ''for el in body.iter('{'+W+'}t'))
 norm=lambda s:re.sub(r'\s+','',s)
 assert norm(raw)==norm(txt),(path.name,'projection text mismatch')
 return {'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'text_sha256':hashlib.sha256(txt.encode()).hexdigest(),'paragraphs':counter,'top_level_blocks':len(blocks),'headings':heading_entries,'text_parity':True,'scope':'Complete document-body text and table cells; repeating headers/footers and exact pagination remain in DOCX/PDF.'}

def main():
 result=[export_one(p)for p in sorted((ROOT/'Core_15').glob('*.docx'))]
 (ROOT/'Reading_HTML/reading.css').write_text(CSS,encoding='utf-8')
 index={'scope':'Reading index, not a replacement for normative precedence. Historical tags identify the explicitly marked terminal release zone only; active origin-stamped appendices remain current.','documents':result}
 (ROOT/'Publication/Active_Source_Index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding='utf-8')
 (ROOT/'Verification/Source_Projection_Parity.json').write_text(json.dumps({'status':'PASS','documents':len(result),'text_parity':all(x['text_parity']for x in result),'body_text_only':True},indent=2))
 print(json.dumps({'status':'PASS','documents':len(result),'complete_body_text':True}))
if __name__=='__main__':main()
