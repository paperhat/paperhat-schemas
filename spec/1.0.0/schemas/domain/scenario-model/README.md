Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# ScenarioModel

A named set of parameter assumptions for comparative analysis — a scenario in a financial projection, planning exercise, or sensitivity analysis.

## When to Use

Use `ScenarioModel` to declare a named set of assumptions for comparative analysis: a baseline, optimistic, pessimistic, or stress scenario in financial projections or planning exercises.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the scenario. |
| scenarioKind | $EnumeratedToken | no | The type of scenario. |

## Design Notes

- `$MustBeEntity` because scenarios have stable identity and are referenced by projections and comparison views.
- `scenarioKind` vocabulary: `$Baseline`, `$Optimistic`, `$Pessimistic`, `$Stress`, `$Custom`.
- Parameter overrides are wired by higher-level composers, not imported here. ScenarioModel is a leaf that carries identity and classification.

---

**End of ScenarioModel v1.0.0**
