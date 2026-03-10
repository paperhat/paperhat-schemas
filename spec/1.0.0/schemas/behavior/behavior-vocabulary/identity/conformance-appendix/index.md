Status: INFORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Identity and Reference Conformance Appendix

This document provides **test vectors** for the v1.0.0 Identity and Reference operator family.

This document is **Informative**.

---

## 1. Test Vector Format

Each case specifies:

- operator
- inputs
- expected output (`Valid(...)` or `Invalid([...])`)

---

## 2. UUID Operations

### 2.1 `MakeUuid`

| Input | Expected |
| --- | --- |
| `"550e8400-e29b-41d4-a716-446655440000"` | `Valid(Uuid("550e8400-e29b-41d4-a716-446655440000"))` |
| `"not-a-uuid"` | `Invalid(["Identity::INVALID_UUID"])` |

### 2.2 `IsNilUuid`

| Input | Expected |
| --- | --- |
| `NilUuid()` | `Valid(true)` |
| `MakeUuid("550e8400-e29b-41d4-a716-446655440000")` | `Valid(false)` |

---

## 3. IRI Reference Operations

### 3.1 `MakeIriReference`

| Input | Expected |
| --- | --- |
| `"https://paperhat.dev/spec"` | `Valid(IriReference("https://paperhat.dev/spec"))` |
| `":://bad"` | `Invalid(["Identity::INVALID_IRI"])` |

### 3.2 `IsAbsoluteIri`

| Input | Expected |
| --- | --- |
| `MakeIriReference("https://paperhat.dev/spec")` | `Valid(true)` |
| `MakeIriReference("/relative/path")` | `Valid(false)` |

---

## 4. Token Operations

### 4.1 `MakeLookupToken`

| Input | Expected |
| --- | --- |
| `"primaryLabel"` | `Valid(LookupToken("~primaryLabel"))` |
| `"PrimaryLabel"` | `Invalid(["Identity::INVALID_LOOKUP_TOKEN"])` |

### 4.2 `MakeEnumeratedToken`

| Input | Expected |
| --- | --- |
| `"InStock"` | `Valid(EnumeratedToken("$InStock"))` |
| `"in stock"` | `Invalid(["Identity::INVALID_ENUMERATED_TOKEN"])` |

---

**End of Identity and Reference Conformance Appendix v1.0.0**
