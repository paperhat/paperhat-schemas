# Paperhat Schemas

Paperhat Schemas is the canonical repository for the universal Paperhat schema corpus.

It contains reusable schema packages, behavior packages, system packages, and reference vocabularies consumed by Paperhat systems. These schemas are not owned by Lexis. Lexis consumes them. Other Paperhat implementations can consume them as well.

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
│   ├── assembly/
│   ├── behavior/
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

## Naming

Repository package names currently use the `paperhat-` prefix for reusable Paperhat-owned schema packages.

Examples:

- `paperhat-recipe`
- `paperhat-food`
- `paperhat-person`
- `paperhat-location`
- `paperhat-tips`

Reference vocabulary packages keep their existing neutral names.

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

- `/Users/guy/Workspace/@paperhat/specifications/paperhat-schemas`

Compatibility location still present inside Lexis:

- `/Users/guy/Workspace/@paperhat/specifications/lexis-spec/spec/1.0.0/schemas`
- `/Users/guy/Workspace/@paperhat/specifications/lexis-spec/manifest.cdx`

The canonical source is this repository.
