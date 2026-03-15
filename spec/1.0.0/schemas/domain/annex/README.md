Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Annex

A supplementary section of a specification or formal document with an explicit normative status — a normative annex contains binding requirements, an informative annex contains guidance.

## When to Use

Use `Annex` for supplementary sections of specifications and formal documents where the normative status must be explicit. Distinct from Appendix (a general document-structure division) — an Annex carries binding normative/informative status that governs how conformance testing interprets its content.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| annexStatus | $EnumeratedToken | yes | The normative status of the annex. |
| name | $Text | yes | The title of the annex. |
| annexDesignator | $Text | no | The letter or number identifying this annex. |

## Design Notes

- `$MustBeEntity` because annexes have stable identity and are cross-referenced by conformance classes and requirement traceability.
- `annexStatus` vocabulary: `$Normative` (contains binding requirements), `$Informative` (contains guidance only).
- `annexDesignator` carries the conventional letter identifier ("A", "B", "C").
- Distinct from Appendix: an Annex is a standards/specification construct with normative status. An Appendix is a general document-structure division.

---

**End of Annex v1.0.0**
