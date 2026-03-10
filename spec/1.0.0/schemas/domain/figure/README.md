Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Figure

A semantic figure container for one or more media resources, with optional title and caption metadata.

## When to Use

Use `Figure` when media needs explicit semantic structure for rendering, indexing, and cross-reference workflows.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| Figure | Semantic | ForbidsContent | Ordered media figure with optional title and required media references. |

Allowed child concepts:

- `text:Title` (max 1)
- `media:MediaReference` (min 1)

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | Stable token for binding/reference workflows. |
| label | $Text | no | Optional label text for renderers and references. |
| caption | $Text | no | Optional figure-level caption text. |

## Constraints

- `Figure` must contain at least one `media:MediaReference` child.

## Design Notes

- A figure can aggregate multiple related media references.
- `caption` is figure-level metadata and does not replace per-media captions.

---

**End of Figure v1.0.0**
