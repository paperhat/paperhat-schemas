Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Math

This specification defines the **Math operator family** for the Behavior Vocabulary.

This document is **Normative**.

---

## 1. Purpose

This specification defines comprehensive mathematical operations for Behavior Programs, including:

- Basic arithmetic
- Complex and imaginary number operations
- Rounding and precision
- Exponentials, logarithms, and powers
- Trigonometry and hyperbolic functions
- Linear algebra
- Statistics
- Combinatorics
- Calculus operations

All operators are fully specified and implemented.

---

## 2. Shared Definitions (Normative)

### 2.1 Evaluation Contract

- Each operand is a Behavior expression evaluated to `Validation<Value>`.
- Unless explicitly stated otherwise, if any required operand evaluates to `Invalid(...)`, the operator result MUST be `Invalid(...)` (propagation).
- Operators MUST NOT encode failures as `<Absent/>`.

Diagnostic code rule:
- Where this specification requires an `Invalid(...)` produced by the operator itself, it MUST use the corresponding `Math::...` code defined by §14 (Behavior Diagnostics).

### 2.2 Numeric Domains

As defined by §7 (Behavior Dialect):

- `Integer` — exact integer values (unbounded)
- `Fraction` — exact rational numbers
- `PrecisionNumber` — decimal with explicit precision
- `RealNumber` — approximate real (IEEE 754)
- `Imaginary` — pure imaginary numbers
- `Complex` — complex numbers

Derived domains:
- `OrderableNumber` := `Integer` | `Fraction` | `PrecisionNumber`
- `ExactNumber` := `Integer` | `Fraction`
- `AnyRealNumber` := `Integer` | `Fraction` | `PrecisionNumber` | `RealNumber`
- `AnyNumber` := `AnyRealNumber` | `Imaginary` | `Complex`

### 2.3 Special Values

- `PositiveInfinity`
- `NegativeInfinity`
- `NegativeZero`

NaN is not a Behavior value. Any operation that would produce IEEE 754 NaN MUST return `Invalid(...)` with an appropriate diagnostic code.

### 2.4 Presence

Unless explicitly stated otherwise, Math operators MUST treat `<Absent/>` as a domain violation and return `Invalid(...)` with code `Math::NEED_PRESENT_NUMBER`.

### 2.5 Numeric Promotion

When operators accept mixed numeric domains:

1. `Integer` + `Fraction` -> `Fraction`
2. `Integer` + `PrecisionNumber` -> `PrecisionNumber`
3. `Fraction` + `PrecisionNumber` -> `PrecisionNumber`
4. Any exact type + `RealNumber` -> `RealNumber`
5. Any real type + `Imaginary` -> `Complex`
6. Any real type + `Complex` -> `Complex`

---

## 3. Mathematical Constants (Normative)

Zero-arity operators returning constant values.

### 3.1 Real Constants

| Operator | Returns | Value |
|----------|---------|-------|
| `Pi` | `RealNumber` | π ≈ 3.14159265358979... |
| `Tau` | `RealNumber` | τ = 2π ≈ 6.28318530717958... |
| `EulerNumber` | `RealNumber` | e ≈ 2.71828182845904... |
| `GoldenRatio` | `RealNumber` | φ ≈ 1.61803398874989... |

### 3.2 Special Values

| Operator | Returns |
|----------|---------|
| `PositiveInfinity` | `PositiveInfinity` |
| `NegativeInfinity` | `NegativeInfinity` |
| `NegativeZero` | `NegativeZero` |

### 3.3 Complex Constants

| Operator | Returns | Value |
|----------|---------|-------|
| `ImaginaryUnit` | `Imaginary` | i (√-1) |

---

## 4. Basic Arithmetic (Normative)

### 4.1 `Add`

Arity: 2 or more

Domain: `AnyNumber`

```
Add(a, b, ...) -> AnyNumber
```

Semantics:
- Returns the sum of all operands.
- Result domain follows promotion rules.

### 4.2 `Subtract`

Arity: 2

Domain: `AnyNumber`

```
Subtract(left, right) -> AnyNumber
```

Semantics:
- Returns `left - right`.

### 4.3 `Multiply`

Arity: 2 or more

Domain: `AnyNumber`

```
Multiply(a, b, ...) -> AnyNumber
```

Semantics:
- Returns the product of all operands.
- Result domain follows promotion rules.

### 4.4 `Divide`

Arity: 2

Domain: `AnyNumber`

```
Divide(dividend, divisor) -> AnyNumber
```

Semantics:
- Returns `dividend / divisor`.

Error behavior:
- If divisor is zero and dividend is nonzero: return `PositiveInfinity` or `NegativeInfinity` (sign follows standard sign rules).
- If both divisor and dividend are zero: return `Invalid(...)` with code `Divide::INDETERMINATE_FORM`.

This rule applies uniformly to all numeric domains.

### 4.5 `Negate`

Arity: 1

Domain: `AnyNumber`

```
Negate(x) -> AnyNumber
```

Semantics:
- Returns `-x`.

### 4.6 `Reciprocal`

Arity: 1

Domain: `AnyNumber`

```
Reciprocal(x) -> AnyNumber
```

Semantics:
- Returns `1/x`.

Error behavior:
- If x is zero: return `Invalid(...)` with code `Reciprocal::DIVISOR_IS_ZERO`.

### 4.7 Infinity Arithmetic Rules (Normative)

The following rules govern arithmetic on infinite operands. They apply uniformly across all operators in §4.

**Indeterminate forms** — these produce `Invalid(...)`:

| Expression | Diagnostic Code |
|-----------|----------------|
| `∞ + (-∞)` | `Add::INDETERMINATE_FORM` |
| `(-∞) + ∞` | `Add::INDETERMINATE_FORM` |
| `∞ - ∞` | `Subtract::INDETERMINATE_FORM` |
| `∞ × 0` | `Multiply::INDETERMINATE_FORM` |
| `0 × ∞` | `Multiply::INDETERMINATE_FORM` |
| `∞ / ∞` | `Divide::INDETERMINATE_FORM` |
| `0 / 0` | `Divide::INDETERMINATE_FORM` |

**Well-defined infinity operations** — these produce valid values:

| Expression | Result |
|-----------|--------|
| `∞ + ∞` | `PositiveInfinity` |
| `(-∞) + (-∞)` | `NegativeInfinity` |
| `∞ × x` (x > 0) | `PositiveInfinity` |
| `∞ × x` (x < 0) | `NegativeInfinity` |
| `x / ∞` (x finite) | `0` (or `NegativeZero` if x < 0) |
| `x / (-∞)` (x finite) | `0` (or `NegativeZero` if x > 0) |
| `Power(∞, x)` (x > 0) | `PositiveInfinity` |
| `Power(∞, x)` (x < 0) | `0` |

