Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Brand

A named brand identity owned by an organization, such as a product brand, institutional brand, or sub-brand.

## When to Use

Use `Brand` to represent a brand as a first-class entity with stable identity. Examples include "Paperhat" (institutional brand), "Lexis" (product brand), or "Codex" (technology brand). Brand is an entity (`$MustBeEntity`) and can be referenced from Product, Organization, and other schemas by IRI. It is distinct from Organization (the legal/institutional entity that owns the brand) and Product (a specific offering sold under the brand).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The brand name (e.g., "Paperhat", "Lexis", "Codex"). |
| brandKind | $EnumeratedToken | no | Classification token, e.g., `$Institutional`, `$Product`, `$SubBrand`, `$Technology`. Open vocabulary. |
| owner | $Iri | no | Reference to the Organization entity that owns the brand. Marked as a reference trait (`isReferenceTrait=true`). |
| brandStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Active`, `$Retired`, `$Pending`. Open vocabulary. |

## Constraints

`name` is required. A brand without a name is empty.

## Design Notes

- Brand is an entity (`$MustBeEntity`) because brands need stable identity for cross-references. Products, marketing materials, legal documents, and organizational records all reference brands.
- This is a pure leaf with no imports and no children. Higher-level composers will compose Brand with Description, MediaAsset (for logos), Tags, and other leaf schemas as needed.
- Product currently has a `brand` trait as `$Text`. When Brand is composed into a higher-level schema alongside Product, the Product's `brand` trait can hold a brand name while the Brand entity holds the canonical record. Alternatively, importing schemas can add a reference trait pointing to a Brand entity.
- Visual identity (logo, colors, fonts) is a projection concern. Brand captures the semantic identity; presentation details belong in projection schemas or theme configuration.

---

**End of Brand v1.0.0**
