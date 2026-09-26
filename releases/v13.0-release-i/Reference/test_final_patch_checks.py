import copy,itertools,math,unittest
from final_patch_checks import recovery_mode, crossed_pair, RECOVERY_CHECKS
from decision_fixture import r38a_serialization_fixture,serialize_fixture
from dependence_sensitivity import covariance_valid

class RecoveryTests(unittest.TestCase):
 def full(self):return dict.fromkeys(RECOVERY_CHECKS,True)
 def test_connectivity_alone_cannot_restore(self):self.assertEqual(recovery_mode(4,{'connected':True})['permitted_mode_ceiling'],0)
 def test_no_automatic_authority(self):self.assertFalse(recovery_mode(4,self.full())['execution_authorized'])
 def test_all_conditions_needed(self):
  for k in RECOVERY_CHECKS:
   x=self.full();x[k]=False
   with self.subTest(check=k):self.assertEqual(recovery_mode(4,x)['permitted_mode_ceiling'],0)
 def test_missing_checks_stay_zero(self):
  for k in RECOVERY_CHECKS:
   x=self.full();del x[k]
   with self.subTest(check=k):self.assertEqual(recovery_mode(3,x)['permitted_mode_ceiling'],0)
 def test_valid_reentry_ceiling(self):self.assertEqual(recovery_mode(3,self.full())['permitted_mode_ceiling'],3)
 def test_boolean_strings_rejected(self):
  with self.assertRaises(ValueError):recovery_mode(4,{'operator_approved':'true'})
 def test_invalid_modes_rejected(self):
  for m in[-1,5,True,1.5]:
   with self.subTest(m=m),self.assertRaises(ValueError):recovery_mode(m,self.full())

class JointStressTests(unittest.TestCase):
 def test_one_at_a_time_can_miss_joint_failure(self):
  sigma= crossed_pair(.06,.03,.004,.004,[2],[0],model_warranted=True)
  dep= crossed_pair(.06,.03,.004,.004,[1],[-1],model_warranted=True)
  joint=crossed_pair(.06,.03,.004,.004,[1,2],[0,-1],model_warranted=True)
  self.assertTrue(sigma['comparison_survives']);self.assertTrue(dep['comparison_survives']);self.assertFalse(joint['comparison_survives'])
  self.assertAlmostEqual(min(r['signed_gap']for r in joint['comparisons']),1.871348584655416)
 def test_second_rival_joint_failure(self):
  r=crossed_pair(.06,.02,.004,.006,[2],[-1],model_warranted=True)
  self.assertAlmostEqual(r['comparisons'][0]['signed_gap'],1.9975046777556895);self.assertFalse(r['comparison_survives'])
 def test_nontriggered_synthetic_fixture_still_selects(self):
  f=r38a_serialization_fixture();m=f['modules']['fixture.cross_option']
  self.assertEqual(m['state'],'NOT_TRIGGERED_WITH_RATIONALE');self.assertIn('independent',m['rationale'])
  self.assertEqual(serialize_fixture(f)['conditional_decision_state'],'SELECTED_DECISIVE')
 def test_removed_stipulation_precludes_unique_claim(self):
  f=r38a_serialization_fixture();f['modules']['fixture.cross_option']={'state':'UNRESOLVED','rationale':'Joint construction no longer warranted.'}
  self.assertEqual(serialize_fixture(f)['conditional_framework_verdict'],'REFUSE_DETERMINISTIC_SELECTION')
 def test_unjustified_nontrigger_rejected(self):
  f=r38a_serialization_fixture();f['modules']['fixture.cross_option']['rationale']=''
  with self.assertRaises(ValueError):serialize_fixture(f)
 def test_no_operational_authority(self):self.assertEqual(serialize_fixture(r38a_serialization_fixture())['execution_state'],'NOT_AUTHORIZED')
 def test_stipulated_joint_distribution_has_zero_covariance(self):
  widths=[.004,.004,.006];points=[[a*w for a,w in zip(s,widths)]for s in itertools.product([-1,1],repeat=3)]
  cov=[[sum(row[i]*row[j]for row in points)/8 for j in range(3)]for i in range(3)]
  self.assertTrue(covariance_valid(cov))
  for i in range(3):
   for j in range(3):self.assertAlmostEqual(cov[i][j],widths[i]**2 if i==j else 0)
 def test_within_option_cluster_doubled_under_each_basis(self):
  r=crossed_pair(.06,.03,.004,.004,[.5,1,2],[0],model_warranted=True)
  self.assertTrue(r['comparison_survives']);self.assertAlmostEqual(r['comparisons'][-1]['signed_gap'],2.6413527189768713)
 def test_unwarranted_model_refuses(self):self.assertFalse(crossed_pair(.06,.03,.004,.004,[1],[0],model_warranted=False)['comparison_survives'])
 def test_incomplete_joint_set_refuses(self):self.assertFalse(crossed_pair(.06,.03,.004,.004,[1],[0],model_warranted=True,comparisons_complete=False)['comparison_survives'])
 def test_favorable_covariance_cannot_rescue_nominal(self):self.assertFalse(crossed_pair(.03,.025,.004,.004,[1],[1],model_warranted=True)['comparison_survives'])
 def test_nonfinite_refused(self):
  with self.assertRaises(ValueError):crossed_pair(.1,0,float('nan'),.01,[1],[0],model_warranted=True)
 def test_empty_variant_refused(self):
  with self.assertRaises(ValueError):crossed_pair(.1,0,.01,.01,[],[0],model_warranted=True)
 def test_invalid_rho_refused(self):
  with self.assertRaises(ValueError):crossed_pair(.1,0,.01,.01,[1],[-2],model_warranted=True)
 def test_negative_scale_refused(self):
  with self.assertRaises(ValueError):crossed_pair(.1,0,.01,.01,[-1],[0],model_warranted=True)

if __name__=='__main__':unittest.main()
