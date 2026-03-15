Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# ComplianceStatus

The compliance state of an obligation, requirement, or control — whether the responsible party has satisfied, failed, or not yet addressed the item.

## When to Use

Use `ComplianceStatus` to record the compliance state of an obligation, requirement, or control. Attach as a child to Obligation, Requirement, or any entity that carries compliance obligations.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| status | $EnumeratedToken | yes | The compliance state: compliant, non-compliant, pending, waived, expired, or not applicable. |
| assessmentDate | $Date | no | The date the compliance assessment was performed. |
| assessor | $Text | no | The person or entity that performed the assessment. |
| evidence | $Text | no | A reference to or description of the evidence supporting the assessment. |

## Design Notes

- `$MustNotBeEntity` because compliance status is a point-in-time assessment attached to another entity, not independently referenceable.
- `status` uses `$EnumeratedToken` for controlled vocabulary: `$Compliant`, `$NonCompliant`, `$Pending`, `$Waived`, `$Expired`, `$NotApplicable`.
- `evidence` is plain text. Structured evidence references belong in a higher-level composer.

---

**End of ComplianceStatus v1.0.0**
