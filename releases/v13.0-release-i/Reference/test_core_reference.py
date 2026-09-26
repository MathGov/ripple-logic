import unittest,math,tempfile,json,random
from pathlib import Path
from core_reference import *

def zero(n=7):return [[0. for _ in range(n)] for _ in range(n)]

class ReferenceTests(unittest.TestCase):
    def test_contribution_exact_margins(self):
        rng=random.Random(1300)
        for _ in range(100):
            x=[[rng.uniform(-1,1) for _ in range(7)] for _ in range(7)]
            w=[[rng.uniform(0,2) for _ in range(7)] for _ in range(7)]
            c=contributions(x,w)
            self.assertAlmostEqual(c.score,sum(c.by_scope),14)
            self.assertAlmostEqual(c.score,sum(c.by_dimension),14)
            self.assertAlmostEqual(c.score,c.positive+c.negative,14)
            self.assertLessEqual(abs(c.score),1)
    def test_zero_mass_unknown(self):
        with self.assertRaisesRegex(RecordError,'NO_ACTIVE'):contributions(zero(),zero())
    def test_negative_weight(self):
        w=zero();w[0][0]=-1
        with self.assertRaises(RecordError):contributions(zero(),w)
    def test_out_of_range_impact(self):
        x=zero();x[0][0]=-4.33
        with self.assertRaises(RecordError):contributions(x,[[1]*7]*7)
    def test_unknown_not_zero(self):
        x=zero();x[0][0]=None
        with self.assertRaises(RecordError):contributions(x,[[1]*7]*7)
    def test_nan_rejected(self):
        with self.assertRaises(RecordError):finite(float('nan'),'v')
    def test_infinity_rejected(self):
        with self.assertRaises(RecordError):finite(float('inf'),'v')
    def test_boolean_rejected(self):
        with self.assertRaises(RecordError):finite(True,'v')
    def test_shape_rejected(self):
        with self.assertRaises(RecordError):contributions([[0]*6]*7,[[1]*7]*7)
    def test_sign_and_100_display(self):
        c=contributions([[.25]*7]*7,[[1]*7]*7)
        self.assertAlmostEqual(c.score,.25);self.assertAlmostEqual(100*c.score,25)
    def test_weight_scale_invariant(self):
        x=zero();x[2][4]=.8;w=[[1.]*7 for _ in range(7)]
        self.assertEqual(contributions(x,w).score,contributions(x,[[3.]*7]*7).score)
    def test_block_direction(self):
        k=zero(49);k[cell_index('U6','D4')][cell_index('U5','D5')]=.3
        self.assertEqual(kernel_block(k,'U6','U5')[3][4],.3)
        self.assertEqual(kernel_block(k,'U5','U6')[4][3],0)
    def test_block_full_reconstruction(self):
        k=[[i*49+j for j in range(49)] for i in range(49)]
        for u in SCOPES:
            for v in SCOPES:
                b=kernel_block(k,u,v)
                self.assertEqual(b[6][6],k[cell_index(u,'D7')][cell_index(v,'D7')])
    def test_coordinate_unknown(self):
        with self.assertRaises(RecordError):cell_index('U8','D1')
    def test_none_identity(self):
        x=[.6]*49;self.assertEqual(propagate(x,'NONE'),x)
    def test_none_rejects_implicit_kernel(self):
        with self.assertRaises(RecordError):propagate([0]*49,'NONE',zero(49))
    def test_quick_zero_kernel_preserves_declared_saturation(self):
        y=propagate([.6]*49,'QUICK',zero(49))
        self.assertAlmostEqual(y[0],math.tanh(.6))
    def test_quick_direction_signed(self):
        k=zero(49);k[1][0]=.4;x=[0]*49;x[0]=-.5
        y=propagate(x,'QUICK',k);self.assertAlmostEqual(y[1],math.tanh(-.2))
    def test_quick_row_norm(self):
        k=zero(49);k[0][0]=.5;k[0][1]=.5
        with self.assertRaises(RecordError):propagate([0]*49,'QUICK',k)
    def test_quick_edge_bound(self):
        k=zero(49);k[0][1]=.6
        with self.assertRaises(RecordError):propagate([0]*49,'QUICK',k)
    def test_full_not_supported(self):
        with self.assertRaises(RecordError):propagate([0]*49,'FULL',zero(49))
    def test_cvar_fractional_boundary(self):
        self.assertAlmostEqual(tail_cvar([1,.5,0],[.02,.04,.94]),.7)
    def test_cvar_bad_probability(self):
        with self.assertRaises(RecordError):tail_cvar([1,0],[.2,.2])
    def test_cvar_alpha_one(self):
        with self.assertRaises(RecordError):tail_cvar([0],[1],1)
    def test_upper_bound_not_breach(self):
        r=aggregate_risk_bounds([[0,.08],[0,.08]],.1)
        self.assertEqual(r['verdict'],'UNKNOWN')
    def test_lower_bound_breach(self):
        self.assertEqual(aggregate_risk_bounds([[.11,.12]],.1)['verdict'],'EXCEEDS_BOUND')
    def test_risk_safe(self):
        self.assertEqual(aggregate_risk_bounds([[0,.02],[0,.03]],.1)['verdict'],'WITHIN_BOUND')
    def test_risk_missing(self):
        with self.assertRaises(RecordError):aggregate_risk_bounds([],.1)
    def test_every_contender_lower_uncertain_rival(self):
        v={'A':(.8,.01),'B':(.5,.01),'C':(.4,.3)}
        self.assertEqual(every_contender([v],list(v))['status'],'NON_DECISIVE')
    def test_decisive_arithmetic_only(self):
        v={'A':(.8,.01),'B':(.1,.01)}
        self.assertEqual(every_contender([v],list(v))['status'],'DECISIVE_ARITHMETIC_ONLY')
    def test_sole_no_gap(self):
        r=every_contender([{'A':(.1,.1)}],['A']);self.assertEqual(r['status'],'SOLE_SURVIVOR');self.assertIsNone(r['minimum_gap'])
    def test_empty_not_vacuous_pass(self):
        self.assertEqual(every_contender([],[])['status'],'NO_SELECTABLE_OPTION')
    def test_variants_missing_rival(self):
        with self.assertRaises(RecordError):every_contender([{'A':(.1,.1)}],['A','B'])
    def test_variant_reversal(self):
        self.assertEqual(every_contender([{'A':(.8,.01),'B':(0,.01)},{'A':(0,.01),'B':(.8,.01)}],['A','B'])['status'],'NON_DECISIVE')
    def test_incomplete_no_decision(self):
        self.assertEqual(every_contender([],['A'],completeness=False)['status'],'INCOMPLETE')
    def test_nonfinite_contender(self):
        with self.assertRaises(RecordError):every_contender([{'A':(float('nan'),.1)}],['A'])
    def test_timely_control(self):
        r=timely_prevention(1,3,1,evidence_supported=True,authority_valid=True)
        self.assertTrue(r['timely_prevention_supported']);self.assertFalse(r['execution_authorized'])
    def test_late_not_erases_mitigation(self):
        r=timely_prevention(5,3,evidence_supported=True,authority_valid=True)
        self.assertFalse(r['timely_prevention_supported']);self.assertIn('separate evidence',r['separate_late_or_ex_ante_mitigation'])
    def test_equal_time_not_before(self):
        self.assertFalse(timely_prevention(3,3,evidence_supported=True,authority_valid=True)['timely_prevention_supported'])
    def test_unsupported_control(self):
        self.assertFalse(timely_prevention(1,3,evidence_supported=False,authority_valid=True)['timely_prevention_supported'])
    def test_authority_not_invented(self):
        self.assertFalse(timely_prevention(1,3,evidence_supported=True,authority_valid=False)['timely_prevention_supported'])
    def test_json_nonfinite(self):
        with self.assertRaises(RecordError):strict_json_loads('{"x":NaN}')
    def test_json_duplicate_key(self):
        with self.assertRaises(RecordError):strict_json_loads('{"x":1,"x":2}')
    def test_json_key_order_semantic(self):
        self.assertEqual(strict_json_loads('{"D2":2,"D1":1}')['D1'],1)
    def effect(self):return dict(effect_id='e1',bearer='b1',state_construct='s1',baseline='baseline',causal_pathway='p1',window='t1',scope='U1',dimension='D2')
    def test_effect_valid(self):validate_effect_identities([self.effect()])
    def test_effect_duplicate_id(self):
        with self.assertRaises(RecordError):validate_effect_identities([self.effect(),self.effect()])
    def test_effect_duplicate_views(self):
        a=self.effect();b=dict(a,effect_id='e2',scope='U2')
        with self.assertRaises(RecordError):validate_effect_identities([a,b])
    def test_effect_distinct_downstream(self):
        a=self.effect();b=dict(a,effect_id='e2',state_construct='caregiving cost',dimension='D1')
        validate_effect_identities([a,b])
    def test_effect_missing(self):
        a=self.effect();del a['baseline']
        with self.assertRaises(RecordError):validate_effect_identities([a])
    def test_nonlinear_source_nonadditivity(self):
        self.assertNotAlmostEqual(math.tanh(.5)+math.tanh(.5),math.tanh(1))
    def test_allocation_not_invariance_theorem(self):
        # Same raw effect split across unequal-weight cells changes weighted saturated sum.
        a=.8*math.tanh(1);b=.8*math.tanh(.5)+.2*math.tanh(.5)
        self.assertNotAlmostEqual(a,b)
    def test_local_canonical_order(self):
        self.assertEqual(action_digest('d',{'a':1,'b':'2'}),action_digest('d',{'b':'2','a':1}))
    def test_domain_bound_identity(self):
        self.assertNotEqual(action_digest('d1',{'a':1}),action_digest('d2',{'a':1}))
    def test_float_action_rejected(self):
        with self.assertRaises(RecordError):action_digest('d',{'a':.1})
    def test_action_restart_no_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'a.db';a=ActionLedger(p);i,ok=a.reserve('scope',{'option':'protect','config':'c1'})
            self.assertTrue(ok);a.outcome(i,'UNKNOWN','request sent, acknowledgement absent');a.close()
            b=ActionLedger(p);j,ok=b.reserve('scope',{'option':'protect','config':'c1'})
            self.assertFalse(ok);self.assertEqual(i,j);self.assertEqual(b.state(i),'UNKNOWN')
            b.outcome(i,'CONFIRMED','external read reconciled');self.assertEqual(b.state(i),'CONFIRMED');b.close()
    def test_action_terminal_cannot_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            a=ActionLedger(Path(d)/'a.db');i,_=a.reserve('d',{'n':1});a.outcome(i,'CONFIRMED','receipt')
            with self.assertRaises(RecordError):a.outcome(i,'UNKNOWN','later')
            a.close()
    def test_finite_field_linear_commitment_not_hiding(self):
        p=2**255-19;s=123456789;c=(41923*s)%p
        self.assertEqual(c*pow(41923,-1,p)%p,s)
    def test_hyperinflation_time_units(self):
        # Doubling every 15 hours is not merely 10,000 percent over 30 days.
        factor=2**(30*24/15);self.assertGreater(factor,10**12)

if __name__=='__main__':unittest.main(verbosity=2)
