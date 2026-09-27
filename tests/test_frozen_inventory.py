import hashlib,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import frozen_inventory

class FrozenInventoryTests(unittest.TestCase):
    def test_reject_extra_missing_changed_and_ledger_tampering(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);content=root/'paper.md';content.write_bytes(b'original')
            ledger=root/'SHA256SUMS.txt';data=(hashlib.sha256(b'original').hexdigest()+'  paper.md\n').encode();ledger.write_bytes(data)
            with patch.object(frozen_inventory,'LEDGER_SHA256',hashlib.sha256(data).hexdigest()):
                self.assertEqual(frozen_inventory.verify(root),2)
                extra=root/'old-version.md';extra.write_bytes(b'old')
                with self.assertRaisesRegex(ValueError,'extra'):frozen_inventory.verify(root)
                extra.unlink();content.write_bytes(b'changed')
                with self.assertRaisesRegex(ValueError,'bytes changed'):frozen_inventory.verify(root)
                content.unlink()
                with self.assertRaisesRegex(ValueError,'missing'):frozen_inventory.verify(root)
                ledger.write_bytes(b'altered ledger')
                with self.assertRaisesRegex(ValueError,'ledger changed'):frozen_inventory.verify(root)

if __name__=='__main__':unittest.main()
