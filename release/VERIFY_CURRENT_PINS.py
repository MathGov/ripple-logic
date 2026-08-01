#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, yaml, zipfile
sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
FAIL=[]
def ck(c,m):
    if not c: FAIL.append(m)
def txt(r): return (ROOT/r).read_text(encoding='utf-8',errors='replace')

vm=yaml.safe_load(txt('VERSION_MANIFEST.yaml'))
release_id='MathGov_Core_2026_09_v12.5_SGP_v8.4'
ck(vm.get('release_id')==release_id,'release id')
ck(vm.get('release_line')=='v12.5','release line')
ck(vm.get('exact_release_version')=='v12.5','exact release version')
ck(vm.get('governing_cascade')=='RG -> RF/NCRC -> TRC -> CSV -> RLS','governing cascade')

expected={
'docs/canon/RippleLogic_v12.5_Canon.md':['RippleLogic Canon v12.5','pins Sentience Gradient Protocol v8.4','active normative rules in this artifact apply under the v12.5 line','Any implementation claiming v12.5 conformance','WDBIP: v1.5','Foundations Primer: v4.3','CSV Gate Standard: v2.3','I_rights(u,d,a,r)','The canonical source terminates after Appendix AX','RippleLogic Aligners Sheet: v5.5','RLS Validation Workbook: v0.3'],
'docs/sgp/SGP_v8.4.md':['Sentience Gradient Protocol v8.4','Canonical Architecture','RippleLogic v12.5 consumes only','The current protocol preserves the separation','Identifier stability note','E.0B Configuration-Bound Evidence and Capability-Language Discipline','E.0C Current Release at a Glance'],
'docs/standards/ripple_md_Standard_v5.4.md':['ripple.md Standard v5.4','canon_v12.5_section_10.2A','No wrapper obligation becomes a sixth'],
'docs/agents/RippleLogic_Agent_System_v12.3.md':['Agent System v12.3','"core_release": "2026.09-v12.5"','Spec Version        | RippleLogic v12.5','REFUSE_DETERMINISTIC_SELECTION','"agent_package_version": "12.3"','canon_v12.5_section_10.2A'],
'docs/standards/CSV_Gate_Standard_v2.3.md':['CSV Gate Standard v2.3'],
'docs/standards/RippleLogic_Cascade_Standard_v2.5.md':['Cascade Standard v2.5'],
'docs/implementation/MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.md':['Reproducibility and Use Standard v1.3'],
'docs/standards/wdbip/Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.md':['Welfare Dimension Boundary and Interaction Protocol v1.5','The v12.5 release incorporates','Sentience Gradient Protocol v8.4','v1_5','artifact namespace'],
'docs/validation/rls/RippleLogic_RLS_Validation_Protocol_v2_5.md':['RLS Validation Protocol v2.5','RippleLogic v12.5 Canon','v12.5 mandatory conformance vectors','RLS_Validation_Workbook_v0.3'],
'docs/primer/RippleLogic_Foundations_Primer_v4.3.md':['Foundations Primer','Release alignment (v12.5)','ripple.md Standard v5.4'],
'docs/guides/MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.md':['Public Introduction v12.5'],
'docs/standards/Physical_Causal_Admissibility_Evidence_Profile_v2.2.md':['Evidence Profile v2.2'],
'docs/standards/Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.md':['Integrity Standard v2.2'],
'docs/standards/Source_Coupling_Integrity_Standard_v2.2.md':['Source-Coupling Integrity Standard v2.2'],
}
for rel,phrases in expected.items():
    p=ROOT/rel; ck(p.is_file(),f'missing {rel}')
    if p.is_file():
        s=txt(rel)
        for phrase in phrases: ck(phrase.lower() in s.lower(),f'{rel} missing {phrase}')

