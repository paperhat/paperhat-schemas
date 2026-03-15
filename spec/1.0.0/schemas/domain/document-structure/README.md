Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Document Structure

Named structural divisions of a document with semantic identity. Abstract, Introduction, Conclusion, Preface, Appendix, and Foreword are general-purpose discourse primitives usable across document types.

## When to Use

Use these concepts to mark named divisions within a document. Essays, white papers, specifications, technical reports, and books all use some subset of these divisions. Each concept carries semantic identity — an Abstract is not just "a section titled Abstract" but a typed discourse unit with its own meaning.

## Concepts

| Concept | Kind | Entity Eligibility | Content | Description |
|---|---|---|---|---|
| Abstract | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | A condensed summary of the work's content and findings. |
| Introduction | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | Opening section that establishes context, scope, and purpose. |
| Conclusion | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | Closing section that summarizes findings and implications. |
| Preface | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | Author's preliminary remarks on purpose, scope, and acknowledgments. |
| Appendix | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | Supplementary material following the main body. |
| Foreword | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | Introductory remarks written by someone other than the document author. |

## Traits

| Trait | Type | Required | Applies To | Description |
|---|---|---|---|---|
| key | $LookupToken | no | All concepts | A stable identifier for cross-referencing. |
| label | $Text | no | Appendix | A display label such as "Appendix A". |
| author | $Text | no | Foreword | The author of the foreword. |
| language | $EnumeratedToken | no | All concepts | BCP 47 language tag. |

## Design Notes

- All six concepts use flow content. They are semantic labels for document divisions, not structural containers. The composing schema determines what child elements each division accepts in context.
- Preface and Foreword are semantically distinct. A Preface is written by the document's author and addresses purpose, scope, and acknowledgments. A Foreword is written by someone other than the author, introducing the work or the author to the reader.
- Abstract is distinct from Summary (`paperhat:domain:summary`). An Abstract is a document division that summarizes the work's content. Summary is a general-purpose condensation usable in metadata, cards, or any context.
- Appendix carries a `label` trait for conventional identification ("Appendix A", "Appendix B"). Other divisions do not need this because they appear at most once in a document.
- Pure leaf package with no imports. Document-type schemas (Essay, WhitePaper, Specification) import this package and wire these concepts as children.

---

**End of Document Structure v1.0.0**
