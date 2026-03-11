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
| desc:Description | `paperhat:domain:description` | Free-text product description. |
| offer:Offer | `paperhat:domain:offer` | Pricing, availability, and condition. |
| ident:Identifier | `paperhat:domain:identifier` | GTIN, SKU, MPN, ASIN, ISBN. |
| rating:Rating | `paperhat:domain:rating` | Aggregate product reviews. |
| measure:Measure | `paperhat:domain:measure` | Physical dimensions: weight, height, width, depth, volume. |
| money:MonetaryAmount | `paperhat:domain:monetary-amount` | Price when not expressed via Offer. |
| tags:Tags | `paperhat:domain:tags` | Freeform categorization. |
| work:Work | `paperhat:domain:work` | Authorship, licensing, provenance. |
| audience:Audience | `paperhat:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `paperhat:domain:accessibility` | Accessibility information. |
| nutrition:NutritionInformation | `paperhat:domain:nutrition-information` | Nutritional data for food products. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| offer | `paperhat:domain:offer` |
| ident | `paperhat:domain:identifier` |
| rating | `paperhat:domain:rating` |
| measure | `paperhat:domain:measure` |
| money | `paperhat:domain:monetary-amount` |
| tags | `paperhat:domain:tags` |
| work | `paperhat:domain:work` |
| audience | `paperhat:domain:audience` |
| a11y | `paperhat:domain:accessibility` |
| nutrition | `paperhat:domain:nutrition-information` |

## Design Notes

- Product is the canonical consumer of the Offer and Measure leaves. A single Product can compose multiple Offers (different sellers, conditions, or date ranges) and multiple Measures (weight, height, width, etc.).
- The `brand` trait is a simple string rather than a reference to Organization. Once the cross-entity Reference pattern is established, brand can optionally reference an Organization entity.
- Media attachment uses the `media-reference` schema package.

---

**End of Product v1.0.0**
