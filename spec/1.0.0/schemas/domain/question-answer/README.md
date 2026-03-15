Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Question and Answer

General-purpose discourse primitives for questions and answers. These are semantically paired but structurally independent — a Question exists without requiring an Answer, and vice versa.

## When to Use

Use `Question` and `Answer` as general discourse primitives wherever interrogative and responsive content appears. These are the building blocks for FAQ schemas, interview transcripts, Q&A documentation sections, Socratic dialogues, catechisms, and any other context where questions and answers have semantic identity. A Question without an Answer is valid (rhetorical questions, open questions). An Answer without a Question is valid (standalone responses to implied context).

## Concepts

| Concept | Kind | Entity Eligibility | Content | Description |
|---|---|---|---|---|
| Question | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | An interrogative discourse unit. |
| Answer | $Semantic | $MustNotBeEntity | RequiresContent (Flow) | A responsive discourse unit. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $LookupToken | no | A stable identifier for cross-referencing this question or answer. |
| language | $EnumeratedToken | no | BCP 47 language tag identifying the language of the content. |

## Design Notes

- Question and Answer are general discourse primitives, not FAQ-specific. The FAQ schema imports this package and composes them into FAQ entries.
- Both concepts use `$MustNotBeEntity` because they are embedded within their composing context.
- Both require flow content to support Gloss span bindings.
- The traits are shared between both concepts. Each trait is defined once in the schema and allowed on both Question and Answer.
- Pure leaf with no imports. Composing schemas wire Question and Answer as child concepts and define their structural relationship.

---

**End of Question and Answer v1.0.0**
