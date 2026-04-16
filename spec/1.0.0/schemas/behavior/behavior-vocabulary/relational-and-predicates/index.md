Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Relational and Predicates

This specification defines the v1.0.0 **Relational and predicate operator family** for the Behavior Vocabulary.

This document is **Normative**.

---

## 1. Purpose

This family covers:

- equality over Behavior values
- ordering over the comparable domains
- boolean predicate composition

All operators in this family are **core operators** whose canonical definitions are in the Lexis Specification §7 (Behavior Dialect). This document enumerates the family membership and references the defining sections.

---

## 2. Operator Inventory

### 2.1 Equality Operators

| Operator | Canonical Definition |
|----------|---------------------|
| `IsEqualTo` | §7.13.1 |
| `IsUnequalTo` | §7.13.2 |

### 2.2 Ordering Operators

| Operator | Canonical Definition |
|----------|---------------------|
| `IsLessThan` | §7.13.3 |
| `IsGreaterThan` | §7.13.3 |
| `IsLessThanOrEqualTo` | §7.13.3 |
| `IsGreaterThanOrEqualTo` | §7.13.3 |

### 2.3 Boolean Predicate Composition

| Operator | Canonical Definition |
|----------|---------------------|
| `Not` | §7.12.1 |
| `And` | §7.12.2 |
| `Or` | §7.12.3 |
| `Xor` | §7.12.4 |
| `Ternary` | §7.12.5 |

---

## 3. Shared Rules

- Evaluation contract, structural equality, ordering comparability, and diagnostic codes are governed by the Behavior Dialect (§7) and Value Ordering and Structural Equality (§15).
- Diagnostic codes are defined in Behavior Diagnostics (§14).

---

## 4. Conformance Appendix (Informative)

See [conformance-appendix/index.md](conformance-appendix/index.md).

---

**End of Behavior Vocabulary — Relational and Predicates v1.0.0**
