# ISO Document Metadata

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines ISO/IEC-specific document metadata for international standards. This schema supplements the generic `document-metadata` schema with organization-specific structure: committee hierarchy (TC, SC, WG), ISO document numbering and part structure, edition history, ICS classification codes, secretariat assignments, and the structured ISO foreword with its required edition history and part relationships. Designed to capture the metadata mandated by ISO/IEC Directives, Part 2.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| ISODocumentMetadata | Semantic | MustNotBeEntity | ForbidsContent | Committee, Subcommittee, WorkingGroup, ICSClassification, ISOForeword, EditionHistory, RelatedPart, Description | Top-level container for all ISO-specific metadata. Carries document number, part, edition, language, secretariat, publication date, and stage. |
| Committee | Semantic | MustNotBeEntity | ForbidsContent | -- | Technical committee (e.g. ISO/TC 176). Requires number and name; optional type. |
| Subcommittee | Semantic | MustNotBeEntity | ForbidsContent | -- | Subcommittee within a TC (e.g. SC 1). Requires number and name. |
| WorkingGroup | Semantic | MustNotBeEntity | ForbidsContent | -- | Working group within a SC or TC (e.g. WG 24). Requires number; name optional. |
| ICSClassification | Semantic | MustNotBeEntity | ForbidsContent | -- | International Classification for Standards entry. Requires ICS code; title optional. |
| ISOForeword | Semantic | MustNotBeEntity | ForbidsContent | EditionHistory, RelatedPart, Paragraph, Description | Structured ISO foreword section containing edition history, part relationships, and introductory prose. |
| EditionHistory | Semantic | MustNotBeEntity | ForbidsContent | EditionEntry (1+, ordered) | Container for the history of editions, as required in ISO forewords. |
| EditionEntry | Semantic | MustNotBeEntity | ForbidsContent | Description | A single edition record with edition number, date, and change description. |
| RelatedPart | Semantic | MustNotBeEntity | ForbidsContent | Description | Declares the relationship between this document and another part of the same multi-part standard. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `documentNumber` | `$Text` | -- | ISO/IEC document number (e.g. "ISO 9001", "ISO/IEC 27001"). |
| `partNumber` | `$Text` | -- | Part number within a multi-part standard. |
| `edition` | `$Text` | -- | Edition number. |
| `language` | `$Text` | -- | Document language (e.g. "en", "fr", "en,fr"). |
| `secretariat` | `$Text` | -- | National body holding the secretariat (e.g. "ANSI", "BSI"). |
| `publicationDate` | `$Text` | -- | Publication date in ISO 8601 format. |
| `stage` | `$EnumeratedToken` | ISOStage | Current harmonized stage. |
| `label` | `$Text` | -- | Short display label. |
| `committeeNumber` | `$Text` | -- | TC number (e.g. "176"). |
| `committeeName` | `$Text` | -- | Full committee name. |
| `committeeType` | `$EnumeratedToken` | CommitteeType | Type of committee. |
| `subcommitteeNumber` | `$Text` | -- | SC number. |
| `subcommitteeName` | `$Text` | -- | Full subcommittee name. |
| `workingGroupNumber` | `$Text` | -- | WG number. |
| `workingGroupName` | `$Text` | -- | Full working group name. |
| `icsCode` | `$Text` | -- | ICS code (e.g. "35.040"). |
| `icsTitle` | `$Text` | -- | ICS code title. |
| `changeDescription` | `$Text` | -- | Brief description of edition changes. |
| `partTitle` | `$Text` | -- | Title of a related part. |
| `relationship` | `$EnumeratedToken` | PartRelationship | Relationship to a related part. |

## Enumerated Value Sets

### ISOStage (9 members)

The ISO harmonized stage code system covering the full document lifecycle.

| Member | Description |
|---|---|
| `Preliminary` | Stage 00: Preliminary work item registered. |
| `Proposal` | Stage 10: New work item proposal. |
| `Preparatory` | Stage 20: Working draft under development. |
| `Committee` | Stage 30: Committee draft circulated for comment. |
| `Enquiry` | Stage 40: DIS circulated for five-month vote. |
| `Approval` | Stage 50: FDIS circulated for two-month approval. |
| `Publication` | Stage 60: International Standard published. |
| `Review` | Stage 90: Systematic review (confirm, revise, or withdraw). |
| `Withdrawal` | Stage 95: Standard withdrawn. |

### CommitteeType (4 members)

| Member | Description |
|---|---|
| `TC` | Technical Committee (ISO only). |
| `JTC` | Joint Technical Committee (ISO/IEC joint). |
| `PC` | Project Committee (ISO, limited-scope). |
| `IEC` | IEC Technical Committee. |

### PartRelationship (7 members)

| Member | Description |
|---|---|
| `Supersedes` | This document supersedes the related part. |
| `SupersededBy` | This document is superseded by the related part. |
| `Complements` | This document complements the related part. |
| `ComplementedBy` | This document is complemented by the related part. |
| `Amends` | This document amends the related part. |
| `AmendedBy` | This document is amended by the related part. |
| `Corrigendum` | This document is a technical corrigendum to the related part. |

## Design Decisions

- `ISODocumentMetadata` is a separate top-level container rather than extending DocumentMetadata. Composition over inheritance: a specification includes both a generic DocumentMetadata and an ISODocumentMetadata when needed. This avoids polluting the generic schema with ISO-specific structure.
- `ISOStage` uses the ISO harmonized stage code names (Preliminary through Withdrawal) rather than raw numeric codes (00–95). The numeric codes are implementation details; the stage names are the semantic content. A projection layer emits the numeric codes when needed.
- Committee, Subcommittee, and WorkingGroup are separate concepts rather than a single "CommitteeLevel" with a depth trait. The ISO hierarchy is fixed at exactly three levels, so three concepts is clearer and more type-safe.
- `ISOForeword` is a distinct concept because ISO/IEC Directives Part 2 mandates specific foreword structure (committee identification, edition history, part relationships). This is not a generic foreword.
- `EditionHistory` contains ordered `EditionEntry` children to capture the full publication history required by ISO forewords.
- `RelatedPart` with `PartRelationship` captures the mandatory foreword text about relationships to other parts of a multi-part standard.
- All number and date traits are `$Text` because ISO document numbers include slashes, colons, and other punctuation (e.g. "ISO/IEC 27001:2022"), and Codex lacks a native date type.
