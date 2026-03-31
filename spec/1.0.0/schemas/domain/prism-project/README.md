Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Prism Project

Root Prism project-document composer. Defines PrismProject assembly, project-scoped source references, governance packs, review dispositions, and publication scopes above color-governance and color-policy packages.

## When to Use

Use this package to author the durable root document that Prism, terminal workflows, Lexis, and foundries consume. `paperhat-prism-project` composes governed color systems and policy objects into one project authority. It does not define retained color semantics, inner policy primitives, or derived workflow results.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| PrismProject | yes | Root Prism project authority for one governed repository. |
| GovernancePack | yes | Durable governance assembly for publication scopes and review dispositions. |
| SourceReference | yes | Stable project-scoped external source reference, such as an imported token registry or brand source. |
| ReviewDisposition | yes | Stable governance review decision that targets one entity through a typed reference. |
| PublicationScope | yes | Stable publication grouping that targets one or more entities through typed references. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| title | $Text | PrismProject | Human-readable project title. |
| prismProjectStatus | $EnumeratedToken | no | Lifecycle or governance status for a PrismProject. |
| name | $Text | GovernancePack | Human-readable governance-pack name. |
| governancePackStatus | $EnumeratedToken | no | Lifecycle or governance status for a GovernancePack. |
| key | $LookupToken | SourceReference, ReviewDisposition, PublicationScope | Stable document-scoped lookup key. |
| label | $Text | SourceReference, ReviewDisposition, PublicationScope | Human-readable display label. |
| sourceKind | $EnumeratedToken | SourceReference | Open classification for one source reference. |
| sourceLocator | $Iri | SourceReference | External locator for one source reference. |
| sourceStatus | $EnumeratedToken | no | Lifecycle or governance status for a SourceReference. |
| dispositionKind | $EnumeratedToken | ReviewDisposition | Open classification for one review disposition. |
| approvalState | $EnumeratedToken | ReviewDisposition | Governance approval state for one review disposition. |
| reviewDate | $Date | no | Date on which the review disposition was recorded. |
| reviewDispositionStatus | $EnumeratedToken | no | Lifecycle or governance status for a ReviewDisposition. |
| scopeLevel | $EnumeratedToken | PublicationScope | Intended publication scope level, such as project, color system, palette, token set, or token. |
| publicationIntent | $EnumeratedToken | PublicationScope | Intended publication target for the scope, such as CSS, application tokens, or print swatches. |
| targetMedium | $EnumeratedToken | no | Target medium for the publication scope when one medium is declared explicitly. |
| publicationScopeStatus | $EnumeratedToken | no | Lifecycle or governance status for a PublicationScope. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| PrismProject | desc:Description | `paperhat:domain:description` | Human-readable description of the project authority. |
| PrismProject | docmeta:DocumentMetadata | `paperhat:domain:document-metadata` | Optional shared document metadata. |
| PrismProject | project:Project | `paperhat:domain:project` | Optional generic project identity block. |
| PrismProject | colorgovernance:ColorSystem | `paperhat:domain:color-governance` | One or more governed color systems. |
| PrismProject | colorpolicy:AccessibilityPolicy | `paperhat:domain:color-policy` | Optional accessibility policies used by the project. |
| PrismProject | colorpolicy:ProofPolicy | `paperhat:domain:color-policy` | Optional proof policies used by the project. |
| PrismProject | SourceReference | local | Optional external source references. |
| PrismProject | GovernancePack | local | Optional durable governance assembly. |
| GovernancePack | desc:Description | `paperhat:domain:description` | Human-readable description of the governance assembly. |
| GovernancePack | PublicationScope | local | One or more stable publication scopes. |
| GovernancePack | ReviewDisposition | local | Optional stable review dispositions. |
| SourceReference | desc:Description | `paperhat:domain:description` | Human-readable description of the source reference. |
| ReviewDisposition | desc:Description | `paperhat:domain:description` | Human-readable description of the review decision. |
| ReviewDisposition | ref:Reference | `paperhat:domain:reference` | Exactly one target entity under review. |
| PublicationScope | desc:Description | `paperhat:domain:description` | Human-readable description of the publication scope. |
| PublicationScope | ref:Reference | `paperhat:domain:reference` | One or more targeted entities included in the publication scope. |

## Constraints

`PrismProject` requires at least one `ColorSystem`.

`GovernancePack` requires at least one `PublicationScope`.

`ReviewDisposition` requires exactly one `ref:Reference`.

`PublicationScope` requires at least one `ref:Reference`.

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| colorgovernance | `paperhat:domain:color-governance` | Provides durable color-system, palette, token-set, token, and semantic-role objects. |
| colorpolicy | `paperhat:domain:color-policy` | Provides authored accessibility and proof policy objects. |
| desc | `paperhat:domain:description` | Provides descriptive text for project-scoped governance objects. |
| docmeta | `paperhat:domain:document-metadata` | Provides optional shared document metadata. |
| project | `paperhat:domain:project` | Provides optional generic project identity metadata. |
| ref | `paperhat:domain:reference` | Provides stable entity references for review and publication targeting. |

## Design Notes

- `PrismProject` is the root durable authority for one Prism repository. It composes authored color systems and policy objects without duplicating their inner concept definitions.
- `GovernancePack` keeps publication scopes and review dispositions together as durable governance state. Derived audit bundles and proof bundles remain outside this package.
- `SourceReference` uses an external IRI locator rather than a local entity reference because the source often exists outside the Prism repository boundary.
- `PublicationScope` and `ReviewDisposition` target entities through imported `ref:Reference` children so the package reuses the shared Paperhat reference model instead of inventing a Prism-only reference syntax.
- `RepairSuggestion`, `Proof`, `AuditReport`, `ContrastPair`, and other derived workflow artifacts remain intentionally absent. They belong in `paperhat-prism-result-bundle`.

---

**End of Prism Project v1.0.0**
