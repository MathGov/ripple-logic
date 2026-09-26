import unittest,math
from core_reference import propagate,RecordError
from final_review_checks import *
class FinalReviewChecks(unittest.TestCase):
 def test_cancellation_proxy(self):self.assertAlmostEqual(method_b_from_ledger([.3,-.28],.7),.174)
 def test_ledger_not_net(self):self.assertGreater(method_b_from_ledger([.3,-.28],.7),40*.0042)
 def test_missing_ledger_no_imputation(self):
  with self.assertRaises(RecordError):method_b_from_ledger(None,.7)
 def test_empty_ledger_not_reviewed_zero(self):
  with self.assertRaises(RecordError):method_b_from_ledger([],.7)
 def test_bool_not_instance(self):
  with self.assertRaises(RecordError):method_b_from_ledger([True],.7)
 def test_nan_not_instance(self):
  with self.assertRaises(RecordError):method_b_from_ledger([float('nan')],.7)
 def test_mass_cap_retained(self):self.assertAlmostEqual(method_b_from_ledger([2,-3],.4),.6)
 def test_single_inverse(self):self.assertAlmostEqual(single_instance_reconstruction(math.tanh(2*.7*.3),2,.7),.3)
 def test_zero_confidence_inverse_unavailable(self):
  with self.assertRaises(RecordError):single_instance_reconstruction(.1,2,0)
 def test_saturated_inverse_unavailable(self):
  with self.assertRaises(RecordError):single_instance_reconstruction(1,2,.7)
 def test_product_zero_preserved(self):self.assertEqual(rmci_coverage_fixture([0,4,4,4],[.25]*4)['summary'],0)
 def test_known_intermediate_product(self):self.assertAlmostEqual(rmci_coverage_fixture([1,4,4,4],[.25]*4)['summary'],70.71067811865476)
 def test_partial_raw_number_not_improvement(self):
  r=rmci_coverage_fixture([None,4,4,4],[.25]*4,minimum_coverage=.75);self.assertEqual(r['summary'],100);self.assertFalse(r['capacity_improvement_established'])
 def test_critical_missing_unavailable(self):self.assertIsNone(rmci_coverage_fixture([None,4,4,4],[.25]*4,[0],.75)['summary'])
 def test_coverage_shortfall_unavailable(self):self.assertIsNone(rmci_coverage_fixture([None,4,4,4],[.25]*4,minimum_coverage=.8)['summary'])
 def records(self):return (rmci_coverage_fixture([0,4,4,4],[.25]*4),rmci_coverage_fixture([None,4,4,4],[.25]*4,minimum_coverage=.75))
 def test_unsupported_zero_to_ne(self):
  r=compare_rmci_records(*self.records());self.assertEqual(r['disposition'],'REVIEW_EVIDENCE_REMOVAL');self.assertFalse(r['same_basis_numeric_comparison'])
 def test_reason_without_reviewer_insufficient(self):self.assertFalse(compare_rmci_records(*self.records(),evidence_invalidation_reason='invalid instrument')['evidence_change_documented'])
 def test_review_without_reason_insufficient(self):self.assertFalse(compare_rmci_records(*self.records(),reviewer_confirmed=True)['evidence_change_documented'])
 def test_valid_invalidation_allowed_not_inflation(self):
  r=compare_rmci_records(*self.records(),evidence_invalidation_reason='instrument invalidated',reviewer_confirmed=True);self.assertTrue(r['evidence_change_documented']);self.assertEqual(r['disposition'],'CHANGED_COVERAGE_NOT_COMPARABLE');self.assertEqual(r['prior_profile_retained'][0],0)
 def test_new_evidence_not_silent_comparison(self):
  a,b=self.records();self.assertFalse(compare_rmci_records(b,a)['same_basis_numeric_comparison'])
 def test_same_basis_still_no_empirical_claim(self):
  a=rmci_coverage_fixture([1,4,4,4],[.25]*4);b=rmci_coverage_fixture([2,4,4,4],[.25]*4);r=compare_rmci_records(a,b);self.assertTrue(r['same_basis_numeric_comparison']);self.assertFalse(r['capacity_improvement_established'])
 def test_zero_weight_invalid(self):
  with self.assertRaises(RecordError):rmci_coverage_fixture([0,4],[0,1])
 def test_unknown_mode_category_denied(self):self.assertFalse(mode4_permission_fixture('invented',{}))
 def test_empty_authority_denied(self):self.assertFalse(mode4_permission_fixture('Tools: External actions',{}))
 def test_forbidden_overrides(self):
  for c in FORBIDDEN:self.assertFalse(mode4_permission_fixture(c,{k:True for k in COMMON}))
 def test_truthy_strings_not_authorization(self):self.assertFalse(mode4_permission_fixture('Read: Public data',{k:'true'for k in COMMON}))
 def test_public_data_permission_ceiling(self):self.assertTrue(mode4_permission_fixture('Read: Public data',{k:True for k in COMMON}))
 def test_dm_requires_thread(self):self.assertFalse(mode4_permission_fixture('Write: DMs',{k:True for k in COMMON}))
 def test_dm_thread_permission(self):self.assertTrue(mode4_permission_fixture('Write: DMs',{**{k:True for k in COMMON},'thread_approved':True}))
 def test_file_io_explicit_prerequisites(self):
  e={**{k:True for k in COMMON},'file_operation_allowlisted':True,'structural_viability_record':True};self.assertTrue(mode4_permission_fixture('Tools: File I/O',e));e['current_qualification']=False;self.assertFalse(mode4_permission_fixture('Tools: File I/O',e))
 def test_external_action_structural_record(self):self.assertFalse(mode4_permission_fixture('Tools: External actions',{**{k:True for k in COMMON},'external_action_allowlisted':True}))
 def test_signed_envelope_required(self):
  e={k:True for k in COMMON};e['applicable_signed_envelope']=False;self.assertFalse(mode4_permission_fixture('Read: Public data',e))
 def test_quick_model_unchanged(self):
  x=[.6]*49;k=[[0.]*49 for _ in range(49)];self.assertAlmostEqual(propagate(x,'QUICK',k)[0],math.tanh(.6));self.assertEqual(propagate(x,'NONE')[0],.6)
 def test_epsilon_can_change_gap(self):self.assertLess(.001/(1e-6**.5),2)
if __name__=='__main__':unittest.main()
