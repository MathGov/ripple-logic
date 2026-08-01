#!/usr/bin/env python3
from pathlib import Path
import sys, json, csv, re
sys.dont_write_bytecode = True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
 if not c: FAIL.append(m)
def txt(r): return (ROOT/r).read_text(encoding='utf-8',errors='replace')
canon=txt('docs/canon/RippleLogic_v12.5_Canon.md')
sgp=txt('docs/sgp/SGP_v8.4.md')
primer=txt('docs/primer/RippleLogic_Foundations_Primer_v4.3.md')
intro=txt('docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.md')
agent=txt('docs/agents/RippleLogic_Agent_System_v12.3.md')
csv_std=txt('docs/standards/CSV_Gate_Standard_v2.3.md')
for p in ['RG -> RF/NCRC -> TRC -> CSV -> RLS','no sixth gate','unknown, not zero','selection from execution authority','rho_r','h_{k,base}','h_{k,welfare}']:
 ck(p.lower() in canon.lower(),f'Canon missing {p}')
for p in ['DIRECT_Q_NORMALIZATION_V1','Phantom-dependence rule','Weight-separability assumption','Provisional-UCI high-stakes restriction','accountability-and-flourishing field']:
 ck(p.lower() in canon.lower(),f'Canon final-closure surface missing {p}')
ck('to ensure the example produces a decisive rls lead' not in canon.lower(),'post-hoc worked-example tuning sentence remains')

for phrase in ['Reviewer-to-machine status crosswalk (Normative)','Sign-aware reach-bound rule (Normative)','counterfactual/audit-only tail calculation']:
 ck(phrase.lower() in canon.lower(),f'Canon finishing-touch surface missing {phrase}')
repro=txt('docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.md')
ck('reviewer-to-machine status crosswalk (normative)' in repro.lower(),'Reproducibility standard missing RG reviewer-machine crosswalk')
ripple=txt('docs/standards/ripple_md_Standard_v5.4.md')
ck('goal structuring notation community standard, version 3' in ripple.lower(),'ripple.md missing GSN Version 3')
ck('gsn community standard v2' not in ripple.lower() and 'version 2.' not in ripple.lower(),'ripple.md stale GSN Version 2 reference')

for p in ['Human FPP-100','open P100 plateau','capacity score creates standing or authority','weaponization_signatures_checked','remediation_and_rereview_reference']:
 ck(p.lower() in sgp.lower(),f'SGP missing {p}')
for p in ['SGP83-IF-01','SGP83-IF-17','MPS-NE','Public-summary rule']:
 ck(p.lower() in sgp.lower(),f'SGP final-closure surface missing {p}')
ck('sgp8-if-' not in sgp.lower() and 'sgp81-if-' not in sgp.lower(),'stale current SGP conformance-vector ID family remains')
ck('p101' not in re.sub(r'no p101','',sgp.lower()),'active P101 hierarchy found')
for p in ['RG_SUPPORTED','RG_NARROWED','TRC_NOT_TRIGGERED','CSV_PASS_WITH_CONTROLS']:
 ck(p.lower() in primer.lower(),f'Primer admissibility/selectability surface missing {p}')
for p in ['REFUSE_DETERMINISTIC_SELECTION','AuthoritySelectionRecord','unique decisive leader']:
 ck(p.lower() in intro.lower(),f'Public Introduction decision-state surface missing {p}')
for p in ['NCRC_UNKNOWN','CSV_FAIL','CSV_REDESIGN_REQUIRED','review conditions']:
 ck(p.lower() in agent.lower(),f'Agent self-audit/routing surface missing {p}')
csv_flat=' '.join(csv_std.lower().split())
ck('must not be the sole basis of a high-stakes' in csv_flat and 'structured csv evidence case' in csv_flat,'CSV Standard missing provisional-UCI restriction')
for p in ['reality-reference boundary','material obligation integrity','hidden human compensation load','dependency-localized falsification rule']:
 ck(p in canon.lower(),f'Canon obligation/reality hardening missing {p}')
for p in ['binding-control minimum','procedure occurred or a review was recorded does not establish','hidden human compensation load']:
 ck(p in csv_flat,f'CSV obligation-integrity surface missing {p}')
for p in ['carrier-nonperformance rule','hidden-human-compensation rule','affected obligation id']:
 ck(p in agent.lower(),f'Agent obligation-integrity surface missing {p}')
rows=list(csv.DictReader((ROOT/'docs/canon/AD_49_Cell_Welfare_Dictionary.csv').open(encoding='utf-8-sig')))
ck(len(rows)==49,f'49-cell dictionary count {len(rows)}')
schema=json.loads(txt('schemas/mathgov_run_record_v3.schema.json'))
ident=schema['properties']['identity']['properties']
ck(ident['canon_version'].get('const')=='v12.5','schema Canon pin')
ck(ident['ripple_md_version'].get('const')=='v5.4','schema wrapper pin')
rcp=schema['properties']['responsibility_continuity']['properties']
ck('material_obligations' in rcp and 'human_compensation_load' in rcp,'schema obligation-integrity fields')
w=txt('docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.md').lower()
for p in ['not an eighth welfare dimension','not an option gate','provenance and compliance certificate','all-encompassing infinite union','accountability-and-flourishing field']:
 ck(p in w,f'WDBIP missing {p}')
for rel in ['VALIDATION_STATUS.md','RELEASE_CLAIMS_AND_NON_CLAIMS.md','CAPABILITIES_AND_BOUNDARIES.md']:
 t=txt(rel)
 for line in t.splitlines():
  if 'v12.2' in line and line.lstrip().startswith('##'):
   ck('historical' in line.lower() or 'lineage' in line.lower(),f'{rel} contains stale active v12.2 section heading: {line}')
if FAIL:
 print('FAIL semantic surfaces:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS semantic, cascade, type, claim-boundary, and final-closure surfaces')
