# Math Expression

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines a semantic expression tree for mathematical content in technical specifications. Unlike presentational math markup (LaTeX, MathML Presentation), this schema captures the *meaning* of mathematical expressions so that a machine reasons about the math, not just render it. Projection layers emit MathML Content Markup, LaTeX, or other formats at render time from this semantic representation.

## Concepts

### Core Expression Nodes

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Expression | Semantic | MustNotBeEntity | ForbidsContent | Any expression node (1+, ordered) | Generic wrapper for a compound expression. Recursive. |
| Variable | Semantic | MayBeEntity | ForbidsContent | -- | A named mathematical variable with optional type, unit, and domain. |
| Number | Semantic | MustNotBeEntity | ForbidsContent | -- | A numeric literal with optional unit and base. |
| Operator | Semantic | MustNotBeEntity | ForbidsContent | -- | A mathematical operator token from the MathOperator set. |
| Apply | Semantic | MustNotBeEntity | ForbidsContent | Operator or expression nodes (1+, ordered) | Function/operator application. First child is the operator or function; remaining children are arguments. |
| Relation | Semantic | MustNotBeEntity | ForbidsContent | Expression nodes (2+, ordered) | A mathematical relation (equals, less-than, element-of, etc.) between two or more operands. |

### Equation

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Equation | Semantic | MayBeEntity | ForbidsContent | Relation/Apply/Expression (1+), Description, Condition | A named, cross-referenceable mathematical assertion. Classified by type (definition, identity, constraint, etc.). |

### Calculus

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Integral | Semantic | MustNotBeEntity | ForbidsContent | Integrand (1), DifferentialVariable (1), LowerBound, UpperBound, IntegrationDomain | Definite or indefinite integral over a variable. |
| Integrand | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | The expression being integrated. |
| DifferentialVariable | Semantic | MustNotBeEntity | ForbidsContent | Variable (1) | The variable of integration or differentiation. |
| Derivative | Semantic | MustNotBeEntity | ForbidsContent | Operand (1), DifferentialVariable (1+), EvaluationPoint | Ordinary or partial derivative with configurable order. |
| Summation | Semantic | MustNotBeEntity | ForbidsContent | Operand (1), IndexVariable (1), LowerBound, UpperBound | Sigma summation over an index variable. |
| Limit | Semantic | MustNotBeEntity | ForbidsContent | Operand (1), IndexVariable (1), ApproachesValue (1) | Limit of an expression as a variable approaches a value. |
| Series | Semantic | MustNotBeEntity | ForbidsContent | Operand (1), IndexVariable (1), LowerBound, UpperBound | Infinite or finite series (sum or product). |

### Linear Algebra

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Matrix | Semantic | MustNotBeEntity | ForbidsContent | MatrixRow (1+, ordered) | Matrix with typed structure (dense, diagonal, symmetric, etc.). |
| MatrixRow | Semantic | MustNotBeEntity | ForbidsContent | Expression nodes (1+, ordered) | A single row of matrix entries. |

### Set Theory

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Set | Semantic | MustNotBeEntity | ForbidsContent | Expression nodes, Condition | A mathematical set (enumerated, builder notation, or interval). |

### Piecewise

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Piecewise | Semantic | MustNotBeEntity | ForbidsContent | PiecewiseCase (1+), OtherwiseCase | Piecewise-defined function or expression. |
| PiecewiseCase | Semantic | MustNotBeEntity | ForbidsContent | Operand (1), Condition (1) | A single case with value and condition. |
| OtherwiseCase | Semantic | MustNotBeEntity | ForbidsContent | Operand (1) | Default case when no condition matches. |

### Structural Helpers

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Operand | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | Wraps a single expression node in a named role. |
| Condition | Semantic | MustNotBeEntity | ForbidsContent | Relation/Apply/Expression (1) | A boolean condition. |
| IndexVariable | Semantic | MustNotBeEntity | ForbidsContent | Variable (1) | The index variable for summation, series, or limits. |
| LowerBound | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | Lower bound of a range. |
| UpperBound | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | Upper bound of a range. |
| ApproachesValue | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | The value a limit variable approaches. |
| EvaluationPoint | Semantic | MustNotBeEntity | ForbidsContent | Expression node (1) | Point at which a derivative is evaluated. |
| IntegrationDomain | Semantic | MustNotBeEntity | ForbidsContent | Set/Variable/Expression (1) | Domain over which integration is performed. |

