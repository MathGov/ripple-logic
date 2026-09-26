"""Loopback-only transport tests; no real external publication is asserted."""
import unittest,sys,tempfile,hashlib,threading
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'Publication'))
from verify_hosted import compare_downloads,safe_relative,validate_base
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
class HostedVerifierTests(unittest.TestCase):
    def test_matching_corrupt_missing(self):
        with tempfile.TemporaryDirectory()as d:
            p=Path(d)/'file.bin';p.write_bytes(b'original')
            artifact={'path':'file.bin','bytes':8,'sha256':hashlib.sha256(b'original').hexdigest()}
            server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=d));t=threading.Thread(target=server.serve_forever,daemon=True);t.start()
            try:
                base=f'http://127.0.0.1:{server.server_port}/'
                self.assertEqual(compare_downloads(base,[artifact],allow_local_http=True)['status'],'PASS')
                p.write_bytes(b'changed!');self.assertEqual(compare_downloads(base,[artifact],allow_local_http=True)['status'],'FAIL')
                p.unlink();self.assertEqual(compare_downloads(base,[artifact],allow_local_http=True)['status'],'FAIL')
            finally:server.shutdown();server.server_close();t.join()
    def test_reject_path_escape(self):
        for p in ['../x','/x','a/../b','a\\b','']:
            with self.assertRaises(ValueError):safe_relative(p)
    def test_reject_cleartext_and_credentials(self):
        for url in ['http://example.test/','https://user:pass@example.test/','https://example.test/?key=x']:
            with self.assertRaises(ValueError):validate_base(url)
if __name__=='__main__':unittest.main()
