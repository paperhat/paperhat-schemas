Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Tier

A named packaging level within a product or service — a tier, plan, or edition that bundles specific features and pricing.

## When to Use

Use `Tier` to model named product tiers such as "Lexis FOSS", "Lexis Pro", or "Nexus Premium". Tiers have stable identity and are referenced from offers, contracts, and support entitlements. Features within a tier are expressed as content (Description, List children) on the composing schema, not as separate entities.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the tier (e.g., "Pro", "Premium", "Enterprise"). |
| tierKind | $EnumeratedToken | no | Classification token, e.g., `$Free`, `$Standard`, `$Professional`, `$Enterprise`, `$Custom`. Open vocabulary. |
| product | $Iri | no | Reference to the product this tier belongs to. |
| tierStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Active`, `$Deprecated`, `$Planned`. Open vocabulary. |

## Constraints

`name` is required. A tier without a name is ambiguous.

## Design Notes

- `$MustBeEntity` because tiers have stable identity and are cross-referenced from offers, contracts, and documentation.
- `product` is a reference trait (`isReferenceTrait=true`) pointing to a Product entity.
- Features, capabilities, and eligibility are expressed as structured content (Description, List) on composing schemas, not as standalone entities.
- Pricing is handled by composing Offer as a child on the consuming schema, not by traits on Tier itself.
- Pure leaf with no imports, keeping the dependency graph minimal.

---

**End of Tier v1.0.0**
