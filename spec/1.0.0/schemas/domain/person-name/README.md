Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# PersonName

A structured personal name with support for cultural variants, multiple name kinds, and decomposed name parts.

**Package:** `paperhat-person-name`
**Schema ID:** `paperhat:domain:person-name`

---

## When to Use

Use PersonName whenever you need to represent a person's name in a structured way. A single Person has multiple PersonName instances to capture legal names, birth names, preferred names, aliases, stage names, religious names, and other variants.

PersonName is a leaf concept with no concept dependencies. It is designed to be composed into higher-level schemas such as Person.

---

## Traits

### nameKind

A token classifying the role this name plays. Common values include `$Legal`, `$Birth`, `$Preferred`, `$Maiden`, `$Married`, `$Stage`, `$Pen`, `$Religious`, `$Alias`, `$Regnal`.

This is an open vocabulary. The consuming schema constrains which values are accepted.

### full

The complete name as a single unstructured string. Use this when the name is not decomposable into parts (mononyms, names in unfamiliar scripts, names where decomposition loses meaning).

Examples: `full="Pelé"`, `full="Prince"`, `full="Banksy"`.

### given

The given (first) name.

### middle

An ordered list of middle names. Order matters, and duplicates are permitted.

### family

The family (last or surname) name.

### title

An ordered list of titles preceding the name, for example `"Dr."`, `"Professor"`, `"The Honourable"`.

### honorific

An ordered list of honorifics, for example `"Sir"`, `"Dame"`, `"Saint"`.

### suffix

An ordered list of suffixes following the name, for example `"Jr."`, `"III"`, `"PhD"`, `"OBE"`.

### effectiveFrom / effectiveTo

Date values defining the period during which this name is valid. Useful for tracking legal name changes, married names, or regnal names.

A name with no dates is assumed to be current and unbounded.

---

## Constraints

At least one of `full`, `given`, or `family` must be present. A PersonName with only metadata (`nameKind`, dates) and no actual name content is invalid.

---

## Design Notes

**Why PersonName and not Name?** The structure of this schema is specific to personal names. An organization name, a place name, or a product name has different decomposition. The concept is named for what it models.

**Why `$List<$Text>` for middle, title, honorific, suffix?** Order matters and duplicates are possible. `$List<$Text>` preserves both.

**Why is nameKind an $EnumeratedToken?** Name kinds vary across cultures and contexts. A closed enumeration is incomplete. The token vocabulary is open; consuming schemas constrain it as needed.

**Why effectiveFrom/effectiveTo?** Names change. A person's birth name, married name, and legal name all have different validity periods. Temporal traits allow precise biographical modeling.

---

**End of PersonName v1.0.0**
