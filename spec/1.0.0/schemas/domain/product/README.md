Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Product

A product or service offered for sale, rental, or subscription — physical goods, digital downloads, or service plans.

## When to Use

Use `Product` to represent any item offered commercially: consumer electronics, clothing, handmade goods, software licenses, or professional services. Products are entities (`$MustBeEntity`) and can be referenced from other schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The product name. |
| brand | $Text | no | Brand or manufacturer name. |
| category | $EnumeratedToken | no | Product category, e.g. `$electronics`, `$clothing`, `$software`. |
| color | $Text | no | Primary color or color description. |
| material | $Text | no | Primary material composition. |
| model | $Text | no | Model name or number. |
| releaseDate | $Date | no | When the product was released or first available. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `codex:domain:description` | Free-text product description. |
| offer:Offer | `codex:domain:offer` | Pricing, availability, and condition. |
| ident:Identifier | `codex:domain:identifier` | GTIN, SKU, MPN, ASIN, ISBN. |
| rating:Rating | `codex:domain:rating` | Aggregate product reviews. |
| measure:Measure | `codex:domain:measure` | Physical dimensions: weight, height, width, depth, volume. |
| money:MonetaryAmount | `codex:domain:monetary-amount` | Price when not expressed via Offer. |
| tags:Tags | `codex:domain:tags` | Freeform categorization. |
| work:Work | `codex:domain:work` | Authorship, licensing, provenance. |
| audience:Audience | `codex:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `codex:domain:accessibility` | Accessibility information. |
| nutrition:NutritionInformation | `codex:domain:nutrition-information` | Nutritional data for food products. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| offer | `codex:domain:offer` |
| ident | `codex:domain:identifier` |
| rating | `codex:domain:rating` |
| measure | `codex:domain:measure` |
| money | `codex:domain:monetary-amount` |
| tags | `codex:domain:tags` |
| work | `codex:domain:work` |
| audience | `codex:domain:audience` |
| a11y | `codex:domain:accessibility` |
| nutrition | `codex:domain:nutrition-information` |

## Design Notes

- Product is the canonical consumer of the Offer and Measure leaves. A single Product can compose multiple Offers (different sellers, conditions, or date ranges) and multiple Measures (weight, height, width, etc.).
- The `brand` trait is a simple string rather than a reference to Organization. Once the cross-entity Reference pattern is established, brand can optionally reference an Organization entity.
- Media attachment uses the `media-reference` schema package.

---

**End of Product v1.0.0**
