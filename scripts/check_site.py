"""Check the maintained doorway's links and the deployed publication identity."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / 'releases/v13.0-release-i'
SITE = ROOT / '_site'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

def check():
    ledger = FROZEN / 'SHA256SUMS.txt'
    assert hashlib.sha256(ledger.read_bytes()).hexdigest() == 'ac0f82d4d0fca09dc92e2ad0a6365203561664a129d20a86275ee216f0e995b1', 'Trusted release ledger changed'
    for line in ledger.read_text().splitlines():
        digest, relative = line.split('  ', 1)
        assert hashlib.sha256((FROZEN / relative).read_bytes()).hexdigest() == digest, relative
    original_files = [p for p in FROZEN.rglob('*') if p.is_file()]
    assert len(original_files) == 288, 'Unexpected frozen file inventory'
    for original in original_files:
        relative = original.relative_to(FROZEN)
        deployed = SITE / ('publication-index.html' if str(relative) == 'index.html' else relative)
        assert deployed.read_bytes() == original.read_bytes(), f'Deployed bytes differ: {relative}'
    checked = 0
    for filename in ['index.html', '404.html']:
        parser = Links()
        parser.feed((SITE / filename).read_text(encoding='utf-8'))
        for href in parser.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path).removeprefix('/ripple-logic/')
            target = SITE / (path or filename)
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), f'Broken link {filename}: {href}'
            if url.fragment and target.suffix == '.html':
                destination = Links()
                destination.feed(target.read_text(encoding='utf-8'))
                assert url.fragment in destination.ids, f'Broken anchor: {href}'
            checked += 1
    print(f'PASS: {len(original_files)} frozen files preserved; {checked} maintained-page links resolve')

if __name__ == '__main__':
    check()
