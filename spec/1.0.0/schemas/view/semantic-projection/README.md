Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Semantic Projection View Schema

This package defines View-family schema concepts for authoring deterministic semantic projection definitions described by Lexis Specification `§20`.

## Concepts

| Concept | Kind | Purpose |
|---|---|---|
| SemanticProjectionDefinition | Semantic | Root definition entity containing parameter declarations and ordered projection rules. |
| ProjectionParameter | Structural | Declares a named projection parameter and references its `ValueShapeDefinition`. |
| ProjectionRule | Structural | Abstract rule concept used to anchor shared rule traits. |
| SelectRule | Structural | Initializes the working set from canonical universe `U`. |
| PruneRule | Structural | Removes selected structures from the working set. |
| CollapseRule | Structural | Rewrites selected source structures into coarser nodes. |
| DeriveAnnotationRule | Structural | Adds deterministic derived nodes or edges. |
| RuleSelectors | Structural | Rule-local selector list container. |
| ConceptTypeSelector | Structural | Selector primitive by concept type. |
| TraitPathSelector | Structural | Selector primitive by trait path. |
| RelationshipEdgeSelector | Structural | Selector primitive by relationship type. |
| ValuePredicateSelector | Structural | Selector primitive using Behavior `Validation` expression. |
| IntersectionSelector | Structural | Selector primitive that intersects multiple selector operands. |
| CollapseTraitMapping | Structural | Maps source trait path to target trait name for collapse operations. |
| FixedStructuralTransform | Structural | Declares deterministic non-Behavior transform name for DeriveAnnotation. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| ruleIdentifier | `$IriReference` | rule concepts | Stable rule identifier used for provenance and derivation identity. |
| parameterName | `$Text` | ProjectionParameter | Parameter identifier. |
| parameterShapeReference | `$IriReference` | ProjectionParameter | IRI reference to `ValueShapeDefinition` used for parameter validation. |
| parameterRequired | `$Boolean` | no | Explicit required flag for parameter binding. |
| selectorTarget | `$EnumeratedToken` | no | Selector evaluation target (`$CanonicalUniverse` or `$WorkingSet`). |
| selectorConceptType | `$Text` | ConceptTypeSelector | Concept type selector operand. |
| selectorTraitPath | `$Text` | TraitPathSelector | Trait path selector operand. |
| selectorRelationshipType | `$Text` | RelationshipEdgeSelector | Relationship type selector operand. |
| targetConceptType | `$Text` | CollapseRule | Target concept type for replacement node creation. |
| sourceTraitPath | `$Text` | CollapseTraitMapping | Source trait path in collapse mapping. |
| targetTraitName | `$Text` | CollapseTraitMapping | Target trait in collapse mapping. |
| transformClass | `$EnumeratedToken` | no | DeriveAnnotation transform class (`$BehaviorExpression` or `$StructuralTransform`). |
| transformName | `$Text` | FixedStructuralTransform | Stable identifier for fixed deterministic transform behavior. |

## Constraints

- `SemanticProjectionDefinition` MUST include exactly one `SelectRule`.
- Every rule concept (`SelectRule`, `PruneRule`, `CollapseRule`, `DeriveAnnotationRule`) MUST include one `RuleSelectors` child.
- `ValuePredicateSelector` MUST include one `behavior:Validation` child.

## Notes

- This package defines schema surface and structure. Normative runtime semantics remain in `spec/1.0.0/index.md` `§20`.
- This package does not redefine Codex or Behavior semantics.

**End of Semantic Projection View Schema v1.0.0**
