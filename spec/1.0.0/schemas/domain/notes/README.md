Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Notes

A container for keyed annotations such as footnotes, endnotes, or bibliographic references.

## When to Use

Use `Notes` to collect supplementary annotations that are referenced from the body text by key. Footnotes, endnotes, citations, translator notes, and editor annotations all fit this pattern. Each `Note` carries a `key` trait (a LookupToken) that the body text uses to reference it.

## Concepts

### Notes

The unordered container. Order of notes does not matter because they are accessed by key.

### Note

A single annotation. The note text is the element's content.

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | yes | The reference key used to cite this note from the body text, e.g. `1`, `a`, `smith2024`. |
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the note text. |

## Design Notes

- Notes is unordered because notes are looked up by key, not read sequentially. Presentation order (numeric, alphabetical) is a rendering concern.
- The `key` trait is required so every note is addressable. Keys must be unique within a Notes container (enforced by LookupToken semantics).
- Notes appear inside Sections (for section-scoped footnotes) or at the document level (for endnotes).

---

**End of Notes v1.0.0**
