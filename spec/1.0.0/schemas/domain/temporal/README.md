Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Temporal

Temporal annotations for text spans using the canonical Paperhat Temporal type
family together with formatting and internationalisation support.

## When to Use

Use `TemporalAnnotations` to define keyed temporal values that appear as text
spans in prose. Each concept wraps a canonical temporal value type and adds
`text`, `format`, and `language` traits for display.

Temporal semantics are owned by:

- [Paperhat Temporal](/Users/guy/Workspace/@paperhat/specifications/libraries/paperhat-temporal/spec/1.0.0/index.md)

This schema does not define independent temporal meanings and does not restore
the obsolete `Plain*`, `Zoned*`, `TimeZone`, or `Calendar` surface.

## Concepts

### TemporalAnnotations (Container)

Structural container for temporal annotation definitions. Unordered. Multiple
annotations of the same concept kind are allowed and are distinguished by
their `key` values.

### Supported Annotation Concepts

Each concept requires:

- `key` — `$LookupToken`
- `value` — the concept's temporal value type

Each concept also carries (optionally):

- `text` — `$Text`
- `format` — `$EnumeratedToken`
- `language` — `$LanguageTag`

| Concept | Value Type | Description |
|---|---|---|
| `Date` | `$Date` | Calendar date. |
| `HourMinute` | `$HourMinute` | Minute-precision time of day. |
| `Time` | `$Time` | Second-precision time of day. |
| `DateTime` | `$DateTime` | Local civil date and time. |
| `YearMonth` | `$YearMonth` | Year and month. |
| `MonthDay` | `$MonthDay` | Month and day without year. |
| `YearWeek` | `$YearWeek` | ISO week-based year and week. |
| `YearWeekWeekday` | `$YearWeekWeekday` | ISO week-based year, week, and weekday. |
| `DateWithTimezone` | `$DateWithTimezone` | Date qualified by an IANA timezone identifier. |
| `TimeWithTimezone` | `$TimeWithTimezone` | Time qualified by an IANA timezone identifier. |
| `DateTimeWithTimezone` | `$DateTimeWithTimezone` | Date-time qualified by an IANA timezone identifier. |
| `TimeWithOffset` | `$TimeWithOffset` | Time qualified by a numeric UTC offset. |
| `DateTimeWithOffset` | `$DateTimeWithOffset` | Date-time qualified by a numeric UTC offset. |
| `Instant` | `$Instant` | Exact UTC timeline value. |
| `Duration` | `$Duration` | Duration in the Paperhat duration algebra. |

## Constraints

- `TemporalAnnotations` must contain at least one child annotation concept.

## Design Notes

- These concepts exist because a raw temporal trait value has no display or
  localisation context. The wrapper concept adds `text`, `format`, and
  `language`.
- Concept names match the canonical Paperhat Temporal type names.
- `HourMinute` and `Time` are intentionally distinct because temporal
  precision is type-level.
- `DateTimeWithTimezone` and `DateTimeWithOffset` are intentionally distinct.
  Timezone-qualified and offset-qualified civil values are not the same thing.
- This schema intentionally excludes host/runtime temporal keywords such as
  `now` and `today`. Those are not canonical temporal value types.

---

**End of Temporal v1.0.0**
