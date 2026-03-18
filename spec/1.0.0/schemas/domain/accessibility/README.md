Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Accessibility

Accessibility characteristics of a resource or venue, including access modes, features, and hazards.

## When to Use

Use `Accessibility` wherever an entity needs to describe how accessible it is: products with assistive features, events with venue accommodations, organizations with accessibility commitments, creative works with alternative formats.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| accessMode | $EnumeratedToken | no | Sensory mode required, e.g. `$auditory`, `$textual`, `$visual`, `$tactile`. |
| accessibilityFeature | $Text | no | Accessibility feature provided, e.g. "captions", "largePrint", "wheelchairAccessible". |
| accessibilityHazard | $Text | no | Known hazard, e.g. "flashing", "motionSimulation", "sound". |
| accessibilitySummary | $Text | no | Human-readable summary of accessibility characteristics. |
| accessibilityControl | $Text | no | Input method supported, e.g. "fullKeyboardControl", "fullMouseControl". |

## Design Notes

- All traits are optional because different contexts need different subsets. The "at least one" constraint prevents empty Accessibility elements.
- `accessMode` uses $EnumeratedToken because the set of sensory modes is small and well-defined (auditory, textual, visual, tactile).
- Feature, hazard, and control traits are $Text because the W3C accessibility vocabulary is large and continuously updated; consuming schemas impose constraints as needed.
- Use multiple Accessibility children on a single entity to describe multiple access modes or features independently.
- Mirrors schema.org CreativeWork's accessibility properties: accessMode, accessibilityFeature, accessibilityHazard, accessibilitySummary, accessibilityControl.

**End of Accessibility v1.0.0**
