Status: INFORMATIVE  
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Behavior Vocabulary — Color Conformance Appendix

This document provides **test vectors** for the v1.0.0 Color operator family.

This document is **Informative**.

---

## 1. Test Vector Format

Each case specifies:

- operator
- inputs
- expected output (`Valid(...)` or `Invalid([...])`)

---

## 2. Color Construction

### 2.1 `NamedColor`

| Input | Expected |
| --- | --- |
| `"red"` | `Valid(RgbColor(...))` |
| `"not-a-color-name"` | `Invalid(["Color::UNKNOWN_COLOR_NAME"])` |

### 2.2 `MakeHexColor`

| Input | Expected |
| --- | --- |
| `"#ff8800"` | `Valid(HexColor("#ff8800"))` |
| `"#xyz"` | `Invalid([...])` |

---

## 3. Format Conversion

### 3.1 `ParseColor`

| Input | Expected |
| --- | --- |
| `"rgb(255 136 0)"` | `Valid(Color(...))` |
| `"definitely not color syntax"` | `Invalid(["Color::INVALID_COLOR_STRING"])` |

### 3.2 `ColorToHexString`

| Input | Expected |
| --- | --- |
| `MakeRgbColor(255, 136, 0)` | `Valid("#ff8800")` |

---

## 4. Analysis and Guards

### 4.1 `ContrastRatio`

| Left | Right | Expected |
| --- | --- | --- |
| `NamedColor("black")` | `NamedColor("white")` | `Valid(21.0)` |

### 4.2 `IsColor`

| Input | Expected |
| --- | --- |
| `NamedColor("red")` | `Valid(true)` |
| `"red"` | `Valid(false)` |

---

**End of Color Conformance Appendix v1.0.0**
