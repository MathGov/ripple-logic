import json,sys,time,hashlib,uno
from pathlib import Path
from com.sun.star.beans import PropertyValue
port=int(sys.argv[1]);src=Path(sys.argv[2]).resolve();cellsfile=Path(sys.argv[3]);out=Path(sys.argv[4])
def p(n,v):x=PropertyValue();x.Name=n;x.Value=v;return x
ctx=uno.getComponentContext();resolver=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
for i in range(100):
 try:r=resolver.resolve(f'uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext');break
 except Exception:time.sleep(.1)
else:raise RuntimeError('Could not connect to Calc')
desk=r.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',r)
doc=desk.loadComponentFromURL(uno.systemPathToFileUrl(str(src)),'_blank',0,(p('Hidden',True),p('ReadOnly',True),p('MacroExecutionMode',uno.getConstantByName('com.sun.star.document.MacroExecMode.NEVER_EXECUTE')),p('UpdateDocMode',uno.getConstantByName('com.sun.star.document.UpdateDocMode.NO_UPDATE'))))
if doc is None:raise RuntimeError('Native saved XLSX did not reopen')
try:
 doc.calculateAll()
 result={};errors=[]
 for sn,addrs in json.loads(cellsfile.read_text()).items():
  sheet=doc.Sheets.getByName(sn);result[sn]={}
  for addr in addrs:
   cell=sheet.getCellRangeByName(addr);v=cell.getDataArray()[0][0];err=cell.getError()
   result[sn][addr]={'value':v,'error':err}
   if err:errors.append([sn,addr,err])
 named={}
 for sn,addr in [('Build_Integrity','B14'),('Build_Integrity','C14'),('Build_Integrity','B6'),('NCRC','A5'),('Sanity_Checklist','B41'),('RLS','B5'),('RLS','B32')]:
  c=doc.Sheets.getByName(sn).getCellRangeByName(addr);named[sn+'!'+addr]={'value':c.getValue(),'text':c.getString(),'error':c.getError()}
 out.write_text(json.dumps({'native_file':str(src),'native_file_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'formula_results':result,'errors':errors,'named':named,'boundary':'Saved Calc XLSX reloaded in a fresh process; read-only, macros disabled, external updates disabled, calculateAll executed.'},indent=2))
 print(json.dumps({'formula_cells':sum(map(len,result.values())),'errors':errors,'named':named},indent=2))
finally:doc.close(True)
