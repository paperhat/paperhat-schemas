Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification Foundation

Shared foundation for specification schemas. Provides all common traits, enumerated value sets, shared concepts, constraints, and content-schema imports consumed by both the strict (`paperhat-specification`, Must/MustNot only) and loose (`paperhat-specification-rfc2119`, full RFC 2119 keyword set) specification schema variants.

## Purpose

The foundation package exists so that both specification schema variants share identical structural concepts, trait definitions, and base enumerated value sets. Consuming schemas import this foundation and define only their own `Specification` root concept and `Requirement` concept (with variant-specific modality constraints).

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Section | Semantic | MustBeEntity | ForbidsContent | Paragraph, OrderedList, UnorderedList, CodeBlock, Section, Requirement, GlossaryEntry, Note, SectionReference, ExternalReference, Figure, Example, RelationType, RelationInstance, admonitions, RequirementSet, TermBinding, Issue, OpenQuestion, Citation, Description, DocumentMetadata, Procedure, Summary, TermEntry, AbbreviationList, Acknowledgments, ConformanceClause, Grammar, IPNotice, ISODocumentMetadata, MathBlock, RevisionHistory, SymbolTable, TestSuite | Recursive section block with stable identity and semantic heading traits. |
| Note | Semantic | MustNotBeEntity | RequiresContent (Flow) | -- | Explicit note block for side remarks and clarifications. |
| SectionReference | Semantic | MustNotBeEntity | ForbidsContent | -- | Internal cross-reference to a Section entity via reference trait `target`. |
| ExternalReference | Semantic | MustNotBeEntity | ForbidsContent | -- | Reference to a non-entity external IRI via `uri`. |
| Rationale | Semantic | MustNotBeEntity | ForbidsContent | Paragraph (1+), OrderedList, UnorderedList, Citation (ordered) | Justification for a requirement. Structured block explaining why a requirement exists. |
| RequirementSet | Semantic | MustNotBeEntity | ForbidsContent | Requirement (1+, ordered) | A named group of related requirements, independent of section structure. |
| TermBinding | Semantic | MustNotBeEntity | ForbidsContent | -- | Formal declaration binding a term to a definition source. |
| Issue | Semantic | MayBeEntity | RequiresContent (Flow) | -- | A tracked issue in a draft specification. |
| OpenQuestion | Semantic | MayBeEntity | RequiresContent (Flow) | -- | A tracked open question in a draft specification. |

Note: `Section` and `RequirementSet` allow `Requirement` children. The `Requirement` concept itself is defined by each consuming variant schema, not by this foundation. The foundation's child rules reference `Requirement` by name; the consuming schema supplies the definition.

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| admonition | `paperhat:domain:admonition` | Warning, Danger, Critical, Notice, Informational, Tip |
| cite | `paperhat:domain:citation` | Citation, Contributor |
| code | `paperhat:domain:code` | CodeBlock |
| example | `paperhat:domain:example` | Example |
| figure | `paperhat:domain:figure` | Figure |
| glossary | `paperhat:domain:glossary` | GlossaryEntry |
| list | `paperhat:domain:list` | OrderedList, UnorderedList, ListItem |
| desc | `paperhat:domain:description` | Description |
| docmeta | `paperhat:domain:document-metadata` | DocumentMetadata |
| procedure | `paperhat:domain:procedure` | Procedure |
| relation | `paperhat:domain:relation` | RelationType, RelationInstance |
| summary | `paperhat:domain:summary` | Summary |
| term | `paperhat:domain:term-entry` | TermEntry, Sense, UsageExample, Etymology, TermForm, TermRelation |
| text | `paperhat:domain:text` | Paragraph |
| abbr | `paperhat:domain:abbreviation` | Abbreviation, Initialism, Acronym, AbbreviationList |
| ack | `paperhat:domain:acknowledgments` | Acknowledgments, Participant, ParticipantGroup |
| conf | `paperhat:domain:conformance-class` | ConformanceClause, ConformanceClass, ConformanceRequirement |
| grammar | `paperhat:domain:formal-grammar` | Grammar, ProductionRule, ProductionAlternative, RuleReference |
| ip | `paperhat:domain:intellectual-property` | Copyright, Trademark, ServiceMark, RegisteredTrademark, Patent, LicenseGrant, IPNotice |
| isometa | `paperhat:domain:iso-document-metadata` | ISODocumentMetadata, Committee, Subcommittee, WorkingGroup, ICSClassification, ISOForeword, EditionHistory, EditionEntry, RelatedPart |
| math | `paperhat:domain:math-expression` | Expression, Variable, Number, Operator, Apply, MathBlock, and 23 more |
| revhist | `paperhat:domain:revision-history` | RevisionHistory, RevisionEntry, Change |
| sym | `paperhat:domain:symbol` | Symbol, MathSymbol, Emoji, SymbolTable |
| test | `paperhat:domain:test-assertion` | TestAssertion, Precondition, ExpectedOutcome, TestProcedure, TestSuite |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `amends` | `$Iri` | -- | IRI of a specification that this specification amends without replacing. |
| `answer` | `$Text` | -- | The answer to an open question once decided. |
| `conformance` | `$EnumeratedToken` | SectionConformance | Whether a section is normative or informative. |
| `deprecated` | `$Boolean` | -- | Whether this item is deprecated and should no longer be relied upon. |
| `deprecatedSince` | `$Semver` | -- | The specification version at which this item was deprecated. |
| `designation` | `$Text` | -- | Projection-layer display label for a section. |
| `division` | `$EnumeratedToken` | SectionDivision | Structural division of a section within the document. |
| `editor` | `$Text` | -- | Name of the responsible editor. |
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `label` | `$Text` | -- | Human-readable label for a reference. |
| `locked` | `$Boolean` | -- | Whether the specification is locked against editing. |
| `maturityLevel` | `$EnumeratedToken` | (external vocabulary) | Maturity stage of the specification within its standards track. Values from an imported maturity vocabulary. |
| `modality` | `$EnumeratedToken` | RequirementModality | Requirement modality keyword. |
| `normative` | `$Boolean` | -- | Whether the specification is normative. |
| `obsoletes` | `$Iri` | -- | IRI of a specification rendered obsolete by this one. Stronger than supersedes. |
| `requirementId` | `$LookupToken` | -- | Stable identifier for a specific requirement. |
| `resolution` | `$Text` | -- | How an issue was resolved. |
| `source` | `$Iri` | -- | Reference to a definition source (internal entity or external IRI). |
| `status` | `$EnumeratedToken` | -- | Current status of a draft item (Issue or OpenQuestion). |
| `supersedes` | `$Iri` | -- | IRI of a specification superseded by this one. Target may still be valid for historical reference. |
| `target` | `$Iri` | reference | Reference trait pointing to a target entity. |
| `term` | `$Text` | -- | The term being defined in a definition block. |
| `title` | `$Text` | -- | Title of a specification or section. |
| `uri` | `$Iri` | -- | External IRI for an external reference. |
| `version` | `$Semver` | -- | Semantic version of the specification. |

