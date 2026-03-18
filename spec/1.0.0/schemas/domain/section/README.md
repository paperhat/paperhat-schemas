Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Section

An ordered subdivision of a long-form document. Sections nest recursively and compose rubrics, paragraphs, descriptions, lists, and notes.

## When to Use

Use `Section` to divide any long-form document into logical parts: chapters, subsections, numbered clauses, or thematic groupings. Sections appear in essays, articles, scientific papers, white papers, legal documents, and technical manuals. They nest: a top-level section contains subsections, which contain sub-subsections, to any depth.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Section | Structural | ForbidsContent | rubric:Rubric (0..1), text:Paragraph, desc:Description, list:OrderedList, list:UnorderedList, Section (recursive), notes:Notes | An ordered container for document content. Children appear in reading order. |

## Imports

| Namespace | Schema |
|---|---|
| text | `paperhat:domain:text` |
| rubric | `paperhat:domain:rubric` |
| desc | `paperhat:domain:description` |
| list | `paperhat:domain:list` |
| notes | `paperhat:domain:notes` |

## Design Notes

- Section preserves order. Paragraphs, nested sections, lists, and descriptions appear in the sequence the author intends.
- Rubric provides title, subtitle, teaser, difficulty, and temporal metadata for a section.
- Rubric is optional because some document structures use numbered or untitled sections.
- Section allows Notes children for section-scoped footnotes. Document-level endnotes belong in a Notes sibling of the Narrative.
- Description children support inline "what is this section about?" blocks within a section.
- Media attachment uses the `media-reference` schema package.

---

**End of Section v1.0.0**
