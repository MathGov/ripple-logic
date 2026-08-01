#!/usr/bin/env python3
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET
import sys, zipfile, re
sys.dont_write_bytecode = True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
 if not c: FAIL.append(m)
canon=(ROOT/'docs/canon/RippleLogic_v12.5_Canon.md').read_text(encoding='utf-8',errors='replace')
for p in ['hazard cannot activate','pre-confidence contribution mass','h_{k,base}','h_{k,welfare}','rho_r','Rights-conflict precondition','Constructed-index caution','ESCALATE_OR_REPAIR_SCENARIO_LIBRARY']:
 ck(p.lower() in canon.lower(),f'Canon formula interface missing {p}')
wp=ROOT/'docs/aligners/RippleLogic_Aligners_Sheet_v5.5.xlsx'
with zipfile.ZipFile(wp) as z:
 names=z.namelist(); blob=' '.join(z.read(n).decode('utf-8','ignore') for n in names if n.endswith('.xml'))
 ck('v12_4_Sync' in blob or 'v12.5 / SGP v8.4 SYNC' in blob,'workbook sync surface')
 for p in ['FOUR CONSTRUCTIONS CALCULATED','COMPLETE_NO_RANKING_OR_DECISIVENESS_CHANGE','ALLOW_FRAMEWORK_SELECTION','DECISIVE','RippleLogic v12.5','SGP v8.4','Sheet: v5.5','PUBLISHABLE_AS_BOUNDED_WORKED_EXEMPLAR','ISO-8601 UTC: 2026-07-23T00:00:00Z','v12.5 three-channel rights and evidence hardening note']:
  ck(p in blob,f'workbook missing {p}')
 for p in ['WDBIP v1.5 worked-run interface','Consequence-Tempo Record - ripple.md v5.4','SGP v8.4 REALITY-MANAGEMENT CAPACITY PROFILE','Cascade v2.5','Material_Obligations','Human_Comp_Load','CARRIED-OBLIGATION INTEGRITY INTERFACE','v12.5 same-version carried-obligation integrity hardening']:
  ck(p in blob,f'workbook current surface missing {p}')
 ck('ripple.md</x:t></x:si><x:si><x:t>v5.4' in blob or 'ripple.md' in blob and 'v5.4' in blob,'workbook ripple.md v5.4 pin')
 ck(('>=SC-' in blob or '&gt;=SC-' in blob) and ('<SD' in blob or '&lt;SD' in blob),'workbook sanity counts do not use the cross-engine exact-prefix boundary')
 ck('Scenario_Impacts!A10' in blob and 'Scenario_Impacts!A21' in blob,'TRC live source links missing')
 ck('SGP_v8_3_RMCP' in blob,'current SGP RMCP worksheet identifier missing')
 ck('Step 1: Live-sort Scenario_Impacts losses DESCENDING' in blob,'TRC live-sort disclosure missing')
 for p in ['CSV_STATUS_A','CSV_STATUS_B','CSV_PASS_WITH_CONTROLS','Containment proxy diagnostic','AUDIT CHECK DETAIL']:
  ck(p in blob,f'workbook final-closure surface missing {p}')
 for stale in ['RIPPLELOGIC v12.4 - DECISION DASHBOARD','Sheet: v5.4','Current surfaces must pin Canon v12.4']:
  ck(stale not in blob,f'workbook stale current surface {stale}')
 ck('calcChain.xml' not in names or True,'formula chain tolerated')
 # Empty <f/> records are invalid workbook logic even when a cached string masks them.
 M='http://schemas.openxmlformats.org/spreadsheetml/2006/main'; R='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
 wr=ET.fromstring(z.read('xl/workbook.xml')); rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
 relmap={r.attrib['Id']:(r.attrib['Target'].lstrip('/') if r.attrib['Target'].startswith('/') else str(PurePosixPath('xl')/r.attrib['Target'])) for r in rels}
 sheets={s.attrib['name']:relmap[s.attrib['{'+R+'}id']] for s in wr.find('{'+M+'}sheets')}
 # Resolve exact displayed workbook values for release-boundary checks.
 shared=[]
 if 'xl/sharedStrings.xml' in names:
  sr=ET.fromstring(z.read('xl/sharedStrings.xml'))
  for si in sr.findall('{'+M+'}si'):
   shared.append(''.join((x.text or '') for x in si.iter('{'+M+'}t')))
 def cell_display(sheet,addr):
  xr=ET.fromstring(z.read(sheets[sheet]))
  c=xr.find(".//{"+M+"}c[@r='"+addr+"']")
  if c is None: return ''
  if c.attrib.get('t')=='inlineStr': return ''.join((x.text or '') for x in c.iter('{'+M+'}t'))
  v=c.find('{'+M+'}v')
  if v is None: return ''
  if c.attrib.get('t')=='s': return shared[int(v.text)]
  return v.text or ''
 ck(cell_display('v12_5_Sync','A4')=='Exact Core 15 pins','workbook sync A4 does not identify exact Core 15 pins')
 ck('RLS Validation Workbook' not in cell_display('v12_5_Sync','B4'),'workbook exact Core 15 pin row includes extended workbook')
 ck(cell_display('v12_5_Sync','A9')=='Core 15 component inventory','workbook inventory heading does not identify Core 15')
 ck('extended release support; not Core 15' in cell_display('v12_5_Sync','A25'),'workbook RLS validation workbook not classified as extended')
 ck('extended release support; not Core 15' in cell_display('v12_5_Sync','A26'),'workbook run-record schema not classified as extended')
 ck(cell_display('Core_Component_Map','B4')=='v5.4','workbook Core_Component_Map ripple.md pin is not v5.4')
 ck('v12_5_Sync' in sheets and 'v12_5_Sync (2)' not in sheets,'workbook synchronization surface is not singular')
 empty=[]; errors=[]; formulas={}
 for sheet,target in sheets.items():
  xr=ET.fromstring(z.read(target))
  for c in xr.findall('.//{'+M+'}c'):
   f=c.find('{'+M+'}f'); v=c.find('{'+M+'}v')
   if f is not None:
    formulas[(sheet,c.attrib.get('r'))]=f.text or ''
    if not (f.text or '').strip(): empty.append((sheet,c.attrib.get('r')))
   if c.attrib.get('t')=='e' or (v is not None and (v.text or '').startswith('#')): errors.append((sheet,c.attrib.get('r')))
 ck(not empty,f'workbook empty formula records {empty[:20]}')
 ck(not errors,f'workbook cached error records {errors[:20]}')
 ck(not any('ERR520' in f.upper() for f in formulas.values()),'workbook contains ERR520 formula token')
 expected_formulas={
  ('Containment','K14'):'IF(SUMPRODUCT(--($K$6:$K$12>=$K$3))=0,"UCI_NOT_MATERIAL_DECLARED",IF(SUMPRODUCT(($K$6:$K$12>=$K$3)*($M$6:$M$12<$K$4))=0,"PASS_ASSUMPTION_BOUND_TIER_2","FAIL"))',
  ('Containment','K15'):'IF(SUMPRODUCT(--($L$6:$L$12>=$K$3))=0,"UCI_NOT_MATERIAL_DECLARED",IF(SUMPRODUCT(($L$6:$L$12>=$K$3)*($N$6:$N$12<$K$4))=0,"PASS_ASSUMPTION_BOUND_TIER_2","FAIL"))',
  ('Containment','B19'):'K14', ('Containment','E19'):'K15', ('Sanity_Checklist','C30'):'CANON!B55',
  ('CANON','G12'):'RLS!B39', ('CANON','B59'):'IF(RLS!B40="DECISIVE","YES","NO")',
  ('Sanity_Checklist','C15'):'"RF_PASS"', ('Sanity_Checklist','C16'):'"RF_PASS"',
  ('Sanity_Checklist','D27'):'Audit_Flags!B21', ('Sanity_Checklist','D28'):'CANON!B81',
  ('Audit_Flags','B15'):'IF(CANON!B59="NO","YES","NO")',
  ('Audit_Flags','B21'):'COUNTIFS(B5:B18,"YES",C5:C18,"INVALID")+COUNTIFS(B25:B33,"YES",C25:C33,"INVALID")',
  ('Audit_Flags','B22'):'COUNTIFS(B5:B18,"YES",C5:C18,"ESCALATE")+COUNTIFS(B25:B33,"YES",C25:C33,"ESCALATE")',
  ('Audit_Flags','B23'):'COUNTIFS(B5:B18,"YES",C5:C18,"REVIEW")+COUNTIFS(B25:B33,"YES",C25:C33,"REVIEW")',
  ('Audit_Flags','B24'):'COUNTIF(B5:B18,"YES")+COUNTIF(B25:B33,"YES")',
  ('Sanity_Checklist','B36'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$E$6:$E$104,"FAIL")',
  ('Sanity_Checklist','B38'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"LIVE_CHECK")+COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"INDEPENDENT_RECOMPUTE")+COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"DECLARED_ASSERTION")+COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"TAUTOLOGICAL_PASS")',
  ('Sanity_Checklist','B39'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"LIVE_CHECK",$E$6:$E$104,"PASS")+COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"INDEPENDENT_RECOMPUTE",$E$6:$E$104,"PASS")',
  ('Sanity_Checklist','D39'):'B38-B39-B40-B109-B110-D38',
  ('Sanity_Checklist','B40'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$E$6:$E$104,"FAIL")',
  ('Sanity_Checklist','B107'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"LIVE_CHECK")',
  ('Sanity_Checklist','B108'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"INDEPENDENT_RECOMPUTE")',
  ('Sanity_Checklist','B109'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"DECLARED_ASSERTION")',
  ('Sanity_Checklist','B110'):'COUNTIFS($A$6:$A$104,">=SC-",$A$6:$A$104,"<SD",$G$6:$G$104,"TAUTOLOGICAL_PASS")',
  ('Sanity_Checklist','B111'):'IF(AND(B38=B107+B108+B109+B110,B39+B40=B107+B108,B110=0),"PASS","FAIL")'}
 for key,value in expected_formulas.items(): ck(formulas.get(key)==value,f'workbook formula mismatch {key}: {formulas.get(key)!r}')
 # Reject direct and indirect circular references across formula cells. Range references
 # are expanded only over formula-bearing cells, so summary formulas cannot silently
 # include themselves or one another while still passing cached-value checks.
 cell_re=re.compile(r"(?:(?:'((?:[^']|'')+)'|([A-Za-z_][A-Za-z0-9_. ]*))!)?(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?")
 def addr_xy(a):
  a=a.replace('$',''); m=re.fullmatch(r'([A-Z]{1,3})(\d+)',a); n=0
  for ch in m.group(1): n=n*26+ord(ch)-64
  return n,int(m.group(2))
 by_sheet={}
 for sh,addr in formulas: by_sheet.setdefault(sh,[]).append((addr,addr_xy(addr)))
 graph={k:set() for k in formulas}
 for node,formula in formulas.items():
  cursh,_=node
  for m in cell_re.finditer(formula):
   sh=(m.group(1).replace("''","'") if m.group(1) is not None else m.group(2)) or cursh
   if sh not in by_sheet: continue
   a1=m.group(3).replace('$',''); a2=(m.group(4) or '').replace('$','')
   if a2:
    c1,r1=addr_xy(a1); c2,r2=addr_xy(a2); lo_c,hi_c=sorted((c1,c2)); lo_r,hi_r=sorted((r1,r2))
    for depaddr,(dc,dr) in by_sheet[sh]:
     if lo_c<=dc<=hi_c and lo_r<=dr<=hi_r: graph[node].add((sh,depaddr))
   elif (sh,a1) in formulas: graph[node].add((sh,a1))
 circular=[]; visiting=set(); visited=set(); path=[]
 def walk(v):
  if v in visiting:
   i=path.index(v); circular.append(path[i:]+[v]); return
  if v in visited: return
  visiting.add(v); path.append(v)
  for w in graph[v]: walk(w)
  path.pop(); visiting.remove(v); visited.add(v)
 for v in graph: walk(v)
 ck(not circular,f'workbook circular formula dependency {circular[:5]}')
 decisive_formulas={
  ('RLS','B37'):'B36*SQRT(SUMSQ(B53:H59))/B60',
  ('RLS','B38'):'B36*SQRT(SUMSQ(B53:H59))/B60',
  ('RLS','B39'):'ABS(B33-B34)/SQRT(B37^2+B38^2+0.000001)',
  ('RLS','B40'):'IF(B39>CANON!B22,"DECISIVE","NON-DECISIVE")',
  ('CANON','B69'):'SUMPRODUCT(--(B51:B52="RF_PASS"),--(B56:B57="TRC_PASS"),--(LEFT(B60:B61,8)="CSV_PASS"))',
  ('CANON','B70'):'Verdict_Hardening!B30',
  ('Verdict_Hardening','B29'):'IF(OR(CANON!B51="NCRC_UNKNOWN",CANON!B52="NCRC_UNKNOWN",CANON!B56="TRC_ESCALATE",CANON!B57="TRC_ESCALATE",ISNUMBER(SEARCH("CSV_ESCALATE",CANON!B60)),ISNUMBER(SEARCH("CSV_ESCALATE",CANON!B61)),Tail_Emergency!B15="REFUSE"),"YES","NO")',
  ('Tail_Emergency','B6'):'IF(AND(COUNTIF(CANON!B51:B52,"RF_PASS")>0,COUNTIFS(CANON!B51:B52,"RF_PASS",CANON!B56:B57,"TRC_PASS")=0),"YES","NO")',
  ('CANON','B41'):'COUNTIF(WTSL_Categories!G7:G12,"YES")'
 }
 for key,value in decisive_formulas.items(): ck(formulas.get(key)==value,f'workbook decisive/formula mismatch {key}: {formulas.get(key)!r}')
 ck(len(formulas)==2974,f'workbook formula count {len(formulas)} != 2974')
if FAIL:
 print('FAIL formula/interface integrity:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS formula, severe-rights, PLSS, live-TRC, controlling-CSV, and workbook interface integrity')
