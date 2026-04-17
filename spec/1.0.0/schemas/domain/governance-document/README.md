Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Governance Document

A strict constitutional-governance schema for authoring the single normative governance source for
Paperhat and other similarly governed semantic systems.

## When to Use

Use `GovernanceDocument` when the document defines shared authority, shared architectural doctrine,
shared contributor obligations, shared prohibitions, shared conflict rules, or mandatory
restatement rules for an entire governed corpus.

This schema exists for constitutional governance, not for general governance, risk, and compliance
record-keeping.

## Concepts

| Concept | Kind | Entity | Content | Description |
|---|---|---|---|---|
| GovernanceDocument | Semantic | MustNotBeEntity | ForbidsContent | Root constitutional governance document with required front-matter traits and one or more GovernanceSection children. |
| GovernanceSection | Semantic | MustBeEntity | ForbidsContent | Recursive section block with stable identity for governance structure. |
| GovernancePrinciple | Semantic | MustBeEntity | ForbidsContent | A stable constitutional principle such as determinism, source-of-truth authority, or non-deception. |
| GovernanceRequirement | Semantic | MustBeEntity | ForbidsContent | A binding governance requirement with strict Must or MustNot modality. |
| GovernanceAuthorityRule | Semantic | MustBeEntity | ForbidsContent | A rule defining authority flow, precedence, or normative-source status. |
| GovernanceConflictRule | Semantic | MustBeEntity | ForbidsContent | A rule defining conflict resolution between sources or statements. |
| GovernanceBoundary | Semantic | MustBeEntity | ForbidsContent | A rule defining a hard architectural or semantic boundary. |
| GovernanceRestatementRule | Semantic | MustBeEntity | ForbidsContent | A rule governing how shared governance claims are repeated in secondary documents. |
| GovernanceSectionReference | Semantic | MustNotBeEntity | ForbidsContent | Internal reference to a GovernanceSection entity. |
| GovernanceSourceClause | Semantic | MustNotBeEntity | ForbidsContent | Explicit clause naming the normative governance source that governs a restated claim. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| conf | `paperhat:domain:conformance-class` | Reuses conformance clauses, classes, and requirement bindings for governed document classes. |
| specbase | `paperhat:domain:specification-foundation` | Reuses shared specification traits, notes, rationale blocks, and external references. |
| cite | `paperhat:domain:citation` | Provides Citation for evidence-rich governance rules. |
| desc | `paperhat:domain:description` | Provides structured descriptive text where needed. |
| list | `paperhat:domain:list` | Provides ordered and unordered lists. |
| text | `paperhat:domain:text` | Provides Paragraph blocks. |

## Shared Trait Reuse

This schema deliberately reuses the following traits from `specbase`:

- `editor`
- `locked`
- `normative`
- `title`
- `version`
- `key`
- `conformance`
- `division`
- `designation`
- `deprecated`
- `deprecatedSince`
- `label`
- `target`
- `modality`

## Local Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| governanceScope | $EnumeratedToken | no | Closed classification for the scope of a governance rule, such as workspace, repository, specification, implementation, foundry, projection, or contributor. |

## Constraints

| Identifier | Description |
|---|---|
| governance-section-reference-target-type | GovernanceSectionReference target must be a GovernanceSection. |
| governance-section-reference-must-resolve | GovernanceSectionReference target must resolve. |
| governance-source-clause-target-entity | GovernanceSourceClause target must be an entity. |
| governance-source-clause-must-resolve | GovernanceSourceClause target must resolve. |

## Design Notes

- This schema is intentionally constitutional. It models authority, conflict, boundary, and
  restatement semantics directly instead of treating them as untyped prose.
- The schema reuses the specification foundation for stable keys, front matter, notes, rationale,
  and modality rather than rebuilding those primitives.
- `GovernanceSourceClause` exists because repeated governance claims must carry an explicit
  normative-source clause. The clause is not optional decoration. It is part of the governance
  model.
- `GovernanceRequirement` is restricted to Must and MustNot modality only.
- Existing `conformance-class` is reused as a leaf schema because its conformance binding model fits
  governed document classes without duplicating that structure locally.
- The existing `policy` schema remains useful for institutional policies, but it is not sufficient
  for constitutional governance because it leaves precedence, conflict, and restatement semantics
  untyped.
- The `governance-spec` repository under `specifications/libraries/` is the constitutional
  governance source that this schema is designed to author.

---

**End of Governance Document v1.0.0**
