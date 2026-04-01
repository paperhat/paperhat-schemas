Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Editorial Markup

Semantic treatments applied to text spans: emphasis, importance, highlighting, track-changes operations, annotations, corrections, redactions, spoilers, and quotations.

## When to Use

Use `EditorialMarkup` to define span-binding targets for Gloss inline references. Each child concept is a semantic marker or content-bearing concept that Gloss spans bind to via `{~key}` or `{~key | label}` references.

Two complementary patterns:
- **Pattern A (Label on the Binding):** Define a marker with a key. Supply display text via the Gloss label: `{~em | emphasized text}`.
- **Pattern B (Text on the Entity):** Define a marker with a key and `text` trait. Reference without a label: `{~em}`. Useful when the same term recurs.

## Concepts

### EditorialMarkup (Container)

Structural container for editorial markup definitions. Unordered, no duplicates.

### Span-Binding Markers

These concepts forbid content. They are type markers bound from Gloss spans. All require a `key` trait. All allow an optional `text` trait for Pattern B.

| Concept | Additional Required Traits | Additional Optional Traits | Description |
|---|---|---|---|
| Emphasis | -- | -- | Stress emphasis on a text span. |
| Important | -- | -- | Urgency or importance marking. |
| Highlight | -- | -- | Visual attention marking. |
| Deletion | -- | -- | Text that has been deleted (track changes). |
| Insertion | -- | -- | Text that has been inserted (track changes). |
| MoveFrom | moveIdentifier | -- | Source location of moved text. Paired with a MoveTo sharing the same moveIdentifier. |
| MoveTo | moveIdentifier | -- | Destination of moved text. Paired with a MoveFrom sharing the same moveIdentifier. |
| Redaction | -- | reason | Intentionally hidden or obscured text. |
| Spoiler | -- | -- | Content hidden by default, revealed on user interaction. |
| Correction | -- | original | Marks corrected text. The `original` trait records pre-correction text. |

### Content-Bearing Concepts

These concepts require content. The content carries the concept's primary text.

| Concept | Required Traits | Optional Traits | Content | Description |
|---|---|---|---|---|
| Annotation | key | author | The comment text | Editorial comment attached to a span (tracked-changes commenting). |
| Quote | key | author, source, language | The quoted text | Inline quotation with attribution. Carries structured data for foundry output (including JSON-LD). |

### Block-Level Concepts

These concepts require content and are placed by the importing entity schema, not inside the EditorialMarkup container.

| Concept | Required Traits | Optional Traits | Content | Description |
|---|---|---|---|---|
| BlockQuotation | -- | key, author, source, language | The quoted text | Block-level quotation. |
| PullQuote | -- | key, source | The quoted text | Highlighted excerpt pulled from the same document. |

## Traits

| Trait | Type | Cardinality | Description |
|---|---|---|---|
| key | $LookupToken | Single | Gloss binding key for `{~key}` references. |
| text | $Text | Single | Display text for Pattern B (label-less Gloss references). |
| author | $Text | Single | Creator of the annotation, quotation, or comment. |
| source | $Text | Single | Origin or attribution of a quotation. |
| language | $LanguageTag | Single | Language of the quoted or annotated text (BCP 47). |
| moveIdentifier | $LookupToken | Single | Links a MoveFrom/MoveTo pair. Both must share the same identifier. |
| reason | $Text | Single | Why text was redacted. |
| original | $Text | Single | Pre-correction text for a Correction. |

## Constraints

- EditorialMarkup must contain at least one child.

## Design Notes

- MoveFrom and MoveTo are always paired via a shared `moveIdentifier`. A foundry validates that every MoveFrom has a corresponding MoveTo with the same identifier, and vice versa.
- BlockQuotation and PullQuote are not children of the EditorialMarkup container. They are block-level content elements placed by entity schemas that import this leaf.
- Quote carries `author` and `source` traits to support structured data output (JSON-LD, RDFa, microdata). The foundry decides the output format.
- Annotation content is the comment body. The Gloss span wraps the text being commented on. The foundry renders both.

**End of Editorial Markup v1.0.0**
