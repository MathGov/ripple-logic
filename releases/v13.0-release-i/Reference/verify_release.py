"""Verify a release against an independently trusted SHA-256 ledger. Read-only.

A ledger obtained from the same untrusted source is not an independent trust root.
This checks file identity, not scientific truth, semantic completeness or authority.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, re

def verify(root: Path, ledger: Path) -> dict:
    root=root.resolve();rows=[];seen=set();fail=[]
    for n,line in enumerate(ledger.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():continue
        match=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        if not match:fail.append(f'Invalid ledger line {n}');continue
        expected,name=match.groups();rel=PurePosixPath(name)
        if rel.is_absolute()or'..'in rel.parts or '\\' in name or name in seen:
            fail.append(f'Unsafe or duplicate ledger entry {n}');continue
        seen.add(name);p=root.joinpath(*rel.parts)
        if p.is_symlink() or not p.resolve().is_relative_to(root) or not p.is_file():
            fail.append(f'Missing or unsafe file {name}');continue
        h=hashlib.sha256()
        with p.open('rb')as f:
            for part in iter(lambda:f.read(1048576),b''):h.update(part)
        ok=h.hexdigest()==expected
        rows.append({'path':name,'passed':ok})
        if not ok:fail.append('Hash mismatch: '+name)
    if not rows:fail.append('No verifiable ledger entries')
    return {'status':'PASS'if not fail else'FAIL','checked':len(rows),'failures':fail,'boundary':'Exact identity only; ledger trust must be established independently.'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--ledger',type=Path);a=p.parse_args()
    try:r=verify(a.root,a.ledger or a.root/'SHA256SUMS.txt')
    except (OSError,ValueError)as e:r={'status':'FAIL','error':str(e)}
    print(json.dumps(r,indent=2));raise SystemExit(0 if r['status']=='PASS'else 1)
