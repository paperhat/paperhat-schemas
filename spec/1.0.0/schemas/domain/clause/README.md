Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Clause

A single legally operative provision within a contract or agreement — an obligation, grant, limitation, indemnification, or other binding clause.

## When to Use

Use `Clause` inside a Contract to represent an individual binding provision. The clause's text content is the operative language. Clause is a semantic concept distinct from Section: a Section is structural (organizational hierarchy), while a Clause is legally operative (it creates obligations, grants rights, or limits liability). Clauses are independently referenceable ("per Clause 7.2") and carry legal meaning that sections do not.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| key | $Text | yes | The clause identifier (e.g., "7.2", "3.1.a"). |
| clauseKind | $EnumeratedToken | no | Classification token, e.g., `$Operative`, `$Grant`, `$Obligation`, `$Limitation`, `$Indemnification`, `$Termination`, `$Renewal`, `$Payment`, `$ServiceLevel`, `$Confidentiality`, `$Boilerplate`. Open vocabulary. |

## Content

Clause requires text content (`RequiresContent whitespaceMode=$Flow`). The operative legal language is the content of the Clause element, following the same pattern as Requirement, Step, and Paragraph.

## Constraints

`key` is required. A clause without an identifier cannot be cross-referenced.

## Design Notes

- `$MayBeEntity` because clauses are sometimes cross-referenced ("per Clause 7.2") and sometimes embedded without external reference.
- `RequiresContent` follows the same pattern as Requirement in the specification schema — the operative text IS the content.
- `clauseKind` absorbs what would otherwise be separate schemas for Obligation, Right, PaymentTerm, ServiceLevel, Renewal, and Termination — these are all clause types, not independent concepts.
- Pure leaf with no imports. The composing schema wires Clause as a child of Contract and can also wire subclause nesting (Clause within Clause) for hierarchical clause structures.
- Parallel to Step for Procedure: Clause is the fundamental semantic building block of a Contract.

---

**End of Clause v1.0.0**
