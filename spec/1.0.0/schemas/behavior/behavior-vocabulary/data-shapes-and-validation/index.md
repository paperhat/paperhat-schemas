Status: NORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Data Shapes and Validation

This specification defines the v1.0.0 **Data shapes and validation** family for the Behavior Vocabulary.

This document is **Normative**.

---

## 1. Purpose

This family provides deterministic, runtime-neutral predicates for validating collection shapes.

Naming conventions and totality rules for these predicates follow §16 (Predicate Guard and Validation Composition).

---

## 2. Shared Definitions (Normative)

### 2.1 Evaluation contract

- Each operand is a Behavior expression evaluated to `Validation<Value>`.
- Unless explicitly stated otherwise, if any operand evaluates to `Invalid(...)`, the operator result MUST be `Invalid(...)` (propagation).

### 2.2 Predicate totality policy (Normative)

Unless explicitly stated otherwise, operators in this family are *total predicates*:

- If an operand evaluates to `Valid(<Absent/>)`, the result MUST be `Valid(false)`.
- If an operand evaluates to `Valid(x)` where `x` is not in the required domain, the result MUST be `Valid(false)`.

This matches the v1.0.0 predicate totality rule used by the validation surface.

### 2.3 Equality and membership

All equality-dependent behavior (element membership, key membership, distinctness) MUST use structural equality as defined by §15 (Value Ordering and Structural Equality).

---

## 3. Collection Size Predicates (Normative)

For these predicates, `count(list)` is the number of elements in the list.

### 3.1 `HasElementCountEqualTo`

Arity: 2

Signature:

- `HasElementCountEqualTo(list, n) -> Validation<boolean>`

Semantics:

- If `list` is not a `List`, return `Valid(false)`.
- If `n` is not an `Integer`, return `Valid(false)`.
- If `n < 0`, return `Valid(false)`.
- Otherwise return `Valid(count(list) == n)`.

### 3.2 `HasElementCountAtLeast`

Arity: 2

- Same domain rules as `HasElementCountEqualTo`.
- Return `Valid(count(list) >= n)`.

### 3.3 `HasElementCountAtMost`

Arity: 2

- Same domain rules as `HasElementCountEqualTo`.
- Return `Valid(count(list) <= n)`.

### 3.4 `HasElementCountBetweenInclusive`

Arity: 3

Signature:

- `HasElementCountBetweenInclusive(list, min, max) -> Validation<boolean>`

Semantics:

- If `list` is not a `List`, return `Valid(false)`.
- If `min` or `max` is not an `Integer`, return `Valid(false)`.
- If `min < 0` or `max < 0`, return `Valid(false)`.
- If `min > max`, return `Valid(false)`.
- Otherwise return `Valid(min <= count(list) <= max)`.

---

## 4. Element Membership Predicates (Normative)

### 4.1 `ContainsElement`

Arity: 2

Signature:

- `ContainsElement(list, element) -> Validation<boolean>`

Semantics:

- If `list` is not a `List`, return `Valid(false)`.
- Otherwise return `Valid(true)` iff `element` is structurally equal to some element of `list`.

### 4.2 `DoesNotContainElement`

Arity: 2

- Same domain rules as `ContainsElement`.
- Return `Valid(!ContainsElement(list, element))`.

---

## 5. Record Key Predicates (Normative)

### 5.1 `ContainsKey`

Arity: 2

Signature:

- `ContainsKey(record, key) -> Validation<boolean>`

Semantics:

- If `record` is not a `Record`, return `Valid(false)`.
- If `key` is not `Text`, return `Valid(false)`.
- Otherwise return `Valid(true)` iff `record` has a key equal to `key`.

### 5.2 `DoesNotContainKey`

Arity: 2

- Same domain rules as `ContainsKey`.
- Return `Valid(!ContainsKey(record, key))`.

---

## 6. Higher-Order Shape Predicates (Normative)

These operators evaluate a boolean predicate per key or per value.

### 6.1 `AllKeysSatisfy`

