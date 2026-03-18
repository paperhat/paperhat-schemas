# Conformance Class

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the structure for conformance clauses in technical specifications. A conformance clause declares named conformance classes, each of which binds a set of requirements that an implementation must satisfy to claim conformance to that class. This is a universal pattern in standards documents (W3C, ISO, IETF, OASIS, IEEE).

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| ConformanceClause | Semantic | MustBeEntity | ForbidsContent | ConformanceClass (1+), Description, Paragraph | Top-level container for all conformance classes. Typically one per specification. |
| ConformanceClass | Semantic | MustBeEntity | ForbidsContent | Description, ConformanceRequirement, Paragraph | A named conformance target (e.g. "Conforming User Agent", "Conforming Document"). Lists the requirements that must be met. |
| ConformanceRequirement | Semantic | MustNotBeEntity | ForbidsContent | -- | A reference to a specific requirement that an implementation must satisfy. Uses `target` reference trait to point to a Requirement entity. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing conformance classes and clauses. |
| `title` | `$Text` | -- | Human-readable title (e.g. "Conforming Processor", "Level A Conformance"). |
| `label` | `$Text` | -- | Short display label for projection. |
| `target` | `$Iri` | reference | Reference to a requirement entity that must be satisfied. |
| `conditional` | `$Boolean` | -- | Marks a conformance requirement as conditional on implementation choices. |

## Constraints

| Constraint | Target | Rule | Description |
|---|---|---|---|
| conformance-requirement-must-resolve | ConformanceRequirement | ReferenceMustResolve | ConformanceRequirement target must resolve to an existing entity. |

## Design Decisions

- `ConformanceClause` is the top-level container; `ConformanceClass` is a named target within it. This two-level structure matches real specification practice where a single conformance section defines multiple target classes.
- `ConformanceRequirement` uses a reference trait (`target`) pointing to Requirement entities. This creates a machine-verifiable link between conformance classes and their requirements.
- `conditional` trait on ConformanceRequirement supports the common pattern where some requirements only apply if an implementation supports an optional feature.
- No `ReferenceTargetsConcept` constraint on ConformanceRequirement because the target Requirement concept is defined in variant schemas (not in this schema's import closure). The constraint that targets must resolve is still enforced.
- ConformanceClass is MustBeEntity so it is cross-referenceable from other parts of the specification (e.g. "implementations conforming to ConformanceClass X must...").