# Explicit release-facing identity surfaces. Historical changelogs are intentionally excluded.
release_surface={
'NOTICE':['MathGov Core Release 2026.09 v12.5 / SGP v8.4','Configuration-Bound Assurance Public Research Source Release'],
'CAPABILITIES_AND_BOUNDARIES.md':['MathGov Core v12.5','Run-record schema v3'],
'FUTURE_WORK_ROADMAP.md':['Current v12.5 Release','current v12.5 Tier 1-3'],
'ROADMAP.md':['Current v12.5 / SGP v8.4','Current v12.5 source work'],
'GLOSSARY_AND_ACRONYM_INDEX.md':['Release 2026.09 v12.5 / SGP v8.4','WDBIP v1.5','ripple.md v5.4','Run-record schema v3'],
'ARTIFACT_ROLE_MAP.md':['Reproducibility and Use Standard v1.3','Run Record Schema v3','Run-record schema v3'],
'RELEASE_CLAIMS_AND_NON_CLAIMS.md':['v12.5 integration note','Run-record schema v3'],
'LINEAGE.md':['Current: v12.5 / SGP v8.4','run-record schema v3'],
'docs/assurance/README.md':['MathGov Core v12.5'],
'docs/assurance/DISTRIBUTION_SHIFT_AND_REQUALIFICATION_PROTOCOL.md':['MathGov Core v12.5'],
'docs/assurance/ALIGNMENT_SCOPE_AND_CONTROL_LAYER_BOUNDARY.md':['MathGov Core v12.5','current v12.5 claim'],
'docs/assurance/SCIENTIFIC_MATURITY_LADDER.md':['Current v12.5 status'],
'docs/validation/rls/RLS_Validation_Package_README.md':['Core Release 2026.09 v12.5','Canon v12.5'],
'docs/guides/GATE_BOUNDARY_DISCRIMINATOR_TRC_CSV_RLS.md':['Core Release 2026.09 v12.5'],
'docs/guides/PHYSICAL_ADMISSIBILITY_AND_EXECUTION_BOUNDARY.md':['Core Release 2026.09 v12.5 / SGP v8.4'],
'release/CITATION_VERIFICATION_REPORT.md':['MathGov v12.5 / SGP v8.4','Sentience Gradient Protocol v8.4','Top 10 for Agentic Applications for 2026','Center for AI Standards and Innovation'],
'README.md':['Core 15 component pins','Extended release-support pins','fourteen DOCX reading mirrors','RLS Validation Workbook v0.3'],
'core_15/README.md':['fourteen genuine OOXML DOCX reading mirrors','worked-run exemplar','not a validator','release/SHA256SUMS_CORE15.txt'],
}
for rel,phrases in release_surface.items():
    s=txt(rel)
    for phrase in phrases: ck(phrase.lower() in s.lower(),f'{rel} missing current release phrase: {phrase}')

# Stale live-current identifiers that must not survive active release-facing surfaces.
for rel in release_surface:
    s=txt(rel)
    for pat in [r'Current v12\.[0-4]\b',r'current v12\.[0-4]\b',r'MathGov Core v12\.[0-4]\b',r'MathGov Core Release 2026\.09 v12\.[0-4]\b',r'Run-record v[12]\b',r'Run Record Schema v[12]\b']:
        ck(not re.search(pat,s),f'{rel} stale active identity: {pat}')
canon=txt('docs/canon/RippleLogic_v12.5_Canon.md')
ck('RippleLogic Aligners Sheet: v5.4' not in canon,'Canon stale Aligners v5.4 current-line pin')
ck('RLS Validation Workbook: v0.2' not in canon,'Canon stale RLS workbook v0.2 current-line pin')
ck('No such extension is normative in v12.5.' in canon,'Canon Appendix N future-extension boundary not current to v12.5')
ck('Integrates SGP v8.3 type-separated' in canon and 'Aligners Sheet v5.4' in canon,'Canon v12.4 lineage pins')
ck('Core operating-document pins are' in canon and 'complete release inventory' in canon and 'VERSION_MANIFEST.yaml' in canon,'Canon release-inventory authority boundary')

# Reader-first opening discipline: exact release identity remains in filenames, manifests,
# footers, and appendices rather than release-delta blocks before the abstract.
canon_front=canon.split('# **ABSTRACT**',1)[0]
ck('v12.5 Configuration-Bound Assurance' not in canon_front,'Canon release-delta block still precedes abstract')
ck('Version: 12.5' not in canon_front and 'Date: 23 July 2026' not in canon_front,'Canon version/date metadata still precedes abstract')
ck('Governing interpretation.' in canon_front and 'Appendix AC' in canon_front,'Canon missing concise front-door precedence note')
sgp_text=txt('docs/sgp/SGP_v8.4.md')
sgp_front=sgp_text.split('# **ABSTRACT**',1)[0]
for phrase in ['v8.4 Configuration-Bound Evidence','Current Release at a Glance','Minor release:','Release status:']:
    ck(phrase not in sgp_front,f'SGP release-specific front matter remains before abstract: {phrase}')
ck('Release identity, integration status, and version history are recorded in Appendix E' in sgp_front,'SGP missing clean appendix pointer')

