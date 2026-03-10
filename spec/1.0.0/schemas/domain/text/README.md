Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Text

Reusable text primitives: title, teaser, and paragraph.

## When to Use

Use `Title` for the primary name of any content block. Use `Teaser` for a short hook or preview sentence. Use `Paragraph` for a block of running prose. All three use `RequiresContent` because empty text is meaningless.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| Title | Semantic | RequiresContent (Flow) | The primary name or heading text of a content block. |
| Teaser | Semantic | RequiresContent (Flow) | A short hook or preview sentence. |
| Paragraph | Semantic | RequiresContent (Flow) | A block of running prose. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| language | $EnumeratedToken | no | The language of the text content, e.g. `$en`, `$fr`. |

## Design Notes

- All three concepts use `RequiresContent` (not `AllowsContent`) because empty text primitives are semantically meaningless.
- These are the shared building blocks imported by list, description, rubric, section, and other compositor schemas.

---

**End of Text v1.0.0**
