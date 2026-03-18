Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Duration

A temporal duration expressed as an amount and a unit.

## When to Use

Use `Duration` wherever a time span must be recorded: cooking times, movie runtimes, course lengths, event durations, preparation times. The `amount` trait accepts both exact numbers and numeric ranges (e.g. "55 to 60 minutes").

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| amount | $Number or $Range($Number) | yes | The numeric duration value or range. |
| unit | $EnumeratedToken | yes | Temporal unit, e.g. `$seconds`, `$minutes`, `$hours`, `$days`, `$weeks`, `$months`, `$years`. Consuming schemas constrain the allowed units. |

## Design Notes

- Both traits are required. A duration without a unit is ambiguous.
- The `amount` trait accepts `$Range($Number)` to support approximate durations (e.g. "55 to 60 minutes").
- Duration is intentionally separate from a general-purpose Measure leaf. Temporal duration and physical measurement are cognitively distinct; conflating them produces a concept that is too abstract to guide authors.
- Recipe's PreparationTime and CookingTime concepts duplicate this pattern with locally defined `duration` + `unit` traits. Those are refactorable to compose Duration as a child.

**End of Duration v1.0.0**
