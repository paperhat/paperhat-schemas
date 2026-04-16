Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Form Definition

A FormDefinition declares which fields from a source concept a form collects, in what order, and with what grouping. It is the data-collection counterpart to the ViewDefinition. It declares *what to collect*, not *how it looks*. The design system (CDL/SDL/PDL) governs perceptual relationships. The foundry decides concrete presentation. Validation rules come from behavior shapes attached to the target concept; the form definition references but does not duplicate them.

A composition Binding references a FormDefinition by IRI. The FormDefinition declares the target concept type and either lists the fields to collect (whitelist mode) or includes all fields with specific exclusions (includeAll mode). The pipeline evaluates the Binding by extracting the declared fields, their value types, and their behavior-shape constraints from the source schema and passing them to the foundry in the adaptive plan.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| FormDefinition | Semantic (Entity) | ForbidsContent | `text:Title` (1), `desc:Description` (0..1), `FormField` (0..n), `FormExclude` (0..n), `FormGroup` (0..n) | Root form definition entity. Declares what the form collects. |
| FormField | Structural (non-entity) | ForbidsContent | `FormField` (0..n) | Declares one field to collect. Nested FormField elements represent child-concept expansion with relative field paths. |
| FormExclude | Structural (non-entity) | ForbidsContent | -- | Excludes one field when `includeAllFields` is true. |
| FormGroup | Structural (non-entity) | ForbidsContent | `FormField` (1..n) | Groups related fields. The group is a structural hint for the design system and foundry. |

## Traits

| Trait | Type | Meaning |
|---|---|---|
| targetConcept | $Iri | IRI of the concept type this form collects data for. |
| includeAllFields | $Boolean | When true, all fields from the target concept are included by default. FormExclude elements remove specific fields. FormField elements provide configuration overrides. When absent or false, only explicitly listed FormField elements appear. |
| entityShape | $Iri | IRI of an EntityShapeDefinition for cross-field validation. The foundry reads entity-level Constraints and Derivations from this shape. |
| fieldPath | $Text | Trait name or child concept name to collect from the source entity. Nested FormField elements use paths relative to their parent FormField. Flat FormField elements use dot-separated paths for nested access (e.g., "PersonName.given"). |
| overrideRequired | $Boolean | When true, this field is required in this form regardless of the schema default. When absent, the schema's required status applies. A schema-required field is always required; this trait adds the requirement, never removes it. |
| readOnly | $Boolean | When true, this field is display-only in this form. Derived fields (those with Derivations in the referenced EntityShapeDefinition) are automatically read-only. This trait forces non-derived fields to be display-only. |
| helpText | $Text | Form-specific input hint for this field. The foundry emits this as accessible help content (aria-describedby). Different from the label (which comes from the localization system). |
| groupIdentifier | $Text | Machine-readable identifier for the group. The localization system provides the display label. |

## How It Works

### Whitelist Mode (Default)

The author creates a FormDefinition targeting a concept type (e.g., Person). Inside it, the author lists FormField elements naming the fields to collect, in the order they are presented. Fields not listed do not appear. This is explicit by construction.

### IncludeAll Mode

The author sets `includeAllFields=true` on the FormDefinition. All fields from the target concept are included in schema declaration order. FormExclude elements remove specific fields. FormField elements provide configuration overrides (overrideRequired, readOnly, helpText) and reposition the field to their authored location. Fields not referenced by a FormField or FormExclude follow schema declaration order and appear after positioned fields.

### Nested Fields

When a FormField names a child concept (e.g., `fieldPath="PersonName"`), it represents an expansion point. Child FormField elements inside it use relative paths (e.g., `fieldPath="given"` means PersonName.given). The foundry generates a nested fieldset. Without child FormField elements, the foundry expands all fields of the child concept in schema declaration order.

### Validation

Per-field validation comes from behavior shapes (ValueShapeDefinition) attached to the field's value type in the source schema. The form definition does not duplicate these constraints. The foundry reads the constraints from the store and generates HTML5 validation attributes (Layer 0) and JavaScript validation (Layer 2).

Cross-field validation comes from the EntityShapeDefinition referenced by the `entityShape` trait. The foundry reads entity-level Constraints and generates JavaScript validation at Layer 2. Cross-field validation is not expressible in HTML5 native form validation.

### Derived Fields

Fields with Derivations in the referenced EntityShapeDefinition are automatically read-only. The foundry generates an `<output>` element for derived fields. At Layer 2, JavaScript evaluates the Derivation expression tree and updates the output live. At Layer 0, the output element is empty (the derivation is computed server-side on submission).

### Labels and Help Text

Labels come from the localization system, not from the FormDefinition. The FormDefinition declares what to collect; localization declares what to call it. The `helpText` trait provides form-specific contextual guidance that supplements the label.

## Constraints

- When `includeAllFields` is absent or false, at least one FormField or FormGroup with FormField children is required.
- FormExclude is valid only when `includeAllFields` is true.
- FormField and FormExclude within the same FormDefinition do not reference the same fieldPath.

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| desc | `paperhat:domain:description` | Provides descriptive text for the form definition. |
| text | `paperhat:domain:text` | Provides the Title concept for the form heading. |

## Design Notes

- FormDefinition is a sibling of ViewDefinition, not a subtype. The two schemas share the same structural patterns (targetConcept, fieldPath, grouping) but serve fundamentally different purposes: ViewDefinition renders existing data, FormDefinition collects new data.
- FormDefinition does not specify form actions (submit endpoint, HTTP method). Form actions are a deployment concern specified in the composition document.
- FormDefinition does not specify input types (text field, dropdown, checkbox). The foundry determines the HTML input type from the Codex value type of each field.
- FormDefinition does not carry validation rules. Validation comes from behavior shapes attached to the target concept's fields. The form references these shapes indirectly through the targetConcept and entityShape traits.
- The `overrideRequired` trait is one-way: it adds a requirement, never removes one. A schema-required field is always required in every form. This prevents a form from silently accepting incomplete data.
- The `readOnly` trait on derived fields is automatic. The form author uses it to force non-derived fields to be display-only (e.g., showing a user's email in a profile form where email changes go through a separate verification flow).

---

**End of Form Definition v1.0.0**
