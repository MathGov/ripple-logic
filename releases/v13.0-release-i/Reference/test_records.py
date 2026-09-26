import unittest,json,copy
from pathlib import Path
from validate_records import validate
P=Path(__file__).parent/'examples'
class RecordTests(unittest.TestCase):
 def setUp(self):self.e=json.loads((P/'effect_known.json').read_text());self.c=json.loads((P/'control_timing.json').read_text())
 def test_known(self):self.assertFalse(validate(self.e)['execution_authorized'])
 def test_unknown(self):validate(json.loads((P/'effect_unknown.json').read_text()))
 def test_control(self):validate(self.c)
 def test_missing_bearer(self):
  del self.e['bearer_ref']
  with self.assertRaises(Exception):validate(self.e)
 def test_extra_field(self):
  self.e['production_safe']=True
  with self.assertRaises(Exception):validate(self.e)
 def test_u6_requires_view(self):
  self.e['primary_home']['scope']='U6'
  with self.assertRaises(Exception):validate(self.e)
 def test_u6_valid(self):
  self.e['primary_home']['scope']='U6';self.e['u6_view']='U6_COORDINATION';validate(self.e)
 def test_unknown_cannot_have_value(self):
  self.e['signed_impact']={'status':'UNKNOWN','value':0,'reason':'missing'}
  with self.assertRaises(Exception):validate(self.e)
 def test_schema_cannot_grant_authority(self):
  self.e['execution_authorized']=True
  with self.assertRaises(Exception):validate(self.e)
 def test_timestamp(self):
  self.e['observed_at']='uptime:45'
  with self.assertRaises(Exception):validate(self.e)
 def test_interval(self):
  self.e['signed_impact']['upper']=-.5
  with self.assertRaises(Exception):validate(self.e)
 def test_negative_time(self):
  self.c['control_time_upper']=-1
  with self.assertRaises(Exception):validate(self.c)
 def test_wrong_release(self):
  self.e['release_id']='different release'
  with self.assertRaises(Exception):validate(self.e)
 def test_infinite_in_memory(self):
  self.c['control_time_upper']=float('inf')
  with self.assertRaises(Exception):validate(self.c)
if __name__=='__main__':unittest.main(verbosity=2)
