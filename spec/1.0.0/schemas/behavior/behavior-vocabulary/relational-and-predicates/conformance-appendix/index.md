Status: INFORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Relational and Predicates Conformance Appendix

This document provides **test vectors** for the v1.0.0 Relational and Predicates operator family.

This document is **Informative**.

---

## 1. Test Vector Format

Each case specifies:

- operator
- inputs
- expected output (`Valid(...)` or `Invalid([...])`)

---

## 2. Equality

### 2.1 `IsEqualTo`

| Left | Right | Expected |
| --- | --- | --- |
| `Integer(3)` | `Integer(3)` | `Valid(true)` |
| `Integer(3)` | `Integer(4)` | `Valid(false)` |

### 2.2 `IsUnequalTo`

| Left | Right | Expected |
| --- | --- | --- |
| `Integer(3)` | `Integer(4)` | `Valid(true)` |
| `Integer(3)` | `Integer(3)` | `Valid(false)` |

---

## 3. Ordering

### 3.1 `IsLessThan`

| Left | Right | Expected |
| --- | --- | --- |
| `Integer(1)` | `Integer(2)` | `Valid(true)` |
| `Integer(2)` | `Integer(1)` | `Valid(false)` |

### 3.2 `IsNoMoreThan`

| Left | Right | Expected |
| --- | --- | --- |
| `Integer(2)` | `Integer(2)` | `Valid(true)` |
| `Integer(3)` | `Integer(2)` | `Valid(false)` |

---

## 4. Boolean Composition

### 4.1 `And`

| Left | Right | Expected |
| --- | --- | --- |
| `true` | `true` | `Valid(true)` |
| `true` | `false` | `Valid(false)` |

### 4.2 `Not`

| Input | Expected |
| --- | --- |
| `true` | `Valid(false)` |
| `false` | `Valid(true)` |

---

**End of Relational and Predicates Conformance Appendix v1.0.0**
