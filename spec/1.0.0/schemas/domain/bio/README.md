Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Bio

A biography document about a referenced entity, composed from metadata, ordered narrative content, and referenced annotations.

## When to Use

Use `Bio` for an authored biography or about-document whose subject is a referenced entity such as a person or organization. `Bio` is an entity document. It identifies its subject through the `subject` reference trait and carries the body of the biography in ordered narrative content.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Bio | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), narrative:Narrative (1), notes:Notes (0..1) | Root biography document. Requires `title` and `subject`. |

## Imports

| Namespace | Schema |
|---|---|
| docmeta | `codex:domain:document-metadata` |
| narrative | `codex:domain:narrative` |
| notes | `codex:domain:notes` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the biography document. |
| subject | $Iri | yes | The referenced entity the biography is about. Marked as a reference trait. |

## Constraints

- `subject` is the only permitted reference trait on `Bio`.
- `subject` must resolve.
- `subject` must target an entity.
- `narrative:Narrative` is required.

## Design Notes

- `Bio` is a document about an entity, not the entity itself. Person and Organization remain separate entity schemas.
- Unordered metadata belongs in `docmeta:DocumentMetadata`.
- Ordered prose belongs in `narrative:Narrative`.
- Referenced annotations belong in `notes:Notes`.

**End of Bio v1.0.0**
