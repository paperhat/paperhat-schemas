# Paperhat Schemas

Paperhat Schemas is the canonical repository for the universal Paperhat schema corpus.

It contains reusable schema packages, behavior packages, system packages, and reference vocabularies consumed by Paperhat systems. These schemas are not owned by Lexis. Lexis consumes them. Other Paperhat implementations consume them as well.

## What This Repository Contains

This repository contains:

- domain schema packages
- behavior schema packages and operator vocabulary
- view schema packages
- system schema packages
- reference vocabularies
- the root repository manifest

Current canonical manifest:

- `manifest.cdx`

Current canonical schema tree:

- `spec/1.0.0/schemas/`

## Repository Structure

```text
manifest.cdx
spec/1.0.0/
├── schemas/
│   ├── behavior/
│   ├── composition/
│   ├── design/
│   ├── domain/
│   ├── system/
│   ├── view/
│   └── vocabularies/
```

## Package Structure

A schema package uses this structure:

```text
<package>/
├── manifest.cdx
├── schema.cdx
├── README.md
├── examples/
├── templates/
└── localizations/
```

Vocabulary packages use `vocabulary.cdx` instead of `schema.cdx` as their primary document. Vocabularies define closed token sets, not structural schemas.

## Schema Identifier Policy

Paperhat-authored schema vocabulary identifiers MUST use the `paperhat:` namespace.

Paperhat-authored corpus entities and authored documents MUST use the `urn:paperhat:` namespace.

`SchemaImport.reference` MUST remain `urn:cdx:sha256:<hex-digest>`.

Authoritative policy file:

- `IDENTIFIER_POLICY.md`

## Naming

Paperhat-authored schema packages use the `paperhat-` prefix. This applies to domain, system, view, composition, and design families.

Examples:

- `paperhat-recipe` (domain)
- `paperhat-person` (domain)
- `paperhat-localization` (system)
- `paperhat-adaptive-plan` (design)
- `paperhat-composition` (composition)

Behavior packages use a `behavior-` prefix that identifies the family directly.

Examples:

- `behavior-expression-schema`
- `behavior-shape-schema`

Reference vocabulary packages keep neutral names derived from their source standards.

Examples:

- `iso-3166-countries`
- `units-volume`
- `food-categories`

## Authority Boundary

This repository defines schema packages.

This repository does not define:

- Codex language semantics
- Gloss language semantics
- Lexis pipeline semantics
- foundry behavior

Those belong in their own specifications and implementations.

## Relationship To Lexis

Lexis currently points to this repository through compatibility links while the wider workspace catches up.

Canonical schema location:

- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas`

Compatibility location still present inside Lexis:

- `/Users/guy/Workspace/@paperhat/specifications/applications/lexis-spec/spec/1.0.0/schemas`
- `/Users/guy/Workspace/@paperhat/specifications/applications/lexis-spec/manifest.cdx`

The canonical source is this repository.

## Closure Refresh

Refresh SchemaImport references and manifest closure hashes with the local repository tool:

```bash
python3 tools/refresh_repository_closure.py
```

This command iterates SchemaImport normalization to a fixed point, runs manifest normalization, reruns both sanctioned checks, and fails if any drift remains.
