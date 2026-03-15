Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# RecurrenceException

An override or cancellation of a single instance in a recurrence pattern — a date that is skipped, moved, or replaced.

## When to Use

Use `RecurrenceException` as a child of a Recurrence to override or cancel a single occurrence. If `replacementDate` is absent, the instance is cancelled. If present, the instance is moved.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| originalDate | $Date | yes | The date of the recurrence instance being overridden or cancelled. |
| reason | $Text | no | The reason for the exception. |
| replacementDate | $Date | no | The replacement date, if the instance is moved rather than cancelled. |

## Design Notes

- `$MustNotBeEntity` because exceptions are children of a Recurrence, not independently referenceable.
- Absent `replacementDate` means the instance is cancelled. Present `replacementDate` means the instance is moved to the new date.
- `reason` is plain text providing human-readable justification.

---

**End of RecurrenceException v1.0.0**
