Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification

A strict specification schema for authoring formal specifications in Codex with stable section identity and typed semantic document structure. Narrows requirement modality to Must and MustNot only.

This schema imports shared traits from `paperhat-specification-foundation`. For the full RFC 2119 keyword set (Must, MustNot, Shall, ShallNot, Should, ShouldNot, May, Required, Recommended, Optional), use `paperhat-specification-rfc2119` instead.

## When to Use

Use `Specification` when the document is normative or policy-defining and requires deterministic section identity, typed block structure, and machine-checkable requirements with strict Must/MustNot modality.

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
| Requirement | Semantic (Entity) | RequiresContent (Flow) | -- | A normative requirement statement with explicit modality and stable identity. |
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
| cite | `paperhat:domain:citation` | Citation, Contributor (bibliographic references within specification sections) |
| admonition | `paperhat:domain:admonition` | Warning, Danger, Critical, Notice, Informational, Tip |
| code | `paperhat:domain:code` | CodeBlock |
| example | `paperhat:domain:example` | Example |
| figure | `paperhat:domain:figure` | Figure |
| list | `paperhat:domain:list` | OrderedList, UnorderedList, ListItem |
| specbase | `paperhat:domain:specification-foundation` | Shared traits and enumerated value sets |
| relation | `paperhat:domain:relation` | RelationType, RelationInstance |
| text | `paperhat:domain:text` | Paragraph |

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

## Requirement Traits

Required on `Requirement` (imported from `specbase`):

- `id` (language-level entity identity)
- `key` (`$LookupToken`)
- `modality` (`$EnumeratedToken`: `Must` | `MustNot`)

The `modality` trait is narrowed at concept level to strict modality only. The foundation trait-level constraint allows the full RFC 2119 set, but this schema's concept-level AllowedValues restricts to `Must` and `MustNot`.

## RequirementSet Traits

Required:

- `title` (`$Text`) — names the requirement set (e.g., "Serialization Conformance Requirements")

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

## Gloss Binding Patterns

Inline content within `Paragraph`, `Requirement`, `ListItem`, and other flow-content concepts supports Gloss span-bindings. These bindings create semantic references from inline text spans to addressable entities within the document.

- **Term references**: `{~term-key | display text}` resolves to a `Definition` entity by its `term` value
- **Section references**: `{~section-key | display text}` resolves to a `Section` entity by its `key`
- **Requirement references**: `{~requirement-key | display text}` resolves to a `Requirement` entity by its `key`
- **External references**: `{@iri | display text}` resolves to an external IRI

Example:

```
<Paragraph>
	Processors MUST satisfy {~deterministic-output | Requirement 1} as defined in {~scope | Section 1}.
</Paragraph>
```

## Code Block Language

`CodeBlock.language` is an optional `$EnumeratedToken` to signal grammar or code notation (for example `$ebnf` or `$peg`).

## Design Decisions

- Section identity is explicit and stable via `id` + `key`.
- Section numbering is projection concern, not source-of-truth heading text.
- Section references are explicit semantic nodes (`SectionReference`, `ExternalReference`).
- Historical lineage concepts are intentionally excluded.
- Traits are imported from `paperhat-specification-foundation` and referenced with `specbase:` prefix in the schema definition. Authored documents use unqualified trait names.
- Conformance and division constraints are enforced at trait level in the foundation. Only modality is narrowed at concept level in this schema.

---

**End of Specification v1.0.0**
