Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Measure

A general-purpose quantitative measurement. Use this for any physical or abstract quantity that needs a numeric value paired with a unit.

## When to Use

Use `Measure` for non-temporal, non-monetary quantities: weights, distances, temperatures, volumes, screen sizes, speeds, dosages. For time-based quantities, prefer `Duration`. For money, prefer `MonetaryAmount`.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| value | $Number, $Range($Number) | yes | The numeric measurement. Accepts a range for approximate values (e.g. "3–5"). |
| unit | $EnumeratedToken | yes | The unit of measurement, e.g. `$kg`, `$cm`, `$inches`, `$celsius`. Consuming schemas constrain the allowed units. |

## Design Notes

- Both traits are required. A measurement without a unit is ambiguous; a unit without a value is meaningless.
- The `value` trait accepts `$Range($Number)` (same as Duration) for approximate measurements like "3–5 cm".
- The `unit` trait uses `$EnumeratedToken` so consuming schemas constrain accepted units via the "leaves are open, composers constrain" pattern.
- Distinct from Duration (temporal) and MonetaryAmount (financial) — those are domain-specific specializations of the same value+unit pattern.

**End of Measure v1.0.0**