# Active machine-readable current-pin surfaces.
for rel, phrases in {
    'docs/implementation/NORMATIVE_KERNEL_INDEX_v1.0.yaml':['canon_pin: RippleLogic v12.5','Reproducibility and Use Standard v1.3','CSV Gate Standard v2.3'],
    'docs/assurance/PARAMETER_AND_AUTHORITY_LOCK_RECORD.schema.yaml':['canon_pin: RippleLogic v12.5'],
    'docs/standards/wdbip/WDBIP_PROVISIONAL_VALIDATION_TRIGGERS_v1.0.yaml':['wdbip: v1.5'],
}.items():
    s=txt(rel)
    for phrase in phrases: ck(phrase.lower() in s.lower(),f'{rel} missing {phrase}')

schema=json.loads(txt('schemas/mathgov_run_record_v3.schema.json'))
ck(schema['properties']['identity']['properties']['package_release_id'].get('const')==release_id,'run-record schema package release const')
for p in sorted((ROOT/'tests/run_records').glob('*.json')):
    d=json.loads(p.read_text(encoding='utf-8'))
    expected_id = 'MathGov_Core_2026_09_v12.4_SGP_v8.4' if p.name=='fail_wrong_package_release_id.json' else release_id
    ck(d['identity']['package_release_id']==expected_id,f'{p.relative_to(ROOT)} package_release_id')
example=ROOT/'docs/examples/reproducibility/reusable_cups_run_v3.json'
ck(example.is_file(),'missing v3 reproducibility example')
if example.is_file():
    ck(json.loads(example.read_text(encoding='utf-8'))['identity']['package_release_id']==release_id,'v3 example release identity')
ck((ROOT/'docs/examples/reproducibility/REPRODUCIBLE_RUN_WALKTHROUGH_v3.md').is_file(),'missing v3 walkthrough')
ck(not (ROOT/'docs/examples/reproducibility/reusable_cups_run_v2.json').exists(),'obsolete v2 example active')

# Public source hygiene.
for p in ROOT.rglob('*'):
    if p.is_file(): ck(p.suffix.lower() not in {'.pyc','.pyo'},f'compiled artifact {p.relative_to(ROOT)}')
    if p.is_dir(): ck(p.name!='__pycache__',f'bytecode directory {p.relative_to(ROOT)}')

# Exact Core 15 set and genuine OOXML.
core_expected={'CSV_Gate_Standard_v2.3.docx','MATHGOV_3R_1_2_PUBLIC_INTRO_v12_5.docx','MATHGOV_REPRODUCIBILITY_AND_USE_STANDARD_v1.3.docx','Methodological_Falsifiability_and_Dependency_Integrity_Standard_v2.2.docx','Physical_Causal_Admissibility_Evidence_Profile_v2.2.docx','RippleLogic_Agent_System_v12.3.docx','RippleLogic_Aligners_Sheet_v5.5.xlsx','RippleLogic_Cascade_Standard_v2.5.docx','RippleLogic_Foundations_Primer_v4.3.docx','RippleLogic_RLS_Validation_Protocol_v2_5.docx','RippleLogic_v12.5_Canon.docx','SGP_v8.4.docx','Source_Coupling_Integrity_Standard_v2.2.docx','Welfare_Dimension_Boundary_and_Interaction_Protocol_v1.5.docx','ripple_md_Standard_v5.4.docx'}
core=ROOT/'core_15'; actual={p.name for p in core.iterdir() if p.is_file() and p.name!='README.md'} if core.exists() else set()
ck(actual==core_expected,f'Core 15 mismatch missing={core_expected-actual} extra={actual-core_expected}')
for p in core.iterdir() if core.exists() else []:
    if p.suffix.lower() in {'.docx','.xlsx'}: ck(p.read_bytes()[:4]==b'PK\x03\x04',f'not genuine OOXML: {p.name}')

# SGP printed footer current identity.
sgp=ROOT/'docs/sgp/SGP_v8.4.docx'
if sgp.is_file():
    with zipfile.ZipFile(sgp) as z:
        foot=' '.join(z.read(n).decode('utf-8','ignore') for n in z.namelist() if n.startswith('word/footer') and n.endswith('.xml'))
    ck('Sentience Gradient Protocol v8.4' in foot,'SGP footer does not identify v8.4')
    ck('Sentience Gradient Protocol v8.3' not in foot,'SGP footer still identifies v8.3')

if FAIL:
    print('FAIL current pins and release identity:'); [print('-',x) for x in FAIL]; raise SystemExit(1)
print('PASS current v12.5 / SGP v8.4 pins, release-facing identity, machine fixtures, public-source hygiene, and exact Core 15')
