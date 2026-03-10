Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification (RFC 2119)

A specification schema for authoring formal specifications in Codex with stable section identity and typed semantic document structure. Supports the full RFC 2119 requirement modality keyword set.

This schema imports shared traits from `paperhat-specification-foundation`. For strict Must/MustNot-only modality, use `paperhat-specification` instead.

## When to Use

Use this schema when the document follows RFC 2119 conventions and requires the full keyword set: Must, MustNot, Shall, ShallNot, Should, ShouldNot, May, Required, Recommended, Optional.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Specification | Semantic | ForbidsContent | Section (1+) | Root specification concept with required front-matter traits. |
| Section | Semantic (Entity) | ForbidsContent | Paragraph, OrderedList, UnorderedList, CodeBlock, Section, Requirement, Definition, Note, SectionReference, ExternalReference | Recursive section block with stable identity and semantic heading traits. |
| Paragraph | Semantic | RequiresContent (Flow) | -- | Standard paragraph block for prose content. |
| OrderedList | Structural | ForbidsContent | ListItem (1+) | Ordered list container. |
| UnorderedList | Structural | ForbidsContent | ListItem (1+) | Unordered list container. |
| ListItem | Semantic | RequiresContent (Flow) | -- | List item text content. |
| CodeBlock | Semantic | RequiresContent (Preformatted) | -- | Preformatted code or grammar block, with optional language token. |
| Requirement | Semantic | RequiresContent (Flow) | -- | A normative requirement statement with explicit modality. |
| Definition | Semantic | RequiresContent (Flow) | -- | A terminology definition with explicit `term`. |
| Note | Semantic | RequiresContent (Flow) | -- | Explicit note block for side remarks and clarifications. |
| SectionReference | Semantic | ForbidsContent | -- | Internal cross-reference to a `Section` entity via reference trait `target`. |
| ExternalReference | Semantic | ForbidsContent | -- | Reference to a non-entity external IRI via `uri`. |

## Front Matter Traits

Required on `Specification` (imported from `specbase`):

- `title` (`$Text`)
- `normative` (`$Boolean`)
- `locked` (`$Boolean`)
- `version` (`$Semver`)
- `editor` (`$Text`)

## Section Traits

Required on `Section` (imported from `specbase`):

- `id` (language-level entity identity)
- `key` (`$LookupToken`)
- `title` (`$Text`)
- `conformance` (`$EnumeratedToken`: `Normative` | `Informative`)

Optional on `Section` (imported from `specbase`):

- `division` (`$EnumeratedToken`: `Body` | `Appendix` | `FrontMatter` | `BackMatter`)
- `designation` (`$Text`) for projection-layer display labels

## Requirement Modality

`Requirement.modality` supports the full RFC 2119 keyword set, inherited from the foundation trait-level constraint:

- `Must` (MUST)
- `MustNot` (MUST NOT)
- `Shall` (SHALL)
- `ShallNot` (SHALL NOT)
- `Should` (SHOULD)
- `ShouldNot` (SHOULD NOT)
- `May` (MAY)
- `Required` (REQUIRED)
- `Recommended` (RECOMMENDED)
- `Optional` (OPTIONAL)

## Code Block Language

`CodeBlock.language` is an optional `$EnumeratedToken` to signal grammar or code notation (for example `$ebnf` or `$peg`).

## Design Decisions

- Section identity is explicit and stable via `id` + `key`.
- Section numbering is projection concern, not source-of-truth heading text.
- Section references are explicit semantic nodes (`SectionReference`, `ExternalReference`).
- Historical lineage concepts are intentionally excluded.
- Traits are imported from `paperhat-specification-foundation` and referenced with `specbase:` prefix in the schema definition. Authored documents use unqualified trait names.
- No concept-level modality narrowing. The full 10-member RequirementModality set from the foundation applies directly.

---

**End of Specification (RFC 2119) v1.0.0**
