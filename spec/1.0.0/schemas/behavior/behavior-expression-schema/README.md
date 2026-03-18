Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Behavior Expression Schema

The expression language for authoring computable behaviors in Codex surface form. Defines the full vocabulary of expression nodes that Calculation, Validation, and Derivation blocks contain.

## When to Use

Use Behavior Expression Schema concepts inside `<Calculation>`, `<Validation>`, and `<Derivation>` blocks to express computable logic. The schema provides expression nodes for arithmetic, comparison, logic, text manipulation, temporal operations, statistics, geometry, collections, and more. Expressions compose as trees: operator nodes contain argument-wrapper children that hold sub-expressions.

## Concept Groups

| Group | Description |
|---|---|
| Expression Containers | `Calculation`, `Validation` top-level wrappers. |
| Core Expression Nodes | `Argument`, `Variable`, `Constant`, `FieldStep`, `Index`, `Source`, `Position`, `Absent`. |
| Context and Input Nodes | `Input`, `ThisNode`, `Field`, `Element`, `Parameter`, `Literal`. |
| Argument Wrappers | Generic (`Referent`, `Comparator`) and semantic (`Augend`/`Addend`, `Multiplicand`/`Multiplier`, `Dividend`/`Divisor`, etc.) positional wrappers. |
| Mathematical Constants | `Pi`, `Tau`, `EulerNumber`, `GoldenRatio`, `ImaginaryUnit`, `PositiveInfinity`, `NegativeInfinity`, `NegativeZero`. |
| Arithmetic | `Add`, `Subtract`, `Multiply`, `DivideBy`, `Negate`, `Reciprocal`, `Power`, `QuotientTowardZero`, `Remainder`, `Modulus`, etc. |
| Rounding | `RoundTowardNegativeInfinity`, `RoundToNearestTiesToEven`, `RoundToDecimalPlaces`, `RoundToSignificantFigures`, etc. |
| Powers / Roots / Exponentials | `SquareRoot`, `CubeRoot`, `NthRoot`, `Exponential`, `NaturalLogarithm`, `Logarithm`, etc. |
| Trigonometry | Full set: `Sine` through `ArcCotangent`, hyperbolic variants, angle conversions. |
| Comparison | `IsEqualTo`, `IsNotEqualTo`, `IsLessThan`, `IsGreaterThan`, `IsLessThanOrEqualTo`, `IsGreaterThanOrEqualTo`. |
| Logic | `And`, `Or`, `Not`, `Ternary`. |
| Type Guards | `IsAbsent`, `IsPresent`, `IsInteger`, `IsNumber`, `IsText`, `IsList`, `IsBoolean`. |
| Text Operations | Length, case, trim, pad, search, replace, split, pattern matching, validation (`IsValidEmail`, `IsValidUrl`, `IsValidUuid`). |
| Temporal | Construction (`MakePlainDate`, `MakePlainTime`), decomposition (`Year`, `Month`, `Day`), arithmetic, comparison, calendar, formatting, parsing, type guards. |
| Statistics | Central tendency, dispersion, position, correlation. |
| Combinatorics / Number Theory | `Factorial`, `BinomialCoefficient`, `IsPrime`, `GreatestCommonDivisor`, etc. |
| Linear Algebra | Vector and matrix operations. |
| Geometry | 2D and 3D point operations, distance, area, containment tests. |
| Collections | Transform, search, order, slice, combine, aggregate, predicates over lists, sets, maps, records, tuples. |
| Special Functions | `GammaFunction`, `BetaFunction`, `ErrorFunction`, `BesselJ`, `Zeta`, etc. |
| Calculus | `NumericalDerivative`, `NumericalIntegral`, `FindRoot`, `FindMinimum`, `FindMaximum`. |

## Design Notes

- Every operator is a distinct concept with semantically named argument wrappers (e.g., `Dividend`/`Divisor` rather than generic first/second).
- Expressions are trees, not strings. This makes them language-agnostic and amenable to static analysis.
- The schema defines the surface syntax; runtime semantics are specified in the behavior vocabulary specifications under `behavior-vocabulary/`.
- Pure leaf package with no imports.

---

**End of Behavior Expression Schema v1.0.0**
