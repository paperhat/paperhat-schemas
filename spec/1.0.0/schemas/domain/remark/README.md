Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Remark

An authorial observation or commentary within the flow of a document. Remarks are formal discourse units used in academic, mathematical, and technical writing.

## When to Use

Use `Remark` for authorial observations that appear within the body of a document as named, referenceable discourse units. In mathematical and technical writing, remarks are conventionally numbered and cross-referenced: "Remark 3.2: The converse does not hold in general." Remark is distinct from Annotation (which is editorial markup applied to existing text by a reviewer) and from Note (which is supplementary information outside the main flow).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | A stable identifier for cross-referencing this remark. |
| label | $Text | no | A display label for numbering or identification, such as "Remark 3.2". |
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the remark text. |

## Content

Remark requires text content (`RequiresContent whitespaceMode=$Flow`). The remark text is the element's content, not a trait, following the same pattern as Example and Note.

## Design Notes

- Remark is the discourse-layer sibling of Example and Definition. All three are formal, labeled, in-flow discourse units used in structured technical and academic writing.
- Distinct from Annotation (`paperhat:domain:editorial-markup:Annotation`), which belongs to the editorial/review layer and marks up existing text with third-party commentary.
- Distinct from Note (`paperhat:domain:notes:Note`), which is supplementary information presented outside the main discourse flow.
- `$MustNotBeEntity` with a `key` trait for cross-referencing, following the same pattern as Example.
- Pure leaf with no imports. The composing schema wires Remark as a child concept where authorial observations are permitted.

---

**End of Remark v1.0.0**
