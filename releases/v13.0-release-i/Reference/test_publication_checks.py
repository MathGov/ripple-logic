import unittest,math,copy
from datetime import datetime,timezone
from publication_checks import *
class PublicationChecks(unittest.TestCase):
 def test_unsafe_continuation_is_not_free(self):self.assertAlmostEqual(residual_catastrophe_loss([-.6],[1]),.6)
 def test_improvement_retains_residual_loss(self):self.assertAlmostEqual(residual_catastrophe_loss([-.2],[1]),.2)
 def test_positive_does_not_offset_negative(self):self.assertAlmostEqual(residual_catastrophe_loss([1,-.6],[.5,.5]),.3)
 def test_catastrophe_weights_normalized(self):
  with self.assertRaises(RecordError):residual_catastrophe_loss([-.6],[.5])
 def test_missing_catastrophe_not_zero(self):
  with self.assertRaises(RecordError):residual_catastrophe_loss([None],[1])
 def test_interval_image_contains_point(self):
  r=transform_interval(.7,.2,2);self.assertLessEqual(r['lower'],r['transformed_point']);self.assertGreaterEqual(r['upper'],r['transformed_point'])
 def test_interval_small_signal_beta_three(self):
  r=transform_interval(0,.0001,3);self.assertGreater(r['half_width'],2.99*.0001)
 def test_interval_large_signal_compression(self):self.assertLess(transform_interval(2,.1,2)['half_width'],.1)
 def test_interval_zero_width(self):self.assertEqual(transform_interval(.5,0,2)['half_width'],0)
 def test_interval_midpoint_not_point(self):
  r=transform_interval(.5,.4,2);self.assertNotAlmostEqual(r['midpoint'],r['transformed_point']);self.assertGreater(r['maximum_deviation_from_point'],r['half_width'])
 def test_invalid_interval(self):
  with self.assertRaises(RecordError):transform_interval(0,-.1,2)
 def test_temporal_splitting_not_invariant(self):self.assertGreater(2*time_weight(5),time_weight(10))
 def test_linear_mass_splitting_invariant(self):self.assertAlmostEqual(math.tanh(2*.6),math.tanh(2*(.2+.4)))
 def test_cross_cell_splitting_not_automatically_invariant(self):self.assertNotAlmostEqual(math.tanh(2*.6),2*math.tanh(2*.3))
 def test_r38a_fields_and_cluster(self):
  f=r38a_fixture();self.assertEqual(f['arithmetic']['status'],'DECISIVE_ARITHMETIC_ONLY');self.assertAlmostEqual(f['records']['A']['sigma'],.004)
 def test_r38a_positive_summary(self):self.assertEqual(fixture_decision(r38a_fixture(),qualification_supported=True,required_variants_complete=True,uncertainty_warrant_stipulated=True)['conditional_decision_state'],'SELECTED_DECISIVE')
 def test_r38a_no_authority(self):self.assertEqual(fixture_decision(r38a_fixture(),qualification_supported=True,required_variants_complete=True,uncertainty_warrant_stipulated=True)['execution_state'],'NOT_AUTHORIZED')
 def test_r38a_qualification_failure(self):self.assertEqual(fixture_decision(r38a_fixture(),qualification_supported=False,required_variants_complete=True,uncertainty_warrant_stipulated=True)['conditional_decision_state'],'NO_SELECTABLE_OPTION')
 def test_r38a_missing_variant(self):self.assertEqual(fixture_decision(r38a_fixture(),qualification_supported=True,required_variants_complete=False,uncertainty_warrant_stipulated=True)['conditional_decision_state'],'REFUSE')
 def test_r38a_unsupported_uncertainty(self):self.assertEqual(fixture_decision(r38a_fixture(),qualification_supported=True,required_variants_complete=True,uncertainty_warrant_stipulated=False)['conditional_decision_state'],'REFUSE')
 def test_smaller_sigma_can_change_nondecisive(self):
  a=every_contender([{'A':(.03,.015),'B':(0,.015)}],['A','B']);b=every_contender([{'A':(.03,.0075),'B':(0,.0075)}],['A','B']);self.assertEqual(a['status'],'NON_DECISIVE');self.assertEqual(b['status'],'DECISIVE_ARITHMETIC_ONLY')
 def test_zero_summary_keeps_profile(self):
  r=rmci_profile_record([0,4,4,4],[.25]*4,[0,1]);self.assertEqual(r['summary'],0);self.assertEqual(len(r['dimension_lower_bounds']),4);self.assertFalse(r['authority'])
 def test_missing_critical_not_zero(self):self.assertIsNone(rmci_profile_record([None,4,4,4],[.25]*4,[0])['summary'])
 def test_missing_noncritical_not_silently_imputed(self):self.assertEqual(rmci_profile_record([None,4,4,4],[.25]*4,[1])['status'],'UNAVAILABLE')
 def test_boolean_not_capacity(self):
  with self.assertRaises(RecordError):rmci_profile_record([True,4],[.5,.5],[0])
 def test_zero_weight_not_retained(self):
  with self.assertRaises(RecordError):rmci_profile_record([0,4],[0,1],[0])
 def meta(self):return dict(schema_version='OACP-1.1',sig_alg='Ed25519',jcs='RFC8785',aud='fixture',cmd_id='cmd',nonce='nonce-fixture',kid='key',issued_utc='2026-09-11T10:00:00Z',expires_utc='2026-09-11T10:05:00Z')
 def checkmeta(self,m):return oacp_metadata_check(m,audience='fixture',now=datetime(2026,9,11,10,2,tzinfo=timezone.utc),max_validity_seconds=600)
 def test_meta_not_signature_or_execution(self):
  r=self.checkmeta(self.meta());self.assertFalse(r['signature_verified']);self.assertFalse(r['execution_authorized']);self.assertEqual(r['maximum_acceptance_span_seconds'],540)
 def test_meta_legacy_rejected(self):
  m=self.meta();m['schema_version']='OACP-1.0'
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_wrong_audience_rejected(self):
  m=self.meta();m['aud']='other'
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_missing_audience_rejected(self):
  m=self.meta();del m['aud']
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_inverted_time(self):
  m=self.meta();m['expires_utc']='2026-09-11T09:59:00Z'
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_overlong(self):
  m=self.meta();m['expires_utc']='2026-09-11T11:00:00Z'
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_expired(self):
  m=self.meta();m['issued_utc']='2026-09-11T09:50:00Z';m['expires_utc']='2026-09-11T09:55:00Z'
  with self.assertRaises(RecordError):self.checkmeta(m)
 def test_meta_naive_clock(self):
  with self.assertRaises(RecordError):oacp_metadata_check(self.meta(),audience='fixture',now=datetime(2026,9,11,10,2),max_validity_seconds=600)
if __name__=='__main__':unittest.main()
