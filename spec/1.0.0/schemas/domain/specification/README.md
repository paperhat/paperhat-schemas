Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification

A strict specification schema for authoring formal specifications in Codex. Narrows requirement modality to Must and MustNot only. All shared concepts, traits, constraints, and content-schema imports are provided by `paperhat-specification-foundation`.

For the full RFC 2119 keyword set (Must, MustNot, Shall, ShallNot, Should, ShouldNot, May, Required, Recommended, Optional), use `paperhat-specification-rfc2119` instead.

## When to Use

Use `Specification` when the document is normative or policy-defining and requires deterministic section identity, typed block structure, and machine-checkable requirements with strict Must/MustNot modality. This is the schema used for Paperhat's own specifications.

## Concepts

This schema defines only the variant-specific concepts. All other concepts (Section, Note, Rationale, SectionReference, ExternalReference, RequirementSet, TermBinding, Issue, OpenQuestion) are provided by the foundation.

| Concept | Kind | Entity | Content | Description |
|---|---|---|---|---|
| Specification | Semantic | MustNotBeEntity | ForbidsContent | Root specification concept with required front-matter traits. Children: Section (1+). |
| Requirement | Semantic | MustBeEntity | RequiresContent (Flow) | A normative requirement statement with strict modality and stable identity. Optional structured children: Rationale, Note, Paragraph, OrderedList, UnorderedList, Citation. |

## Requirement Traits

Required (imported from `specbase`):

- `key` (`$LookupToken`) — stable lookup key, required
- `modality` (`$EnumeratedToken`: `Must` | `MustNot`) — narrowed from the foundation's full RequirementModality set

Optional (imported from `specbase`):

- `deprecated` (`$Boolean`) — whether this requirement is deprecated
- `deprecatedSince` (`$Semver`) — version at which this requirement was deprecated

## Requirement Modality

The `modality` trait is narrowed at concept level to strict modality only via the local `StrictRequirementModality` enumerated value set. Documents authored against this schema cannot express any modality other than Must or MustNot.

## Design Decisions

- This schema imports only the specification foundation. All content-schema dependencies (text, list, code, figure, example, admonition, citation, glossary, relation) are transitively available through the foundation.
- Requirement requires `key` (RequiresTrait), unlike the RFC 2119 variant where it is optional.
- No `requirementId` trait is surfaced. The strict variant uses `key` alone for requirement identity.
- Requirement allows optional structured children (Rationale, Note, Paragraph, OrderedList, UnorderedList, Citation) beneath the normative statement text. This supports explanatory paragraphs, justification blocks, and citations within a requirement.
- `deprecated` and `deprecatedSince` are optional on Requirement for marking individual requirements as deprecated.

---

**End of Specification v1.0.0**
