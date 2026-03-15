Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# RoundingPolicy

An explicit declaration of rounding behavior — the method, scale, and scope of numeric rounding applied to a value or computation.

## When to Use

Use `RoundingPolicy` wherever numeric rounding occurs and the method must be declared explicitly: financial calculations, statistical reporting, or any domain where silent rounding is unacceptable.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| method | $EnumeratedToken | yes | The rounding method, such as half-even, half-up, floor, or ceiling. |
| scale | $Integer | yes | The number of decimal places to round to. |
| scope | $EnumeratedToken | no | Whether rounding is applied to stored values or display only. |

## Design Notes

- `$MustNotBeEntity` because a rounding policy is a value-like configuration, not a referenceable entity.
- `method` uses `$EnumeratedToken` for controlled vocabulary: `$HalfUp`, `$HalfDown`, `$HalfEven`, `$Ceiling`, `$Floor`, `$Truncate`.
- `scope` distinguishes display-only rounding (`$DisplayOnly`) from rounding applied to stored values (`$Stored`). This distinction matters in financial and regulatory contexts.

---

**End of RoundingPolicy v1.0.0**
