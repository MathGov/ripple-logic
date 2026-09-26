import unittest,math,json,hashlib,copy,tempfile
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from dependence_sensitivity import signed_gap,review_pair,covariance_valid
from minimum_records import SPECS,validate_record
from Workbook_Verifier import verify
ROOT=Path(__file__).resolve().parents[1]

def fixture(name):
    return {'record_id':'SYNTHETIC-'+name,'record_type':name,'run_id':'SYNTHETIC-NOT-A-REAL-DECISION',
     'configuration_ref':'synthetic-configuration','source_clauses':[SPECS[name]['source']],
     'applicability':{'triggered':True,'rationale':'Synthetic structural fixture'},
     'review_status':'SYNTHETIC_STRUCTURAL_TEST_ONLY',
     'evidence_refs':[{'id':'synthetic-test-input','sha256':hashlib.sha256(b'synthetic-test-input-not-empirical-evidence').hexdigest()}],
     'result':{'evaluated':True,'unresolved':[],'disposition':'Recorded; no authority or real-world validation'},
     'content':{f:{'synthetic':'For testing field presence, not evidence truth'}for f in SPECS[name]['fields']}}

class DependenceTests(unittest.TestCase):
    def test_independence_unchanged(self):self.assertAlmostEqual(signed_gap(.032,0,.01,.01),.032/math.sqrt(.000201),14)
    def test_adverse_negative_reversal(self):
        x=review_pair(.032,0,.01,.01,-1,model_warranted=True)
        self.assertGreater(x['nominal'],2);self.assertLess(x['adverse'],2);self.assertFalse(x['comparison_survives']);self.assertEqual(x['status'],'RLS_DEPENDENCE_SENSITIVE')
    def test_unbounded_means_adverse_not_zero(self):
        self.assertEqual(review_pair(.032,0,.01,.01,None,model_warranted=True)['rho_lower'],-1)
    def test_positive_covariance_cannot_rescue_nominal(self):
        r=review_pair(.02,0,.01,.01,.99,model_warranted=True)
        self.assertGreater(r['adverse'],2);self.assertFalse(r['comparison_survives'])
    def test_unsupported_model_no_selection(self):self.assertFalse(review_pair(1,0,.01,.01,0,model_warranted=False)['comparison_survives'])
    def test_zero_sigma(self):self.assertEqual(signed_gap(.1,0,0,.01,-1),signed_gap(.1,0,0,.01,1))
    def test_zero_both(self):self.assertAlmostEqual(signed_gap(.1,0,0,0),100)
    def test_negative_sigma(self):
        with self.assertRaises(ValueError):signed_gap(0,0,-.01,.01)
    def test_invalid_rho(self):
        with self.assertRaises(ValueError):signed_gap(0,0,.01,.01,-1.1)
    def test_nan(self):
        with self.assertRaises(ValueError):signed_gap(math.nan,0,.01,.01)
    def test_boolean(self):
        with self.assertRaises(ValueError):signed_gap(True,0,.01,.01)
    def test_epsilon_zero(self):
        with self.assertRaises(ValueError):signed_gap(.1,0,.01,.01,epsilon=0)
    def test_valid_covariance(self):self.assertTrue(covariance_valid([[.0001,-.0001],[-.0001,.0001]]))
    def test_impossible_all_pair_minus_one(self):self.assertFalse(covariance_valid([[1,-1,-1],[-1,1,-1],[-1,-1,1]]))
    def test_non_symmetric(self):self.assertFalse(covariance_valid([[1,.1],[.2,1]]))
    def test_zero_variance_nonzero_covariance(self):self.assertFalse(covariance_valid([[0,.1],[.1,1]]))
    def test_negative_variance(self):self.assertFalse(covariance_valid([[-.1]]))
    def test_true_positive_control(self):self.assertTrue(review_pair(.1,0,.01,.01,-1,model_warranted=True)['comparison_survives'])
    def test_confidence_example(self):
        a=math.tanh(2*(.2-.18*.1));b=math.tanh(.2);bound=math.tanh(2*(.2-.18))
        self.assertGreater(a,b);self.assertLess(bound,b);self.assertAlmostEqual(a,.3487324660,10);self.assertAlmostEqual(bound,.0399786803,10)

