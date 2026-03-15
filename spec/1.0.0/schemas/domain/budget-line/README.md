Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# BudgetLine

A single line item in a budget — an amount allocated to a category for a specific period with a tracking status.

## When to Use

Use `BudgetLine` as a child of Budget to represent individual budget allocations. Each line item carries an amount, a category, and tracking metadata.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| amount | $Number | yes | The monetary amount allocated to this line item. |
| category | $Text | yes | The budget category for this line item. |
| budgetLineStatus | $EnumeratedToken | no | The tracking status of this line item. |
| currency | $EnumeratedToken | no | The ISO 4217 currency code for this amount. |
| period | $Text | no | The time period this line item covers. |

## Design Notes

- `$MustNotBeEntity` because budget lines are children of a Budget entity, not independently referenceable.
- `currency` uses `$EnumeratedToken` with ISO 4217 codes (`$USD`, `$EUR`, `$NZD`). Consuming schemas constrain accepted currencies.
- `budgetLineStatus` vocabulary: `$Projected`, `$Committed`, `$Spent`, `$Remaining`.

---

**End of BudgetLine v1.0.0**
