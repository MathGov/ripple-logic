"""Generate accessible reading projections while preserving original text and anchors."""
import html
import re
from html.parser import HTMLParser

BASE = 'https://mathgov.github.io/ripple-logic/'

def reader(original, filename, title):
    metadata = f'''<meta name="description" content="Read {html.escape(title, quote=True)} from MathGov / RippleLogic Release I. Maintained reading layout; original publication available alongside.">
<link rel="canonical" href="{BASE}read/{filename}">
<meta property="og:title" content="{html.escape(title, quote=True)} — MathGov / RippleLogic">
<meta property="og:type" content="article"><meta property="og:url" content="{BASE}read/{filename}">
<meta property="og:image" content="{BASE}social-card.png">
<link rel="stylesheet" href="../reader.css">'''
    original = original.replace('</head>', metadata + '</head>', 1)
    banner = f'''<aside class="reader-tools" aria-label="Reading edition"><p><strong>Maintained reading edition · Release I</strong></p><p>Publication wording and anchors are preserved. Layout and navigation are maintained separately. <a href="../Reading_HTML/{filename}">Original frozen HTML</a> · <a href="../search.html">Search document text</a></p><p class="table-help">Wide tables scroll within their borders. Use touch, or focus a table and use the arrow keys.</p></aside>'''
    original = original.replace('<main>', '<a class="reader-skip" href="#reader-content">Skip to publication text</a><main>' + banner, 1)
    original = original.replace('<h1 ', '<h1 tabindex="-1" ', 1)
    # A separate bookmark keeps every supplied ID unchanged.
    first_heading = original.index('<h1 ')
    original = original[:first_heading] + '<span id="reader-content" tabindex="-1"></span>' + original[first_heading:]
    counter = iter(range(1, 10000))
    original = re.sub(r'<div class="table-wrap">', lambda _: f'<div class="table-wrap" tabindex="0" role="region" aria-label="Publication table {next(counter)}">', original)
    original = original.replace('<pre>', '<pre tabindex="0" role="region" aria-label="Publication code block">')
    # Two supplied Canon citations contain nested anchors. Browsers turn the
    # outer one into an empty link. Preserve its destination and all wording,
    # removing only the invalid inner anchor markup in this maintained copy.
    original = re.sub(r'<a\s+([^>]*)>(\s*)<a\s+[^>]*>(.*?)</a>(.*?)</a>', r'<a \1>\2\3\4</a>', original, flags=re.DOTALL)
    return original

class PublicationText(HTMLParser):
    """Extract anchored passages, excluding explicitly historical appendices."""
    def __init__(self):
        super().__init__()
        self.historical = 0
        self.details = []
        self.active = None
        self.parts = []
        self.passages = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'details':
            historical = 'historical' in attrs.get('class', '').split()
            self.details.append(historical)
            self.historical += historical
        if not self.historical and tag in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6') and attrs.get('id'):
            self.active = (tag, attrs['id'])
            self.parts = []

    def handle_data(self, data):
        if self.active and not self.historical:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if self.active and tag == self.active[0]:
            text = ' '.join(''.join(self.parts).split())
            if text:
                self.passages.append({'anchor': self.active[1], 'text': text})
            self.active = None
        if tag == 'details' and self.details:
            self.historical -= self.details.pop()
