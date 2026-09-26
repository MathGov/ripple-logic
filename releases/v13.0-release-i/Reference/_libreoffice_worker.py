#!/usr/bin/python3
import uno,json,math,sys,time,hashlib
from pathlib import Path
from com.sun.star.beans import PropertyValue
W=Path(sys.argv[2]).resolve();R=Path(sys.argv[1]).resolve();src=R/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx';PORT=int(sys.argv[3])
def prop(n,v):p=PropertyValue();p.Name=n;p.Value=v;return p
ctx=uno.getComponentContext();rr=ctx.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver',ctx)
for _ in range(100):
 try:remote=rr.resolve('uno:socket,host=localhost,port='+str(PORT)+';urp;StarOffice.ComponentContext');break
 except Exception:time.sleep(.2)
desk=remote.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop',remote)
import shutil
inputcopy=W/'native_input'/src.name;inputcopy.parent.mkdir(exist_ok=True);shutil.copy2(src,inputcopy)
doc=desk.loadComponentFromURL(uno.systemPathToFileUrl(str(inputcopy)),'_blank',0,(prop('Hidden',True),prop('ReadOnly',False),prop('MacroExecutionMode',4)))
assert doc is not None
checks=[]
def cell(s,a):return doc.Sheets.getByName(s).getCellRangeByName(a)
def obs(s,a):c=cell(s,a);return {'value':c.getValue(),'text':c.getString(),'error':c.getError()}
def recalc():doc.calculateAll()
def check(label,ok,observed):checks.append({'test':label,'status':'PASS'if ok else'FAIL','observed':observed})
def mutate(label,changes,predicate,observe):
 backups=[]
 try:
  for s,a,val,kind in changes:
   c=cell(s,a);backups.append((c,c.getFormula()))
   if kind=='number':c.setValue(val)
   elif kind=='formula':c.setFormula(val)
   else:c.setString(val)
  recalc();o={s+'!'+a:obs(s,a)for s,a in observe};check(label,predicate(o),o)
 finally:
  for c,f in backups:c.setFormula(f)
  recalc()
try:
 doc.enableAutomaticCalculation(True);recalc();recalc()
 check('Unmodified hard recalculation: no false staleness',cell('Build_Integrity','B14').getValue()==0,obs('Build_Integrity','B14'))
 out=W/'native_final'/src.name;out.parent.mkdir(exist_ok=True)
 doc.storeAsURL(uno.systemPathToFileUrl(str(out)),(prop('FilterName','Calc MS Excel 2007 XML'),prop('Overwrite',True)))
 # Every migrated calculation and the new NCRC header must retain a formula.
 for row in range(1805,1817):
  s=cell('Workbook_Formula_Guard','A'+str(row)).getString();a=cell('Workbook_Formula_Guard','B'+str(row)).getString();c=cell(s,a);kind='number'if c.getType().value=='VALUE' or c.getValue()!=0 else'string';v=c.getValue()if kind=='number'else c.getString()
  if a in ('B38','D38','B39','D39','B40','B107','B108','B109','B42'):kind='number';v=c.getValue()
  g='D'+str(row)
  mutate('Formula replaced by equal literal: '+s+'!'+a,[(s,a,v,kind)],lambda o,g=g:o['Workbook_Formula_Guard!'+g]['value']==1 and 'STALE' in o['Build_Integrity!C14']['text'],[('Workbook_Formula_Guard',g),('Build_Integrity','C14')])
 for label,val,kind,expected in [('valid impact edit',.6,'number',None),('missing impact','','string','UNKNOWN_INPUT'),('text impact','bad','string','INVALID_INPUT'),('out-of-range impact',1.5,'number','INVALID_INPUT')]:
  mutate(label,[('Impact_Input','F7',val,kind)],lambda o,expected=expected:('STALE'in o['Build_Integrity!C14']['text'])and(expected is None or o['Impact_Input!V7']['text']==expected),[('Build_Integrity','C14'),('Impact_Input','V7'),('NCRC','A5')])
 for label,val,kind in [('unknown integrity','','string'),('invalid integrity',-1,'number')]:
  mutate(label,[('Build_Integrity','B14',val,kind)],lambda o:'UNVERIFIED'in o['NCRC!A5']['text'],[('NCRC','A5')])
 mutate('Checklist unknown class is not reconciled',[('Sanity_Checklist','G10','UNKNOWN_CLASS','string')],lambda o:o['Sanity_Checklist!B41']['text']=='REVIEW RECORDS',[('Sanity_Checklist','B41')])
 vals=['OVR-07','A','U1-D5','U1','D5',-.70,'Synthetic mutation only']
 mutate('Added adverse subgroup record signals stale frozen rights', [('Subgroup_Overrides',chr(65+i)+'11',v,'number'if isinstance(v,float)else'string')for i,v in enumerate(vals)],lambda o:'STALE'in o['NCRC!A5']['text'] and 'STALE'in o['NCRC!B18']['text'],[('NCRC','A5'),('NCRC','B18'),('Build_Integrity','B28')])
 # Presence is not exact identity; the external manifest must reject this separate case.
 mutate('Different formula retains presence (honest guard boundary)',[('Sanity_Checklist','B38','=95','formula')],lambda o:o['Workbook_Formula_Guard!D1805']['value']==0,[('Workbook_Formula_Guard','D1805')])
 check('Restored workbook has no false staleness',cell('Build_Integrity','B14').getValue()==0,obs('Build_Integrity','B14'))
 result={'status':'PASS'if all(c['status']=='PASS'for c in checks)else'FAIL','engine':sys.argv[4],'execution':'UNO calculateAll; each mutation restored before next case; separate saved test copy','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'tests':checks,'passed':sum(c['status']=='PASS'for c in checks),'total':len(checks),'test_copy':str(out),'boundary':'Native-engine regression checks for these bytes and scenarios, not Microsoft Excel parity, a general editable selector, empirical validation or deployment certification.'}
 (W/'Native_Final_Acceptance.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='tests'},indent=2));print([c for c in checks if c['status']!='PASS'])
finally:doc.close(True)
