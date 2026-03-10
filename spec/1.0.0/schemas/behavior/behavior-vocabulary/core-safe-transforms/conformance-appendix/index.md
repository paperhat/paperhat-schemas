Status: INFORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Core Safe Transforms Conformance Appendix

This document provides **test vectors** for the v1.0.0 Core Safe Transforms operator family.

This document is **Informative**.

---

## 1. Test Vector Format

Each case specifies:

- operator
- inputs
- expected output (`Valid(...)` or `Invalid([...])`)

---

## 2. List Operations

### 2.1 `MapElements`

| Input List | Mapping | Expected |
| --- | --- | --- |
| `[1, 2, 3]` | `x -> x + 1` | `Valid([2, 3, 4])` |
| `"not-a-list"` | `x -> x` | `Invalid(["MapElements::NEED_LIST"])` |

### 2.2 `FilterElements`

| Input List | Predicate | Expected |
| --- | --- | --- |
| `[1, 2, 3, 4]` | `x -> IsEqualTo(Modulo(x, 2), 0)` | `Valid([2, 4])` |
| `[1, 2]` | `x -> "not-boolean"` | `Invalid(["FilterElements::NEED_BOOLEAN"])` |

### 2.3 `FoldElements`

| Input List | Fold | Expected |
| --- | --- | --- |
| `[1, 2, 3]` | `(a, b) -> a + b` | `Valid(6)` |
| `[]` | `(a, b) -> a + b` | `Invalid(["FoldElements::NEED_NONEMPTY_LIST"])` |

---

## 3. Ordering and Shape

### 3.1 `SortElements`

| Input List | Expected |
| --- | --- |
| `[3, 1, 2]` | `Valid([1, 2, 3])` |
| `[1, "x"]` | `Invalid(["SortElements::NEED_COMPARABLE_ELEMENTS"])` |

### 3.2 `FlattenElements`

| Input | Expected |
| --- | --- |
| `[[1, 2], [3]]` | `Valid([1, 2, 3])` |
| `[1, [2, 3]]` | `Invalid(["FlattenElements::NEED_LIST_ELEMENTS"])` |

---

## 4. String Operations

### 4.1 `SplitString`

| Input Text | Separator | Expected |
| --- | --- | --- |
| `"a,b,c"` | `","` | `Valid(["a", "b", "c"])` |
| `"abc"` | `""` | `Invalid(["SplitString::NEED_NONEMPTY_SEPARATOR"])` |

### 4.2 `JoinStrings`

| Input List | Separator | Expected |
| --- | --- | --- |
| `["a", "b", "c"]` | `"-"` | `Valid("a-b-c")` |
| `["a", 2, "c"]` | `"-"` | `Invalid(["JoinStrings::NEED_TEXT_ELEMENTS"])` |

---

**End of Core Safe Transforms Conformance Appendix v1.0.0**
