import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib, json, zipfile

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def text(root,rel): return (Path(root)/rel).read_text(encoding='utf-8',errors='replace')
def check_docx(path):
    with zipfile.ZipFile(path) as z:
        names=z.namelist(); xml=z.read('word/document.xml').decode('utf-8','ignore')
        return {'document': 'word/document.xml' in names,'comments':'word/comments.xml' in names,'tracked':('<w:ins' in xml or '<w:del' in xml),'vba':any('vbaProject' in n for n in names),'blue_headers':xml.count('w:fill="1F4E78"'),'light_rows':xml.count('w:fill="D9EAF7"'),'repeat_headers':xml.count('<w:tblHeader')}
