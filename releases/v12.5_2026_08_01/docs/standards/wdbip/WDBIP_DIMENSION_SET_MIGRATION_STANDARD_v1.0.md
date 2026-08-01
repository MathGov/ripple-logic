# WDBIP Dimension-Set Migration Standard v1.0

## 1. Purpose

This standard governs changes to the welfare-dimension taxonomy used by WDBIP. It prevents silent retroactive recoding, false comparability, and schema drift if evidence later supports narrowing, merging, dividing, adding, or removing a dimension.

**Current dimension set:** `WELFARE_DIMENSION_SET_7D_V1`  
**Current dimensions:** D1 Material, D2 Health, D3 Social, D4 Knowledge, D5 Agency, D6 Meaning, D7 Environment.

The seven dimensions are an auditable anti-omission and classification architecture, not a metaphysically exhaustive claim.

## 2. Migration triggers

A governed review may be initiated by:

- persistent low inter-rater reliability;
- excessive `BOUNDARY_CONTESTED` rates;
- poor discriminant validity across credible models;
- systematic cultural or substrate non-invariance;
- no incremental decision value;
- repeated omission of a material construct;
- repeated double counting caused by the taxonomy;
- severe gaming vulnerability;
- disproportionate implementation burden;
- a governed Canon revision.

## 3. Required proposal contents

A dimension-set proposal SHALL contain:

1. proposed taxonomy identifier and version;
2. definitions and exclusion boundaries;
3. evidence and alternative models;
4. expected benefits, costs, and new gaming risks;
5. crosswalk from every old dimension and token type;
6. schema and validator changes;
7. historical comparability classification;
8. active-decision rerun rule;
9. public challenge and appeal process;
10. independent review and adoption authority.

## 4. Record immutability

Existing records retain their original:

- WDBIP version;
- dimension-set version;
- schema version;
- evidence and model versions;
- hashes and timestamps.

They SHALL NOT be silently overwritten, relabeled, or recalculated under a later taxonomy.

## 5. Crosswalk statuses

Each old token or dimension mapping SHALL receive one status:

| Status | Meaning |
|---|---|
| `MIGRATION_EXACT` | Semantics and use are materially unchanged. |
| `MIGRATION_NARROWER` | New construct is a documented subset of the old construct. |
| `MIGRATION_BROADER` | New construct includes additional content. |
| `MIGRATION_SPLIT` | Old construct maps to multiple new constructs. |
| `MIGRATION_MERGED` | Multiple old constructs map to one new construct. |
| `MIGRATION_RECLASSIFIED` | Primary home changes without simple set inclusion. |
| `MIGRATION_NONCOMPARABLE` | No defensible direct bridge exists. |
| `MIGRATION_CONTESTED` | Credible disagreement remains. |

## 6. Historical comparability

For each metric or result, declare:

- `COMPARABLE_AS_RECORDED`;
- `COMPARABLE_WITH_BRIDGE_MODEL`;
- `COMPARABLE_FOR_QUALITATIVE_TREND_ONLY`;
- `NONCOMPARABLE`.

A bridge model requires evidence, uncertainty, and validation appropriate to the claim. A crosswalk table alone does not prove score equivalence.

## 7. Active-decision rerun

An active or monitored decision SHALL be rerun when taxonomy change could materially alter:

- primary dimension assignment;
- duplicate-effect treatment;
- subgroup harm visibility;
- gate routing;
- option ranking or decisiveness;
- weight sensitivity;
- monitoring or reopening triggers.

Low-stakes historical records may remain unrecomputed if clearly labeled and no current claim depends on them.

## 8. Schema and validator synchronization

A taxonomy revision is not released until the following are synchronized and hash-pinned:

- canonical definitions;
- Markdown, DOCX, and PDF protocol;
- JSON Schema;
- validator;
- passing and failing vectors;
- worked examples;
- PCC fields;
- migration crosswalk;
- component map and manifest.

## 9. No automatic eighth dimension

A new dimension is neither prohibited nor presumed. It must demonstrate a material improvement in coverage, discriminant validity, decision utility, rights protection, or interpretability that justifies its complexity and does not introduce unacceptable overlap or gaming.

## 10. No taxonomy preservation bias

The objective is not to protect the seven-part design from evidence. The objective is to preserve auditable records while improving the measurement architecture when evidence warrants change.
