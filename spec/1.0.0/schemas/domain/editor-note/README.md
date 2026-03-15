Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# EditorNote

An editorial annotation intended for reviewers and editors, excluded from published output — a comment, query, or instruction about the document itself.

## When to Use

Use `EditorNote` to record editorial comments, queries, or instructions during document review. Editor notes are excluded from published output — they are metadata about the document, not part of the document.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| author | $Text | no | The person who wrote the editorial note. |
| date | $Date | no | The date the editorial note was written. |

## Design Notes

- `$Structural` and `$MustNotBeEntity` because editor notes are transient review artifacts, not referenceable semantic entities.
- Content carries the note text in `$Flow` whitespace mode.
- Consuming systems and foundries exclude EditorNote from published output. The note is preserved in the semantic graph for review workflows.

---

**End of EditorNote v1.0.0**
