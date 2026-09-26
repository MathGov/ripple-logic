"""Release-I errata regression tests. Synthetic metric tests are not wrapper conformance certification."""
from pathlib import Path
from zipfile import ZipFile
from copy import deepcopy
import json,tempfile,unittest
from lxml import etree as E
from Workbook_Verifier import inspect,verify
from full_formula_replay import Evaluator
ROOT=Path(__file__).resolve().parents[1]
N={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
SN={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
S='{'+SN['s']+'}'

def doc(name):
 with ZipFile(ROOT/'Core_15'/name)as z:return E.fromstring(z.read('word/document.xml'))
def tx(e):return ''.join(e.xpath('.//w:t/text()',namespaces=N))
def reliability_fixture(agreement,kappa,threshold=.60,preregistered=True):
 """I1A's one reliability requirement only; no reconstructability/overall conformance claim."""
 if not preregistered or agreement is None or kappa is None:return 'UNVERIFIED'
 if not 0<=agreement<=1 or not -1<=kappa<=1 or not .60<=threshold<=1:raise ValueError('invalid or below-minimum criterion')
 return 'PASS'if kappa>=threshold else'FAIL'

class FinalErrata(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.path=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx';cls.data=inspect(cls.path)
 def test_print_area_scopes(self):
  with ZipFile(self.path)as z:r=E.fromstring(z.read('xl/workbook.xml'))
  sheets=[x.get('name')for x in r.find('s:sheets',SN)]
  names=r.findall('s:definedNames/s:definedName[@name="_xlnm.Print_Area"]',SN)
  self.assertEqual(len(names),2)
  for n in names:self.assertEqual(sheets[int(n.get('localSheetId'))],n.text.split('!')[0].strip("'"))
 def test_integrity_scope_disclosed(self):
  s=self.data['cells']['Build_Integrity']['A2']['value']
  self.assertIn('not verdict-display replacement',s);self.assertIn('External Workbook_Verifier checks all bytes',s)
 def test_display_mutation_local_scope_is_not_overclaimed(self):
  ev=Evaluator(self.data).clone_with('RLS','B40','SELECTED_DECISIVE')
  self.assertEqual(ev.get('Build_Integrity','B14'),0)
  self.assertEqual(ev.get('RLS','B40'),'SELECTED_DECISIVE')
 def test_display_mutation_rejected_by_external_verifier(self):
  with ZipFile(self.path)as z:parts={n:z.read(n)for n in z.namelist()}
  r=E.fromstring(parts['xl/workbook.xml']);rel={e.get('Id'):e.get('Target')for e in E.fromstring(parts['xl/_rels/workbook.xml.rels'])}
  sn=next(x for x in r.find('s:sheets',SN)if x.get('name')=='RLS');p=rel[sn.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')];p=p.lstrip('/')if p.startswith('/')else'xl/'+p
  sr=E.fromstring(parts[p]);c=sr.find('s:sheetData/s:row/s:c[@r="B40"]',SN)
  for x in list(c):c.remove(x)
  c.set('t','inlineStr');E.SubElement(E.SubElement(c,S+'is'),S+'t').text='SELECTED_DECISIVE';parts[p]=E.tostring(sr)
  with tempfile.TemporaryDirectory()as td:
   target=Path(td)/'mutated.xlsx'
   with ZipFile(target,'w')as z:
    for n,b in parts.items():z.writestr(n,b)
   self.assertEqual(verify(target,ROOT/'Verification/Workbook_Manifest.json')['status'],'FAIL')
 def test_raw_difference_label(self):
  c=self.data['cells']['Sensitivity_Analysis'];self.assertEqual(c['E13']['value'],'ΔRLS (raw)');self.assertEqual(c['E14']['formula'],'B14-C14')
 def test_seven_local_ids_classified_at_emission(self):
  c=self.data['cells']['Audit_Flags']
  for row in [5,12,13,18,27,28,33]:self.assertTrue(c['F'+str(row)]['value'].startswith('TOOL_LOCAL;'))
  self.assertEqual(c['A46']['value'],c['A18']['value'])
  self.assertIn('informative, non-controlling',c['A39']['value'])
 def test_counts_are_not_registry_coverage(self):
  c=self.data['cells']['Dashboard']
  self.assertEqual([c['I'+str(r)]['value']for r in[5,6,7]],['INVALID records by severity','ESCALATE records by severity','REVIEW records by severity'])
  self.assertEqual([c['J'+str(r)]['value']for r in[5,6,7]],[0,2,1])
 def test_primer_selection_boundary(self):
  r=doc('RippleLogic_Foundations_Primer_v4.7.docx');p=next(p for p in r.findall('./w:body/w:p',N)if tx(p).startswith('Selected.'))
  self.assertIn('separate authority selection after a non-decisive result',tx(p));self.assertIn('does not remove framework refusal',tx(p))
 def test_primer_no_construct_validity_claim(self):
  t=tx(doc('RippleLogic_Foundations_Primer_v4.7.docx'));self.assertNotIn('construct-valid split',t);self.assertIn('an explicit separation of constructs',t)
 def test_wrapper_metric_precedence(self):
  t=tx(doc('ripple_md_Standard_v5.8.docx'))
  for s in ['minimum of 0.60','Percent agreement alone does not establish this reliability requirement','90% reconstructability pass-rate requirement is separate','Appendix I1A additionally requires','do not switch estimators after viewing results']:self.assertIn(s,t)
 def test_ordered_agreement_alone_not_acceptance(self):self.assertEqual(reliability_fixture(.92,None),'UNVERIFIED')
 def test_below_existing_kappa_floor_fails(self):self.assertEqual(reliability_fixture(.92,.59),'FAIL')
 def test_at_existing_kappa_floor_passes_this_requirement_only(self):self.assertEqual(reliability_fixture(.92,.60),'PASS')
 def test_stricter_threshold_remains_binding(self):self.assertEqual(reliability_fixture(.99,.70,.75),'FAIL')
 def test_missing_preregistration_unknown(self):self.assertEqual(reliability_fixture(.99,.8,preregistered=False),'UNVERIFIED')
 def test_invalid_threshold_not_laundered(self):
  with self.assertRaises(ValueError):reliability_fixture(.99,.8,.59)
 def test_wdbip_native_table_exact_content(self):
  r=doc('Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.9.docx')
  p=next(p for p in r.findall('./w:body/w:p',N)if tx(p)=='18.2 Primary effect tokens');table=p.getnext();self.assertEqual(table.tag,'{'+N['w']+'}tbl')
  rows=[[tx(c)for c in tr.findall('w:tc',N)]for tr in table.findall('w:tr',N)]
  change=next(x for x in json.loads((ROOT/'Verification/Final_I/Exact_Document_Changes.json').read_text())if x['operation']=='malformed_pipe_paragraph_to_native_table')
  self.assertEqual(rows,change['after_rows']);self.assertEqual(len(rows),12);self.assertTrue(all(len(row)==4 for row in rows))
 def test_unchanged_numerics_current_guard(self):
  ev=Evaluator(self.data)
  self.assertEqual(ev.get('Build_Integrity','B14'),0)
  self.assertAlmostEqual(ev.get('RLS','B5'),.0153129427168233,14);self.assertAlmostEqual(ev.get('RLS','B6'),-.00112238738505248,14)
if __name__=='__main__':unittest.main()
