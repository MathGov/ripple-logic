"""Verify exact frozen workbook bytes, cell/formula/cache inventory and the independent exact-formula baseline.

Uses only Python's standard library. It does not recalculate arbitrary Excel
functions or prove evidence truth. The manifest is an external trust anchor.
"""
from pathlib import Path
from zipfile import ZipFile,BadZipFile
import xml.etree.ElementTree as E
import hashlib,json,posixpath,re,sys,argparse,math
S='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def sha(b):return hashlib.sha256(b).hexdigest()
def inspect(path):
    p=Path(path)
    with ZipFile(p) as z:
        bad=z.testzip()
        if bad:raise ValueError('corrupt ZIP member '+bad)
        b={n:z.read(n) for n in z.namelist()}
    rel=E.fromstring(b['xl/_rels/workbook.xml.rels']);targets={r.attrib['Id']:r.attrib['Target'] for r in rel}
    ss=[]
    if 'xl/sharedStrings.xml' in b:
        ss=[''.join(x.itertext()) for x in E.fromstring(b['xl/sharedStrings.xml'])]
    cells={};sheet_order=[];sheet_files={};formula_count=0;error_cells=[];struct={}
    for sn in E.fromstring(b['xl/workbook.xml']).find(S+'sheets'):
        name=sn.attrib['name'];t=targets[sn.attrib[R+'id']];f=t.lstrip('/') if t.startswith('/') else posixpath.normpath('xl/'+t)
        sheet_files[name]=f;sheet_order.append(name);r=E.fromstring(b[f]);cc={}
        for c in r.findall('.//'+S+'sheetData/'+S+'row/'+S+'c'):
            formula=c.find(S+'f');v=c.find(S+'v');typ=c.get('t','n')
            if typ=='s':value=ss[int(v.text)] if v is not None else None;typ='string'
            elif typ=='inlineStr':value=''.join(c.find(S+'is').itertext());typ='string'
            elif typ=='str':value=(v.text or '') if v is not None else None;typ='string'
            elif typ=='b':value=v.text=='1' if v is not None else None;typ='boolean'
            elif typ=='e':value=v.text if v is not None else None;error_cells.append(name+'!'+c.attrib['r'])
            else:
                value=v.text if v is not None else None
                if value is not None:
                    try:value=float(value)
                    except ValueError:pass
                typ='number' if value is not None else 'blank'
            cc[c.attrib['r']]={'type':typ,'value':value,'formula':formula.text if formula is not None else None,'style':c.get('s'),'cache_present':v is not None or c.find(S+'is') is not None}
            formula_count+=formula is not None
        cells[name]=cc
        # Geometry and higher-level structures independently hashed.
        structure=[]
        for x in r:
            if x.tag not in {S+'sheetData',S+'dimension'}:structure.append(E.tostring(x))
        rows=[dict(x.attrib) for x in r.findall('./'+S+'sheetData/'+S+'row')]
        struct[name]={'noncell_structure_sha256':sha(b'\n'.join(structure)),'row_attributes':rows}
    guards=[]
    g=cells.get('Workbook_Formula_Guard',{})
    for addr,c in g.items():
        if not re.fullmatch(r'D\d+',addr) or c['formula'] is None:continue
        row=addr[1:];sn=g['A'+row]['value'];cell=g['B'+row]['value'];expected=g['C'+row]['value']
        target=cells.get(sn,{}).get(cell);actual='F:='+target['formula'] if target and target['formula'] is not None else None
        match=actual==expected
        guards.append({'guard':addr,'target':sn+'!'+cell,'match':match,'formula_present':actual is not None,'presence_cache_matches':c['value']==(0 if actual is not None else 1),'cache_matches':c['value']==(0 if actual is not None else 1)})
    counter=sum(c['formula'] is not None or c['type']!='blank' for c in cells.get('Subgroup_Overrides',{}).values())
    count_cache=cells.get('Build_Integrity',{}).get('B28',{}).get('value')
    count_check={'populated_or_formula_cells':counter,'expected':162,'cached_mismatch':count_cache,'cache_matches':count_cache==abs(counter-162)}
    return {'counter_check':count_check,'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'sheet_order':sheet_order,'formula_count':formula_count,'cells':cells,'structure':struct,'styles_sha256':sha(b['xl/styles.xml']),'formula_guards':guards,'formula_errors':error_cells}
def verify(path,manifest):
    expected=json.loads(Path(manifest).read_text());a=inspect(path);issues=[];count=0
    for k in ('sha256','bytes','sheet_order','formula_count','styles_sha256'):
        if a[k]!=expected[k]:issues.append(k+' differs');count+=1
    for sn in set(a['cells'])|set(expected['cells']):
        aa=a['cells'].get(sn,{});ee=expected['cells'].get(sn,{})
        for cell in set(aa)|set(ee):
            if aa.get(cell)!=ee.get(cell):
                count+=1
                if len(issues)<30:issues.append(sn+'!'+cell+' differs')
        if a['structure'].get(sn)!=expected['structure'].get(sn):
            count+=1
            if len(issues)<30:issues.append(sn+' geometry/structure differs')
    guard_bad=sum(not x['match'] or not x['cache_matches'] for x in a['formula_guards'])
    if not a['counter_check']['cache_matches']:guard_bad+=1
    result={'status':'PASS' if count==0 and guard_bad==0 and not a['formula_errors'] else 'FAIL','bytes':a['bytes'],'sha256':a['sha256'],'sheets':len(a['sheet_order']),'formula_cells':a['formula_count'],'protected_formula_checks':len(a['formula_guards']),'internal_guard_scope':'Formula presence only; exact identity verified here against trusted reference','protected_formula_failures':guard_bad,'structural_count_check':a['counter_check'],'formula_error_cells':a['formula_errors'],'difference_count':count,'differences_first_30':issues,'boundary':'Frozen-file integrity only; no evidence-truth, general Excel recalculation, production or authority claim.'}
    return result


def numerical_fingerprint(data):
    import hashlib,json
    rows=[(s,a,c['formula'],c['type'],c['value']) for s,cs in data['cells'].items() for a,c in cs.items() if c['formula'] is not None]
    return hashlib.sha256(json.dumps(rows,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('workbook');parser.add_argument('manifest',nargs='?',default=str(Path(__file__).resolve().parents[1]/'Verification/Workbook_Manifest.json'));parser.add_argument('--write-manifest',action='store_true');args=parser.parse_args()
    if args.write_manifest:
        Path(args.manifest).write_text(json.dumps(inspect(args.workbook),ensure_ascii=False,indent=2));print('Manifest written. This action is not independent verification.')
    else:
        try:result=verify(args.workbook,args.manifest)
        except (ValueError,BadZipFile,KeyError,OSError) as e:result={'status':'FAIL','error':str(e)}
        print(json.dumps(result,indent=2));sys.exit(0 if result.get('status')=='PASS' else 1)
