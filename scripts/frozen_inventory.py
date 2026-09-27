"""Fail closed before copying a publication with changed or extra files."""
from pathlib import Path
import hashlib

LEDGER_SHA256='ac0f82d4d0fca09dc92e2ad0a6365203561664a129d20a86275ee216f0e995b1'

def verify(root):
    root=Path(root)
    ledger=root/'SHA256SUMS.txt'
    if hashlib.sha256(ledger.read_bytes()).hexdigest()!=LEDGER_SHA256:
        raise ValueError('The trusted publication ledger changed')
    entries={name:digest for digest,name in (line.split('  ',1) for line in ledger.read_text(encoding='utf-8').splitlines())}
    expected=set(entries)|{'SHA256SUMS.txt'}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    if actual!=expected:
        raise ValueError(f'Frozen inventory differs: {len(actual-expected)} extra, {len(expected-actual)} missing files. Preserve extra material outside the release tree before building.')
    for name,digest in entries.items():
        path=root/name
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):raise ValueError('Unsafe publication path: '+name)
        if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError('Frozen bytes changed: '+name)
    return len(actual)
