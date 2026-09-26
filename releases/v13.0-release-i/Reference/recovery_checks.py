"""Recovery-build numerical checks. No actuator, empirical validation or full Canon validator."""
import math
from core_reference import finite,RecordError,every_contender

def rmci_lower_bound(lower_bounds,weights):
    """Optional geometric profile summary; known zero is not missing evidence.

    Inputs are declared ordinal/profile values. The ratio-scale interpretation is a
    governed convention, not proof of cross-substrate capacity or moral standing.
    Missing/boolean/non-finite input is rejected rather than converted to zero.
    """
    if not lower_bounds or len(lower_bounds)!=len(weights):raise RecordError('incomplete profile')
    ll=[finite(x,'lower bound',0,4)for x in lower_bounds]
    ww=[finite(x,'weight',0,1)for x in weights]
    if any(w<=0 for w in ww)or not math.isclose(math.fsum(ww),1,rel_tol=0,abs_tol=1e-12):raise RecordError('retained positive weights must sum to one')
    if any(x==0 for x in ll):return 0.0
    return 100*math.exp(math.fsum(w*math.log(x/4)for x,w in zip(ll,ww)))

def stress_base_gap_boundary(variance,multiplier,delta=2.0,epsilon=1e-6):
    """Boundary must be exceeded, not equalled, for strict decisive selection."""
    v=finite(variance,'variance',0);k=finite(multiplier,'multiplier',0)
    d=finite(delta,'delta',0);e=finite(epsilon,'epsilon',0)
    if k<=0 or e<=0:raise RecordError('positive multiplier and epsilon required')
    return d*math.sqrt((k*k*v+e)/(v+e))
