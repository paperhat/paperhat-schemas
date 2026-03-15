Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# View Definition

A ViewDefinition declares which fields and content from a source concept a view presents, and in what authored order. It is the data selection and arrangement layer — it says *what to show*, not *how it looks*. The design system (CDL/SDL/PDL) governs perceptual relationships. The foundry decides concrete presentation.

A composition Binding references a ViewDefinition by IRI. The ViewDefinition declares the target concept type and lists the fields to include. The pipeline evaluates the Binding by extracting the declared fields from the source entity and passing them to the foundry in the adaptive plan.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| ViewDefinition | Semantic (Entity) | ForbidsContent | `text:Title` (1), `desc:Description` (0..1), `ViewField` (1..n), `ViewGroup` (0..n) | Root view definition entity. Declares what the view presents. Trait: `targetConcept`. |
| ViewField | Structural (non-entity) | ForbidsContent | -- | Declares one field to include from the source entity. Traits: `fieldPath`, `required`. |
| ViewGroup | Structural (non-entity) | ForbidsContent | `ViewField` (1..n) | Groups related fields. The group is a structural hint for the design system and foundry. Trait: `groupIdentifier`. |

## Traits

| Trait | Type | Meaning |
|---|---|---|
| targetConcept | $Iri | IRI of the concept type this view renders. |
| fieldPath | $Text | Trait name or child concept path to extract from the source entity. Dot-separated for nested paths (e.g., "Ingredients.Ingredient"). |
| required | $Boolean | Whether the field must have a value in the source entity. Default: false. |
| groupIdentifier | $Text | Machine-readable identifier for the group. Used by the design system and localization. |

## How It Works

The author creates a ViewDefinition targeting a concept type (e.g., Recipe). Inside it, the author lists ViewField elements in the order they are presented. Each ViewField names a trait or child concept from the source entity using `fieldPath`. ViewGroup wraps related ViewFields — for example, grouping prepTime and cookTime under a "timing" group.

The ViewDefinition does not specify sizes, colors, spacing, typography, or layout. It declares what data is included and in what structural order. The design system attaches semantic roles (heading, body, label, data_value) and constraint relationships (proximity, contrast, alignment) to the fields declared by the view. The foundry renders the result.

ViewFields and ViewGroups are ordered: their authored sequence in the ViewDefinition is the canonical presentation order. The design system and foundry honor this order unless adaptation rules (PDL) explicitly adjust it.

## Design Notes

- ViewDefinitions are authored content, not universal schemas. Each composition references specific ViewDefinitions. Different compositions use different views for the same concept type.
- Labels for fields come from the localization system, not from the ViewDefinition. The ViewDefinition declares what to show; localization declares what to call it.
- ViewGroup is a structural grouping hint — it tells the design system and foundry that these fields are semantically related. It does not prescribe visual grouping.

---

**End of View Definition v1.0.0**
