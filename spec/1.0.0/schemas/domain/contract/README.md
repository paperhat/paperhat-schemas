Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Contract

A named binding agreement between parties — a software license, support agreement, consulting contract, partnership memorandum, or other commercial/legal commitment.

## When to Use

Use `Contract` to model any named agreement that binds parties to mutual obligations: software licenses, support agreements, consulting contracts, training agreements, partnership MOUs, or certification terms. Contract is an entity with stable identity, designed to be referenced from products, organizations, and operational records. Clause children are wired by the composing schema to provide the contract's operative provisions.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the contract (e.g., "Lexis Pro Support Agreement", "Consulting Services Agreement"). |
| contractKind | $EnumeratedToken | no | Classification token, e.g., `$License`, `$Support`, `$Consulting`, `$Training`, `$Partnership`, `$MOU`, `$LetterOfIntent`. Open vocabulary. |
| contractStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Draft`, `$Negotiating`, `$Executed`, `$Active`, `$Expired`, `$Terminated`. Open vocabulary. |
| effectiveDate | $Date | no | The date the contract takes effect. |
| expirationDate | $Date | no | The date the contract expires. |

## Children

| Child | Source | Description |
|---|---|---|
| Jurisdiction | jurisdiction (imported) | The governing legal jurisdiction under which the contract is interpreted and enforced. |

## Constraints

`name` is required. A contract without a name is ambiguous.

## Imports

| Import | Namespace | Purpose |
|---|---|---|
| paperhat-jurisdiction | jurisdiction | Provides Jurisdiction as an allowed child for governing law. |

## Design Notes

- `$MustBeEntity` because contracts have stable identity and are cross-referenced from products, organizations, support records, and invoices.
- Distinct from Policy: a policy is a unilateral declaration of rules by an organization; a contract is a bilateral or multilateral binding commitment between parties.
- `contractKind` covers the full spectrum from formal contracts to non-binding MOUs and letters of intent, eliminating the need for separate Agreement and Contract schemas.
- Clause children are wired by the composing schema, not imported here. Contract declares no child rules for Clause because Clause is a content building block (like Step for Procedure) wired by the document composer.
- `effectiveDate` and `expirationDate` are `$Date` rather than importing the `temporal` package, keeping the dependency graph minimal.

---

**End of Contract v1.0.0**
