Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Frequently Asked Questions

A frequently asked questions collection composed of question-answer pairs. Imports the general-purpose Question and Answer discourse primitives from `paperhat-question-answer`.

## When to Use

Use `FrequentlyAskedQuestions` to model a structured FAQ section in a document, website, or knowledge base. Each Entry pairs exactly one Question with exactly one Answer. The FAQ is an ordered collection of entries.

## Concepts

| Concept | Kind | Entity Eligibility | Content | Children | Description |
|---|---|---|---|---|---|
| FrequentlyAskedQuestions | $Structural | $MustNotBeEntity | ForbidsContent | Entry (1+) | An ordered collection of FAQ entries. |
| Entry | $Structural | $MustNotBeEntity | ForbidsContent | question:Question (1), question:Answer (1) | A single question-answer pair. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | no | A title for the FAQ collection. |
| key | $LookupToken | no | A stable identifier for cross-referencing a specific entry. |
| language | $EnumeratedToken | no | BCP 47 language tag. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| question | `paperhat:domain:question` | Question, Answer |

## Constraints

- A FrequentlyAskedQuestions collection must contain at least one Entry.

## Design Notes

- Question and Answer are general-purpose discourse primitives defined in `paperhat-question-answer`. This schema imports and composes them into FAQ entries. The same primitives are reusable in interview transcripts, Q&A documentation sections, and other contexts.
- Entry is Structural because it is an organizational container pairing one Question with one Answer. It carries no semantic content of its own.
- FrequentlyAskedQuestions is Structural and ordered — FAQ entry order is meaningful.

---

**End of Frequently Asked Questions v1.0.0**
