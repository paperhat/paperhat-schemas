Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Example

A rich, ordered container for worked examples that combine narrative, code, figures, lists, relation data, and admonitions.

## When to Use

Use `Example` when you want a bounded, reusable example block that can be referenced or rendered as a coherent unit in documentation and specifications.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| Example | Semantic | ForbidsContent | Ordered container for example material. |

Allowed child concepts:

- `text:Title` (max 1)
- `text:Paragraph`
- `list:OrderedList`
- `list:UnorderedList`
- `code:CodeBlock`
- `figure:Figure`
- `relation:RelationType`
- `relation:RelationInstance`
- `admonition:Informational`
- `admonition:Warning`
- `admonition:Danger`
- `admonition:Critical`
- `admonition:Notice`
- `admonition:Tip`

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | Stable token for binding/reference workflows. |
| label | $Text | no | Optional label text for renderers and references. |

## Constraints

- `Example` must contain at least one allowed child concept.

## Design Notes

- Nested `Example` blocks are intentionally disallowed.
- Child ordering is preserved.
- Duplicate child concepts are allowed.

---

**End of Example v1.0.0**
