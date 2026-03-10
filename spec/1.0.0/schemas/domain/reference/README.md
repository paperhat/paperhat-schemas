Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Reference

A typed link to an entity, used to express relationships between concepts without embedding.

## When to Use

Use `Reference` to point at an entity defined elsewhere rather than embedding it inline. For example, an event's organiser might be a Reference to a Person entity rather than a nested Person.

## Concepts

| Concept | Kind | Content | Description |
|---|---|---|---|
| Reference | Structural | ForbidsContent | A link to an entity via its `target` trait. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| target | $IriReference | yes | The IRI of the referenced entity. Marked as a reference trait (`isReferenceTrait=true`). |

## Constraints

- The `target` trait must resolve to an entity (`ReferenceTargetsEntity`).

## Design Notes

- Reference is content-free by design: it is a pointer, not a container. Any descriptive content belongs on the target entity itself.

---

**End of Reference v1.0.0**