## Enumerated Value Sets

### SectionConformance

| Member | Description |
|---|---|
| `Normative` | Section contains normative requirements. |
| `Informative` | Section contains non-normative explanatory content. |

### SectionDivision

| Member | Description |
|---|---|
| `Body` | Main body of the specification. |
| `Appendix` | Supplementary appendix material. |
| `FrontMatter` | Front matter preceding the body. |
| `BackMatter` | Back matter following the body. |

### RequirementModality

The full RFC 2119 keyword set. The strict specification schema narrows this to {Must, MustNot} at concept level.

| Member | RFC 2119 Keyword |
|---|---|
| `Must` | MUST |
| `MustNot` | MUST NOT |
| `Shall` | SHALL |
| `ShallNot` | SHALL NOT |
| `Should` | SHOULD |
| `ShouldNot` | SHOULD NOT |
| `May` | MAY |
| `Required` | REQUIRED |
| `Recommended` | RECOMMENDED |
| `Optional` | OPTIONAL |

### IssueStatus

Status values for Issues. Issues are resolved, not answered.

| Member | Description |
|---|---|
| `Open` | The issue is unresolved and requires attention. |
| `Resolved` | The issue has been resolved. |
| `Deferred` | The issue has been deferred to a future revision. |

### OpenQuestionStatus

Status values for OpenQuestions. Questions are answered, not resolved.

| Member | Description |
|---|---|
| `Open` | The question is unanswered and requires attention. |
| `Answered` | The question has been answered. |
| `Deferred` | The question has been deferred to a future revision. |

## Constraints

| Constraint | Target | Rule | Description |
|---|---|---|---|
| section-reference-target-type | SectionReference | ReferenceTargetsConcept → Section | SectionReference target must resolve to a Section. |
| section-reference-must-resolve | SectionReference | ReferenceMustResolve | SectionReference target must resolve to an existing entity. |

## Design Decisions

- The foundation defines all structural concepts shared across specification variants. Only the `Specification` root and `Requirement` concept are variant-specific.
- `IssueStatus` and `OpenQuestionStatus` are separate value sets with distinct semantics: issues are resolved, questions are answered. There is no union set.
- `Section` and `RequirementSet` allow `Requirement` children by name. The consuming variant schema supplies the actual `Requirement` concept definition.
- Trait-level AllowedValues are declared on `conformance`, `division`, and `modality` so that any consuming schema inherits the constraint automatically.
- `maturityLevel` has no inline AllowedValues; the constraint is supplied at concept level when a maturity vocabulary package (e.g. `maturity-w3c`, `maturity-ietf`) is composed in.
- `supersedes`, `obsoletes`, and `amends` are `$Iri` traits (not reference traits) because they point to external specifications, not in-document entities.
- `deprecated` and `deprecatedSince` are wired as AllowsTrait on Section. Wiring to Specification root and Requirement will occur in the variant schemas and during final integration.
- Trait IRI prefix is `paperhat:domain:specification-foundation:trait:*`, distinct from the consuming schemas' concept IRI prefixes.

---

**End of Specification Foundation v1.0.0**