---

## 5. Integer Arithmetic (Normative)

All operators in this section share the following error behavior:

- If divisor is zero: return `Invalid(...)` with code `Math::DIVISOR_IS_ZERO`.

### 5.1 `QuotientTowardZero`

Arity: 2

Domain: `Integer`

```
QuotientTowardZero(dividend, divisor) -> Integer
```

Semantics:
- Integer division truncated toward zero.

### 5.2 `QuotientTowardNegativeInfinity`

Arity: 2

Domain: `Integer`

```
QuotientTowardNegativeInfinity(dividend, divisor) -> Integer
```

Semantics:
- Integer division truncated toward negative infinity (floor division).

### 5.3 `Remainder`

Arity: 2

Domain: `Integer`

```
Remainder(dividend, divisor) -> Integer
```

Semantics:
- Returns `dividend - divisor * QuotientTowardZero(dividend, divisor)`.
- Sign follows the dividend.

### 5.4 `Modulus`

Arity: 2

Domain: `Integer`

```
Modulus(dividend, divisor) -> Integer
```

Semantics:
- Euclidean modulus: `dividend - divisor * QuotientTowardNegativeInfinity(dividend, divisor)`.
- Result is always non-negative when divisor is positive.

### 5.5 `QuotientAndRemainder`

Arity: 2

Domain: `Integer`

```
QuotientAndRemainder(dividend, divisor) -> Tuple(Integer, Integer)
```

Semantics:
- Returns `(quotient, remainder)` using truncation toward zero.

### 5.6 `QuotientAndModulus`

Arity: 2

Domain: `Integer`

```
QuotientAndModulus(dividend, divisor) -> Tuple(Integer, Integer)
```

Semantics:
- Returns `(quotient, modulus)` using floor division.

---

## 6. Complex Number Operations (Normative)

### 6.1 `MakeComplex`

Arity: 2

Domain: `AnyRealNumber`, `AnyRealNumber`

```
MakeComplex(real, imaginary) -> Complex
```

Semantics:
- Constructs a complex number from real and imaginary parts.

### 6.2 `MakeImaginary`

Arity: 1

Domain: `AnyRealNumber`

```
MakeImaginary(coefficient) -> Imaginary
```

Semantics:
- Constructs a pure imaginary number.

### 6.3 `RealPart`

Arity: 1

Domain: `Complex` | `Imaginary` | `AnyRealNumber`

```
RealPart(z) -> AnyRealNumber
```

Semantics:
- Returns the real part.
- For `Imaginary`, returns 0.
- For real numbers, returns the value itself.

### 6.4 `ImaginaryPart`

Arity: 1

Domain: `Complex` | `Imaginary` | `AnyRealNumber`

```
ImaginaryPart(z) -> AnyRealNumber
```

Semantics:
- Returns the imaginary coefficient.
- For real numbers, returns 0.

### 6.5 `Conjugate`

Arity: 1

Domain: `Complex` | `Imaginary`

```
Conjugate(z) -> Complex | Imaginary
```

Semantics:
- Returns the complex conjugate (negates imaginary part).

### 6.6 `Magnitude`

Arity: 1

Domain: `Complex` | `Imaginary` | `AnyRealNumber`

```
Magnitude(z) -> RealNumber
```

Semantics:
- Returns |z| = √(real² + imaginary²).
- For real numbers, returns absolute value.

### 6.7 `Phase`

Arity: 1

Domain: `Complex` | `Imaginary`

```
Phase(z) -> RealNumber
```

Semantics:
- Returns the argument (angle) in radians, range (-π, π].

Error behavior:
- If z is zero (0 + 0i): return `Invalid(...)` with code `Phase::NEED_NONZERO_INPUT`.

### 6.8 `MakeComplexFromPolar`

Arity: 2

Domain: `AnyRealNumber`, `AnyRealNumber`

```
MakeComplexFromPolar(magnitude, phase) -> Complex
```

Semantics:
- Constructs a complex number from polar form.
- `real = magnitude * cos(phase)`
- `imaginary = magnitude * sin(phase)`

---

## 7. Value Operations (Normative)

### 7.1 `AbsoluteValue`

Arity: 1

Domain: `AnyRealNumber`

```
AbsoluteValue(x) -> AnyRealNumber
```

Semantics:
- Returns |x|.

### 7.2 `Sign`

Arity: 1

Domain: `AnyRealNumber`

```
Sign(x) -> Integer
```

Semantics:
- Returns -1 if x < 0, 0 if x = 0, 1 if x > 0.

### 7.3 `CopySign`

Arity: 2

Domain: `AnyRealNumber`

```
CopySign(magnitude, signSource) -> AnyRealNumber
```

Semantics:
- Returns a value with the magnitude of the first operand and the sign of the second.

### 7.4 `Minimum`

Arity: 2 or more

Domain: `OrderableNumber`

```
Minimum(a, b, ...) -> OrderableNumber
```

Semantics:
- Returns the smallest value.

### 7.5 `Maximum`

Arity: 2 or more

Domain: `OrderableNumber`

```
Maximum(a, b, ...) -> OrderableNumber
```

Semantics:
- Returns the largest value.

### 7.6 `Clamp`

Arity: 3

Domain: `OrderableNumber`

```
Clamp(value, minimum, maximum) -> OrderableNumber
```

Semantics:
- Returns value constrained to [minimum, maximum].

Error behavior:
- If minimum > maximum, return `Invalid(...)` with code `Math::NEED_VALID_RANGE`.

---

## 8. Rounding Operations (Normative)

### 8.1 `RoundTowardNegativeInfinity`

Arity: 1

Domain: `AnyRealNumber`

```
RoundTowardNegativeInfinity(x) -> Integer
```

Semantics:
- Floor function. Returns the largest integer ≤ x.

### 8.2 `RoundTowardPositiveInfinity`

Arity: 1

Domain: `AnyRealNumber`

```
RoundTowardPositiveInfinity(x) -> Integer
```

Semantics:
- Ceiling function. Returns the smallest integer ≥ x.

### 8.3 `RoundTowardZero`

Arity: 1

Domain: `AnyRealNumber`

```
RoundTowardZero(x) -> Integer
```

Semantics:
- Truncation. Removes fractional part toward zero.

### 8.4 `RoundToNearestTiesToEven`

Arity: 1

Domain: `AnyRealNumber`

```
RoundToNearestTiesToEven(x) -> Integer
```

Semantics:
- Banker's rounding. Ties go to nearest even integer.

### 8.5 `RoundToNearestTiesAwayFromZero`

Arity: 1

