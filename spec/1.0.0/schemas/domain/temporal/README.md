Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Temporal

Temporal annotations for text spans: dates, times, datetimes, durations, and instants with formatting and internationalisation support.

## When to Use

Use `TemporalAnnotations` to define temporal values that appear as text spans in prose. Each concept wraps a Codex temporal value type and adds formatting and internationalisation traits. Bound from Gloss spans via `{~key}` or `{~key | label}` references.

## Concepts

### TemporalAnnotations (Container)

Structural container for temporal annotation definitions. Unordered, no duplicates.

### PlainDate

A calendar date without time or timezone.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $Date | Single | yes | The date value (e.g. `2024-03-15`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format (e.g. `$full`, `$long`, `$medium`, `$short`). Foundry default applies if absent. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). Overrides the document language. |

### PlainTime

A time of day without date or timezone.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $Time | Single | yes | The time value (e.g. `14:30:00`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### PlainDateTime

A date and time without timezone.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $DateTime | Single | yes | The datetime value (e.g. `2024-03-15T14:30:00`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### PlainYearMonth

A year and month without a specific day.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $YearMonth | Single | yes | The year-month value (e.g. `2024-03`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### PlainMonthDay

A month and day without a year.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $MonthDay | Single | yes | The month-day value (e.g. `03-15`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### YearWeek

A year and ISO week number.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $YearWeek | Single | yes | The year-week value (e.g. `2024-W12`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### Instant

An absolute point in time with timezone offset (no timezone identifier).

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $Instant | Single | yes | The instant value (e.g. `2024-03-15T14:30:00Z`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### ZonedDateTime

An absolute point in time with both timezone offset and timezone identifier.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $ZonedDateTime | Single | yes | The zoned datetime value (e.g. `2024-03-15T14:30:00-04:00[America/New_York]`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

### Duration

An ISO 8601 duration (period of time, not a point in time).

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| value | $Duration | Single | yes | The duration value (e.g. `P1Y2M3DT4H5M6S`). |
| text | $Text | Single | no | Display text override for Gloss references. |
| format | $EnumeratedToken | Single | no | Display format. |
| language | $EnumeratedToken | Single | no | Locale for formatting (BCP-47). |

## Constraints

- TemporalAnnotations must contain at least one child.

## Design Notes

- Temporal concepts exist because a raw temporal trait value has no formatting or internationalisation context. The wrapping concept adds `format` and `language` traits that the foundry uses to produce locale-appropriate text.
- Format tokens follow CLDR/ICU date format styles. The foundry maps these to the target locale's conventions.
- When referenced from Gloss without a label: if `text` is present, use it; otherwise the foundry formats `value` according to `format` and `language`.
- Concept names match Codex value type names (PlainDate, PlainDateTime, etc.) which follow the Temporal proposal naming conventions.
- The `value` trait definition uses `defaultValueTypes` (plural) to accept all nine temporal value types. Each concept's name establishes which type is semantically correct; Codex's temporal kind determination parses the value into the appropriate type automatically.
- Duration is included because durations appear in prose (e.g. "the event lasts {~length}") and benefit from the same formatting and internationalisation traits as point-in-time values.

---

**End of Temporal v1.0.0**
