Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Work

Creative work metadata covering authorship, publication dates, versioning, licensing, and lifecycle status.

## When to Use

Use `Work` wherever an entity carries creative-work metadata: articles, books, software releases, recipes with version tracking, event programmes, product manuals, or any content that has an author, publication date, or license.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| author | $Text | no | Creator or author name. |
| dateCreated | $Date | no | When the work was created. |
| datePublished | $Date | no | When first published or released. |
| dateModified | $Date | no | When last modified. |
| version | $Text | no | Version identifier (supports semantic version, edition numbers, etc.). |
| language | $EnumeratedToken | no | Content language, e.g. `$en`, `$fr`, `$zh`. Consuming schemas constrain via a vocabulary. |
| status | $EnumeratedToken | no | Lifecycle status, e.g. `$draft`, `$published`, `$archived`, `$retired`. |
| license | $Text | no | License name or SPDX identifier, e.g. "CC-BY-4.0", "MIT". |

## Design Notes

- All traits are optional because different composers need different subsets. The "at least one" constraint prevents empty Work elements.
- `author` is plain text for the common case. Structured attribution (Person/Organization entities) is handled by composing those schemas separately.
- `version` is $Text, not $Number, because version identifiers are often non-numeric (e.g. "3.2.1", "2nd edition").
- `language` and `status` use $EnumeratedToken so consuming schemas constrain the allowed values via vocabularies.
- The Tags schema (`paperhat:domain:tags`) already covers keyword/genre tagging; Work does not duplicate that.
- Mirrors schema.org CreativeWork's core properties: author, dateCreated, datePublished, dateModified, version, inLanguage, creativeWorkStatus, license.

---

**End of Work v1.0.0**