Domain: `AnyRealNumber`

```
RoundToNearestTiesAwayFromZero(x) -> Integer
```

Semantics:
- Standard rounding. Ties go away from zero.

### 8.6 `RoundToDecimalPlaces`

Arity: 2

Domain: `AnyRealNumber`, `Integer`

```
RoundToDecimalPlaces(x, places) -> PrecisionNumber
```

Semantics:
- Rounds to specified decimal places using ties-to-even.

Error behavior:
- If places < 0: return `Invalid(...)` with code `RoundToDecimalPlaces::NEED_NONNEGATIVE_PLACES`.

### 8.7 `RoundToSignificantFigures`

Arity: 2

Domain: `AnyRealNumber`, `Integer`

```
RoundToSignificantFigures(x, figures) -> PrecisionNumber
```

Semantics:
- Rounds to specified significant figures.

Error behavior:
- If figures < 1: return `Invalid(...)` with code `RoundToSignificantFigures::NEED_POSITIVE_FIGURES`.

### 8.8 `FractionalPart`

Arity: 1

Domain: `AnyRealNumber`

```
FractionalPart(x) -> AnyRealNumber
```

Semantics:
- Returns `x - RoundTowardZero(x)`.
- Sign matches the input.

### 8.9 `SplitFractionalAndIntegralParts`

Arity: 1

Domain: `AnyRealNumber`

```
SplitFractionalAndIntegralParts(x) -> Record { integralPart, fractionalPart }
```

Semantics:
- Returns both parts as a record.

---

## 9. Powers, Roots, and Exponentials (Normative)

### 9.1 `Power`

Arity: 2

Domain: `AnyNumber`, `AnyNumber`

```
Power(base, exponent) -> AnyNumber
```

Semantics:
- Returns base^exponent.
- Handles complex results (e.g., negative base with fractional exponent).

Error behavior:
- If base is zero and exponent is zero: return `Invalid(...)` with code `Power::INDETERMINATE_FORM`.

### 9.2 `SquareRoot`

Arity: 1

Domain: `AnyNumber`

```
SquareRoot(x) -> AnyNumber
```

Semantics:
- Returns √x.
- For negative real numbers, returns an Imaginary result.

### 9.3 `CubeRoot`

Arity: 1

Domain: `AnyRealNumber`

```
CubeRoot(x) -> AnyRealNumber
```

Semantics:
- Returns the real cube root.

### 9.4 `NthRoot`

Arity: 2

Domain: `AnyNumber`, `Integer`

```
NthRoot(x, n) -> AnyNumber
```

Semantics:
- Returns the nth root.

Error behavior:
- If n is zero: return `Invalid(...)` with code `NthRoot::NEED_NONZERO_DEGREE`.

### 9.5 `Exponential`

Arity: 1

Domain: `AnyNumber`

```
Exponential(x) -> AnyNumber
```

Semantics:
- Returns e^x.

### 9.6 `ExponentialMinusOne`

Arity: 1

Domain: `AnyNumber`

```
ExponentialMinusOne(x) -> AnyNumber
```

Semantics:
- Returns e^x - 1 with higher precision for small x.

### 9.7 `ExponentialBaseTwo`

Arity: 1

Domain: `AnyRealNumber`

```
ExponentialBaseTwo(x) -> RealNumber
```

Semantics:
- Returns 2^x.

### 9.8 `ExponentialBaseTen`

Arity: 1

Domain: `AnyRealNumber`

```
ExponentialBaseTen(x) -> RealNumber
```

Semantics:
- Returns 10^x.

### 9.9 `NaturalLogarithm`

Arity: 1

Domain: `AnyNumber`

```
NaturalLogarithm(x) -> AnyNumber
```

Semantics:
- Returns ln(x).
- For negative real numbers, returns a Complex result.

### 9.10 `NaturalLogarithmOfOnePlus`

Arity: 1

Domain: `AnyNumber`

```
NaturalLogarithmOfOnePlus(x) -> AnyNumber
```

Semantics:
- Returns ln(1 + x) with higher precision for small x.

### 9.11 `BaseTwoLogarithm`

Arity: 1

Domain: `AnyRealNumber`

```
BaseTwoLogarithm(x) -> RealNumber
```

Semantics:
- Returns log₂(x).
- If x is zero, returns `NegativeInfinity`.

Error behavior:
- If x < 0: return `Invalid(...)` with code `BaseTwoLogarithm::NEED_POSITIVE_INPUT`.

### 9.12 `BaseTenLogarithm`

Arity: 1

Domain: `AnyRealNumber`

```
BaseTenLogarithm(x) -> RealNumber
```

Semantics:
- Returns log₁₀(x).
- If x is zero, returns `NegativeInfinity`.

Error behavior:
- If x < 0: return `Invalid(...)` with code `BaseTenLogarithm::NEED_POSITIVE_INPUT`.

### 9.13 `Logarithm`

Arity: 2

Domain: `AnyNumber`, `AnyNumber`

```
Logarithm(x, base) -> AnyNumber
```

Semantics:
- Returns log_base(x).

Error behavior:
- If base equals 1: return `Invalid(...)` with code `Logarithm::NEED_VALID_BASE`.

### 9.14 `HypotenuseLength`

Arity: 2

Domain: `AnyRealNumber`

```
HypotenuseLength(x, y) -> RealNumber
```

Semantics:
- Returns √(x² + y²) without intermediate overflow.

### 9.15 `HypotenuseLengthThree`

Arity: 3

Domain: `AnyRealNumber`

```
HypotenuseLengthThree(x, y, z) -> RealNumber
```

Semantics:
- Returns √(x² + y² + z²).

---

## 10. Trigonometry (Normative)

All angles are in radians unless otherwise specified.

### 10.1 Basic Trigonometric Functions

| Operator | Arity | Domain | Returns |
|----------|-------|--------|---------|
| `Sine` | 1 | `AnyNumber` | `AnyNumber` |
| `Cosine` | 1 | `AnyNumber` | `AnyNumber` |
| `Tangent` | 1 | `AnyNumber` | `AnyNumber` |
| `Secant` | 1 | `AnyNumber` | `AnyNumber` |
| `Cosecant` | 1 | `AnyNumber` | `AnyNumber` |
| `Cotangent` | 1 | `AnyNumber` | `AnyNumber` |

### 10.2 Inverse Trigonometric Functions

