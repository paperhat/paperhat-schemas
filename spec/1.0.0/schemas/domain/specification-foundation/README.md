Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Specification Foundation

Shared foundation traits and enumerated value sets for specification schemas. This package provides the common trait vocabulary and value sets consumed by both the strict (`paperhat-specification`, Must/MustNot only) and loose (`paperhat-specification-rfc2119`, full RFC 2119 keyword set) specification schema variants.

## Purpose

The foundation package exists so that both specification schema variants share identical trait definitions and base enumerated value sets. Consuming schemas import this foundation and define their own concepts locally. The foundation defines no concepts and no constraints.

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `conformance` | `$EnumeratedToken` | SectionConformance | Whether a section is normative or informative. |
| `designation` | `$Text` | -- | Projection-layer display label for a section. |
| `division` | `$EnumeratedToken` | SectionDivision | Structural division of a section within the document. |
| `editor` | `$Text` | -- | Name of the responsible editor. |
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `label` | `$Text` | -- | Human-readable label for a reference. |
| `language` | `$EnumeratedToken` | -- | Grammar or code notation token for code blocks. |
| `locked` | `$Boolean` | -- | Whether the specification is locked against editing. |
| `modality` | `$EnumeratedToken` | RequirementModality | Requirement modality keyword. |
| `normative` | `$Boolean` | -- | Whether the specification is normative. |
| `requirementId` | `$LookupToken` | -- | Stable identifier for a specific requirement. |
| `target` | `$IriReference` | -- | Reference trait pointing to a target entity. |
| `term` | `$Text` | -- | The term being defined in a definition block. |
| `title` | `$Text` | -- | Title of a specification or section. |
| `uri` | `$IriReference` | -- | External IRI for an external reference. |
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

The full RFC 2119 keyword set. Consuming schemas may narrow this set at concept level.

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

## Design Decisions

- Trait-level AllowedValues are declared on `conformance`, `division`, and `modality` so that any consuming schema inherits the constraint automatically, even without concept-level AllowedValues.
- The RequirementModality set contains all 10 RFC 2119 keywords. The strict specification schema narrows this to {Must, MustNot} at concept level. The RFC 2119 specification schema inherits the full set.
- Trait IRI prefix is `codex:domain:specification-foundation:trait:*`, distinct from the consuming schemas' concept IRI prefixes.

---

**End of Specification Foundation v1.0.0**
