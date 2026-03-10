Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Release

A versioned artifact snapshot of a product — a specific release such as v2.3.1 of a software system, carrying version, lifecycle status, and a back-reference to the product it belongs to.

## When to Use

Use `Release` to model versioned snapshots of products and systems. A Product is the ongoing entity (Codex, Lexis); a Release is a specific version of that entity (Codex v2.3.1). Releases have stable identity and are referenced from documentation, changelogs, and compatibility matrices.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| version | $Text | yes | The version identifier (e.g., "2.3.1", "1.0.0-rc.1"). |
| releaseKind | $EnumeratedToken | no | Classification token, e.g., `$Major`, `$Minor`, `$Patch`, `$Prerelease`, `$Hotfix`. Open vocabulary. |
| releaseStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Stable`, `$Deprecated`, `$Yanked`, `$ReleaseCandidate`, `$Beta`, `$Alpha`. Open vocabulary. |
| releaseDate | $Date | no | The date this release was published. |
| product | $Iri | no | Reference to the product this release belongs to. |

## Constraints

`version` is required. A release without a version identifier is meaningless.

## Design Notes

- `$MustBeEntity` because releases have stable identity ("Codex v2.3.1") and are cross-referenced from documentation, compatibility matrices, and changelogs.
- `product` is a reference trait (`isReferenceTrait=true`) pointing to a Product entity. Follows the same pattern as Tier.product.
- Distinct from Publication: a Publication is a published creative work (book, journal). A Release is a versioned product artifact (software version, standard version). Different semantic purpose, different trait set.
- Children (Description, MediaAsset for download artifacts, Identifier for checksums, Tags) are wired by composing schemas, not imported here.
- Pure leaf with no imports, keeping the dependency graph minimal.

---

**End of Release v1.0.0**