| Operator | Arity | Domain | Returns |
|----------|-------|--------|---------|
| `ArcSine` | 1 | `AnyNumber` | `AnyNumber` |
| `ArcCosine` | 1 | `AnyNumber` | `AnyNumber` |
| `ArcTangent` | 1 | `AnyNumber` | `AnyNumber` |
| `ArcTangentFromCoordinates` | 2 | `AnyRealNumber` | `RealNumber` |
| `ArcSecant` | 1 | `AnyNumber` | `AnyNumber` |
| `ArcCosecant` | 1 | `AnyNumber` | `AnyNumber` |
| `ArcCotangent` | 1 | `AnyNumber` | `AnyNumber` |

`ArcTangentFromCoordinates(y, x)` returns atan2(y, x) in range (-π, π].

### 10.3 Angle Conversion

| Operator | Arity | Semantics |
|----------|-------|-----------|
| `RadiansFromDegrees` | 1 | degrees × (π/180) |
| `DegreesFromRadians` | 1 | radians × (180/π) |
| `RadiansFromGradians` | 1 | gradians × (π/200) |
| `GradiansFromRadians` | 1 | radians × (200/π) |

### 10.4 Pi-Multiple Functions

| Operator | Semantics |
|----------|-----------|
| `SineOfPiTimes(x)` | sin(πx) with higher precision |
| `CosineOfPiTimes(x)` | cos(πx) with higher precision |
| `TangentOfPiTimes(x)` | tan(πx) with higher precision |

---

## 11. Hyperbolic Functions (Normative)

### 11.1 Basic Hyperbolic Functions

| Operator | Arity | Domain | Returns |
|----------|-------|--------|---------|
| `HyperbolicSine` | 1 | `AnyNumber` | `AnyNumber` |
| `HyperbolicCosine` | 1 | `AnyNumber` | `AnyNumber` |
| `HyperbolicTangent` | 1 | `AnyNumber` | `AnyNumber` |
| `HyperbolicSecant` | 1 | `AnyNumber` | `AnyNumber` |
| `HyperbolicCosecant` | 1 | `AnyNumber` | `AnyNumber` |
| `HyperbolicCotangent` | 1 | `AnyNumber` | `AnyNumber` |

### 11.2 Inverse Hyperbolic Functions

| Operator | Arity | Domain | Returns |
|----------|-------|--------|---------|
| `AreaHyperbolicSine` | 1 | `AnyNumber` | `AnyNumber` |
| `AreaHyperbolicCosine` | 1 | `AnyNumber` | `AnyNumber` |
| `AreaHyperbolicTangent` | 1 | `AnyNumber` | `AnyNumber` |
| `AreaHyperbolicSecant` | 1 | `AnyNumber` | `AnyNumber` |
| `AreaHyperbolicCosecant` | 1 | `AnyNumber` | `AnyNumber` |
| `AreaHyperbolicCotangent` | 1 | `AnyNumber` | `AnyNumber` |

---

## 12. Statistics (Normative)

All statistical operators take a List of numbers.

Shared error behavior for §12:

- If the input list is empty: return `Invalid(...)` with code `Math::NEED_NONEMPTY_LIST`.

### 12.1 Central Tendency

| Operator | Semantics |
|----------|-----------|
| `ArithmeticMean(values)` | Sum / count |
| `GeometricMean(values)` | nth root of product |
| `HarmonicMean(values)` | n / sum of reciprocals |
| `Median(values)` | Middle value (average of two if even count) |
| `Mode(values)` | Most frequent value(s) — returns List |
| `WeightedMean(values, weights)` | Weighted average |

Error behavior:

- `GeometricMean`: if any element is non-positive, return `Invalid(...)` with code `GeometricMean::NEED_POSITIVE_ELEMENTS`.
- `HarmonicMean`: if any element is zero, return `Invalid(...)` with code `HarmonicMean::NEED_NONZERO_ELEMENTS`.
- `WeightedMean`: if `values` and `weights` have different lengths, return `Invalid(...)` with code `Math::LENGTH_MISMATCH`.

### 12.2 Dispersion

| Operator | Semantics |
|----------|-----------|
| `Range(values)` | max - min |
| `InterquartileRange(values)` | Q3 - Q1 |
| `PopulationVariance(values)` | Σ(x - μ)² / n |
| `SampleVariance(values)` | Σ(x - μ)² / (n-1) |
| `PopulationStandardDeviation(values)` | √(PopulationVariance) |
| `SampleStandardDeviation(values)` | √(SampleVariance) |
| `MeanAbsoluteDeviation(values)` | Σ|x - μ| / n |
| `MedianAbsoluteDeviation(values)` | Median of |x - median| |
| `CoefficientOfVariation(values)` | σ / μ |

Error behavior:

- `SampleVariance` and `SampleStandardDeviation`: if list has fewer than 2 elements, return `Invalid(...)` with code `Math::NEED_MINIMUM_SAMPLE_SIZE`.
- `CoefficientOfVariation`: if the mean is zero, return `Invalid(...)` with code `CoefficientOfVariation::NEED_NONZERO_MEAN`.

### 12.3 Distribution Shape

| Operator | Semantics |
|----------|-----------|
| `Skewness(values)` | Third standardized moment |
| `Kurtosis(values)` | Fourth standardized moment |
| `ExcessKurtosis(values)` | Kurtosis - 3 |

### 12.4 Position

| Operator | Semantics |
|----------|-----------|
| `Quantile(values, p)` | Value at proportion p (0 to 1) |
| `Percentile(values, p)` | Value at percentile p (0 to 100) |
| `Quartile(values, q)` | Q1, Q2, Q3 (q = 1, 2, or 3) |
| `Decile(values, d)` | Value at decile d (1 to 10) |

Error behavior:

- `Quantile`: if p is not in [0, 1], return `Invalid(...)` with code `Quantile::NEED_VALID_PROPORTION`.
- `Percentile`: if p is not in [0, 100], return `Invalid(...)` with code `Percentile::NEED_VALID_PERCENTILE`.
- `Quartile`: if q is not 1, 2, or 3, return `Invalid(...)` with code `Quartile::NEED_VALID_QUARTILE`.
- `Decile`: if d is not in 1–10, return `Invalid(...)` with code `Decile::NEED_VALID_DECILE`.

### 12.5 Correlation and Regression

| Operator | Semantics |
|----------|-----------|
| `Covariance(valuesX, valuesY)` | Population covariance |
| `SampleCovariance(valuesX, valuesY)` | Sample covariance |
| `PearsonCorrelation(valuesX, valuesY)` | Pearson r |
| `SpearmanCorrelation(valuesX, valuesY)` | Spearman rank correlation |
| `LinearRegression(valuesX, valuesY)` | Returns Record { slope, intercept, r } |

Error behavior (shared for §12.5):

- If the two input lists have different lengths: return `Invalid(...)` with code `Math::LENGTH_MISMATCH`.
- `SampleCovariance`: if lists have fewer than 2 elements, return `Invalid(...)` with code `Math::NEED_MINIMUM_SAMPLE_SIZE`.

