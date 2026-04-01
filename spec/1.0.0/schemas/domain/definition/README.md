Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Definition

A formal definition binding a term (definiendum) to its meaning (definiens). Usable in glossaries, specifications, technical documents, and any context that defines terms.

## When to Use

Use `Definition` wherever a term is formally defined. In a glossary, each entry is a Definition. In a specification, "Definition 3.1: A *group* is..." is a Definition. In technical documentation, a definitions section contains Definitions. This is the general-purpose discourse primitive for defining terms. A glossary is a collection of Definitions.

Distinct from LexicalEntry (`paperhat:domain:lexical-entry`), which is a rich lexicographic structure with senses, etymology, inflected forms, and semantic relations. Definition is a discourse primitive; LexicalEntry is a lexicographic artifact.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| term | $Text | yes | The term being defined (the definiendum). |
| key | $LookupToken | no | A stable identifier for cross-referencing this definition. |
| label | $Text | no | A display label for numbering, such as "Definition 3.1". |
| language | $LanguageTag | no | BCP 47 language tag. |

## Content

Definition requires text content (`RequiresContent whitespaceMode=$Flow`). The definition text (the definiens) is the element's content, supporting Gloss span bindings.

## Design Notes

- Definition is `$MustBeEntity` because definitions are cross-referenced by identity. A Gloss span binding referencing "see Definition 3.1" resolves to a specific Definition entity.
- Replaces the former GlossaryEntry concept. A glossary is a collection of Definitions — the container gives context, the Definition gives semantic content.
- The `label` trait supports numbered references ("Definition 3.1") following the same pattern as Example and Remark.
- Pure leaf with no imports. Composing schemas wire Definition as a child concept.

---

**End of Definition v1.0.0**
