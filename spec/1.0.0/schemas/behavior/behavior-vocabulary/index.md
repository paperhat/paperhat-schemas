Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary

This specification defines the **Behavior Vocabulary** for Paperhat: the complete set of operators usable by Behavior Programs.

This document is **Normative**.

---

## 1. Purpose

This specification exists to define:

- the canonical operator inventory
- per-operator meaning, domains, and error behavior
- operator families organized by domain

This specification does not define:

- the evaluation model (see §7)

---

## 2. General Operator Contract (Normative)

For every operator defined in this vocabulary, the specification MUST include:

- **Name** — stable, human-readable, no abbreviations
- **Arity** — fixed or variadic, with minimum
- **Domains** — accepted input types
- **Result type** — output type
- **Semantics** — precise meaning
- **Error behavior** — what becomes `Invalid`, and with what diagnostic codes
- **Special cases** — empty inputs, boundary conditions

---

## 3. Operator Families (Normative)

### 3.1 Math

Comprehensive mathematical operations including:
- Basic arithmetic (Add, Subtract, Multiply, Divide)
- Complex number operations
- Rounding and precision
- Powers, roots, logarithms
- Trigonometry and hyperbolic functions
- Statistics
- Linear algebra
- Combinatorics
- Calculus (numerical)

See [math/index.md](math/index.md).

### 3.2 Core Safe Transforms

Collection and record transformation operations:
- List operations (map, filter, reduce, sort, etc.)
- Set operations (union, intersection, difference)
- Map and Record operations
- Tuple operations
- Range operations
- Join operations

See [core-safe-transforms/index.md](core-safe-transforms/index.md).

### 3.3 Text

Text manipulation operations:
- Basic operations (length, substring, concatenation)
- Searching and pattern matching
- Case transformation
- Unicode operations
- Encoding/decoding

See [text/index.md](text/index.md).

### 3.4 Temporal

Date and time operations:
- Construction and decomposition
- Temporal arithmetic
- Comparison and ordering
- Time zone operations
- Formatting and parsing

See [temporal/index.md](temporal/index.md).

### 3.5 Color

Color manipulation operations:
- Color construction
- Color space conversion
- Color manipulation (lighten, darken, mix)
- Color analysis (contrast, luminance)
- Palette operations

See [color/index.md](color/index.md).

### 3.6 Identity and Reference

Identity and reference operations:
- UUID operations
- IRI reference operations
- Lookup token operations
- Enumerated token operations

See [identity/index.md](identity/index.md).

### 3.7 Relational and Predicates

Comparison and logical operations:
- Equality operators
- Ordering operators
- Boolean composition (And, Or, Not)

See [relational-and-predicates/index.md](relational-and-predicates/index.md).

### 3.8 Data Shapes and Validation

Structural validation operations:
- Collection size predicates
- Collection membership predicates
- Record satisfaction predicates

See [data-shapes-and-validation/index.md](data-shapes-and-validation/index.md).

### 3.9 Presence and Missingness

Missingness handling operations:
- IsAbsent
- IsPresent

See [presence-and-missingness/index.md](presence-and-missingness/index.md).

---

## 4. Cross-References

All operators reference:
- **§7 Behavior Dialect** for the evaluation model and value model
- **§15 Value Ordering and Structural Equality** for comparison rules
- **§14 Behavior Diagnostics** for error codes

---

**End of Behavior Vocabulary v1.0.0**