---

## 13. Combinatorics (Normative)

### 13.1 Basic Combinatorics

| Operator | Semantics |
|----------|-----------|
| `Factorial(n)` | n! |
| `DoubleFactorial(n)` | n!! |
| `BinomialCoefficient(n, k)` | "n choose k" |
| `PermutationCount(n, k)` | n! / (n-k)! |
| `MultisetCoefficient(n, k)` | (n+k-1) choose k |

Error behavior:

- `Factorial` and `DoubleFactorial`: if n < 0, return `Invalid(...)` with code `Math::NEED_NONNEGATIVE_INTEGER`.
- `BinomialCoefficient` and `PermutationCount`: if k < 0 or k > n, return `Invalid(...)` with code `Math::NEED_VALID_COMBINATORIAL_ARGUMENTS`.

### 13.2 Number Theory

| Operator | Semantics |
|----------|-----------|
| `GreatestCommonDivisor(a, b)` | GCD |
| `LeastCommonMultiple(a, b)` | LCM |
| `ExtendedGcd(a, b)` | Returns Record { gcd, x, y } where ax + by = gcd |
| `IsPrime(n)` | Boolean |
| `PrimeFactorization(n)` | List of prime factors with multiplicities |
| `NextPrime(n)` | Smallest prime > n |
| `PreviousPrime(n)` | Largest prime < n |
| `EulerTotient(n)` | φ(n) |
| `DivisorCount(n)` | Number of divisors |
| `DivisorSum(n)` | Sum of divisors |
| `Divisors(n)` | List of all divisors |
| `ModularExponentiation(base, exp, mod)` | base^exp mod mod |
| `ModularInverse(a, mod)` | Multiplicative inverse mod mod |

Error behavior:

- `PrimeFactorization`: if n ≤ 1, return `Invalid(...)` with code `PrimeFactorization::NEED_INTEGER_ABOVE_ONE`.
- `PreviousPrime`: if n ≤ 2, return `Invalid(...)` with code `PreviousPrime::NO_PREVIOUS_PRIME`.
- `ModularExponentiation`: if mod is zero, return `Invalid(...)` with code `Math::DIVISOR_IS_ZERO`.
- `ModularInverse`: if gcd(a, mod) ≠ 1, return `Invalid(...)` with code `ModularInverse::NEED_COPRIME_ARGUMENTS`.

---

## 14. Linear Algebra (Normative)

Vectors are represented as Lists of numbers.
Matrices are represented as Lists of Lists (row-major).

### 14.1 Vector Operations

| Operator | Semantics |
|----------|-----------|
| `DotProduct(a, b)` | Σ(aᵢ × bᵢ) |
| `CrossProduct(a, b)` | 3D cross product |
| `VectorLength(v)` | Euclidean norm |
| `VectorLengthSquared(v)` | Sum of squares |
| `NormalizeVector(v)` | v / |v| |
| `VectorAngle(a, b)` | Angle between vectors in radians |
| `VectorProjection(a, onto)` | Projection of a onto b |
| `ScalarProjection(a, onto)` | Scalar projection |

Error behavior:

- `DotProduct`: if vectors have different lengths, return `Invalid(...)` with code `Math::LENGTH_MISMATCH`.
- `CrossProduct`: if either vector does not have exactly 3 elements, return `Invalid(...)` with code `CrossProduct::NEED_THREE_DIMENSIONS`.
- `NormalizeVector`: if the vector has zero length, return `Invalid(...)` with code `NormalizeVector::NEED_NONZERO_VECTOR`.

### 14.2 Matrix Operations

| Operator | Semantics |
|----------|-----------|
| `MatrixAdd(a, b)` | Element-wise addition |
| `MatrixSubtract(a, b)` | Element-wise subtraction |
| `MatrixMultiply(a, b)` | Matrix multiplication |
| `MatrixScalarMultiply(m, s)` | Multiply by scalar |
| `MatrixTranspose(m)` | Transpose |
| `MatrixDeterminant(m)` | Determinant |
| `MatrixTrace(m)` | Sum of diagonal |
| `MatrixInverse(m)` | Inverse (if exists) |
| `MatrixRank(m)` | Rank |
| `MatrixNullity(m)` | Dimension of null space |

Error behavior:

- `MatrixAdd` and `MatrixSubtract`: if matrices have different dimensions, return `Invalid(...)` with code `Math::DIMENSION_MISMATCH`.
- `MatrixMultiply`: if the column count of the first matrix does not equal the row count of the second, return `Invalid(...)` with code `Math::DIMENSION_MISMATCH`.
- `MatrixDeterminant`, `MatrixTrace`, and `MatrixInverse`: if the matrix is not square, return `Invalid(...)` with code `Math::NEED_SQUARE_MATRIX`.
- `MatrixInverse`: if the matrix is singular, return `Invalid(...)` with code `MatrixInverse::SINGULAR_MATRIX`.

### 14.3 Matrix Decomposition

| Operator | Semantics |
|----------|-----------|
| `LuDecomposition(m)` | Returns Record { L, U, P } |
| `QrDecomposition(m)` | Returns Record { Q, R } |
| `CholeskyDecomposition(m)` | Returns lower triangular L |
| `SingularValueDecomposition(m)` | Returns Record { U, S, V } |
| `EigenDecomposition(m)` | Returns Record { values, vectors } |

Error behavior:

- `LuDecomposition` and `EigenDecomposition`: if the matrix is not square, return `Invalid(...)` with code `Math::NEED_SQUARE_MATRIX`.
- `CholeskyDecomposition`: if the matrix is not symmetric positive definite, return `Invalid(...)` with code `CholeskyDecomposition::NEED_POSITIVE_DEFINITE`.

### 14.4 Linear Systems

| Operator | Semantics |
|----------|-----------|
| `SolveLinearSystem(A, b)` | Solve Ax = b |
| `LeastSquaresSolution(A, b)` | Least squares solution |

Error behavior:

- `SolveLinearSystem`: if A is not square or dimensions are incompatible, return `Invalid(...)` with code `Math::DIMENSION_MISMATCH`. If A is singular, return `Invalid(...)` with code `SolveLinearSystem::SINGULAR_SYSTEM`.

### 14.5 Matrix Creation

| Operator | Semantics |
|----------|-----------|
| `IdentityMatrix(n)` | n×n identity |
| `ZeroMatrix(rows, cols)` | Matrix of zeros |
| `DiagonalMatrix(values)` | Diagonal from list |

Error behavior:

- `IdentityMatrix` and `ZeroMatrix`: if any dimension is < 1, return `Invalid(...)` with code `Math::NEED_POSITIVE_SIZE`.

