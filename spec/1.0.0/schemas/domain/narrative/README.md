Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Narrative

An ordered container for the body content of a document, holding sections and paragraphs in reading order.

## When to Use

Use `Narrative` as the body wrapper in any document-like entity (essays, articles, reports, white papers). It enforces reading order on its children and separates body content from unordered metadata. Pair it with `DocumentMetadata` to cleanly segregate ordered content from unordered document information.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Narrative | Structural | ForbidsContent | section:Section, text:Paragraph | An ordered container. Children appear in the sequence the author intends. |

## Imports

| Namespace | Schema |
|---|---|
| section | `paperhat:domain:section` |
| text | `paperhat:domain:text` |

## Design Notes

- Narrative exists to solve the ordered/unordered segregation problem. A document's metadata (author, dates, tags) has no meaningful order, but its body content must preserve reading order. By placing metadata in an unordered DocumentMetadata sibling and body content in an ordered Narrative, each container enforces the correct semantics.
- Narrative allows both Section and Paragraph children directly, supporting documents that mix sectioned and unsectioned prose.
- Narrative does not allow Rubric as a direct child. The document's own title belongs on the parent entity (e.g., Essay's `title` trait). Section headings belong inside their respective Sections.

---

**End of Narrative v1.0.0**
