import unittest,math
from recovery_checks import rmci_lower_bound,stress_base_gap_boundary
from core_reference import RecordError,every_contender
class RecoveryChecks(unittest.TestCase):
 def test_known_zero(self):self.assertEqual(rmci_lower_bound([0,4,4,4],[.25]*4),0)
 def test_missing_not_zero(self):
  with self.assertRaises(RecordError):rmci_lower_bound([None,4,4,4],[.25]*4)
 def test_positive_anchor(self):self.assertAlmostEqual(rmci_lower_bound([4]*4,[.25]*4),100)
 def test_positive_half(self):self.assertAlmostEqual(rmci_lower_bound([2]*4,[.25]*4),50)
 def test_bad_weight(self):
  with self.assertRaises(RecordError):rmci_lower_bound([4]*4,[.5]*4)
 def test_boolean(self):
  with self.assertRaises(RecordError):rmci_lower_bound([True,4,4,4],[.25]*4)
 def test_exact_stress_guard(self):
  v=2*.005**2;e=1e-6;k=2;d=2
  b=stress_base_gap_boundary(v,k,d,e)
  self.assertAlmostEqual(b*math.sqrt(v+e),d*math.sqrt(k*k*v+e))
 def test_positive_control(self):
  variants=[{x:(s,.005*k)for x,s in [('A',.1),('B',.02),('C',-.02)]}for k in [.5,1,2]]
  r=every_contender(variants,['A','B','C']);self.assertEqual(r['status'],'DECISIVE_ARITHMETIC_ONLY');self.assertAlmostEqual(r['minimum_gap'],5.642764926868787)
 def test_ordinal_change_not_worth(self):self.assertGreater(rmci_lower_bound([3]*4,[.25]*4),rmci_lower_bound([2]*4,[.25]*4))
if __name__=='__main__':unittest.main()