---

## 15. Calculus (Normative)

These operators perform numerical differentiation and integration.

### 15.1 Differentiation

| Operator | Semantics |
|----------|-----------|
| `NumericalDerivative(f, x)` | df/dx at point x |
| `NumericalDerivativeSecond(f, x)` | d²f/dx² at point x |
| `NumericalPartialDerivative(f, point, variableIndex)` | Partial derivative |
| `NumericalGradient(f, point)` | Gradient vector |
| `NumericalJacobian(f, point)` | Jacobian matrix |
| `NumericalHessian(f, point)` | Hessian matrix |

Note: `f` is a Behavior expression where `Argument` is the input.

### 15.2 Integration

| Operator | Semantics |
|----------|-----------|
| `NumericalIntegral(f, lower, upper)` | Definite integral |
| `NumericalIntegralAdaptive(f, lower, upper, tolerance)` | Adaptive quadrature |

### 15.3 Root Finding

| Operator | Semantics |
|----------|-----------|
| `FindRootBisection(f, lower, upper)` | Bisection method |
| `FindRootNewton(f, initialGuess)` | Newton's method |
| `FindRootSecant(f, x0, x1)` | Secant method |
| `FindRootBrent(f, lower, upper)` | Brent's method |

Error behavior:

- `FindRootBisection` and `FindRootBrent`: if f(lower) and f(upper) have the same sign, return `Invalid(...)` with code `Math::NEED_SIGN_CHANGE`.
- If any root-finding method fails to converge: return `Invalid(...)` with code `Math::CONVERGENCE_FAILURE`.

### 15.4 Optimization

| Operator | Semantics |
|----------|-----------|
| `FindMinimumGoldenSection(f, lower, upper)` | Golden section search |
| `FindMinimumBrent(f, lower, upper)` | Brent's method for minimum |
| `FindMinimumGradientDescent(f, initialPoint, learningRate, iterations)` | Gradient descent |

Error behavior:

- If any optimization method fails to converge: return `Invalid(...)` with code `Math::CONVERGENCE_FAILURE`.

---

## 16. Special Functions (Normative)

### 16.1 Gamma and Related

| Operator | Semantics |
|----------|-----------|
| `Gamma(x)` | Γ(x) |
| `LogGamma(x)` | ln(Γ(x)) |
| `Digamma(x)` | ψ(x) = d/dx ln(Γ(x)) |
| `Beta(a, b)` | B(a,b) = Γ(a)Γ(b)/Γ(a+b) |
| `IncompleteBeta(x, a, b)` | Incomplete beta function |
| `IncompleteGamma(a, x)` | Incomplete gamma function |

Error behavior:

- `Gamma`: if x is a non-positive integer, return `Invalid(...)` with code `Gamma::DOMAIN_ERROR`.
- `LogGamma`: if x ≤ 0, return `Invalid(...)` with code `LogGamma::NEED_POSITIVE_INPUT`.

### 16.2 Error Functions

| Operator | Semantics |
|----------|-----------|
| `ErrorFunction(x)` | erf(x) |
| `ComplementaryErrorFunction(x)` | erfc(x) = 1 - erf(x) |
| `InverseErrorFunction(x)` | erf⁻¹(x) |

Error behavior:

- `InverseErrorFunction`: if |x| ≥ 1, return `Invalid(...)` with code `InverseErrorFunction::NEED_VALID_INPUT`.

### 16.3 Bessel Functions

| Operator | Semantics |
|----------|-----------|
| `BesselJ(n, x)` | Bessel function of first kind |
| `BesselY(n, x)` | Bessel function of second kind |
| `BesselI(n, x)` | Modified Bessel first kind |
| `BesselK(n, x)` | Modified Bessel second kind |

---

## 17. Interpolation (Normative)

| Operator | Semantics |
|----------|-----------|
| `LinearInterpolation(start, end, t)` | start + t × (end - start) |
| `InverseLinearInterpolation(start, end, value)` | (value - start) / (end - start) |
| `Remap(value, fromStart, fromEnd, toStart, toEnd)` | Map from one range to another |
| `CubicInterpolation(p0, p1, p2, p3, t)` | Catmull-Rom spline |
| `LagrangeInterpolation(points, x)` | Lagrange polynomial |
| `SplineInterpolation(points, x)` | Cubic spline |

Error behavior:

- `InverseLinearInterpolation` and `Remap`: if start equals end (or fromStart equals fromEnd), return `Invalid(...)` with code `Math::NEED_DISTINCT_ENDPOINTS`.
- `LagrangeInterpolation` and `SplineInterpolation`: if points contains fewer than 2 entries, return `Invalid(...)` with code `Math::NEED_SUFFICIENT_POINTS`.

---

## 18. Geometry (Normative)

### 18.1 2D Geometry

| Operator | Semantics |
|----------|-----------|
| `DistanceBetweenPoints2D(x1, y1, x2, y2)` | Euclidean distance |
| `MidpointBetweenPoints2D(x1, y1, x2, y2)` | Returns Tuple(x, y) |
| `AngleBetweenPoints2D(x1, y1, x2, y2)` | Angle in radians |
| `RotatePoint2D(x, y, angle)` | Rotate around origin |
| `RotatePointAround2D(x, y, cx, cy, angle)` | Rotate around point |

### 18.2 3D Geometry

| Operator | Semantics |
|----------|-----------|
| `DistanceBetweenPoints3D(x1, y1, z1, x2, y2, z2)` | Euclidean distance |
| `MidpointBetweenPoints3D(...)` | Returns Tuple(x, y, z) |

### 18.3 Angle Normalization

| Operator | Semantics |
|----------|-----------|
| `NormalizeAngleRadians(radians)` | Normalize to [0, 2π) |
| `NormalizeAngleRadiansSigned(radians)` | Normalize to (-π, π] |
| `NormalizeAngleDegrees(degrees)` | Normalize to [0, 360) |
| `NormalizeAngleDegreesSigned(degrees)` | Normalize to (-180, 180] |

---

## 19. Classification (Normative)

| Operator | Returns | Semantics |
|----------|---------|-----------|
| `IsFinite(x)` | Boolean | True if not ±Infinity |
| `IsInfinite(x)` | Boolean | True if ±∞ |
| `IsPositiveInfinity(x)` | Boolean | True if +∞ |
| `IsNegativeInfinity(x)` | Boolean | True if -∞ |
| `IsPositive(x)` | Boolean | True if x > 0 |
| `IsNegative(x)` | Boolean | True if x < 0 |
| `IsZero(x)` | Boolean | True if x = 0 |
| `IsEven(x)` | Boolean | True if integer and even |
| `IsOdd(x)` | Boolean | True if integer and odd |
| `IsInteger(x)` | Boolean | True if integral value |
| `IsRational(x)` | Boolean | True if representable as fraction |

