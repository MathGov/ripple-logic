"""Fault-inject temporary ZIP/XML copies; never modify the delivered workbook.

These tests exercise the external exact-byte/logical verifier and structural
formula guards. They are not Excel recalculation or deployment tests.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import tempfile,json,xml.etree.ElementTree as E,posixpath
from Workbook_Verifier import verify,inspect,S,R
ROOT=Path(__file__).resolve().parents[1]
WORKBOOK=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx'
MANIFEST=ROOT/'Verification/Workbook_Manifest.json'

def main():
 baseline=verify(WORKBOOK,MANIFEST)
 assert baseline['status']=='PASS'
 with ZipFile(WORKBOOK) as z:original={n:z.read(n) for n in z.namelist()}
 rel={r.attrib['Id']:r.attrib['Target'] for r in E.fromstring(original['xl/_rels/workbook.xml.rels'])}
 sm={n.attrib['name']:('xl/'+rel[n.attrib[R+'id']]).replace('xl//','') for n in E.fromstring(original['xl/workbook.xml']).find(S+'sheets')}
 for k,t in list(sm.items()):
  if not t.startswith('xl/'):sm[k]=posixpath.normpath(t)
 def patch_cell(b,sn,addr,fn):
  root=E.fromstring(b[sm[sn]]);c=root.find('.//'+S+'c[@r="'+addr+'"]');assert c is not None;fn(c);b[sm[sn]]=E.tostring(root)
 def set_v(c,v):
  q=c.find(S+'v')
  if q is None:q=E.SubElement(c,S+'v')
  q.text=str(v)
 def remove_f(c):
  q=c.find(S+'f');assert q is not None;c.remove(q)
 def change_f(c):
  q=c.find(S+'f');assert q is not None;q.text='0'
 def new_cell(b):
  root=E.fromstring(b[sm['I_prop']]);sd=root.find(S+'sheetData');row=E.SubElement(sd,S+'row',{'r':'1000'});c=E.SubElement(row,S+'c',{'r':'A1000'});set_v(c,999);b[sm['I_prop']]=E.tostring(root)
 def new_subgroup(b):
  root=E.fromstring(b[sm['Subgroup_Overrides']]);sd=root.find(S+'sheetData');row=E.SubElement(sd,S+'row',{'r':'1000'});c=E.SubElement(row,S+'c',{'r':'A1000'});set_v(c,1);b[sm['Subgroup_Overrides']]=E.tostring(root)
 def style_mut(c):c.set('s','0')
 cases=[
 ('literal_severity_change',lambda b:patch_cell(b,'Impact_Input','F7',lambda c:set_v(c,.5)),False),
 ('literal_sign_flip',lambda b:patch_cell(b,'Impact_Input','F7',lambda c:set_v(c,.3)),False),
 ('missing_required_input',lambda b:patch_cell(b,'Impact_Input','F7',lambda c:c.remove(c.find(S+'v'))),False),
 ('paste_value_over_formula',lambda b:patch_cell(b,'Impact_Input','N7',remove_f),True),
 ('zero_replaces_formula',lambda b:patch_cell(b,'Impact_Input','N7',change_f),True),
 ('contribution_formula_overwrite',lambda b:patch_cell(b,'Contribution_Analysis','F9',change_f),True),
 ('stale_formula_cache',lambda b:patch_cell(b,'Contribution_Analysis','F9',lambda c:set_v(c,0)),False),
 ('guard_cache_tamper',lambda b:patch_cell(b,'Workbook_Formula_Guard','D2',lambda c:set_v(c,1)),True),
 ('original_style_tamper',lambda b:patch_cell(b,'Impact_Input','F7',style_mut),False),
 ('new_cell_outside_original_range',new_cell,False),
 ('new_subgroup_far_below_original',new_subgroup,True),
 ('removed_sheet_part',lambda b:b.pop(sm['Impact_Input']),False),
 ]
 results=[]
 with tempfile.TemporaryDirectory() as td:
  for name,mutate,require_guard in cases:
   b=original.copy();mutate(b);p=Path(td)/(name+'.xlsx')
   with ZipFile(p,'w',ZIP_DEFLATED) as z:
    for k,v in b.items():z.writestr(k,v)
   try:r=verify(p,MANIFEST)
   except (KeyError,ValueError) as e:r={'status':'FAIL','error':str(e),'protected_formula_failures':1 if require_guard else 0}
   assert r['status']=='FAIL',name
   if require_guard:assert r['protected_formula_failures']>0,(name,r)
   results.append({'test':name,'expected':'FAIL','observed':r['status'],'guard_failure_count':r.get('protected_formula_failures'),'passed':True})
 output={'baseline_status':baseline['status'],'executed':len(results),'passed':sum(r['passed'] for r in results),'scope':'External frozen-file and structural formula/cache identity; temporary fault-injection fixtures; not Excel-engine recalculation.','tests':results}
 print(json.dumps(output,indent=2));return output
if __name__=='__main__':main()
