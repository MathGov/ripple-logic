"""Check the maintained doorway's links and the deployed publication identity."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / 'releases/v13.0-release-i'
SITE = ROOT / '_site'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.body = False
        self.stack = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'body':
            self.body = True
        if tag in ('aside', 'a'):
            self.stack.append((tag, bool(self.stack and self.stack[-1][1]) or attrs.get('class') in ('reader-tools', 'reader-skip')))
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        if tag == 'body':
            self.body = False
    def handle_data(self, data):
        if self.body and not (self.stack and self.stack[-1][1]):
            self.text.append(data)

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
    cache = {}
    def parsed(path):
        if path not in cache:
            parser = Links()
            parser.feed(path.read_text(encoding='utf-8'))
            cache[path] = parser
        return cache[path]
    readers = sorted((SITE / 'read').glob('*.html'))
    assert len(readers) == 14
    for page in readers:
        source = parsed(FROZEN / 'Reading_HTML' / page.name)
        maintained = parsed(page)
        assert ' '.join(''.join(source.text).split()) == ' '.join(''.join(maintained.text).split()), f'Reader wording changed: {page.name}'
        assert source.ids <= maintained.ids, f'Reader anchors lost: {page.name}'
    for filename in ['index.html', '404.html', 'installation.html', 'search.html'] + [str(page.relative_to(SITE)) for page in readers]:
        parser = Links()
        parser.feed((SITE / filename).read_text(encoding='utf-8'))
        for href in parser.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith('/ripple-logic/'):
                target = SITE / path.removeprefix('/ripple-logic/')
            else:
                target = (SITE / filename).parent / path if path else SITE / filename
            target = target.resolve()
            assert target.is_relative_to(SITE.resolve()), f'Link outside site: {href}'
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), f'Broken link {filename}: {href}'
            if url.fragment and target.suffix == '.html':
                destination = parsed(target)
                assert url.fragment in destination.ids, f'Broken anchor: {href}'
            checked += 1
    index = json.loads((SITE / 'search-index.json').read_text(encoding='utf-8'))
    assert len(index) == 14
    for doc in index:
        target = parsed((SITE / doc['url']).resolve())
        normalized_text = ' '.join(''.join(target.text).split())
        assert doc['passages'], doc['title']
        for passage in doc['passages']:
            assert passage['anchor'] in target.ids, passage
            assert passage['text'] in normalized_text, passage['anchor']
    urls = ET.parse(SITE / 'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    assert len(urls) == 17
    for url in urls:
        target = SITE / url.text.removeprefix('https://mathgov.github.io/ripple-logic/')
        assert target.is_dir() or target.is_file(), url.text
    print(f'PASS: {len(original_files)} frozen files preserved; 14 readers retain all wording and anchors; {checked} links resolve; search passages and 17 sitemap URLs verified')

if __name__ == '__main__':
    check()
