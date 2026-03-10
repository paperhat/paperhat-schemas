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
| Section | Semantic (Entity) | ForbidsContent | Paragraph, OrderedList, UnorderedList, CodeBlock, Section, Requirement, RequirementSet, Definition, Note, TermBinding, Issue, OpenQuestion, SectionReference, ExternalReference, Citation | Recursive section block with stable identity and semantic heading traits. |
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
| RequirementSet | Semantic | ForbidsContent | Requirement (1+, ordered) | A named group of related requirements, independent of section structure. |
| TermBinding | Semantic | ForbidsContent | -- | Formal declaration binding a term to a definition source (internal entity or external IRI). |
| Issue | Semantic (MayBeEntity) | RequiresContent (Flow) | -- | A tracked issue in a draft specification. Typically resolved or removed before locking. |
| OpenQuestion | Semantic (MayBeEntity) | RequiresContent (Flow) | -- | A tracked open question in a draft specification. Typically answered or removed before locking. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| cite | `codex:domain:citation` | Citation, Contributor (bibliographic references within specification sections) |
| admonition | `codex:domain:admonition` | Warning, Danger, Critical, Notice, Informational, Tip |
| code | `codex:domain:code` | CodeBlock |
| example | `codex:domain:example` | Example |
| figure | `codex:domain:figure` | Figure |
| list | `codex:domain:list` | OrderedList, UnorderedList, ListItem |
| specbase | `codex:domain:specification-foundation` | Shared traits and enumerated value sets |
| relation | `codex:domain:relation` | RelationType, RelationInstance |
| text | `codex:domain:text` | Paragraph |

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

## RequirementSet Traits

Required:

- `title` (`$Text`) — names the requirement set

Optional:

- `key` (`$LookupToken`) — stable lookup key for cross-referencing the set

## TermBinding Traits

Required (imported from `specbase`):

- `term` (`$Text`) — the term being bound
- `source` (`$Iri`) — reference to the definition (internal Definition entity IRI or external IRI)

Optional:

- `label` (`$Text`) — human-readable source description (e.g., "RFC 2119, §1")

TermBinding declares formal term-definition associations at the document structure level. Use TermBinding when a specification declares which terms govern a section — especially when the definition lives outside the current document. For inline term references within prose, use Gloss `{~term-key | display text}` instead.

## Issue Traits

Required:

- `key` (`$LookupToken`) — stable reference for the issue

Optional (imported from `specbase`):

- `status` (`$EnumeratedToken`: `Open` | `Resolved` | `Deferred`)
- `resolution` (`$Text`) — how the issue was resolved

Issues are draft-phase items. They are typically resolved or removed before a specification is locked.

## OpenQuestion Traits

Required:

- `key` (`$LookupToken`) — stable reference for the question

Optional (imported from `specbase`):

- `status` (`$EnumeratedToken`: `Open` | `Answered` | `Deferred`)
- `answer` (`$Text`) — the answer once decided

OpenQuestions are draft-phase items. They are typically answered or removed before a specification is locked.

## Citation

Sections may contain `cite:Citation` children from the imported citation schema. This enables structured bibliographic references within specifications. See the Citation schema documentation for full details.

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
