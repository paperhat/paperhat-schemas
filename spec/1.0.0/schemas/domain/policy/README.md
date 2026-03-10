Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Policy

A named institutional policy — a set of rules, obligations, or commitments governing behavior within an organization or jurisdiction.

## When to Use

Use `Policy` to model any named policy that an organization publishes, enforces, or operates under: privacy policies, terms of use, cookie policies, licensing policies, contributor guidelines, or internal operating rules. Policy is an entity with stable identity, designed to be referenced from other schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the policy (e.g., "Privacy Policy", "Contributor License Agreement"). |
| policyKind | $EnumeratedToken | no | Classification token, e.g., `$Privacy`, `$TermsOfUse`, `$Cookie`, `$Licensing`, `$Contributor`, `$Security`, `$Acceptable­Use`. Open vocabulary. |
| policyStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Draft`, `$Active`, `$Superseded`, `$Archived`. Open vocabulary. |
| effectiveDate | $Date | no | The date the policy takes effect. |

## Children

| Child | Source | Description |
|---|---|---|
| Jurisdiction | jurisdiction (imported) | The legal or regulatory jurisdiction under which the policy applies. |

## Constraints

`name` is required. A policy without a name is ambiguous.

## Imports

| Import | Namespace | Purpose |
|---|---|---|
| paperhat-jurisdiction | jurisdiction | Provides Jurisdiction as an allowed child for scoping policies to legal boundaries. |

## Design Notes

- `$MustBeEntity` because policies have stable identity and are cross-referenced from contracts, organizations, products, and other entities.
- Jurisdiction is composed as a child rather than a reference trait because Jurisdiction is `$MustNotBeEntity` — it is a descriptor, not a standalone referenceable object.
- Individual rules, obligations, permissions, and prohibitions within a policy are expressed as structured content, not as separate schemas. The deontic categories (obligation, permission, prohibition) are authoring patterns, not domain entities.
- `effectiveDate` is `$Date` rather than importing the `temporal` package, keeping the dependency graph minimal for this leaf-level concept.

---

**End of Policy v1.0.0**
