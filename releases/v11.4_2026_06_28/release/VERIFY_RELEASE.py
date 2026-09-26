#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
sha_path = root/'release'/'SHA256SUMS.txt'
if not sha_path.exists():
    print('FAIL: SHA256SUMS.txt missing')
    sys.exit(1)
fail=[]
for line in sha_path.read_text().splitlines():
    if not line.strip(): continue
    h, rel = line.split('  ',1)
    p=root/rel
    if not p.exists():
        fail.append((rel,'missing'))
        continue
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    if digest != h:
        fail.append((rel,'hash mismatch'))
if fail:
    print('FAIL:', fail)
    sys.exit(1)
print(f'PASS: {len(sha_path.read_text().splitlines())} files checked')
