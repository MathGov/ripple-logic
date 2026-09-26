import unittest,json,copy,math
from feedback_sensitivity import reconstruct,independent_gap,ROOT
from component_identity import component_entry,source_build_id
class FeedbackTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=reconstruct()
 def test_nominal(self):self.assertAlmostEqual(self.r['nominal_gap'],3.56551781265359,12)
 def test_double(self):self.assertAlmostEqual(self.r['double_sigma_gap'],1.815081024770789,12)
 def test_flip(self):self.assertAlmostEqual(self.r['flip_multiplier'],1.812679919547802,12)
 def test_zeros(self):self.assertEqual(self.r['assessed_zero_cells'],{'A':42,'B':43})
 def test_guard_preserved(self):self.assertEqual(self.r['epsilon'],1e-6)
 def test_guard_effect(self):self.assertAlmostEqual(self.r['epsilon_gap_reduction_percent'],2.381556471412871,11)
 def test_no_zero_guard_rescue(self):self.assertLess(self.r['double_sigma_epsilon_zero_diagnostic'],2)
 def test_Q(self):self.assertAlmostEqual(self.r['active_mass'],1,12)
 def test_refusal(self):self.assertEqual(self.r['verdict'],'REFUSE_DETERMINISTIC_SELECTION')
 def test_common_weight_rescaling(self):
  f=lambda q:independent_gap([.5,0],[.1,0],q,[.2,.2],[.2,.2]);self.assertAlmostEqual(f([.3,.7]),f([3,7]),14)
 def test_uncertain_zero_lowers_gap(self):self.assertLess(independent_gap([.5,0],[.1,0],[1,1],[.2,.2],[.2,.2],0),independent_gap([.5],[.1],[1],[.2],[.2],0))
 def test_exact_zero_cancels_without_guard(self):self.assertAlmostEqual(independent_gap([.5,0],[.1,0],[1,1],[.2,0],[.2,0],0),independent_gap([.5],[.1],[1],[.2],[.2],0),14)
 def test_guard_and_added_mass(self):self.assertLess(independent_gap([.5,0],[.1,0],[1,1],[.2,0],[.2,0],.1),independent_gap([.5],[.1],[1],[.2],[.2],.1))
 def test_guard_reduces(self):self.assertLess(self.r['nominal_gap'],self.r['epsilon_zero_diagnostic'])
 def test_negative_sigma(self):
  with self.assertRaises(ValueError):independent_gap([1],[0],[1],[-1],[1])
 def test_zero_mass(self):
  with self.assertRaises(ValueError):independent_gap([1],[0],[0],[1],[1])
 def test_nan(self):
  with self.assertRaises(ValueError):independent_gap([math.nan],[0],[1],[1],[1])
 def test_size(self):
  with self.assertRaises(ValueError):independent_gap([1,0],[0],[1],[1],[1])
 def test_zero_denominator(self):
  with self.assertRaises(ValueError):independent_gap([1],[0],[1],[0],[0],0)
class IdentityTests(unittest.TestCase):
 def setUp(self):self.m=json.loads((ROOT/'VERSION_MANIFEST.json').read_text());self.p=ROOT/'Core_15/RippleLogic_v13.0_Canon.docx'
 def test_G(self):self.assertEqual(source_build_id(ROOT,self.p),'MG-RL-13.0-20260923-RELEASE-G')
 def test_package_distinct(self):self.assertNotEqual(self.m['build_id'],source_build_id(ROOT,self.p))
 def test_corrected_H(self):self.assertEqual(source_build_id(ROOT,ROOT/'Core_15/RippleLogic_Cascade_Standard_v2.9.docx'),'MG-RL-13.0-20260926-RELEASE-H')
 def test_duplicates(self):
  self.m['components'][1]=copy.deepcopy(self.m['components'][0])
  with self.assertRaises(ValueError):component_entry(ROOT,self.p,self.m)
 def test_bad_hash(self):
  self.m['components'][0]['sha256']='0'*64
  with self.assertRaises(ValueError):component_entry(ROOT,self.p,self.m)
 def test_source_missing(self):
  del self.m['components'][0]['source_build_id']
  with self.assertRaises(ValueError):component_entry(ROOT,self.p,self.m)
 def test_unlisted(self):
  with self.assertRaises(ValueError):component_entry(ROOT,ROOT/'README.md',self.m)
 def test_outside(self):
  with self.assertRaises(ValueError):component_entry(ROOT,ROOT.parent/'wrong.docx',self.m)
 def test_threepart(self):
  self.m['components'][0]['version']='13.0.1'
  with self.assertRaises(ValueError):component_entry(ROOT,self.p,self.m)
