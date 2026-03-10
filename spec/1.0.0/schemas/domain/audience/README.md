Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Audience

A target audience described by demographic criteria such as age range, geographic area, and audience type.

## When to Use

Use `Audience` wherever an entity has an intended audience: products with target demographics, events aimed at specific groups, recipes for particular skill levels, organizations serving defined communities.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| audienceKind | $EnumeratedToken | no | Audience category, e.g. `$consumer`, `$professional`, `$educational`, `$medical`. |
| suggestedMinAge | $Number | no | Minimum recommended age in years. |
| suggestedMaxAge | $Number | no | Maximum recommended age in years. |
| suggestedGender | $Text | no | Target gender if applicable. |
| geographicArea | $Text | no | Target geographic area, e.g. "North America", "Global". |
| audienceDescription | $Text | no | Freeform description of the intended audience. |

## Design Notes

- All traits are optional because different contexts need different subsets. The "at least one" constraint prevents empty Audience elements.
- `suggestedGender` is $Text rather than $EnumeratedToken to accommodate the full range of gender expressions without prescribing a fixed vocabulary.
- Age traits are $Number (in years) rather than $Text to enable range comparisons by tooling.
- `audienceKind` uses $EnumeratedToken so consuming schemas can constrain the allowed values via vocabularies.
- Mirrors schema.org's Audience and PeopleAudience: audienceType, suggestedMinAge, suggestedMaxAge, suggestedGender, geographicArea.

**End of Audience v1.0.0**
