Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Procedure

A named, ordered sequence of steps that accomplishes a specific operational task — a release procedure, deployment workflow, or setup guide.

## When to Use

Use `Procedure` to model any repeatable, step-by-step process: release procedures, deployment workflows, onboarding checklists, build instructions, or troubleshooting runbooks. Procedure is an entity with stable identity, designed to be referenced from documentation, products, and organizational records. A composing schema wires Step children into Procedure to create the ordered instruction sequence.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the procedure (e.g., "Release Procedure", "Production Deployment Workflow"). |
| procedureKind | $EnumeratedToken | no | Classification token, e.g., `$Release`, `$Deployment`, `$Setup`, `$Troubleshooting`, `$Maintenance`, `$Onboarding`. Open vocabulary. |
| procedureStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Draft`, `$Active`, `$Deprecated`, `$Archived`. Open vocabulary. |

## Constraints

`name` is required. A procedure without a name is ambiguous.

## Design Notes

- `$MustBeEntity` because procedures have stable identity and are cross-referenced from documentation, release notes, and operational records.
- `ForbidsContent` because Procedure is a structural container. Step children (and other content concepts) are wired in by the composing schema, following the same pattern as Narrative composing Section and Paragraph.
- Pure leaf with no imports. The composing schema imports both Procedure and Step (and any other content concepts) and declares the child rules.
- Distinct from Work: a Work is a creative/intellectual artifact; a Procedure is an executable instruction set. The distinction is semantic, not structural.

---

**End of Procedure v1.0.0**
