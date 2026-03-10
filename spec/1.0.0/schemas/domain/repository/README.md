Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Repository

A storage and retrieval system for artifacts, such as a source code repository, document archive, package registry, or artifact store.

## When to Use

Use `Repository` to represent a named storage system that holds and serves artifacts. Examples include Git repositories, document management systems, package registries (npm, PyPI), container registries, or archive systems. Repository is an entity (`$MustBeEntity`) and can be referenced from Project, Organization, or any schema that needs to point to where artifacts live. Repository is distinct from Project (an endeavor) and MediaAsset (a single file).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The repository name (e.g., "paperhat-schemas", "codex-lang", "npm registry"). |
| repositoryKind | $EnumeratedToken | no | Classification token, e.g., `$Git`, `$DocumentArchive`, `$PackageRegistry`, `$ContainerRegistry`, `$ArtifactStore`. Open vocabulary. |
| url | $Url | no | The repository URL (e.g., a GitHub URL, registry endpoint). |
| repositoryStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Active`, `$Archived`, `$ReadOnly`, `$Deprecated`. Open vocabulary. |

## Constraints

`name` is required. A repository without a name is empty.

## Design Notes

- Repository is an entity (`$MustBeEntity`) because repositories need stable identity for cross-references. Projects, Organizations, and other schemas reference Repositories by entity IRI.
- This is a pure leaf with no imports and no children. Higher-level composers (Stage 4) will compose Repository as a child of Project or Organization alongside Description, Tags, and other leaf schemas.
- Project already has a `repositoryUrl` trait for the simple single-repository case. Repository as a separate entity handles the case where the repository itself is the primary subject, or when modeling multiple repositories with their own metadata.
- `repositoryKind` is `$EnumeratedToken` rather than `$Text` because repository types are machine-readable classifiers.

---

**End of Repository v1.0.0**
