Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Budget

A named financial plan with categorized line items over a defined period — a project budget, departmental budget, or grant budget.

## When to Use

Use `Budget` to represent a named financial plan: a project budget, departmental budget, or grant budget. BudgetLine children are wired by a composing schema, not imported here.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the budget. |
| budgetStatus | $EnumeratedToken | no | The lifecycle status of the budget. |
| currency | $EnumeratedToken | no | The ISO 4217 currency code for budget amounts. |
| endDate | $Date | no | The end date of the budget period. |
| startDate | $Date | no | The start date of the budget period. |
| totalAmount | $Number | no | The total budget amount. |

## Design Notes

- `$MustBeEntity` because budgets have stable identity and are referenced by financial projections and audit trails.
- BudgetLine children are not imported — they are wired by a higher-level composer. Budget is a leaf.
- `budgetStatus` vocabulary: `$Draft`, `$Approved`, `$Active`, `$Closed`.
- `currency` uses ISO 4217 codes (`$USD`, `$EUR`, `$NZD`).

---

**End of Budget v1.0.0**
