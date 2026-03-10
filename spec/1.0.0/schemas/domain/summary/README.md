Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Summary

A condensed restatement of what a document or resource says, distinct from a description of what it is about.

## When to Use

Use `Summary` when you need to capture the substance of a document's content in abbreviated form. A Description says what the document *is about*; a Summary condenses what the document *says*. In academic contexts this is an abstract; for a book it is a synopsis; for a report it is an executive summary. Maps to schema.org `abstract` and Dublin Core `dcterms:abstract`.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the summary text. |

## Design Notes

- Summary is content-bearing: the summary text is the element's content, not a trait.
- Distinct from Description (`codex:domain:description`), which captures what something *is about* rather than what it *says*.
- Multiple summaries in different languages can coexist as siblings inside a DocumentMetadata container, each with a different `language` value.

---

**End of Summary v1.0.0**