---

## 20. Conversion (Normative)

| Operator | Semantics |
|----------|-----------|
| `ConvertToInteger(x)` | Convert to Integer (must be integral) |
| `ConvertToFraction(x)` | Convert to Fraction |
| `ConvertToPrecisionNumber(x, precision)` | Convert with specified precision |
| `ConvertToRealNumber(x)` | Convert to RealNumber |
| `ConvertToComplex(x)` | Convert real to Complex |

Error behavior:
- `ConvertToInteger` on non-integral value: `Invalid(...)` with code `Math::NOT_INTEGRAL`.

---

## 21. IEEE 754 Specific (Normative)

For RealNumber with IEEE 754 profile:

| Operator | Semantics |
|----------|-----------|
| `NextRepresentableUp(x)` | Next larger representable value |
| `NextRepresentableDown(x)` | Next smaller representable value |
| `NextRepresentableToward(x, direction)` | Next representable toward direction |
| `IsNormal(x)` | True if normal (not subnormal) |
| `IsSubnormal(x)` | True if subnormal |
| `FusedMultiplyAdd(a, b, c)` | a×b + c with single rounding |
| `IsApproximatelyEqual(a, b, absTol, relTol)` | Approximate equality |

---

## 22. Conformance Appendix (Informative)

See [canonical-math-api-surface-conformance-appendix/index.md](canonical-math-api-surface-conformance-appendix/index.md).

---

## 23. Diagnostic Code Table (Normative)

This table consolidates all diagnostic codes defined in the Math operator family. Operators in §3 (constants), §10–§11 (trigonometric and hyperbolic), §18 (geometry), §19 (classification), and §21 (IEEE 754) are total functions on their domains and produce no operator-specific diagnostics beyond the shared §2.4 rule.

### 23.1 Family-Level Codes

| Code | Operators | Expected | Message | Suggestion |
|------|-----------|----------|---------|------------|
| `Math::NEED_PRESENT_NUMBER` | All Math operators (§2.4) | Present numeric value | "Lexis expected a numeric value, but found {received}." | "Math operators require present numeric operands — please check that the value is not absent." |
| `Math::DIVISOR_IS_ZERO` | All §5 integer division operators, ModularExponentiation | Nonzero divisor | "Lexis expected a nonzero divisor, but found zero." | "Division by zero is undefined for integer arithmetic — please provide a nonzero divisor." |
| `Math::NEED_VALID_RANGE` | Clamp | minimum ≤ maximum | "Lexis expected minimum ≤ maximum, but found minimum {received} > maximum {received}." | "Please ensure the minimum bound does not exceed the maximum bound." |
| `Math::NOT_INTEGRAL` | ConvertToInteger | Integral value | "Lexis expected an integral value, but found {received}." | "The value must be a whole number to convert to Integer — consider rounding first." |
| `Math::NEED_NONEMPTY_LIST` | All §12 statistical operators | Non-empty list | "Lexis expected a non-empty list, but found an empty list." | "Statistical operations require at least one element — please provide a non-empty list." |
| `Math::LENGTH_MISMATCH` | WeightedMean, all §12.5 correlation operators, DotProduct | Lists of equal length | "Lexis expected lists of equal length, but found lengths {received} and {received}." | "Please provide lists with the same number of elements." |
| `Math::NEED_MINIMUM_SAMPLE_SIZE` | SampleVariance, SampleStandardDeviation, SampleCovariance | At least 2 elements | "Lexis expected at least 2 elements for sample statistics, but found {received}." | "Sample variance and covariance require at least 2 data points." |
| `Math::NEED_NONNEGATIVE_INTEGER` | Factorial, DoubleFactorial | Non-negative integer | "Lexis expected a non-negative integer, but found {received}." | "Factorial is defined only for non-negative integers." |
| `Math::NEED_VALID_COMBINATORIAL_ARGUMENTS` | BinomialCoefficient, PermutationCount | 0 ≤ k ≤ n | "Lexis expected 0 ≤ k ≤ n, but found n = {received} and k = {received}." | "Please ensure k is between 0 and n inclusive." |
| `Math::DIMENSION_MISMATCH` | MatrixAdd, MatrixSubtract, MatrixMultiply, SolveLinearSystem | Compatible dimensions | "Lexis expected compatible matrix dimensions, but found {received}." | "Please ensure the matrix dimensions are compatible for this operation." |
| `Math::NEED_SQUARE_MATRIX` | MatrixDeterminant, MatrixTrace, MatrixInverse, LuDecomposition, EigenDecomposition | Square matrix | "Lexis expected a square matrix, but found dimensions {received}." | "This operation requires a square (n×n) matrix." |
| `Math::NEED_POSITIVE_SIZE` | IdentityMatrix, ZeroMatrix | Positive dimension | "Lexis expected a positive dimension, but found {received}." | "Matrix dimensions must be at least 1." |
| `Math::NEED_SIGN_CHANGE` | FindRootBisection, FindRootBrent | Opposite signs at endpoints | "Lexis expected f(lower) and f(upper) to have opposite signs, but both have the same sign." | "The function must cross zero in the interval — please choose bounds where the function changes sign." |
| `Math::CONVERGENCE_FAILURE` | All §15.3–§15.4 root-finding and optimization operators | Convergent iteration | "Lexis expected the iterative method to converge, but it did not converge within the allowed iterations." | "The method failed to find a solution — consider adjusting initial values or bounds." |
| `Math::NEED_DISTINCT_ENDPOINTS` | InverseLinearInterpolation, Remap | Distinct start and end | "Lexis expected distinct endpoints, but start equals end." | "The start and end values must differ to define an interpolation range." |
| `Math::NEED_SUFFICIENT_POINTS` | LagrangeInterpolation, SplineInterpolation | At least 2 points | "Lexis expected at least 2 interpolation points, but found {received}." | "Please provide at least 2 data points for interpolation." |

### 23.2 Operator-Specific Codes

