Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification (RFC 2119)

A specification schema for authoring formal specifications in Codex with the full RFC 2119 requirement modality keyword set. All shared concepts, traits, constraints, and content-schema imports are provided by `paperhat-specification-foundation`.

For strict Must/MustNot-only modality, use `paperhat-specification` instead.

## When to Use

Use this schema when the document follows RFC 2119 conventions and requires the full keyword set: Must, MustNot, Shall, ShallNot, Should, ShouldNot, May, Required, Recommended, Optional. This is appropriate for modeling specifications from organizations such as W3C, IEEE, ISO, and IETF.

## Concepts

This schema defines only the variant-specific concepts. All other concepts (Section, Note, Rationale, SectionReference, ExternalReference, RequirementSet, TermBinding, Issue, OpenQuestion) are provided by the foundation.

| Concept | Kind | Entity | Content | Description |
|---|---|---|---|---|
| Specification | Semantic | MustNotBeEntity | RequiresContent (Flow) | Root specification concept with required front-matter traits. Children: Section (1+). |
| Requirement | Semantic | MustNotBeEntity | RequiresContent (Flow) | A normative requirement statement with full RFC 2119 modality. Optional structured children: Rationale, Note, Paragraph, OrderedList, UnorderedList, Citation. |

## Requirement Traits

Required (imported from `specbase`):

- `modality` (`$EnumeratedToken`) — the full RFC 2119 keyword set, inherited from the foundation trait-level constraint

Optional (imported from `specbase`):

- `key` (`$LookupToken`) — stable lookup key
- `requirementId` (`$LookupToken`) — stable identifier for a specific requirement
- `deprecated` (`$Boolean`) — whether this requirement is deprecated
- `deprecatedSince` (`$Semver`) — version at which this requirement was deprecated

## Requirement Modality

No concept-level modality narrowing. The full 10-member RequirementModality set from the foundation applies directly: Must, MustNot, Shall, ShallNot, Should, ShouldNot, May, Required, Recommended, Optional.

## Design Decisions

- This schema imports only the specification foundation. All content-schema dependencies are transitively available through the foundation.
- Requirement makes `key` optional (AllowsTrait), since external specifications being modeled after the fact may not have clean identifiers for every requirement.
- `requirementId` is surfaced as an additional optional trait for organizations that use separate requirement numbering.
- Requirement allows optional structured children (Rationale, Note, Paragraph, OrderedList, UnorderedList, Citation) beneath the normative statement text.
- `deprecated` and `deprecatedSince` are optional on Requirement for marking individual requirements as deprecated.

---

**End of Specification (RFC 2119) v1.0.0**
