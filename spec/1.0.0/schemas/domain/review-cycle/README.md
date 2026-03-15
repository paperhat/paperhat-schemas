Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# ReviewCycle

A scheduled recurring review of a document, policy, contract, or process — a periodic obligation to assess and confirm or update.

## When to Use

Use `ReviewCycle` to declare a periodic review obligation: annual specification reviews, quarterly policy reviews, monthly contract check-ins. Duration children set the review period. Description children explain the review scope.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the review cycle. |
| nextReviewDate | $Date | no | The date of the next scheduled review. |
| responsible | $Iri | no | The person or role responsible for conducting the review. |
| reviewCycleStatus | $EnumeratedToken | no | The lifecycle status of the review cycle. |
| scope | $Text | no | The scope of what is reviewed. |

## Design Notes

- `$MustBeEntity` because review cycles have stable identity and are referenced by compliance records and schedule projections.
- `responsible` is a reference trait pointing to a Person, Organization, or Role entity.
- Duration children represent the review period (e.g., 12 months). Description children explain the scope.
- `reviewCycleStatus` vocabulary: `$Active`, `$Suspended`, `$Completed`.

---

**End of ReviewCycle v1.0.0**
