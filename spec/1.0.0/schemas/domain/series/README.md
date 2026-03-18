Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Series

Series membership metadata for a document that belongs to an ordered, multi-part publication.

## When to Use

Use `SeriesInfo` when a document is part of a numbered series, such as a white paper program, a blog series, a multi-volume specification, or a course module sequence. SeriesInfo captures the series title, the document's position within the series, and an optional track or category.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| SeriesInfo | Semantic | ForbidsContent | Series membership metadata. Requires a series title. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| seriesTitle | $Text | yes | Name of the series (e.g., "Paperhat Institute White Papers"). |
| position | $Integer | no | 1-indexed position within the series or track. |
| track | $Text | no | Sub-track or category within the series (e.g., "Track A", "Architecture"). |

## Design Notes

- SeriesInfo is a leaf concept, not a container. It describes a document's membership in a series, not the series itself.
- The `position` trait is optional because some series members do not have a fixed position (e.g., supplementary papers).
- The `track` trait supports series with internal subdivisions without requiring a separate concept for each subdivision.
- Presentation of series information (e.g., "Paper 7 of 12" or "Track A — Paper 7") is a rendering concern handled by the foundry.

---

**End of Series v1.0.0**
