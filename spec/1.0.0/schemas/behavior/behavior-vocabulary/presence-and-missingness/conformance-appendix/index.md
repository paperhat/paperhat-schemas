Status: INFORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Presence and Missingness Conformance Appendix

This document provides **test vectors** for the v1.0.0 Presence and Missingness operator family.

This document is **Informative**.

---

## 1. Test Vector Format

Each case specifies:

- operator
- inputs
- expected output (`Valid(...)` or `Invalid([...])`)

---

## 2. `IsAbsent`

| Input | Expected |
| --- | --- |
| `Valid(<Absent/>)` | `Valid(true)` |
| `Valid("value")` | `Valid(false)` |
| `Invalid(["Add::AUGEND_NOT_NUMBER"])` | `Invalid(["Add::AUGEND_NOT_NUMBER"])` |

---

## 3. `IsPresent`

| Input | Expected |
| --- | --- |
| `Valid(<Absent/>)` | `Valid(false)` |
| `Valid("value")` | `Valid(true)` |
| `Invalid(["Add::AUGEND_NOT_NUMBER"])` | `Invalid(["Add::AUGEND_NOT_NUMBER"])` |

---

**End of Presence and Missingness Conformance Appendix v1.0.0**
