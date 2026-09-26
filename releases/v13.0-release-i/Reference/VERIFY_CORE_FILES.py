from component_identity import component_entry
from pathlib import Path
import json,hashlib,re
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'VERSION_MANIFEST.json').read_text())
for x in m['components']:
 component_entry(root,root/x['path'],m)
 p=root/x['path'];assert p.is_file(),x['path']
 assert re.fullmatch(r"[0-9]+[.][0-9]+",x['version']),x['version']
 assert p.stat().st_size==x['bytes'],x['path']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'],x['path']
print(json.dumps({'components':len(m['components']),'status':'PASS','scope':'Current Core component identity only'}))
