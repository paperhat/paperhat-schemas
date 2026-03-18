Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Offer

A commercial offer describing the price and terms under which a product or service is available.

## When to Use

Use `Offer` wherever something is being sold, rented, or made available at a price: product listings, service quotes, event tickets, subscription plans, auction bids.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| price | $Number | yes | The numeric price. |
| priceCurrency | $EnumeratedToken | yes | ISO 4217 currency code, e.g. `$USD`, `$EUR`, `$GBP`. Consuming schemas constrain the allowed currencies. |
| availability | $EnumeratedToken | no | Stock or availability status, e.g. `$InStock`, `$OutOfStock`, `$PreOrder`, `$Discontinued`. |
| itemCondition | $EnumeratedToken | no | Condition of the offered item, e.g. `$New`, `$Used`, `$Refurbished`. |
| validFrom | $Date | no | Date from which the offer is valid. |
| validThrough | $Date | no | Date through which the offer is valid. |

## Design Notes

- Both `price` and `priceCurrency` are required. An offer without a price is incomplete; a price without a currency is ambiguous.
- Offer does not compose MonetaryAmount — the price/currency pair is integral to what an offer is, not a separate child concept. Consuming schemas that need both an Offer and a standalone MonetaryAmount use them side by side.
- The `availability` and `itemCondition` traits use `$EnumeratedToken` so consuming schemas define their own vocabularies.
- Validity dates are plain dates, not timestamps — sufficient for most commercial contexts.

---

**End of Offer v1.0.0**
