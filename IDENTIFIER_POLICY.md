# Identifier Policy

## Scope

This file defines the authoritative identifier policy for Paperhat-authored schemas and Paperhat-authored corpus entities.

## Schema Vocabulary Identifiers

Paperhat-authored schema vocabulary identifiers MUST use the `paperhat:` namespace.

This applies to:
- schema root identifiers
- concept identifiers
- trait identifiers
- enumerated value set identifiers
- rule identifiers
- other schema-owned vocabulary identifiers

Examples:
- `paperhat:domain:recipe`
- `paperhat:domain:recipe:Recipe`
- `paperhat:domain:recipe:trait:title`
- `paperhat:domain:specification:set:IssueStatus`

## Corpus Entity And Document Identifiers

Paperhat-authored corpus entities and authored documents MUST use the `urn:paperhat:` namespace.

Examples:
- `urn:paperhat:person:dharmesh-gordhan`
- `urn:paperhat:project:dharmesh-recipe-library`
- `urn:paperhat:recipe:soft-scrambled-eggs`

## Codex Import References

`SchemaImport.reference` MUST remain the Codex-defined content-addressed form:
- `urn:cdx:sha256:<hex-digest>`

This value is fixed by the Codex specification and MUST NOT be replaced with `paperhat:` or `urn:paperhat:`.

## Schema Namespaces

`Schema.namespace` remains a local `camelCase` namespace label used for qualified names inside authored documents.

Examples:
- `recipe`
- `person`
- `tips`
- `term`

A schema namespace label is not the same thing as a schema identifier.

## Forbidden Forms

Paperhat-authored schema vocabulary identifiers MUST NOT use:
- `codex:`
- `lexis:`
- `urn:cdx:`
- `urn:paperhat:`

Paperhat-authored corpus entities and authored documents MUST NOT use:
- `codex:`
- `lexis:`
- `paperhat:`

## Rationale

These schemas are universal Paperhat schemas. They are not owned by Lexis. The vocabulary authority therefore belongs to `paperhat:`.

Corpus entities and authored documents are runtime identities, not schema vocabulary identifiers. They therefore use `urn:paperhat:`.

## Cross-Reference

This repository rule is consistent with:
- the Codex requirement that schema concept and trait identifiers are IRI Values
- the Codex requirement that `SchemaImport.reference` uses `urn:cdx:sha256:<hex-digest>`
- the Lexis rule that Lexis consumes Codex imports and MUST NOT redefine them
