Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Publication

A general published work with stable identity — a book, journal, manual, report, anthology, or other published artifact that does not require the specific structural prescriptions of WhitePaper or Essay.

## When to Use

Use `Publication` to model published works that need stable identity and cross-referencing but do not fit the specialized structures of WhitePaper (which requires Abstract and coreThesis) or Essay. Examples include books, technical manuals, collected volumes, magazine issues, and standards documents. DocumentMetadata, SeriesInfo, Identifier, MediaAsset, and other children are wired by the composing schema.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The title of the publication. |
| publicationKind | $EnumeratedToken | no | Classification token, e.g., `$Book`, `$Journal`, `$Magazine`, `$Report`, `$Manual`, `$Anthology`, `$Collection`, `$Standard`. Open vocabulary. |
| publicationStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$InPreparation`, `$Published`, `$OutOfPrint`, `$Revised`. Open vocabulary. |

## Constraints

`name` is required. A publication without a title is ambiguous.

## Design Notes

- `$MustBeEntity` because publications have stable identity and are cross-referenced from citations, series, releases, and documentation.
- WhitePaper and Essay are specialized publication types that prescribe specific internal structure. Publication is the general case with no required structural prescriptions.
- Children (DocumentMetadata, SeriesInfo, Narrative, Notes, Identifier, MediaAsset, Description, Tags, Audience) are wired by composing schemas, not imported here.
- Pure leaf with no imports, keeping the dependency graph minimal.

---

**End of Publication v1.0.0**