### Container

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| MathBlock | Semantic | MustNotBeEntity | ForbidsContent | Equation/Expression/Apply/Relation (1+), Description, Paragraph | Display-level container for one or more equations or expressions with optional prose. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Description |
|---|---|---|
| `key` | `$LookupToken` | Stable lookup key for cross-referencing. |
| `symbol` | `$Text` | Glyph representing the variable (e.g. "τ", "x", "Σ"). |
| `value` | `$Text` | Numeric value as text for arbitrary precision. |
| `unit` | `$Text` | Unit of measurement. |
| `variableType` | `$Text` | Mathematical type (e.g. "real", "integer", "complex", "vector"). |
| `domain` | `$Text` | Domain of the variable (e.g. "[0, 1]", "positive reals"). |
| `op` | `$EnumeratedToken` | Operator from MathOperator set. |
| `function` | `$Text` | Named function for Apply when not in the operator set. |
| `relationType` | `$EnumeratedToken` | Relation from MathRelation set. |
| `equationType` | `$EnumeratedToken` | Equation classification from EquationType set. |
| `label` | `$Text` | Display label. |
| `order` | `$Integer` | Derivative order. |
| `derivativeType` | `$EnumeratedToken` | Ordinary or partial. |
| `integralType` | `$EnumeratedToken` | Integral classification. |
| `direction` | `$EnumeratedToken` | Limit approach direction. |
| `seriesType` | `$EnumeratedToken` | Sum or product series. |
| `rows` | `$Integer` | Matrix row count. |
| `cols` | `$Integer` | Matrix column count. |
| `matrixType` | `$EnumeratedToken` | Matrix structure classification. |
| `setType` | `$EnumeratedToken` | Set specification method. |
| `base` | `$Integer` | Numeric base (2, 8, 10, 16, etc.). |

## Enumerated Value Sets

### MathOperator (27 members)

Arithmetic: Plus, Minus, Times, Divide, Power, Root, Modulo, Factorial, Negate. Rounding: Abs, Floor, Ceiling. Logarithmic/exponential: Log, Ln, Exp. Trigonometric: Sin, Cos, Tan. Aggregation: Min, Max, Gcd, Lcm. Set operations: Union, Intersection, SetDifference, CartesianProduct. Composition: Compose.

### MathRelation (18 members)

Equality: Equals, NotEquals. Ordering: LessThan, GreaterThan, LessOrEqual, GreaterOrEqual. Approximation: Approximates, ProportionalTo. Set membership: ElementOf, NotElementOf. Set inclusion: SubsetOf, SupersetOf, ProperSubsetOf, ProperSupersetOf. Logic: Equivalent, Congruent, Implies, Iff.

### EquationType (5 members)

Definition, Identity, Constraint, Recurrence, Differential.

### DerivativeType (2 members)

Ordinary, Partial.

### IntegralType (6 members)

Definite, Indefinite, Line, Surface, Volume, Contour.

### LimitDirection (3 members)

FromLeft, FromRight, Both.

### SeriesType (2 members)

Sum, Product.

### MatrixType (7 members)

Dense, Diagonal, Symmetric, Identity, Sparse, UpperTriangular, LowerTriangular.

### SetType (3 members)

Enumerated, BuilderNotation, Interval.

## Design Decisions

- This is a *semantic* expression tree, not a presentation tree. There are no concepts for superscript, fraction bar, or radical sign. The operator `Power` means exponentiation; the projection layer decides whether to render it as a superscript, caret notation, or `pow()` call.
- `Variable` is MayBeEntity: when used as a formal definition ("let τ denote..."), it gets an entity ID for cross-referencing. In-expression occurrences reference the defined entity.
- `Equation` is MayBeEntity for the same reason: named equations (e.g. "Equation 3.1") get entity IDs.
- `Apply` follows the MathML Content Markup model: operator/function first, operands follow in order. This is unambiguous and easy to serialize.
- Named structural helpers (Operand, Condition, IndexVariable, LowerBound, UpperBound, etc.) exist so that the tree is self-describing. A projection layer or validator finds the integrand vs. the differential variable by concept name rather than positional convention.
- `Number.value` is `$Text` not `$Integer` or `$Decimal` to support arbitrary precision, scientific notation, and non-decimal bases.
- The `function` trait on Apply handles named functions not in the MathOperator set (e.g. "Gamma", "Bessel_J", custom domain functions).
- `MathBlock` is the top-level container for embedding math in a specification section. It parallels CodeBlock, Figure, and Example as a display-level block.
