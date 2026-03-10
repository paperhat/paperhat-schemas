Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Relation

Semantic relational data model for deterministic, presentation-agnostic tabular data authoring.

This schema models facts as relations, tuples, attributes, and tuple-attribute bindings. Grid concerns (row/column ordering, spans, merged-cell rendering) are projection concerns and are intentionally excluded from canonical domain data.

## Purpose

- Represent tabular facts canonically as relational data.
- Preserve sparsity by asserting only present tuple-attribute bindings.
- Keep canonical semantics independent from any rendered table layout.
- Enable deterministic projection into table/grid views when projection rules are explicit.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| `RelationType` | Semantic | Yes | Forbids | `text:Title`, `desc:Description` (0..1), `Attribute` (1+), `AttributeKey` | Declares attribute definitions for a relation. |
| `Attribute` | Semantic | Yes | Forbids | `desc:Description` (0..1) | Declares one relation attribute and its expected value type. |
| `AttributeKey` | Structural | No | Forbids | `KeyAttribute` (1+) | Declares key composition from one or more attributes. |
| `KeyAttribute` | Structural | No | Forbids | -- | References one `Attribute` for key composition. |
| `RelationInstance` | Semantic | Yes | Forbids | `text:Title`, `desc:Description` (0..1), `Tuple` | Holds tuples for one relation type via `for`. |
| `Tuple` | Semantic | Yes | Forbids | `desc:Description` (0..1), `Binding` | One relation member with one or more bindings. |
| `Binding` | Structural | No | Forbids | -- | Associates one tuple with one attribute target and one value. |

## Traits

| Trait | Value Type | Scope | Description |
|---|---|---|---|
| `name` | `$Text` | RelationType, Attribute, AttributeKey, RelationInstance, Tuple | Human-readable identifier. |
| `valueType` | `$EnumeratedToken` (built-in type tokens) | Attribute | Declares expected Codex value type for bindings targeting this attribute. |
| `required` | `$Boolean` | Attribute | Declares whether each tuple is expected to provide a binding for the attribute. |
| `value` | Union of all built-in value types | Binding | Actual bound value for `(tuple, attribute)`. |

Reference traits are reused from Codex language semantics:

- `for` on `RelationInstance` points to `RelationType`.
- `target` on `KeyAttribute` and `Binding` points to `Attribute`.

## Determinism Rules

- Collection semantics are explicitly `$Unordered` and duplicate-disallowing where declared.
- Canonical schema data contains no row indices, column indices, row spans, or column spans.
- Any table/grid ordering or merging is defined by projection rules outside this schema.

## Multi-Valued Attributes

This schema supports multi-valued bindings through the `value` trait union.

- A single binding value may itself be a collection (`$List`, `$Set`, `$Map`, `$Tuple`, `$Range`, `$Record`).
- Relation-valued attributes use `$IriReference` values that point to another `RelationInstance`.
- No implicit expansion is defined in canonical form; projection behavior must be explicit.

## Design Notes

- Canonical relation semantics are separated from presentation semantics.
- Existing reusable concepts are imported from `paperhat-text` and `paperhat-description`; no duplicate text/list/description concepts are introduced.
- Reference associations use language-defined reference traits (`for`, `target`) so constraints can be validated with Codex reference constraints.

---

**End of Relation v1.0.0**
