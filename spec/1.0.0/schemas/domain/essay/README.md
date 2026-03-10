Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Essay

A short-to-medium-length prose composition expressing the author's perspective on a single subject.

## When to Use

Use `Essay` for personal essays, opinion pieces, reflective writing, literary essays, and similar forms where a single author develops a sustained argument or exploration of a topic. For longer, multi-section academic or technical documents, consider composing the same building blocks (Narrative, Section, DocumentMetadata) into a dedicated Article or Report entity instead.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Essay | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), narrative:Narrative (1), notes:Notes (0..1) | A prose composition. Requires a title trait and exactly one Narrative. |

## Imports

| Namespace | Schema |
|---|---|
| docmeta | `codex:domain:document-metadata` |
| narrative | `codex:domain:narrative` |
| notes | `codex:domain:notes` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the essay. |

## Design Notes

- The `title` trait lives on Essay itself because it is the entity's primary identifier, not a piece of metadata.
- DocumentMetadata and Notes are optional. A minimal essay is just a title and a Narrative.
- The Essay is ordered so that metadata, body, and notes appear in a predictable sequence. Within DocumentMetadata, order does not matter. Within Narrative, order is preserved.
- All body-level metadata (author, dates, licensing, tags) belongs inside DocumentMetadata via the Work, Description, Summary, Tags, and Audience leaf concepts.
- Section-scoped footnotes can also appear inside individual Sections within the Narrative.

**End of Essay v1.0.0**
