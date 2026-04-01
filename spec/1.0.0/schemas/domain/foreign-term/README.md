Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Foreign Term

A term in a language other than the document's primary language, with pronunciation, translation, and language identification.

## When to Use

Use `ForeignTerms` to define foreign-language terms that appear in the document's prose. Each ForeignTerm is a Gloss span-binding target carrying the term's text, language, and optional pronunciation and translations.

## Concepts

### ForeignTerms (Container)

Structural container for foreign term definitions. Unordered, no duplicates.

### ForeignTerm

A single foreign term. Requires content (the term itself in its original script). Bound from Gloss spans via `{~key}` or `{~key | label}` references.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| language | $LanguageTag | Single | yes | BCP 47 language tag identifying the term's language. |
| pronunciation | $Text | Single | no | IPA pronunciation of the term (e.g. "sɯɕi"). |
| translation | $Text | Multiple | no | One or more translations into the document's language. |

## Constraints

- ForeignTerms must contain at least one ForeignTerm.

## Design Notes

- ForeignTerm requires content because the term text IS the concept. The content carries the term in its original script/language.
- The `translation` trait has `$Multiple` cardinality because a term has several valid translations.
- The `pronunciation` trait uses $Text. Values are expected to be IPA notation.
- When referenced from Gloss without a label, the content (the foreign term text) provides the display text.

**End of Foreign Term v1.0.0**
