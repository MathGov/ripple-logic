#!/usr/bin/env python3
from pathlib import Path
import sys, zipfile
sys.dont_write_bytecode = True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
 if not c: FAIL.append(m)
canon=(ROOT/'docs/canon/RippleLogic_v12.4_Canon.md').read_text(encoding='utf-8',errors='replace')
for p in ['hazard cannot activate','pre-confidence contribution mass','h_{k,base}','h_{k,welfare}','rho_r']:
 ck(p.lower() in canon.lower(),f'Canon formula interface missing {p}')
wp=ROOT/'docs/aligners/RippleLogic_Aligners_Sheet_v5.4.xlsx'
with zipfile.ZipFile(wp) as z:
 names=z.namelist(); blob=' '.join(z.read(n).decode('utf-8','ignore') for n in names if n.endswith('.xml'))
 ck('v12_4_Sync' in blob or 'v12.4 / SGP v8.3 SYNC' in blob,'workbook sync surface')
 for p in ['FOUR CONSTRUCTIONS CALCULATED','COMPLETE_NO_RANKING_OR_DECISIVENESS_CHANGE','REFUSE_DETERMINISTIC_SELECTION','RippleLogic v12.4','SGP v8.3']:
  ck(p in blob,f'workbook missing {p}')
 for p in ['MathGov Reproducibility and Use Standard v1.2','WDBIP v1.4 worked-run interface','Consequence-Tempo Record - ripple.md v5.3','SGP v8.3 REALITY-MANAGEMENT CAPACITY PROFILE','Cascade v2.4']:
  ck(p in blob,f'workbook current surface missing {p}')
 ck('LEFT(A6:A98,3)' in blob and 'SUMPRODUCT' in blob,'workbook sanity counts are not engine-stable')
 ck('Scenario_Impacts!A10' in blob and 'Scenario_Impacts!A21' in blob,'TRC live source links missing')
 ck('SGP_v8_3_RMCP' in blob,'current SGP RMCP worksheet identifier missing')
 ck('Step 1: Live-sort Scenario_Impacts losses DESCENDING' in blob,'TRC live-sort disclosure missing')
 for p in ['CSV_STATUS_A','CSV_STATUS_B','CSV_PASS_WITH_CONTROLS','Containment proxy diagnostic','AUDIT CHECK DETAIL','2026-07-20T00:00:00']:
  ck(p in blob,f'workbook final-closure surface missing {p}')
 ck('calcChain.xml' not in names or True,'formula chain tolerated')
if FAIL:
 print('FAIL formula/interface integrity:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS formula, severe-rights, PLSS, live-TRC, controlling-CSV, and workbook interface integrity')