| Code | Operators | Expected | Message | Suggestion |
|------|-----------|----------|---------|------------|
| `Add::INDETERMINATE_FORM` | Add | Determinate addition | "Lexis encountered an indeterminate form: ∞ + (−∞)." | "Adding positive and negative infinity is undefined — please check your operands." |
| `Subtract::INDETERMINATE_FORM` | Subtract | Determinate subtraction | "Lexis encountered an indeterminate form: ∞ − ∞." | "Subtracting equal infinities is undefined — please check your operands." |
| `Multiply::INDETERMINATE_FORM` | Multiply | Determinate multiplication | "Lexis encountered an indeterminate form: ∞ × 0." | "Multiplying infinity by zero is undefined — please check your operands." |
| `Divide::INDETERMINATE_FORM` | Divide | Determinate division | "Lexis encountered an indeterminate form: 0 / 0 or ∞ / ∞." | "This division produces an indeterminate form — please check your operands." |
| `Reciprocal::DIVISOR_IS_ZERO` | Reciprocal | Nonzero input | "Lexis expected a nonzero value for reciprocal, but found zero." | "The reciprocal of zero is undefined — please provide a nonzero value." |
| `Power::INDETERMINATE_FORM` | Power | Determinate exponentiation | "Lexis encountered an indeterminate form: 0^0." | "Zero raised to the power of zero is undefined — please check your operands." |
| `Phase::NEED_NONZERO_INPUT` | Phase | Nonzero complex number | "Lexis expected a nonzero complex number, but found 0 + 0i." | "The phase angle is undefined for zero — please provide a nonzero complex number." |
| `RoundToDecimalPlaces::NEED_NONNEGATIVE_PLACES` | RoundToDecimalPlaces | Non-negative integer | "Lexis expected a non-negative number of decimal places, but found {received}." | "Please provide 0 or a positive integer for the number of decimal places." |
| `RoundToSignificantFigures::NEED_POSITIVE_FIGURES` | RoundToSignificantFigures | Positive integer | "Lexis expected a positive number of significant figures, but found {received}." | "Please provide at least 1 significant figure." |
| `NthRoot::NEED_NONZERO_DEGREE` | NthRoot | Nonzero degree | "Lexis expected a nonzero root degree, but found 0." | "The zeroth root is undefined — please provide a nonzero degree." |
| `BaseTwoLogarithm::NEED_POSITIVE_INPUT` | BaseTwoLogarithm | Positive real number | "Lexis expected a positive number, but found {received}." | "The base-2 logarithm of a negative number is not a real value — please provide a positive number." |
| `BaseTenLogarithm::NEED_POSITIVE_INPUT` | BaseTenLogarithm | Positive real number | "Lexis expected a positive number, but found {received}." | "The base-10 logarithm of a negative number is not a real value — please provide a positive number." |
| `Logarithm::NEED_VALID_BASE` | Logarithm | Base ≠ 1 | "Lexis expected a logarithm base other than 1, but found 1." | "The logarithm base 1 is undefined — please provide a base other than 1." |
| `GeometricMean::NEED_POSITIVE_ELEMENTS` | GeometricMean | All positive elements | "Lexis expected all positive elements, but found {received}." | "The geometric mean requires all values to be positive." |
| `HarmonicMean::NEED_NONZERO_ELEMENTS` | HarmonicMean | All nonzero elements | "Lexis expected all nonzero elements, but found a zero value." | "The harmonic mean requires all values to be nonzero." |
| `CoefficientOfVariation::NEED_NONZERO_MEAN` | CoefficientOfVariation | Nonzero mean | "Lexis expected a nonzero mean, but the mean is zero." | "The coefficient of variation divides by the mean, which must be nonzero." |
| `Quantile::NEED_VALID_PROPORTION` | Quantile | p in [0, 1] | "Lexis expected a proportion between 0 and 1, but found {received}." | "Please provide a value for p in the range [0, 1]." |
| `Percentile::NEED_VALID_PERCENTILE` | Percentile | p in [0, 100] | "Lexis expected a percentile between 0 and 100, but found {received}." | "Please provide a value for p in the range [0, 100]." |
| `Quartile::NEED_VALID_QUARTILE` | Quartile | q in {1, 2, 3} | "Lexis expected a quartile of 1, 2, or 3, but found {received}." | "Please provide 1 (Q1), 2 (Q2), or 3 (Q3)." |
| `Decile::NEED_VALID_DECILE` | Decile | d in {1, …, 10} | "Lexis expected a decile from 1 to 10, but found {received}." | "Please provide an integer from 1 to 10." |
| `PrimeFactorization::NEED_INTEGER_ABOVE_ONE` | PrimeFactorization | Integer > 1 | "Lexis expected an integer greater than 1, but found {received}." | "Prime factorization is defined only for integers greater than 1." |
| `PreviousPrime::NO_PREVIOUS_PRIME` | PreviousPrime | Integer > 2 | "Lexis expected an integer greater than 2, but found {received}." | "There is no prime less than 2." |
| `ModularInverse::NEED_COPRIME_ARGUMENTS` | ModularInverse | gcd(a, mod) = 1 | "Lexis expected coprime arguments, but gcd({received}, {received}) ≠ 1." | "The modular inverse exists only when a and mod are coprime." |
| `CrossProduct::NEED_THREE_DIMENSIONS` | CrossProduct | 3-element vectors | "Lexis expected 3-element vectors, but found length {received}." | "The cross product is defined only for 3-dimensional vectors." |
| `NormalizeVector::NEED_NONZERO_VECTOR` | NormalizeVector | Nonzero vector | "Lexis expected a nonzero vector, but found the zero vector." | "A zero-length vector cannot be normalized — please provide a vector with nonzero magnitude." |
| `MatrixInverse::SINGULAR_MATRIX` | MatrixInverse | Invertible matrix | "Lexis expected an invertible matrix, but the matrix is singular." | "The matrix has no inverse because its determinant is zero." |
| `CholeskyDecomposition::NEED_POSITIVE_DEFINITE` | CholeskyDecomposition | Symmetric positive definite matrix | "Lexis expected a symmetric positive definite matrix, but found {received}." | "Cholesky decomposition requires a symmetric positive definite matrix." |
| `SolveLinearSystem::SINGULAR_SYSTEM` | SolveLinearSystem | Non-singular coefficient matrix | "Lexis expected a non-singular coefficient matrix, but the system is singular." | "The linear system has no unique solution because the coefficient matrix is singular." |
| `Gamma::DOMAIN_ERROR` | Gamma | Not a non-positive integer | "Lexis expected a valid input for Γ(x), but found non-positive integer {received}." | "The gamma function has poles at non-positive integers — please provide a different value." |
| `LogGamma::NEED_POSITIVE_INPUT` | LogGamma | Positive real number | "Lexis expected a positive number for ln(Γ(x)), but found {received}." | "The log-gamma function requires a positive input." |
| `InverseErrorFunction::NEED_VALID_INPUT` | InverseErrorFunction | \|x\| < 1 | "Lexis expected a value strictly between −1 and 1, but found {received}." | "The inverse error function is defined only for inputs in the open interval (−1, 1)." |

---

**End of Behavior Vocabulary — Math v1.0.0**
