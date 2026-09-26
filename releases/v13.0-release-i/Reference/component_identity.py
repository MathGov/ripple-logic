"""Strict component-source identity within a newer immutable publication package."""
from pathlib import Path,PurePosixPath
import hashlib,json,re

def component_entry(root,path,manifest=None):
 root=Path(root).resolve();path=Path(path).resolve()
 if not path.is_relative_to(root):raise ValueError('Component outside package')
 m=manifest if manifest is not None else json.loads((root/'VERSION_MANIFEST.json').read_text())
 rows=m['components'];paths=[r['path']for r in rows]
 if len(rows)!=15 or len(set(paths))!=15:raise ValueError('Exactly 15 unique Core components required')
 for r in rows:
  pp=PurePosixPath(r['path'])
  if pp.is_absolute()or'..'in pp.parts or len(pp.parts)!=2 or pp.parts[0]!='Core_15':raise ValueError('Invalid Core path')
  if not re.fullmatch(r'\d+\.\d+',r['version'])or not r.get('source_build_id'):raise ValueError('Version/source identity missing')
 rr=[r for r in rows if r['path']==path.relative_to(root).as_posix()]
 if len(rr)!=1:raise ValueError('Unlisted component')
 r=rr[0]
 if not path.is_file()or path.stat().st_size!=r['bytes']or hashlib.sha256(path.read_bytes()).hexdigest()!=r['sha256']:raise ValueError('Exact identity mismatch')
 return r

def source_build_id(root,path,manifest=None):return component_entry(root,path,manifest)['source_build_id']
