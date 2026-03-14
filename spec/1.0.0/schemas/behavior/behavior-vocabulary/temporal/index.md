Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Temporal

This specification defines how Behavior programs expose the canonical
Paperhat Temporal algebra.

This document is **Normative**.

---

## 1. Purpose

Behavior programs may use temporal construction, validation, decomposition,
comparison, conversion, arithmetic, parsing, formatting, and timezone
resolution operations.

This document does **not** define an independent temporal type system or an
independent temporal operator family. Those semantics belong to
`paperhat-temporal`.

---

## 2. Authority

Temporal semantics used by Behavior are owned by:

- [Paperhat Temporal](/Users/guy/Workspace/@paperhat/specifications/paperhat-temporal/spec/1.0.0/index.md)

Behavior bindings MUST preserve the exact temporal type distinctions, operation
semantics, diagnostic behavior, and determinism guarantees defined there.

### 2.1 No Independent Temporal Semantics

- Behavior MUST NOT define a temporal ontology that conflicts with
  `paperhat-temporal`.
- Behavior MUST NOT redefine temporal precision, timezone semantics, offset
  semantics, overlap/gap handling, arithmetic rules, difference rules, parsing
  rules, or RDF meaning.
- If a Behavior document conflicts with `paperhat-temporal`, the
  `paperhat-temporal` rule wins.

### 2.2 Canonical Temporal Type Names

Behavior temporal bindings MUST use the canonical Paperhat Temporal type names:

- `YearMonth`
- `MonthDay`
- `YearWeek`
- `YearWeekWeekday`
- `Date`
- `HourMinute`
- `Time`
- `DateTime`
- `DateWithTimezone`
- `TimeWithTimezone`
- `DateTimeWithTimezone`
- `TimeWithOffset`
- `DateTimeWithOffset`
- `Instant`
- `Duration`
- `Timezone`
- `Offset`

The following names MUST NOT be used as canonical Behavior temporal type names:

- `PlainDate`
- `PlainTime`
- `PlainDateTime`
- `PlainYearMonth`
- `PlainMonthDay`
- `ZonedDate`
- `ZonedTime`
- `ZonedDateTime`
- `TimeZone`
- `Calendar`

---

## 3. Operation Binding Rule

If a Behavior environment exposes temporal operators, it MUST expose the
operators defined by `paperhat-temporal` using the same semantic distinctions
and the same operation names.

This includes the Paperhat Temporal families for:

- checked construction
- validation
- structural decomposition
- canonical parsing
- canonical formatting
- exact conversion
- calendar-structural operations
- arithmetic
- directed difference
- comparison
- timezone resolution
- resolved-timeline comparison and difference

### 3.1 Partial Temporal Operations

Behavior bindings for partial temporal operations MUST preserve the exact
diagnostic cases defined by `paperhat-temporal`.

In particular:

- `DateTimeWithTimezone` resolution MUST preserve the `unique-only`,
  `Earlier`, and `Later` distinction.
- overlap and gap handling MUST follow the exact Paperhat Temporal rules.
- no binding may silently apply `compatible`, gap snapping, host-library
  defaults, or any other hidden policy.

### 3.2 Runtime and Ambient Time

Ambient time is not part of the pure temporal algebra.

- `Now*`, `today`, and similar clock-dependent facilities MUST NOT be treated
  as pure temporal library operations.
- If Behavior later exposes runtime clock operators, they MUST live in an
  explicit runtime/system/effect layer, not in the pure temporal binding.

---

## 4. Removed Legacy Surface

The previously documented `Plain*` / `Zoned*` / `TimeZone` / `Calendar`
operator surface is obsolete and MUST NOT be treated as normative Behavior
temporal authority.

The following legacy behaviors are invalid and MUST NOT be reintroduced:

- conflating `Timezone` and `Offset`
- treating minute-precision time as a shorthand spelling of `Time`
- using `compatible` timezone disambiguation
- allowing negative durations
- exposing millisecond-specific core temporal arithmetic or difference as part
  of the canonical temporal algebra
- defining a second temporal theory inside Behavior

---

## 5. Derived Behavior Functions

Derived temporal convenience functions MAY be specified separately, but only if
all of the following are true:

- they are defined strictly in terms of `paperhat-temporal`
- they do not introduce new temporal value types
- they do not redefine any existing temporal operation
- they make every additional policy choice explicit

This document defines no such derived convenience layer.

---

## 6. Conformance

Conformance for core temporal behavior is inherited from
`paperhat-temporal`.

This document adds:

- no independent temporal semantics
- no independent temporal diagnostics
- no independent temporal disambiguation policies
- no independent temporal conformance vectors

---

**End of Behavior Vocabulary — Temporal v1.0.0**
