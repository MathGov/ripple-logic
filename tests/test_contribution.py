import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_contribution import require_signoffs,classify_changes,has_trusted_approval

class ContributionTests(unittest.TestCase):
    def test_missing_signoff_rejected(self):
        with self.assertRaises(ValueError):require_signoffs([('bad','A change without sign-off')])
    def test_valid_signoff(self):require_signoffs([('ok','Change\n\nSigned-off-by: Maintainer <maintainer@example.org>')])
    def test_frozen_addition_and_modification_rejected(self):
        for path in ['releases/v1/old.md','releases/v1/new.md']:
            with self.assertRaises(ValueError):classify_changes([path],{'v1'},'maintenance')
    def test_new_release_requires_review(self):self.assertTrue(classify_changes(['releases/v2/paper.md'],{'v1'},'maintenance'))
    def test_declared_normative_requires_review(self):self.assertTrue(classify_changes(['README.md'],{'v1'},'normative'))
    def test_maintenance_and_unknown_paths(self):
        self.assertFalse(classify_changes(['INSTALLATION.md','site/index.html'],{'v1'},'maintenance'))
        self.assertTrue(classify_changes(['new_kernel.py'],{'v1'},'maintenance'))
    def test_self_stale_bot_and_untrusted_approvals_rejected(self):
        good={'id':1,'state':'APPROVED','commit_id':'head','user':{'login':'reviewer','type':'User'},'author_association':'COLLABORATOR'}
        self.assertTrue(has_trusted_approval([good],'author','head'))
        self.assertFalse(has_trusted_approval([good],'reviewer','head'))
        self.assertFalse(has_trusted_approval([good],'author','later-head'))
        self.assertFalse(has_trusted_approval([{**good,'user':{'login':'bot','type':'Bot'}}],'author','head'))
        self.assertFalse(has_trusted_approval([{**good,'author_association':'NONE'}],'author','head'))
        self.assertFalse(has_trusted_approval([good,{**good,'id':2,'state':'DISMISSED'}],'author','head'))

if __name__=='__main__':unittest.main()
