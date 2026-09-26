#!/usr/bin/env python3
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import shutil, subprocess, sys, tempfile, time, textwrap, os
sys.dont_write_bytecode=True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
WORKBOOK=ROOT/'docs/aligners/RippleLogic_Aligners_Sheet_v5.5.xlsx'
M='http://schemas.openxmlformats.org/spreadsheetml/2006/main'; R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
def fail(m): print('FAIL workbook live recalculation:',m); raise SystemExit(1)
def sheet_map(z):
 wb=ET.fromstring(z.read('xl/workbook.xml')); rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels')); rm={}
 for rel in rels:
  t=rel.attrib['Target']; rm[rel.attrib['Id']]=t.lstrip('/') if t.startswith('/') else str(PurePosixPath('xl')/t)
 return {s.attrib['name']:rm[s.attrib[f'{{{R}}}id']] for s in wb.find(f'{{{M}}}sheets')}
def cell(z,sm,sh,addr):
 r=ET.fromstring(z.read(sm[sh])); c=r.find(f'.//{{{M}}}c[@r="{addr}"]')
 if c is None: fail(f'missing {sh}!{addr}')
 f=c.find(f'{{{M}}}f');v=c.find(f'{{{M}}}v');return (f.text if f is not None else None,v.text if v is not None else None,c.attrib.get('t'))
soffice=shutil.which('libreoffice') or shutil.which('soffice')
if not soffice: fail('LibreOffice required')
with tempfile.TemporaryDirectory(prefix='mathgov_hard_recalc_') as td:
 td=Path(td); src=td/'source.xlsx'; out=td/'recalculated.xlsx'; profile=td/'profile'; shutil.copy2(WORKBOOK,src)
 port='2087'
 server=subprocess.Popen([soffice,'--headless',f'-env:UserInstallation=file://{profile}',f'--accept=socket,host=localhost,port={port};urp;StarOffice.ComponentContext','--norestore','--nodefault','--nofirststartwizard'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 try:
  time.sleep(2)
  script=td/'recalc.py'
  script.write_text(textwrap.dedent(f'''\
import uno,time
from com.sun.star.beans import PropertyValue
ctx0=uno.getComponentContext(); resolver=ctx0.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver",ctx0)
ctx=resolver.resolve("uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
desktop=ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
def p(n,v): x=PropertyValue();x.Name=n;x.Value=v;return x
doc=desktop.loadComponentFromURL(uno.systemPathToFileUrl(r"{src}"),"_blank",0,(p("Hidden",True),p("ReadOnly",False)))
doc.enableAutomaticCalculation(True);doc.calculateAll();time.sleep(0.5)
doc.storeAsURL(uno.systemPathToFileUrl(r"{out}"),(p("FilterName","Calc MS Excel 2007 XML"),p("Overwrite",True)));doc.close(True)
'''))
  cp=subprocess.run(['/usr/bin/python3',str(script)],capture_output=True,text=True,timeout=180)
  if cp.returncode or not out.is_file(): fail(f'hard recalc failed {cp.stdout} {cp.stderr}')
 finally:
  server.terminate();
  try: server.wait(timeout=10)
  except: server.kill()
 with ZipFile(out) as z:
  sm=sheet_map(z); errors=[]
  for sh,t in sm.items():
   r=ET.fromstring(z.read(t))
   for c in r.findall(f'.//{{{M}}}c'):
    f=c.find(f'{{{M}}}f');v=c.find(f'{{{M}}}v');ft=f.text if f is not None and f.text else '';vt=v.text if v is not None and v.text else ''
    if c.attrib.get('t')=='e' or vt.startswith('#') or 'ERR520' in ft.upper(): errors.append((sh,c.attrib.get('r'),ft,vt))
  if errors: fail(f'{len(errors)} errors {errors[:20]}')
  expected={('Containment','K14'):'PASS_ASSUMPTION_BOUND_TIER_2',('Containment','K15'):'UCI_NOT_MATERIAL_DECLARED',('RLS','B40'):'DECISIVE',('RLS','B41'):'A',('CANON','B59'):'YES',('CANON','B70'):'ALLOW_FRAMEWORK_SELECTION',('CANON','B71'):'A',('CANON','B80'):'0',('CANON','B81'):'YES',('Audit_Flags','B21'):'0',('Audit_Flags','B22'):'0',('Audit_Flags','B23'):'0',('Audit_Flags','B24'):'0',('Sanity_Checklist','E15'):'PASS',('Sanity_Checklist','E16'):'PASS',('Sanity_Checklist','E27'):'PASS',('Sanity_Checklist','E28'):'DISCLOSED_ASSERTION',('Sanity_Checklist','B38'):'89',('Sanity_Checklist','B39'):'44',('Sanity_Checklist','B40'):'0',('Sanity_Checklist','B41'):'COMPLETE_WITH_DISCLOSED_ASSERTIONS',('Sanity_Checklist','B107'):'42',('Sanity_Checklist','B108'):'2',('Sanity_Checklist','B109'):'45',('Sanity_Checklist','B110'):'0',('Sanity_Checklist','B111'):'PASS',('Dashboard','J2'):'PUBLISHABLE_AS_BOUNDED_WORKED_EXEMPLAR',('Dashboard','J3'):'YES',('Dashboard','J5'):'0',('Dashboard','J6'):'0',('Dashboard','J7'):'0',('Dashboard','J8'):'0'}
  for k,v in expected.items():
   got=cell(z,sm,*k)[1]
   if got!=v: fail(f'{k} expected {v!r} got {got!r}')
  # Independently enumerate populated SC rows rather than trusting summary formulas.
  shared=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   sr=ET.fromstring(z.read('xl/sharedStrings.xml'))
   for si in sr.findall(f'{{{M}}}si'):
    shared.append(''.join((t.text or '') for t in si.iter(f'{{{M}}}t')))
  sanity=ET.fromstring(z.read(sm['Sanity_Checklist']))
  def decoded(addr):
   c=sanity.find(f'.//{{{M}}}c[@r="{addr}"]')
   if c is None: return ''
   v=c.find(f'{{{M}}}v')
   if v is None: return ''
   return shared[int(v.text)] if c.attrib.get('t')=='s' else (v.text or '')
  rows=[]
  for r in range(6,105):
   a,e,g=decoded(f'A{r}'),decoded(f'E{r}'),decoded(f'G{r}')
   if a.startswith('SC-'): rows.append((a,e,g))
  counts={
   'total':len(rows),
   'pass':sum(e=='PASS' for _,e,_ in rows),
   'fail':sum(e=='FAIL' for _,e,_ in rows),
   'live':sum(g=='LIVE_CHECK' for *_,g in rows),
   'recompute':sum(g=='INDEPENDENT_RECOMPUTE' for *_,g in rows),
   'declared':sum(g=='DECLARED_ASSERTION' for *_,g in rows),
   'tautological':sum(g=='TAUTOLOGICAL_PASS' for *_,g in rows)}
  wanted={'total':89,'pass':44,'fail':0,'live':42,'recompute':2,'declared':45,'tautological':0}
  if counts!=wanted: fail(f'independent sanity-row census drift {counts!r} expected {wanted!r}')
  for sh,addr in [('RLS','B39'),('CANON','G12')]:
   got=float(cell(z,sm,sh,addr)[1]);
   if not 3.5654<got<3.5657: fail(f'{sh}!{addr} gap drift {got}')
print('PASS workbook hard LibreOffice recalculation: zero errors, canonical decisiveness, zero active flags, and publishability surfaces synchronized')