class RecordTests(unittest.TestCase):
    def test_fifteen_families(self):self.assertEqual(len(SPECS),15)
    def test_all_complete_structures(self):
        for n in SPECS:
            with self.subTest(n=n):self.assertEqual(validate_record(fixture(n)),[])
    def test_every_specific_field_required_when_evaluated(self):
        for n,s in SPECS.items():
            for field in s['fields']:
                with self.subTest(n=n,field=field):
                    r=fixture(n);r['content'].pop(field);self.assertIn('missing content.'+field,validate_record(r))
    def test_missing_config(self):
        r=fixture('GapSensitivityRecord');r.pop('configuration_ref');self.assertTrue(validate_record(r))
    def test_untriggered_needs_rationale(self):
        r=fixture('GapSensitivityRecord');r['applicability']={'triggered':False,'rationale':''};self.assertTrue(validate_record(r))
    def test_untriggered_does_not_need_fabricated_results(self):
        r=fixture('GapSensitivityRecord');r['applicability']['triggered']=False;r['content']={};r['evidence_refs']=[];r['result']={'evaluated':False,'unresolved':[],'disposition':'Not triggered on documented basis'};self.assertEqual(validate_record(r),[])
    def test_unknown_preserved(self):
        r=fixture('GapSensitivityRecord');r['content']={};r['evidence_refs']=[];r['result']={'evaluated':False,'unresolved':['joint uncertainty evidence'],'disposition':'Withhold unique selection'};self.assertEqual(validate_record(r),[])
    def test_unknown_not_empty_reviewed(self):
        r=fixture('GapSensitivityRecord');r['result']={'evaluated':False,'unresolved':[],'disposition':'PASS'};self.assertTrue(validate_record(r))
    def test_invalid_hash(self):
        r=fixture('GapSensitivityRecord');r['evidence_refs'][0]['sha256']='fake';self.assertTrue(validate_record(r))
    def test_unknown_type(self):
        r=fixture('GapSensitivityRecord');r['record_type']='FakeAuthority';self.assertTrue(validate_record(r))

class FormulaIdentityTests(unittest.TestCase):
    def test_equal_value_different_formula_rejected_externally(self):
        source=ROOT/'Core_15/RippleLogic_Aligners_Sheet_v5.9.xlsx'
        with tempfile.TemporaryDirectory()as td:
            target=Path(td)/'mutant.xlsx'
            with ZipFile(source)as z:
                items=z.infolist();parts={i.filename:z.read(i.filename)for i in items}
            S={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
            found=False
            for path,data in parts.items():
                if not path.startswith('xl/worksheets/')or not path.endswith('.xml'):continue
                x=E.fromstring(data)
                f=x.find('.//s:f',S)
                if f is None:continue
                before=f.text;f.text='('+before+')+0';parts[path]=E.tostring(x,encoding='utf-8',xml_declaration=True);found=True;break
            self.assertTrue(found)
            with ZipFile(target,'w',ZIP_DEFLATED)as z:
                for i in items:z.writestr(i,parts[i.filename])
            result=verify(target,ROOT/'Verification/Workbook_Manifest.json')
            self.assertEqual(result['status'],'FAIL');self.assertGreater(result['difference_count'],0)



class JsonSchemaTests(unittest.TestCase):
    def test_schema_valid(self):
        import jsonschema
        s=json.loads((ROOT/'Reference/schemas/pcc_minimum_records.schema.json').read_text());jsonschema.Draft202012Validator.check_schema(s)
    def test_fifteen_schema_examples(self):
        import jsonschema
        s=json.loads((ROOT/'Reference/schemas/pcc_minimum_records.schema.json').read_text());v=jsonschema.Draft202012Validator(s)
        for r in json.loads((ROOT/'Reference/examples/pcc_minimum_records.synthetic.json').read_text()):
            with self.subTest(record=r['record_type']):self.assertEqual(list(v.iter_errors(r)),[])
    def test_schema_missing_pairwise_treatment(self):
        import jsonschema
        s=json.loads((ROOT/'Reference/schemas/pcc_minimum_records.schema.json').read_text());r=fixture('GapSensitivityRecord');r['content'].pop('cross_option_dependence');self.assertTrue(list(jsonschema.Draft202012Validator(s).iter_errors(r)))

if __name__=='__main__':
    unittest.main()
