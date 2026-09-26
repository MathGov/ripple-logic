import copy,unittest
from decision_fixture import serialize_fixture,r38a_serialization_fixture,RecordError
class DecisionFixtureTests(unittest.TestCase):
 def f(self):return r38a_serialization_fixture()
 def nondecisive(self):
  f=self.f();f['variants']=[{'A':(.03,.02),'B':(.02,.02),'C':(.01,.04)}];return f
 def test_positive_control_selects(self):
  r=serialize_fixture(self.f());self.assertEqual(r['conditional_framework_verdict'],'ALLOW_FRAMEWORK_SELECTION');self.assertEqual(r['conditional_decision_state'],'SELECTED_DECISIVE');self.assertEqual(r['selected_option'],'A')
 def test_decisive_controls_not_provisional(self):self.assertEqual(serialize_fixture(self.f())['conditional_decision_state'],'SELECTED_DECISIVE')
 def test_no_execution_authority(self):self.assertEqual(serialize_fixture(self.f())['execution_state'],'NOT_AUTHORIZED')
 def test_tie_break_not_decisiveness(self):
  f=self.nondecisive();f['tie_break_preference']='A';r=serialize_fixture(f);self.assertEqual(r['conditional_framework_verdict'],'REFUSE_DETERMINISTIC_SELECTION');self.assertEqual(r['conditional_decision_state'],'REFUSE');self.assertEqual(r['tie_break_preference'],'A')
 def test_authority_can_record_nondecisive_preference(self):
  f=self.nondecisive();f['tie_break_preference']='A';f['authority_selection']={'option':'A','record_id':'synthetic-1','valid_stipulated':True};r=serialize_fixture(f);self.assertEqual(r['conditional_framework_verdict'],'REFUSE_DETERMINISTIC_SELECTION');self.assertEqual(r['conditional_decision_state'],'SELECTED_BY_AUTHORITY_NON_DECISIVE');self.assertEqual(r['execution_state'],'NOT_AUTHORIZED')
 def test_expired_authority_not_adopted(self):
  f=self.nondecisive();f['authority_selection']={'option':'A','record_id':'synthetic-1','valid_stipulated':False};self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_invalid_execution_authority_does_not_reverse_math(self):
  f=self.f();f['authority_selection']={'option':'A','record_id':'expired','valid_stipulated':False};r=serialize_fixture(f);self.assertEqual(r['conditional_decision_state'],'SELECTED_DECISIVE');self.assertEqual(r['execution_state'],'NOT_AUTHORIZED')
 def test_preference_outside_selectable_set_rejected(self):
  f=self.nondecisive();f['options']['C']['rf']='RF_FAIL';f['tie_break_preference']='C'
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_all_fail_not_repaired_by_preference(self):
  f=self.nondecisive();f['tie_break_preference']='A'
  for o in f['options'].values():o['rf']='RF_FAIL'
  self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'NO_SELECTABLE_OPTION')
 def test_missing_controls_exclude_option(self):
  f=self.f();f['options']['A']['controls_complete']=False;r=serialize_fixture(f);self.assertNotEqual(r['selected_option'],'A')
 def test_sole_survivor_no_fabricated_gap(self):
  f=self.f();f['options']['B']['rf']='RF_FAIL';f['options']['C']['rf']='RF_FAIL';r=serialize_fixture(f);self.assertEqual(r['fixture_result'],'SOLE_SURVIVOR_OUTSIDE_THIS_TEST_PROFILE');self.assertIsNone(r['conditional_framework_verdict']);self.assertIsNone(r['conditional_decision_state']);self.assertEqual(r['execution_state'],'NOT_AUTHORIZED')
 def test_missing_required_variants_refuses(self):
  f=self.f();f['required_variants_complete']=False;self.assertEqual(serialize_fixture(f)['conditional_framework_verdict'],'REFUSE_DETERMINISTIC_SELECTION')
 def test_demonstration_uncertainty_refuses(self):
  f=self.f();f['uncertainty_warrant_stipulated']=False;self.assertEqual(serialize_fixture(f)['conditional_framework_verdict'],'REFUSE_DETERMINISTIC_SELECTION')
 def test_sensitive_module_refuses(self):
  f=self.f();f['modules']['fixture.dependence']['state']='SENSITIVE';self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_unresolved_module_refuses(self):
  f=self.f();f['modules']['fixture.dependence']['state']='UNRESOLVED';self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_unexecuted_module_refuses(self):
  f=self.f();f['modules']['fixture.dependence']['state']='REQUIRED_NOT_EVALUATED';self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_missing_module_rejected(self):
  f=self.f();del f['modules']['fixture.dependence']
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_extra_module_rejected(self):
  f=self.f();f['modules']['unknown']={'state':'PASS_NO_REVERSAL','rationale':'x'}
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_unjustified_not_triggered_rejected(self):
  f=self.f();f['modules']['fixture.dependence']={'state':'NOT_TRIGGERED_WITH_RATIONALE','rationale':''}
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_non_synthetic_rejected(self):
  f=self.f();f['synthetic']=False
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_absent_qualification_rejected(self):
  f=self.f();del f['options']['A']['rf']
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_boolean_strings_rejected(self):
  f=self.f();f['required_variants_complete']='true'
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_nonfinite_score_rejected(self):
  f=self.f();f['variants'][0]['A']=(float('nan'),.02)
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_missing_contender_rejected(self):
  f=self.f();del f['variants'][0]['C']
  with self.assertRaises(RecordError):serialize_fixture(f)
 def test_reversed_leader_refuses(self):
  f=self.f();f['variants'][0]['C']=(.5,.003);self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_runner_up_does_not_hide_rival(self):
  f=self.f();f['variants']=[{'A':(.020,.003),'B':(.010,.001),'C':(.005,.008)}];self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
 def test_metadata_relabel_does_not_create_warrant(self):
  f=self.f();f['uncertainty_warrant_stipulated']=False;f['validated']=True;self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'REFUSE')
if __name__=='__main__':unittest.main()
