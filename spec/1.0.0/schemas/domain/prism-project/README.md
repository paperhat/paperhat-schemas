Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Prism Project

Root Prism project-document composer. Defines PrismProject assembly, project-scoped source references, durable policy bindings, governance packs, review dispositions, and publication scopes above color-governance and color-policy packages.

## When to Use

Use this package to author the durable root document that Prism, terminal workflows, Lexis, and foundries consume. `paperhat-prism-project` composes governed color systems, policy objects, and project-local governance bindings into one project authority. It does not define retained color semantics, inner policy primitives, or derived workflow results.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| PrismProject | yes | Root Prism project authority for one governed repository. |
| GovernancePack | yes | Durable governance assembly for publication scopes and review dispositions. |
| SourceReference | yes | Stable project-scoped external source reference, such as an imported token registry or brand source. |
| AccessibilityPolicyBinding | yes | Durable attachment of one accessibility policy to one or more governed Prism scopes. |
| ProofPolicyBinding | yes | Durable attachment of one proof policy to one or more governed Prism scopes. |
| ReviewDisposition | yes | Stable governance review decision that targets one reviewable Prism entity through a typed local reference. |
| PublicationScope | yes | Stable publication grouping that targets one or more governed Prism scopes through typed local references. |
| AccessibilityPolicyReference | no | Typed reference wrapper that targets exactly one `AccessibilityPolicy`. |
| ProofPolicyReference | no | Typed reference wrapper that targets exactly one `ProofPolicy`. |
| GovernedScopeReference | no | Typed reference wrapper that targets a Prism governed scope: project, color system, palette, token set, or token. |
| ReviewTargetReference | no | Typed reference wrapper that targets a reviewable Prism entity. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| title | $Text | PrismProject | Human-readable project title. |
| prismProjectStatus | $EnumeratedToken | no | Lifecycle or governance status for a PrismProject. |
| name | $Text | GovernancePack | Human-readable governance-pack name. |
| governancePackStatus | $EnumeratedToken | no | Lifecycle or governance status for a GovernancePack. |
| key | $LookupToken | SourceReference, AccessibilityPolicyBinding, ProofPolicyBinding, ReviewDisposition, PublicationScope | Stable document-scoped lookup key. |
| label | $Text | SourceReference, AccessibilityPolicyBinding, ProofPolicyBinding, ReviewDisposition, PublicationScope | Human-readable display label. |
| sourceKind | $EnumeratedToken | SourceReference | Source classification. Allowed values: `$DesignSource`, `$TokenRegistry`, `$BrandSource`. |
| sourceLocator | $Iri | SourceReference | External locator for one source reference. |
| sourceStatus | $EnumeratedToken | no | Lifecycle or governance status for a SourceReference. |
| dispositionKind | $EnumeratedToken | ReviewDisposition | Classification for one review disposition. |
| approvalState | $EnumeratedToken | ReviewDisposition | Governance approval state for one review disposition. |
| reviewDate | $Date | no | Date on which the review disposition was recorded. |
| reviewDispositionStatus | $EnumeratedToken | no | Lifecycle or governance status for a ReviewDisposition. |
| scopeLevel | $EnumeratedToken | PublicationScope | Intended publication scope level. Allowed values: `$Project`, `$ColorSystem`, `$Palette`, `$TokenSet`, `$Token`. |
| publicationIntent | $EnumeratedToken | PublicationScope | Intended publication target. Allowed values: `$Css`, `$ApplicationTokens`, `$PrintSwatches`, `$Proof`, `$Report`, `$Governance`. |
| targetMedium | $EnumeratedToken | no | Target medium for the publication scope when one medium is declared explicitly. |
| publicationScopeStatus | $EnumeratedToken | no | Lifecycle or governance status for a PublicationScope. |
| target | $Iri (reference trait) | AccessibilityPolicyReference, ProofPolicyReference, GovernedScopeReference, ReviewTargetReference | Typed reference target for local Prism reference wrappers. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| PrismProject | description:Description | `paperhat:domain:description` | Human-readable description of the project authority. |
| PrismProject | documentMetadata:DocumentMetadata | `paperhat:domain:document-metadata` | Optional shared document metadata. |
| PrismProject | project:Project | `paperhat:domain:project` | Optional generic project identity block. |
| PrismProject | colorgovernance:ColorSystem | `paperhat:domain:color-governance` | One or more governed color systems. |
| PrismProject | colorpolicy:AccessibilityPolicy | `paperhat:domain:color-policy` | Optional authored accessibility policies used by the project. |
| PrismProject | colorpolicy:ProofPolicy | `paperhat:domain:color-policy` | Optional authored proof policies used by the project. |
| PrismProject | SourceReference | local | Optional external source references. |
| PrismProject | AccessibilityPolicyBinding | local | Optional durable accessibility-policy bindings. |
| PrismProject | ProofPolicyBinding | local | Optional durable proof-policy bindings. |
| PrismProject | GovernancePack | local | Optional durable governance assembly. |
| GovernancePack | description:Description | `paperhat:domain:description` | Human-readable description of the governance assembly. |
| GovernancePack | PublicationScope | local | One or more stable publication scopes. |
| GovernancePack | ReviewDisposition | local | Optional stable review dispositions. |
| SourceReference | description:Description | `paperhat:domain:description` | Human-readable description of the source reference. |
| AccessibilityPolicyBinding | description:Description | `paperhat:domain:description` | Human-readable description of the accessibility-policy binding. |
| AccessibilityPolicyBinding | AccessibilityPolicyReference | local | Exactly one bound accessibility policy. |
| AccessibilityPolicyBinding | GovernedScopeReference | local | One or more governed Prism scopes covered by the binding. |
| ProofPolicyBinding | description:Description | `paperhat:domain:description` | Human-readable description of the proof-policy binding. |
| ProofPolicyBinding | ProofPolicyReference | local | Exactly one bound proof policy. |
| ProofPolicyBinding | GovernedScopeReference | local | One or more governed Prism scopes covered by the binding. |
| ReviewDisposition | description:Description | `paperhat:domain:description` | Human-readable description of the review decision. |
| ReviewDisposition | ReviewTargetReference | local | Exactly one targeted review entity. |
| PublicationScope | description:Description | `paperhat:domain:description` | Human-readable description of the publication scope. |
| PublicationScope | GovernedScopeReference | local | One or more governed Prism scopes included in the publication scope. |

