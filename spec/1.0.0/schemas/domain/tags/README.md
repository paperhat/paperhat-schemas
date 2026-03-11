Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Tags

An unordered collection of keyword labels for categorisation and discovery.

## When to Use

Use `Tags` wherever content needs freeform keyword labels: product categories, article topics, recipe cuisines, event types. Tags are unordered and duplicate-free.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Tags | Structural | ForbidsContent | Tag | An unordered, duplicate-free container of keyword labels. |
| Tag | Semantic | RequiresContent (Flow) | -- | A single keyword label. |

## Constraints

- Tags must contain at least one Tag.

## Design Notes

- Tags uses `CollectionRules` with `ordering=$Unordered` and `allowsDuplicates=false` to enforce set semantics.
- Tag uses `RequiresContent` because an empty tag is meaningless.

---

**End of Tags v1.0.0**
