Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Obligation

A binding commitment by a party to perform or refrain from an action — a contractual, regulatory, or policy obligation with a responsible party and compliance state.

## When to Use

Use `Obligation` to represent a binding commitment: a contractual duty, a regulatory requirement, a policy mandate. Obligations are entities with stable identity, referenced by compliance status records and audit trails.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the obligation. |
| dueDate | $Date | no | The date by which the obligation must be fulfilled. |
| obligatedParty | $Iri | no | The entity responsible for fulfilling the obligation. |
| obligationKind | $EnumeratedToken | no | The type of obligation. |
| obligationStatus | $EnumeratedToken | no | The current fulfillment status of the obligation. |

## Design Notes

- `$MustBeEntity` because obligations have stable identity and are cross-referenced by compliance records, audit trails, and review cycles.
- `obligatedParty` is a reference trait pointing to a Person or Organization entity.
- `obligationKind` vocabulary: `$Contractual`, `$Regulatory`, `$Policy`, `$Operational`.
- `obligationStatus` vocabulary: `$Active`, `$Fulfilled`, `$Breached`, `$Waived`, `$Expired`.

---

**End of Obligation v1.0.0**