Arity: 2

Signature:

- `AllKeysSatisfy(recordExpr, predicateExpr) -> Validation<boolean>`

Domains:

- `recordExpr` MUST evaluate to `Valid(Record)`.
- `predicateExpr` MUST be a Behavior expression evaluated once per key, with `Argument := key`.

Semantics:

1. Evaluate `recordExpr`.
2. For each key `k` in the record (in the record's canonical key order defined by §15):
   - evaluate `predicateExpr` with `Argument := Text(k)`.
   - if the result is `Valid(false)`, return `Valid(false)`.
3. If all evaluations are `Valid(true)`, return `Valid(true)`.

Error behavior:

- If `recordExpr` is not a `Record`, return `Invalid(...)` with code `AllKeysSatisfy::NEED_RECORD`.
- If any predicate evaluation yields `Invalid(...)`, return `Invalid(...)`.
- If any predicate evaluation yields `Valid(x)` where `x` is not `Boolean`, return `Invalid(...)` with code `AllKeysSatisfy::NEED_BOOLEAN`.

Observability constraint:

- `predicateExpr` MUST be evaluated exactly once per key.

### 6.2 `AllValuesSatisfy`

Arity: 2

Signature:

- `AllValuesSatisfy(recordExpr, predicateExpr) -> Validation<boolean>`

Domains:

- `recordExpr` MUST evaluate to `Valid(Record)`.
- `predicateExpr` MUST be a Behavior expression evaluated once per value, with `Argument := value`.

Semantics:

1. Evaluate `recordExpr`.
2. For each key in the record (in the record's canonical key order), evaluate `predicateExpr` with `Argument := record[key]`.
3. If any evaluation is `Valid(false)`, return `Valid(false)`.
4. If all evaluations are `Valid(true)`, return `Valid(true)`.

Error behavior:

- If `recordExpr` is not a `Record`, return `Invalid(...)` with code `AllValuesSatisfy::NEED_RECORD`.
- If any predicate evaluation yields `Invalid(...)`, return `Invalid(...)`.
- If any predicate evaluation yields `Valid(x)` where `x` is not `Boolean`, return `Invalid(...)` with code `AllValuesSatisfy::NEED_BOOLEAN`.

Observability constraint:

- `predicateExpr` MUST be evaluated exactly once per value.

---

## 7. Relationship to Other Specifications

- Naming conventions and totality policy: §16 (Predicate Guard and Validation Composition).
- Equality and ordering rules: §15 (Value Ordering and Structural Equality).

---

## 8. Conformance Appendix (Informative)

See [conformance-appendix/index.md](conformance-appendix/index.md).

---

## 9. Diagnostic Code Table (Normative)

This table consolidates all diagnostic codes defined in the Data Shapes and Validation operator family. Operators in §3–§5 are total predicates that return `Valid(false)` for out-of-domain inputs and produce no diagnostics.

| Code | Operators | Expected | Message | Suggestion |
|------|-----------|----------|---------|------------|
| `AllKeysSatisfy::NEED_RECORD` | AllKeysSatisfy | Record | "Lexis expected a record for the first operand, but found {received}." | "Please provide a record value — AllKeysSatisfy iterates over record keys." |
| `AllKeysSatisfy::NEED_BOOLEAN` | AllKeysSatisfy | Boolean predicate result | "Lexis expected the predicate to return true or false, but it returned {received}." | "You might check that the predicate expression evaluates to a boolean value." |
| `AllValuesSatisfy::NEED_RECORD` | AllValuesSatisfy | Record | "Lexis expected a record for the first operand, but found {received}." | "Please provide a record value — AllValuesSatisfy iterates over record values." |
| `AllValuesSatisfy::NEED_BOOLEAN` | AllValuesSatisfy | Boolean predicate result | "Lexis expected the predicate to return true or false, but it returned {received}." | "You might check that the predicate expression evaluates to a boolean value." |

---

**End of Behavior Vocabulary — Data Shapes and Validation v1.0.0**
