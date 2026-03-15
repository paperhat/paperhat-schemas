Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# DefinedTerm

A term with an authoritative definition that binds within the scope of a governing document — a contractual defined term, specification keyword, or policy term.

## When to Use

Use `DefinedTerm` for terms with authoritative definitions that bind within a governing document: contractual defined terms, specification keywords, or policy terms. Distinct from GlossaryEntry (explanatory) — a DefinedTerm creates binding meaning within its scope.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| term | $Text | yes | The term being defined. |
| scope | $Text | no | The scope within which this definition binds. |

## Design Notes

- `$MustBeEntity` because defined terms have stable identity and are cross-referenced throughout documents.
- Content carries the authoritative definition text in `$Flow` whitespace mode.
- Distinct from Definition/GlossaryEntry: a DefinedTerm binds authoritatively within its scope ("'Software' means..."). A glossary entry explains a concept for the reader's understanding.

---

**End of DefinedTerm v1.0.0**
