Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Caption

A descriptive or explanatory text fragment accompanying a figure, table, or other visual element. Caption is a semantic concept with opaque content, supporting span bindings via Gloss.

## When to Use

Use `Caption` to attach descriptive text to a visual or structural element such as a Figure. Caption is a first-class semantic concept rather than a trait value, which allows its content to participate in Gloss span bindings — enabling inline annotations, foreign terms, emphasis, and other discourse-level markup within caption text.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | A stable identifier for cross-referencing this caption. |
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the caption text. |

## Content

Caption requires text content (`RequiresContent whitespaceMode=$Flow`). The caption text is the element's content, not a trait, following the same pattern as Paragraph and Summary.

## Design Notes

- Caption is a standalone concept rather than a trait on Figure because Gloss span bindings require opaque flow content. A Text-typed trait does not support span bindings.
- `$MustNotBeEntity` because captions are embedded within their parent context, not independently referenceable.
- Pure leaf with no imports. The composing schema (such as Figure) wires Caption as a child concept.

---

**End of Caption v1.0.0**
