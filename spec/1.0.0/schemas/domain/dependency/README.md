Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Dependency

A typed directional relationship between two entities where one depends on the other — a blocking dependency, prerequisite, sequencing constraint, or informational link.

## When to Use

Use `Dependency` to express that one entity depends on another: a milestone that blocks another milestone, a task that requires a prerequisite, or a document that follows another in sequence.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| source | $Iri | yes | The entity that depends on another. |
| target | $Iri | yes | The entity that is depended upon. |
| dependencyKind | $EnumeratedToken | no | The type of dependency relationship. |

## Design Notes

- `$MustNotBeEntity` because a dependency is a relationship between entities, not an entity itself.
- Both `source` and `target` are reference traits (`isReferenceTrait=true`).
- `dependencyKind` vocabulary: `$Blocks` (source cannot proceed until target completes), `$Requires` (source needs target as prerequisite), `$Follows` (source comes after target in sequence), `$Informs` (source benefits from target but is not blocked).

---

**End of Dependency v1.0.0**
