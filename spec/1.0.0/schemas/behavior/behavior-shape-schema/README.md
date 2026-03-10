Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Behavior Shape Schema

Schema for defining behavioral shapes that attach constraints and derivations to value types and entity concepts.

## When to Use

Use `ValueShapeDefinition` to define a constrained value type (e.g., a number that must be positive, a text that must match an email pattern). Use `EntityShapeDefinition` to attach behavioral constraints and computed derivations to an entity concept (e.g., deriving a `fullName` from `firstName` and `lastName` on a Person).

## Concepts

| Concept | Kind | Entity Eligibility | Description |
|---|---|---|---|
| ValueShapeDefinition | $Semantic | $MustBeEntity | Extends a base value type with behavioral constraints and derivations. |
| EntityShapeDefinition | $Semantic | $MustBeEntity | Attaches behavioral constraints and derivations to entity nodes. |
| Constraint | $Structural | $MustNotBeEntity | A validity condition that must evaluate to true for the shape to be satisfied. |
| Derivation | $Structural | $MustNotBeEntity | A computed value that must be materialized for the shape. |

## Traits

| Trait | Type | Used By | Description |
|---|---|---|---|
| baseValueType | $EnumeratedToken | ValueShapeDefinition | The underlying Codex ValueType. |
| targetConcept | $Text | EntityShapeDefinition | The concept name this shape applies to. |
| message | $Text | Constraint | Human-readable error message on failure. |
| targetTrait | $Text | Derivation | The trait where the derived value is materialized. |
| outputShape | $EnumeratedToken | Derivation | The ValueShape the derived value conforms to. |
| derivationClass | $EnumeratedToken | Derivation | Whether the derivation is `$Materialize` (written to graph) or `$Ephemeral` (downstream only). |
| when | $Boolean | Derivation | Optional guard condition for conditional derivations. |

## Constraints

- `ValueShapeDefinition` requires `id`, `name`, and `baseValueType`.
- `EntityShapeDefinition` requires `id` and `targetConcept`.
- `Derivation` requires `name`, `targetTrait`, `outputShape`, and `derivationClass`.
- Both shape definitions allow `Constraint` and `Derivation` as children.

## Design Notes

- Shape definitions are `$MustBeEntity` because they are referenced by name from other schemas and shapes.
- `Constraint` and `Derivation` are `$MustNotBeEntity` structural wrappers that contain expression trees from the Behavior Expression Schema.
- Pure leaf package with no imports. Expression content comes from the behavior-expression-schema package.

---

**End of Behavior Shape Schema v1.0.0**
