# Revision History

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines structured revision history for specifications. Each revision entry records a version, date, editor or author, and a list of individual changes classified by kind. Changes optionally reference the affected section, requirement, or other entity by IRI. This is distinct from `release:Release` (which tracks product snapshots) — revision history is about the evolution of the specification document itself.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| RevisionHistory | Semantic | MustNotBeEntity | ForbidsContent | RevisionEntry (1+, ordered) | Top-level container for the revision history of a specification. |
| RevisionEntry | Semantic | MustBeEntity | ForbidsContent | Change (1+), Description, Paragraph | A single revision record. Carries version, date, and editor/author. Cross-referenceable by key. |
| Change | Semantic | MustNotBeEntity | ForbidsContent | Paragraph (1+), Description | An individual change within a revision. Classified by kind, with optional reference to the affected item. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `title` | `$Text` | -- | Optional title for the revision history section. |
| `version` | `$Semantic Version` | -- | Semantic version of the specification for this revision. |
| `date` | `$Text` | -- | Revision date in ISO 8601 format. |
| `editor` | `$Text` | -- | Editor responsible for this revision. |
| `author` | `$Text` | -- | Author of this revision. |
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `label` | `$Text` | -- | Short display label. |
| `changeKind` | `$EnumeratedToken` | ChangeKind | Classification of the change. |
| `affectedItem` | `$Iri` | reference | Reference to the entity affected by the change. |
| `affectedItemLabel` | `$Text` | -- | Human-readable label for the affected item when the reference cannot be resolved. |

## Enumerated Value Sets

### ChangeKind (7 members)

| Member | Description |
|---|---|
| `Added` | New content added to the specification. |
| `Removed` | Content removed from the specification. |
| `Modified` | Existing content changed in substance. |
| `Deprecated` | Content marked as deprecated. |
| `Fixed` | Erratum or defect corrected. |
| `Clarified` | Existing content reworded for clarity without changing meaning. |
| `Reorganized` | Content moved or restructured without changing substance. |

## Constraints

| Constraint | Target | Rule | Description |
|---|---|---|---|
| affected-item-must-resolve | Change | ReferenceMustResolve | The affectedItem reference must resolve to an existing entity. |

## Design Decisions

- `RevisionEntry` is MustBeEntity so individual revisions are cross-referenceable (e.g. "see changes in revision 2.1.0").
- `Change` requires at least one Paragraph child for the change description. This is structured prose, not a simple text trait, because change descriptions often span multiple sentences.
- `affectedItem` is a reference trait pointing to any entity (Section, Requirement, etc.). No `ReferenceTargetsConcept` constraint because the target is any entity type in the specification.
- `affectedItemLabel` complements `affectedItem` for cases where the referenced item has been removed (the reference cannot resolve, but the label preserves what was affected).
- `Clarified` and `Reorganized` are distinct from `Modified`: clarifications don't change meaning, and reorganizations don't change substance. This distinction matters for conformance impact analysis.
- `version` uses `$Semantic Version` to ensure machine-parseable version strings. `date` is `$Text` because Codex lacks a native date type.
- RevisionHistory is distinct from ISO EditionHistory (in iso-document-metadata): edition history records major ISO publication milestones; revision history records granular per-version changes.
