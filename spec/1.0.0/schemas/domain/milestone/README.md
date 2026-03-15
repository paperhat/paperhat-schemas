Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Milestone

A named target achievement with a date, completion criteria, and lifecycle status — a planned accomplishment that other work depends on or aims toward.

## When to Use

Use `Milestone` to represent a planned achievement in a project, roadmap, or strategic plan: "Lexis FOSS beta," "First enterprise contract," "All specifications in Lexis." A milestone is broader than a Release (which is software-specific) and distinct from an Event (which is an occurrence, not a target). Milestones carry completion criteria and lifecycle status. Other milestones or tasks depend on them.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The milestone name (e.g., "Lexis FOSS Beta", "First Revenue"). |
| targetDate | $Date | no | The target achievement date. |
| milestoneStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Planned`, `$InProgress`, `$Completed`, `$Deferred`, `$Cancelled`. Open vocabulary. |
| completionCriteria | $Text | no | What must be true for this milestone to be considered complete. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `paperhat:domain:description` | Extended description of the milestone and its significance. |
| temporal:TemporalAnnotations | `paperhat:domain:temporal` | Additional keyed temporal values (start date, original target, revised target). |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| temporal | `paperhat:domain:temporal` |

## Design Notes

- `$MustBeEntity` because milestones have stable identity and are referenced by dependency relationships. "Lexis FOSS beta" is the same milestone regardless of where it appears.
- `completionCriteria` is plain text, not a structured condition. Structured completion conditions (behavioral constraints, automated checks) belong in a higher-level composer, not this leaf schema.
- Dependencies between milestones are expressed through a separate Dependency schema, not as traits on Milestone. This follows the Paperhat pattern of composing relationships externally rather than embedding them in leaf schemas.
- Distinct from Release (versioned software artifact), Event (occurrence at a time and place), and Step (action in a procedure). A Milestone is a planned achievement that other work aims toward.

---

**End of Milestone v1.0.0**
