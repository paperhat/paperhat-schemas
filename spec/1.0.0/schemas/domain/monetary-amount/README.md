Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# MonetaryAmount

A monetary value qualified by currency. Follows the same structural pattern as Identifier (qualifier token + payload value).

## When to Use

Use `MonetaryAmount` wherever a financial value must be recorded unambiguously: product prices, salaries, donations, budgets, ticket costs, grant amounts. The currency trait ensures the value is never a bare number.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| amount | $Number | yes | The numeric value. |
| currency | $EnumeratedToken | yes | ISO 4217 currency code, e.g. `$USD`, `$EUR`, `$GBP`, `$JPY`. Consuming schemas constrain the allowed currencies. |

## Design Notes

- Both traits are required. A monetary amount without a currency is ambiguous; a currency without an amount is meaningless.
- The `currency` trait uses `$EnumeratedToken` so consuming schemas constrain accepted currencies via the "leaves are open, composers constrain" pattern.
- No `minAmount`/`maxAmount` traits — use two MonetaryAmount children with a qualifying token if a range is needed.

**End of MonetaryAmount v1.0.0**
