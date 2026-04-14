Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Learning Offering

A training course, workshop, or educational program offered as a catalog entity — the abstract offering, not a specific scheduled instance.

## When to Use

Use `LearningOffering` to model training offerings that appear in catalogs, proposals, and documentation. "Codex Authoring Workshop" is a LearningOffering; a specific workshop on March 15 is an Event. Offerings have stable identity and are referenced from contracts, schedules, and product documentation.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the offering (e.g., "Codex Authoring Workshop"). |
| offeringKind | $EnumeratedToken | no | Classification token, e.g., `$Course`, `$Workshop`, `$Seminar`, `$Tutorial`, `$Certification`, `$Bootcamp`. Open vocabulary. |
| offeringStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Active`, `$Planned`, `$Retired`, `$Archived`. Open vocabulary. |
| deliveryMode | $EnumeratedToken | no | How the offering is delivered, e.g., `$InPerson`, `$Online`, `$Hybrid`, `$SelfPaced`. Open vocabulary. |
| product | $Iri | no | Reference to the product this offering supports. |

## Constraints

`name` is required. An offering without a name is ambiguous.

## Design Notes

- `$MustBeEntity` because offerings have stable identity and are cross-referenced from contracts, events, and documentation.
- `product` is a reference trait (`isReferenceTrait=true`) pointing to a Product entity. Same pattern as Tier.product and Release.product.
- This is the descriptive shell for Praxis. Praxis owns the deeper learning engine (modules, objectives, assessments, competency maps). Lexis owns the catalog entity.
- Children (Description, Duration, Audience, Offer, Tags, SeriesInformation) are wired by composing schemas, not imported here.
- Pure leaf with no imports, keeping the dependency graph minimal.

---

**End of Learning Offering v1.0.0**
