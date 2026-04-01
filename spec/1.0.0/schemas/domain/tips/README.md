Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Tips

An ordered container for reusable advisory content such as cooking tips, preparation hints, handling guidance, or practical recommendations.

## When to Use

Use `Tips` when the document needs advisory content that is read in authored order and is not referenced by key. Recipe advice, handling hints, preparation reminders, and practical guidance all fit this pattern.

Use `notes:Notes` for referenced annotations. Use `admonition` for callout semantics such as warnings, danger notices, and other explicit admonitions.

## Concepts

### Tips

The ordered container. Order matters because the author expresses importance, progression, or preferred reading sequence through the authored order.

### Tip

A single advisory item. The tip text is the element's content.

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | no | A short authored label for the advisory item when a distinct title is needed. |
| language | $LanguageTag | no | BCP 47 language tag identifying the language of the tip content. |

## Design Notes

- `Tips` is ordered because advisory content carries authored priority or sequence.
- `Tips` forbids duplicates so the same advisory item does not appear twice in one container.
- `Tip` carries flow content so the package remains a reusable leaf-style advice surface.

---

**End of Tips v1.0.0**
