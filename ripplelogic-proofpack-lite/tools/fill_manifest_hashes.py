from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path('.').resolve()
    manifest_path = root / 'manifest.json'
    man = json.loads(manifest_path.read_text(encoding='utf-8'))

    for s in man.get('schemas', []):
        p = root / s['path']
        s['sha256'] = sha256(p)

    for tv in man.get('test_vectors', []):
        tv['sha256']['input'] = sha256(root / tv['input_path'])
        tv['sha256']['expected_output'] = sha256(root / tv['expected_output_path'])
        tv['sha256']['notes'] = sha256(root / tv['notes_path'])

    manifest_path.write_text(json.dumps(man, indent=2) + "\n", encoding='utf-8')
    print(f'Updated hashes in {manifest_path}')

if __name__ == '__main__':
    main()
