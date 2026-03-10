Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Linked Data Mapping Schema

Defines a one-way mapping document format used to project Codex-authored data into linked data vocabularies for JSON-LD, RDFa, or microdata emitters.

## When to Use

Use this schema when creating a mapping document that translates a Codex domain schema into a linked data vocabulary. Each mapping document targets one Codex schema and declares how its concepts and traits correspond to target types and properties.

## Concepts

| Concept | Kind | Purpose |
|---|---|---|
| SchemaOrgMapping | Semantic | Root mapping document. Declares the mapping identity and version, and contains type and property mappings. |
| MapType | Structural | Maps a Codex concept to a target linked data type. |
| MapContentToProperty | Structural | Maps the content of a Codex concept to a target linked data property. |
| MapTraitToProperty | Structural | Maps a Codex trait to a target linked data property. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| id | `$IriReference` | SchemaOrgMapping | Stable identity reference for the mapping document. |
| version | `$Text` | SchemaOrgMapping | Version of the mapping document. |
| sourceConcept | `$Text` | MapType, MapContentToProperty, MapTraitToProperty | The Codex concept being mapped. |
| sourceTrait | `$Text` | MapTraitToProperty | The Codex trait being mapped. |
| targetType | `$Text` | MapType | The target linked data type to map to. |
| targetProperty | `$Text` | MapContentToProperty, MapTraitToProperty | The target linked data property to map to. |

## Constraints

- **root-only** — A mapping document must have exactly one root SchemaOrgMapping.

## Design Notes

- Mappings are one-way: Codex to the target vocabulary. There is no round-trip guarantee.
- Each mapping document targets a single Codex schema. To map multiple schemas, create multiple mapping documents.
- The mapping schema defines how to write mapping documents, not the mappings themselves.

---

**End of Linked Data Mapping Schema v1.0.0**
