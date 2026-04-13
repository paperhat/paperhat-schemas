# Design Package

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Bundles design annotation documents into an ordered, referenceable package. A DesignPackage groups related DesignAnnotation documents so the adaptive plan compiler processes them as a single unit.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| DesignPackage | Semantic | MustBeEntity | ForbidsContent | Title (1), Description (0–1), DesignMember (1+) | Root container that bundles design annotation documents into an ordered package. |
| DesignMember | Structural | MustNotBeEntity | ForbidsContent | — | A single entry in the package, pointing to one design annotation document by IRI. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Title |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `annotation` | `$Iri` | — | IRI of the design annotation document this member references. |

## Design Decisions

- DesignPackage is MustBeEntity so it is referenceable from adaptive plan compilation inputs.
- DesignMember is Structural and MustNotBeEntity because it is a positional reference, not a standalone semantic unit.
- The package enforces ordering (CollectionRules ordering=$Ordered) because annotation processing order affects constraint precedence.
- Only one trait exists because the member's sole purpose is to point to an annotation document. All semantics live in the annotations themselves.
