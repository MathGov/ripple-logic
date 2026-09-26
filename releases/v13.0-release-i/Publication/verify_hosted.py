"""Download public artifacts and compare them with a locally trusted manifest.

No upload, remote mutation, credential handling, or hosted-CI claim is performed.
Default: verify all 15 hosted Core files. --all-files verifies the public inventory.
A checksum verifies bytes, not empirical claims or independently trusted origin.
"""
from __future__ import annotations
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urljoin, quote
from urllib.request import Request, urlopen
import argparse, hashlib, json, time
ROOT = Path(__file__).resolve().parents[1]

def safe_relative(path: str) -> str:
    if not isinstance(path,str) or not path or '\\' in path:
        raise ValueError('Invalid relative artifact path')
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or '.' in p.parts or p.as_posix()!=path:
        raise ValueError('Unsafe or noncanonical relative artifact path')
    return path

def validate_base(base: str, allow_local_http: bool=False) -> str:
    p=urlsplit(base)
    if p.username or p.password or p.query or p.fragment or not p.hostname:
        raise ValueError('Use a public directory URL without credentials/query/fragment')
    local=p.hostname in {'localhost','127.0.0.1','::1'}
    if p.scheme!='https' and not (p.scheme=='http' and local and allow_local_http):
        raise ValueError('HTTPS required; loopback HTTP is allowed only for explicit local tests')
    return base.rstrip('/')+'/'

def compare_downloads(base: str, artifacts: list[dict], *, allow_local_http: bool=False, timeout: float=20.0) -> dict:
    base=validate_base(base,allow_local_http)
    if not isinstance(timeout,(int,float)) or timeout<=0 or timeout>300:
        raise ValueError('timeout must be in (0,300] seconds')
    rows=[]
    for a in artifacts:
        path=safe_relative(a['path']);expected=a['sha256'];size=a['bytes']
        if not isinstance(size,int) or not 0<=size<=100_000_000 or len(expected)!=64:
            raise ValueError('Invalid trusted inventory entry')
        requested=urljoin(base,quote(path,safe='/'))
        start=time.monotonic()
        try:
            request=Request(requested,headers={'User-Agent':'MathGov-Frozen-Publication-Verification','Cache-Control':'no-cache'})
            with urlopen(request,timeout=timeout)as r:
                final=r.geturl();content=r.read(size+1)
            digest=hashlib.sha256(content).hexdigest()
            ok=len(content)==size and digest==expected
            row={'path':path,'requested_url':requested,'returned_url':final,'status':'PASS'if ok else'FAIL','expected_sha256':expected,'received_sha256':digest,'expected_bytes':size,'received_bytes':len(content)}
        except Exception as exc:
            row={'path':path,'requested_url':requested,'status':'FAIL','error':str(exc),'expected_sha256':expected,'expected_bytes':size}
        row['elapsed_seconds']=round(time.monotonic()-start,3);rows.append(row)
    return {'status':'PASS'if rows and all(x['status']=='PASS'for x in rows)else'FAIL',
       'verification_surface':'LOCAL_LOOPBACK_TEST'if urlsplit(base).hostname in {'localhost','127.0.0.1','::1'}else'HOSTED_BYTES',
       'base_url':base,'checked':len(rows),'matched':sum(x['status']=='PASS'for x in rows),'results':rows,
       'scope':'Transport and exact-byte verification against a locally trusted manifest; not independent host ownership, hosted CI, full implementation conformance or empirical validation.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--base-url',required=True);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--all-files',action='store_true');ap.add_argument('--allow-local-http',action='store_true')
    ap.add_argument('--commit',default=None);ap.add_argument('--tag',default=None)
    args=ap.parse_args();out=args.output.resolve()
    if out==ROOT or ROOT in out.parents:raise ValueError('Write the receipt outside this immutable package')
    # Verify local immutable inventory before using its manifest as a download reference.
    import sys, subprocess
    checked=subprocess.run([sys.executable,'-B',str(ROOT/'Reference/verify_release.py')],cwd=ROOT,capture_output=True,text=True)
    if checked.returncode:raise ValueError('Local publication identity failed verification')
    manifest=json.loads((ROOT/'VERSION_MANIFEST.json').read_text())
    items=manifest['components']
    if args.all_files:
        items=[]
        for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
            expected,rel=line.split('  ',1)
            items.append({'path':rel,'sha256':expected,'bytes':(ROOT/rel).stat().st_size})
    result=compare_downloads(args.base_url,items,allow_local_http=args.allow_local_http)
    result['publication_id']=manifest['build_id']
    result['operator_supplied_metadata']={'commit':args.commit,'tag':args.tag,'independently_verified':False}
    result['hosted_workflow_status']='NOT_CHECKED'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items()if k!='results'},indent=2))
    return 0 if result['status']=='PASS'else 1
if __name__=='__main__':
    try:raise SystemExit(main())
    except (OSError,ValueError,KeyError)as e:print(json.dumps({'status':'FAIL','error':str(e)}));raise SystemExit(1)
