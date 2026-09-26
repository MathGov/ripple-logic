"""Build a maintained doorway without changing the frozen publication."""
import argparse
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN = ROOT / 'releases/v13.0-release-i'

def build(destination):
    destination = destination.resolve()
    if destination.exists():
        raise SystemExit('Use an empty output directory; the builder never deletes files.')
    shutil.copytree(FROZEN, destination)
    (destination / 'index.html').rename(destination / 'publication-index.html')
    manifest = json.loads((FROZEN / 'VERSION_MANIFEST.json').read_text(encoding='utf-8'))
    cards = []
    for item in manifest['components']:
        path = Path(item['path'])
        links = [(item['path'], 'Editable master')]
        for directory, suffix, label in [('Reading_HTML', '.html', 'Read online'), ('Reading_PDFs', '.pdf', 'PDF'), ('Sources', '.md', 'Markdown')]:
            target = f'{directory}/{path.stem}{suffix}'
            if (FROZEN / target).is_file():
                links.append((target, label))
        links.sort(key=lambda pair: pair[1] != 'Read online')
        name = html.escape(item['component'])
        anchors = ' '.join(f'<a href="{html.escape(url)}">{label}<span class="sr-only">: {name}</span></a>' for url, label in links)
        cards.append(f'<article class="document"><p class="edition">Edition {html.escape(item["version"])}</p><h3>{name}</h3><div class="formats">{anchors}</div></article>')
    for source in (ROOT / 'site').iterdir():
        if source.is_file():
            shutil.copyfile(source, destination / source.name)
    template = (destination / 'index.html').read_text(encoding='utf-8')
    (destination / 'index.html').write_bytes(template.replace('<!-- COMPONENTS -->', '\n'.join(cards)).encode('utf-8'))
    shutil.copyfile(ROOT / 'INSTALLATION.md', destination / 'INSTALLATION.md')
    shutil.copyfile(ROOT / 'requirements-ci.txt', destination / 'requirements-ci.txt')
    (destination / '.nojekyll').touch()
    print(f'Built {len(cards)} component cards at {destination}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / '_site')
    build(parser.parse_args().output)
