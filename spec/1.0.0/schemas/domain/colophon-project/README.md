Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Colophon Project

Root Colophon project-document composer. Defines ColophonProject assembly, project-scoped source references, durable policy bindings, governance packs, review dispositions, and publication scopes above typography-governance and typography-policy packages.

## When to Use

Use this package to author the durable root document that Colophon, terminal workflows, Lexis, and foundries consume. `paperhat-colophon-project` composes governed typography systems, policy objects, project-local governance bindings, and typed references to derived review artifacts into one project authority. It does not define retained typography semantics, inner policy primitives, or derived workflow results.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| ColophonProject | yes | Root Colophon project authority for one governed repository. |
| GovernancePack | yes | Durable governance assembly for publication scopes and review dispositions. |
| SourceReference | yes | Stable project-scoped external source reference, such as a type foundry or brand source. |
| AccessibilityPolicyBinding | yes | Durable attachment of one typography accessibility policy to one or more governed Colophon scopes. |
| ReviewDisposition | yes | Stable governance review decision that targets one reviewable Colophon entity through a typed reference. |
| PublicationScope | yes | Stable publication grouping that targets one or more governed Colophon scopes through typed references. |
| AccessibilityPolicyReference | no | Typed reference wrapper that targets exactly one `TypographyAccessibilityPolicy`. |
| GovernedScopeReference | no | Typed reference wrapper that targets a Colophon governed scope: project, typography system, font family, font role binding, or type scale definition. |
| ReviewTargetReference | no | Typed reference wrapper that targets a reviewable Colophon entity. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| title | $Text | ColophonProject | Human-readable project title. |
| colophonProjectStatus | $EnumeratedToken | no | Lifecycle or governance status for a ColophonProject. |
| name | $Text | GovernancePack | Human-readable governance-pack name. |
| governancePackStatus | $EnumeratedToken | no | Lifecycle or governance status for a GovernancePack. |
| key | $LookupToken | SourceReference, AccessibilityPolicyBinding, ReviewDisposition, PublicationScope | Stable document-scoped lookup key. |
| label | $Text | SourceReference, AccessibilityPolicyBinding, ReviewDisposition, PublicationScope | Human-readable display label. |
| sourceKind | $EnumeratedToken | SourceReference | Source classification. Allowed values: `$DesignSource`, `$TypeFoundry`, `$BrandSource`. |
| sourceLocator | $Iri | SourceReference | External locator for one source reference. |
| sourceStatus | $EnumeratedToken | no | Lifecycle or governance status for a SourceReference. |
| dispositionKind | $EnumeratedToken | ReviewDisposition | Classification for one review disposition. |
| approvalState | $EnumeratedToken | ReviewDisposition | Governance approval state for one review disposition. |
| reviewDate | $Date | no | Date on which the review disposition was recorded. |
| reviewDispositionStatus | $EnumeratedToken | no | Lifecycle or governance status for a ReviewDisposition. |
| publicationIntent | $EnumeratedToken | PublicationScope | Intended publication target. Allowed values: `$Css`, `$ApplicationTokens`, `$PrintStyleGuide`, `$Report`, `$Governance`. |
| targetMedium | $EnumeratedToken | no | Target medium for the publication scope. Allowed values: `$Web`, `$Print`, `$Presentation`, `$Document`, `$Ebook`. |
| publicationScopeStatus | $EnumeratedToken | no | Lifecycle or governance status for a PublicationScope. |
| target | $Iri (reference trait) | AccessibilityPolicyReference, GovernedScopeReference, ReviewTargetReference | Typed reference target for Colophon project reference wrappers. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| ColophonProject | description:Description | `paperhat:domain:description` | Human-readable description of the project authority. |
| ColophonProject | documentMetadata:DocumentMetadata | `paperhat:domain:document-metadata` | Optional shared document metadata. |
| ColophonProject | project:Project | `paperhat:domain:project` | Optional generic project identity block. |
| ColophonProject | typographygovernance:TypographySystem | `paperhat:domain:typography-governance` | One or more governed typography systems. |
| ColophonProject | typographypolicy:SpacingPolicy | `paperhat:domain:typography-policy` | Optional authored spacing policies used by the project. |
| ColophonProject | typographypolicy:ParagraphPolicy | `paperhat:domain:typography-policy` | Optional authored paragraph policies used by the project. |
| ColophonProject | typographypolicy:TypographyAccessibilityPolicy | `paperhat:domain:typography-policy` | Optional authored typography accessibility policies used by the project. |
| ColophonProject | SourceReference | local | Optional external source references. |
| ColophonProject | AccessibilityPolicyBinding | local | Optional durable accessibility-policy bindings. |
| ColophonProject | GovernancePack | local | Optional durable governance assembly. |
| GovernancePack | description:Description | `paperhat:domain:description` | Human-readable description of the governance assembly. |
| GovernancePack | PublicationScope | local | One or more stable publication scopes. |
| GovernancePack | ReviewDisposition | local | Optional stable review dispositions. |
| SourceReference | description:Description | `paperhat:domain:description` | Human-readable description of the source reference. |
| AccessibilityPolicyBinding | description:Description | `paperhat:domain:description` | Human-readable description of the accessibility-policy binding. |
| AccessibilityPolicyBinding | AccessibilityPolicyReference | local | Exactly one bound typography accessibility policy. |
| AccessibilityPolicyBinding | GovernedScopeReference | local | One or more governed Colophon scopes covered by the binding. |
| ReviewDisposition | description:Description | `paperhat:domain:description` | Human-readable description of the review decision. |
| ReviewDisposition | ReviewTargetReference | local | Exactly one targeted review entity. |
| PublicationScope | description:Description | `paperhat:domain:description` | Human-readable description of the publication scope. |
| PublicationScope | GovernedScopeReference | local | One or more governed Colophon scopes included in the publication scope. |

