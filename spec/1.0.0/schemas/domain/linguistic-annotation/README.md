Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Linguistic Annotation

Linguistic metadata applied to text spans, including ruby annotations for displaying reading aids above or beside base text.

## When to Use

Use `LinguisticAnnotations` to define linguistic reading aids for text spans. Currently provides Ruby annotations, common in CJK typography for showing pronunciation guides (furigana, zhuyin, pinyin) above or beside base text.

## Concepts

### LinguisticAnnotations (Container)

Structural container for linguistic annotation definitions. Unordered, no duplicates.

### Ruby

A ruby annotation: text displayed above or beside the base text of a Gloss span. The Gloss label carries the base text; the `annotation` trait carries the reading aid.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| annotation | $Text | Single | yes | The annotation text displayed above or beside the base text (e.g. furigana, pinyin). |
| language | $EnumeratedToken | Single | no | Language of the annotation text, if different from the base text. |
| position | $EnumeratedToken | Single | no | Where to display the annotation relative to the base text (e.g. `$above`, `$beside`). Foundry default is `$above`. |

## Constraints

- LinguisticAnnotations must contain at least one Ruby.

## Design Notes

- Ruby forbids content. The base text is the Gloss span label; the annotation text is the `annotation` trait. This separates the two text layers cleanly.
- The `position` trait allows authors to override the foundry's default placement. Common values: `$above` (East Asian default), `$beside` (used in some vertical text layouts).
- Named after the typographic term "ruby" (small annotation text), not the programming language.

**End of Linguistic Annotation v1.0.0**
