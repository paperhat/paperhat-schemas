Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Recurrence

A temporal recurrence pattern — the frequency, interval, and bounds of a repeating event, obligation, or schedule entry.

## When to Use

Use `Recurrence` to declare a repeating temporal pattern: a biweekly meeting, a monthly review, a yearly renewal. Attach as a child to events, obligations, or review cycles.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| frequency | $EnumeratedToken | yes | The recurrence frequency: daily, weekly, monthly, or yearly. |
| count | $Integer | no | The total number of occurrences. |
| dayOfMonth | $Integer | no | The day of the month for monthly recurrence. |
| dayOfWeek | $EnumeratedToken | no | The day of the week for weekly recurrence. |
| endDate | $Date | no | The date after which no further occurrences are generated. |
| interval | $Integer | no | The number of frequency periods between occurrences. |
| monthOfYear | $EnumeratedToken | no | The month for yearly recurrence. |
| startDate | $Date | no | The date of the first occurrence. |

## Design Notes

- `$MustNotBeEntity` because a recurrence pattern is a value-like declaration attached to an entity.
- `frequency` vocabulary: `$Daily`, `$Weekly`, `$Monthly`, `$Yearly`.
- `interval` defaults conceptually to 1 (every period). `interval=2` with `frequency=$Weekly` means biweekly.
- Bounds are declared with `startDate`/`endDate` or `count`, not both. Consuming schemas enforce this constraint.

---

**End of Recurrence v1.0.0**