## Constraints

| Identifier | Description |
|---|---|
| local-reference-trait-allowed-accessibility-policy | `AccessibilityPolicyReference` allows only `target` as a reference trait. |
| local-reference-trait-allowed-governed-scope | `GovernedScopeReference` allows only `target` as a reference trait. |
| local-reference-trait-allowed-review-target | `ReviewTargetReference` allows only `target` as a reference trait. |
| local-reference-singleton-accessibility-policy | `AccessibilityPolicyReference` declares at most one reference trait. |
| local-reference-singleton-governed-scope | `GovernedScopeReference` declares at most one reference trait. |
| local-reference-singleton-review-target | `ReviewTargetReference` declares at most one reference trait. |
| local-reference-must-resolve-accessibility-policy | `AccessibilityPolicyReference` resolves. |
| local-reference-must-resolve-governed-scope | `GovernedScopeReference` resolves. |
| local-reference-must-resolve-review-target | `ReviewTargetReference` resolves. |
| accessibility-policy-reference-target-type | `AccessibilityPolicyReference.target` targets `typographypolicy:TypographyAccessibilityPolicy`. |
| governed-scope-reference-target-type | `GovernedScopeReference.target` targets `ColophonProject`, `typographygovernance:TypographySystem`, `typographygovernance:FontFamily`, `typographygovernance:FontRoleBinding`, or `typographygovernance:TypeScaleDefinition`. |
| review-target-reference-target-type | `ReviewTargetReference.target` targets a reviewable Colophon entity: project, governance pack, source reference, accessibility-policy binding, publication scope, spacing policy, paragraph policy, typography accessibility policy, typography system, font family, font role binding, or type scale definition. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| typographygovernance | `paperhat:domain:typography-governance` | Provides durable typography-system, font-family, font-role-binding, and type-scale-definition objects. |
| typographypolicy | `paperhat:domain:typography-policy` | Provides authored spacing, paragraph, and typography accessibility policy objects. |
| description | `paperhat:domain:description` | Provides descriptive text for project-scoped governance objects. |
| documentMetadata | `paperhat:domain:document-metadata` | Provides optional shared document metadata. |
| project | `paperhat:domain:project` | Provides optional generic project identity metadata. |

## Design Notes

- `ColophonProject` is the root durable authority for one Colophon repository. It composes authored typography systems and policy objects without duplicating their inner concept definitions.
- Concrete policy attachment belongs in this composer package rather than in `paperhat-typography-policy`. `AccessibilityPolicyBinding` makes those attachments durable and reviewable.
- `GovernancePack` keeps publication scopes and review dispositions together as durable governance state. Derived audit bundles remain outside this package.
- `SourceReference` uses an external IRI locator rather than a local entity reference because the source often exists outside the Colophon repository boundary.
- Typed reference wrappers replace unconstrained generic entity references. Publication scopes, review dispositions, and policy bindings remain constrained to Colophon-relevant entities.

---

**End of Colophon Project v1.0.0**
