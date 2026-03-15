Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# CrossReference

A typed internal reference from one document element to another — a section reference, requirement citation, or figure pointer with display text.

## When to Use

Use `CrossReference` to create typed internal references within a document: section references, requirement citations, figure pointers, table references. The foundry generates display text from the target element unless `displayText` is provided.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| target | $Iri | yes | The referenced element. |
| crossReferenceKind | $EnumeratedToken | no | The type of element being referenced. |
| displayText | $Text | no | Override text for the rendered reference. |

## Design Notes

- `$MustNotBeEntity` because a cross-reference is a pointer, not a referenceable entity.
- `target` is a reference trait (`isReferenceTrait=true`) pointing to an entity in the document.
- `crossReferenceKind` vocabulary: `$Section`, `$Requirement`, `$Figure`, `$Table`, `$Clause`, `$Definition`.
- `displayText` overrides auto-generated text (e.g., "see §3.2" or "per Requirement R-007").

---

**End of CrossReference v1.0.0**
