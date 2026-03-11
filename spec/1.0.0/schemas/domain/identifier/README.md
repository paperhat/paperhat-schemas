Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Identifier

A scheme-qualified identifier for referencing external systems, standards, or registries.

**Package:** `paperhat-identifier`
**Schema ID:** `paperhat:domain:identifier`

---

## When to Use

Use Identifier whenever you need to attach an external reference to an entity. A Person might carry a passport number, an ISBN identifies a book, a DOI identifies a research paper. The Identifier concept pairs a scheme with a value, making the namespace explicit.

Identifier is a leaf concept with no concept dependencies. It is designed to be composed into higher-level schemas such as Person, Organization, or any entity that needs external identification.

---

## Traits

### scheme

**Required.** A token identifying the namespace or registry this identifier belongs to. Common values include `$isbn`, `$doi`, `$orcid`, `$passport`, `$ssn`, `$driverLicense`, `$nationalId`, `$ean`, `$issn`, `$oclc`.

This is an open vocabulary — any token value is valid. The consuming schema (such as Person or Product) may constrain which schemes are accepted.

### value

**Required.** The identifier string within the scheme. Format and validation rules are determined by the scheme, not by this schema.

---

## Constraints

Both `scheme` and `value` are required. An Identifier without a scheme is ambiguous; an Identifier without a value is empty.

---

## Design Notes

**Why are both traits required?** A value without a scheme is meaningless — "978-0-14-028329-7" could be anything without knowing it's an ISBN. A scheme without a value is empty. Both must be present.

**Who defines the schemes?** Nobody, yet. Scheme tokens correspond to external standards and registries. The Identifier leaf keeps the vocabulary open; consuming schemas constrain which schemes they accept. A Person schema might allow `$passport` and `$ssn`; a Book schema might allow `$isbn` and `$doi`. This follows the pattern: leaves are open, composers constrain.

**Why $EnumeratedToken for scheme?** Tokens are machine-readable classifiers. They use the `$` prefix in instance data (e.g., `scheme=$isbn`) and signal a controlled vocabulary without requiring a closed enumeration.

**End of Identifier v1.0.0**
