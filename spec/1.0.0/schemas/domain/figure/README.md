Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Figure

A semantic figure container for one or more media resources, with optional title, caption child, and label metadata.

## When to Use

Use `Figure` when media needs explicit semantic structure for rendering, indexing, and cross-reference workflows.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| Figure | Semantic | ForbidsContent | Ordered media figure with optional title and required media references. |

Allowed child concepts:

- `text:Title` (max 1)
- `media:MediaReference` (min 1)
- `caption:Caption` (max 1)

## Imports

| Namespace | Schema |
|---|---|
| media | `paperhat:domain:media` |
| text | `paperhat:domain:text` |
| caption | `paperhat:domain:caption` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | Stable token for binding/reference workflows. |
| label | $Text | no | Optional label text for renderers and references. |

## Constraints

- `Figure` must contain at least one `media:MediaReference` child.

## Design Notes

- A figure aggregates one or more related media references.
- `caption:Caption` is an optional child concept imported from `paperhat-caption`, providing structured caption content rather than a plain text trait.

---

**End of Figure v1.0.0**
