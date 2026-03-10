Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Codex Data Meta-Schema

Authorizes domain ontology schemas. Defines what domain schemas may declare and forbids individuals, views, policies, layout, and assembly. Content is forbidden by default and must be explicitly allowed per Concept. Sequence and Group are permitted only as ordering overrides under CollectionOverride.

## When to Use

Use the data meta-schema when defining a new domain schema. Every domain schema must conform to this meta-schema: concepts must be declared as `DomainConcept`, content must be explicitly opted in, and collection ordering must be declared.

## Concepts

| Concept | Kind | Purpose |
|---|---|---|
| DomainConcept | Semantic | Defines a domain ontology concept. Content is forbidden by default; entity eligibility is `$MustNotBeEntity`. |
| CollectionOverride | Structural | Provides a context for Sequence and Group ordering overrides within a domain schema. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| id | `$IriReference` | yes | Stable identity reference for the concept or override. |
| priority | `$EnumeratedToken` | no | Priority level. Allowed values: `$Primary`, `$Secondary`. |

## Constraints

- **no-instances** — Domain schemas must not define individuals. No concept may use `$MustBeEntity`.
- **content-opt-in** — Content is forbidden by default in domain concepts. Content must be explicitly allowed.
- **ordering-declared** — Default collection ordering must be declared for every DomainConcept.
- **override-context-only** — Sequence and Group are permitted only within CollectionOverride.

## Design Notes

- The data meta-schema is a governance artifact. It constrains what domain schemas are allowed to declare but does not itself define any domain concepts.
- Content-forbidden-by-default is deliberate: domain concepts are data structures, not prose containers. Content is permitted only when explicitly opted in.

---

**End of Codex Data Meta-Schema v1.0.0**
