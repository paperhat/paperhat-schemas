Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# List

Ordered and unordered lists with nestable items.

## When to Use

Use `OrderedList` when sequence matters (steps, rankings, instructions). Use `UnorderedList` when it does not (ingredients, features, bullet points). Lists nest: a ListItem in children mode can contain paragraphs and sub-lists.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| OrderedList | Structural | ForbidsContent | ListItem | A sequence-significant list. |
| UnorderedList | Structural | ForbidsContent | ListItem | A sequence-insignificant list. |
| ListItem | Semantic | AllowsContentOrChildren (Flow) | text:Paragraph, OrderedList, UnorderedList | A single list entry. Content mode = plain text; children mode = paragraphs + nested lists. |

## Imports

| Namespace | Schema |
|---|---|
| text | `codex:domain:text` |

## Constraints

- OrderedList must contain at least one ListItem.
- UnorderedList must contain at least one ListItem.

## Design Notes

- ListItem uses `AllowsContentOrChildren`: content mode for simple text items, children mode for rich items with paragraphs and nested lists.
- Lists are semantic, not presentational. OrderedList/UnorderedList describe the *relationship* of items (sequence-significant vs. not), not how they render.
- Both list types allow duplicates (`allowsDuplicates=true`) because repeated items are valid in ordered and unordered contexts.

**End of List v1.0.0**
