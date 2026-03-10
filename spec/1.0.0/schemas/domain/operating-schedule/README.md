Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# OperatingSchedule

Operating hours for a specific day of the week, with optional seasonal validity.

## When to Use

Use `OperatingSchedule` wherever an entity has recurring hours of operation: business hours for an organization, venue opening times for an event, service availability windows. Use multiple OperatingSchedule children to describe a full weekly schedule.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| dayOfWeek | $EnumeratedToken | no | Day of the week, e.g. `$Monday`, `$Tuesday`, `$Saturday`. |
| opens | $Text | no | Opening time, e.g. "09:00". |
| closes | $Text | no | Closing time, e.g. "17:00". |
| validFrom | $Date | no | Start of seasonal validity. |
| validThrough | $Date | no | End of seasonal validity. |
| scheduleNote | $Text | no | Freeform note, e.g. "Closed on public holidays". |

## Design Notes

- All traits are optional because different contexts need different subsets. The "at least one" constraint prevents empty OperatingSchedule elements.
- `opens` and `closes` are $Text rather than a time-specific type to accommodate varied formats ("09:00", "9am", "sunrise").
- Use multiple OperatingSchedule children on a single entity to describe different days or seasonal variations.
- Validity dates allow seasonal schedules (e.g. extended summer hours) without duplicating the concept.
- Mirrors schema.org's OpeningHoursSpecification: dayOfWeek, opens, closes, validFrom, validThrough.

---

**End of OperatingSchedule v1.0.0**
