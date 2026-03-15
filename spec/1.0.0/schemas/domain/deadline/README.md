Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Deadline

A named temporal obligation — a date by which something must be accomplished, with a grace period and escalation policy.

## When to Use

Use `Deadline` to represent a date by which something must be accomplished: a grant application deadline, a filing date, a contractual notice period. Distinct from Milestone (a target achievement) — a Deadline is a temporal obligation with consequences for missing it.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the deadline. |
| targetDate | $Date | yes | The date by which the obligation must be fulfilled. |
| deadlineStatus | $EnumeratedToken | no | The lifecycle status of the deadline. |

## Design Notes

- `$MustNotBeEntity` because deadlines are typically attached to other entities (contracts, obligations, projects).
- `deadlineStatus` vocabulary: `$Upcoming`, `$Due`, `$Overdue`, `$Met`, `$Missed`, `$Waived`.
- Duration children represent grace periods. Description children explain the deadline context.

---

**End of Deadline v1.0.0**