## Constraints

| Identifier | Description |
|---|---|
| local-reference-trait-allowed-accessibility-policy | `AccessibilityPolicyReference` allows only `target` as a reference trait. |
| local-reference-trait-allowed-proof-policy | `ProofPolicyReference` allows only `target` as a reference trait. |
| local-reference-trait-allowed-governed-scope | `GovernedScopeReference` allows only `target` as a reference trait. |
| local-reference-trait-allowed-review-target | `ReviewTargetReference` allows only `target` as a reference trait. |
| local-reference-singleton-accessibility-policy | `AccessibilityPolicyReference` declares at most one reference trait. |
| local-reference-singleton-proof-policy | `ProofPolicyReference` declares at most one reference trait. |
| local-reference-singleton-governed-scope | `GovernedScopeReference` declares at most one reference trait. |
| local-reference-singleton-review-target | `ReviewTargetReference` declares at most one reference trait. |
| local-reference-must-resolve-accessibility-policy | `AccessibilityPolicyReference` resolves. |
| local-reference-must-resolve-proof-policy | `ProofPolicyReference` resolves. |
| local-reference-must-resolve-governed-scope | `GovernedScopeReference` resolves. |
| local-reference-must-resolve-review-target | `ReviewTargetReference` resolves. |
| accessibility-policy-reference-target-type | `AccessibilityPolicyReference.target` targets `colorpolicy:AccessibilityPolicy`. |
| proof-policy-reference-target-type | `ProofPolicyReference.target` targets `colorpolicy:ProofPolicy`. |
| governed-scope-reference-target-type | `GovernedScopeReference.target` targets `PrismProject`, `colorgovernance:ColorSystem`, `colorgovernance:Palette`, `colorgovernance:TokenSet`, or `colorgovernance:Token`. |
| review-target-reference-target-type | `ReviewTargetReference.target` targets a reviewable Prism entity: project, governance pack, source reference, policy binding, publication scope, authored policy, color system, palette member, token set, token, or semantic role. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| colorgovernance | `paperhat:domain:color-governance` | Provides durable color-system, palette, token-set, token, and semantic-role objects. |
| colorpolicy | `paperhat:domain:color-policy` | Provides authored accessibility and proof policy objects. |
| description | `paperhat:domain:description` | Provides descriptive text for project-scoped governance objects. |
| documentMetadata | `paperhat:domain:document-metadata` | Provides optional shared document metadata. |
| project | `paperhat:domain:project` | Provides optional generic project identity metadata. |

## Design Notes

- `PrismProject` is the root durable authority for one Prism repository. It composes authored color systems and policy objects without duplicating their inner concept definitions.
- Concrete policy attachment belongs in this composer package rather than in `paperhat-color-policy`. `AccessibilityPolicyBinding` and `ProofPolicyBinding` make those attachments durable and reviewable.
- `GovernancePack` keeps publication scopes and review dispositions together as durable governance state. Derived audit bundles and proof bundles remain outside this package.
- `SourceReference` uses an external IRI locator rather than a local entity reference because the source often exists outside the Prism repository boundary.
- Typed local reference wrappers replace unconstrained generic entity references. Publication scopes, review dispositions, and policy bindings remain constrained to Prism-relevant entities.
- `RepairSuggestion`, `Proof`, `AuditReport`, `ContrastPair`, and other derived workflow artifacts remain intentionally absent. They belong in `paperhat-prism-result-bundle`.

---

**End of Prism Project v1.0.0**
