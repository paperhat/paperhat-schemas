Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Color Policy

Authored accessibility and proof policy objects for Prism. Defines accessibility policies, ordered policy rules, proof policies, proof targets, and Delta E 94 application constants.

## When to Use

Use this package to author durable rule objects that govern accessibility evaluation and target-medium proofing for Prism. `paperhat-color-policy` defines the policy objects themselves. It projects the exact lower-layer `PolicyRule` and `ProofTarget` semantics as authored documents. It does not bind those policies to a specific project object by reference, and it does not contain derived repair suggestions, proofs, or audit bundles.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| AccessibilityPolicy | yes | First-class authored accessibility policy carrying ordered `PolicyRule` children. |
| PolicyRule | no | Exact authored accessibility rule carrying one exact rule identifier and zero or more ordered parameter entries. |
| NamedValueEntry | no | Exact ordered parameter entry for one `PolicyRule`. |
| ProofPolicy | yes | First-class authored proof policy carrying ordered `ProofTarget` children. |
| ProofTarget | yes | Stable authored proof target carrying the exact strengthened proof-target field surface. |
| DeltaE94ApplicationConstants | no | Exact Delta E 94 application-constant triple for one `ProofTarget`. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| name | $Text | AccessibilityPolicy, ProofPolicy | Human-readable policy name. |
| accessibilityPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for an accessibility policy. |
| policyRuleIdentifier | $Text | PolicyRule | Exact policy-rule identifier. Admitted exact values: `minimum-apca-lc`, `minimum-wcag-contrast-ratio`, `require-distinction-preservation`, `require-state-exposure`, `require-consequence-exposure`, `require-no-color-alone-risk`. |
| entryName | $Text | NamedValueEntry | Exact policy-rule parameter name. Admitted exact values: `minimumApcaLc`, `minimumWcagContrastRatio`. |
| entryValue | $FiniteRealNumber | NamedValueEntry | Exact finite decimal parameter value. |
| proofPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for a proof policy. |
| proofTargetIdentifier | $Text | ProofTarget | Exact proof target identifier. |
| proofMedium | $EnumeratedToken | ProofTarget | Declared proof medium. Allowed values: `$Web`, `$Print`, `$Presentation`, `$Document`, `$Ebook`. |
| targetProfileIdentifier | $Text | ProofTarget | Exact target profile identifier. |
| label | $Text | ProofTarget | Human-readable display label. |
| proofGamutMappingMode | $EnumeratedToken | ProofTarget | Exact authored gamut-mapping mode. Allowed values: `$Reject`, `$ClipToOutputSpace`, `$ChromaReduction`, `$Perceptual`. |
| proofComparisonMode | $EnumeratedToken | ProofTarget | Exact authored comparison mode. Allowed values: `$None`, `$RetainedDeltaE`, `$RenderedArtifact`, `$RetainedDeltaEAndRenderedArtifact`. |
| renderingIntent | $EnumeratedToken | ProofTarget | Exact authored rendering intent. Allowed values: `$RelativeColorimetric`, `$AbsoluteColorimetric`, `$Perceptual`, `$Saturation`. |
| retainedComparisonMetric | $Text | no | Exact retained Delta E metric. Admitted exact values: `76`, `94`, `2000`, `Ok`. |
| retainedComparisonTolerance | $FiniteRealNumber | no | Exact retained-comparison tolerance. |
| proofTargetStatus | $EnumeratedToken | no | Lifecycle or governance status for a proof target. |
| kL | $FiniteRealNumber | DeltaE94ApplicationConstants | Exact Delta E 94 `kL` application constant. |
| k1 | $FiniteRealNumber | DeltaE94ApplicationConstants | Exact Delta E 94 `k1` application constant. |
| k2 | $FiniteRealNumber | DeltaE94ApplicationConstants | Exact Delta E 94 `k2` application constant. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| AccessibilityPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the accessibility policy. |
| AccessibilityPolicy | PolicyRule | local | One or more authored policy rules in stored order. |
| PolicyRule | NamedValueEntry | local | Zero or more ordered parameter entries for the governing rule identifier. |
| ProofPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the proof policy. |
| ProofPolicy | ProofTarget | local | One or more authored proof targets in stored order. |
| ProofTarget | DeltaE94ApplicationConstants | local | Exact Delta E 94 application constants when retained comparison uses metric `94`. |

## Constraints

`AccessibilityPolicy` requires at least one `PolicyRule`.

`ProofPolicy` requires at least one `ProofTarget`.

`PolicyRule` requires exactly one `policyRuleIdentifier`.

`minimum-apca-lc` uses exactly one `NamedValueEntry(entryName="minimumApcaLc", entryValue=<finite decimal greater than or equal to 0>)`.

`minimum-wcag-contrast-ratio` uses exactly one `NamedValueEntry(entryName="minimumWcagContrastRatio", entryValue=<finite decimal greater than or equal to 1 and less than or equal to 21>)`.

`require-distinction-preservation`, `require-state-exposure`, `require-consequence-exposure`, and `require-no-color-alone-risk` use zero `NamedValueEntry` children.

`ProofTarget` requires exactly one `proofTargetIdentifier`, exactly one `proofMedium`, exactly one `targetProfileIdentifier`, exactly one `proofGamutMappingMode`, exactly one `proofComparisonMode`, and exactly one `renderingIntent`.

`retainedComparisonMetric` and `retainedComparisonTolerance` appear if and only if `proofComparisonMode` is `$RetainedDeltaE` or `$RetainedDeltaEAndRenderedArtifact`.

`DeltaE94ApplicationConstants` appears if and only if `retainedComparisonMetric` is `94`.

When `DeltaE94ApplicationConstants` appears, `kL`, `k1`, and `k2` are finite positive values.

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| description | `paperhat:domain:description` | Provides descriptive text for authored policy objects. |

## Design Notes

- This package projects exact lower-layer `PolicyRule` and `ProofTarget` semantics directly.
- Concrete policy attachment belongs in higher-level composer packages such as `paperhat-prism-project`, where project-local governance objects and policy objects coexist in one document.
- The generic `paperhat-policy` package is not adopted here. `paperhat-color-policy` owns the exact authored accessibility and proof-policy surface for Prism color workflows.
- Derived `RepairSuggestion`, `Proof`, `AuditReport`, and governance bundles are intentionally absent. They belong in `paperhat-prism-result-bundle`.

---

**End of Color Policy v1.0.0**
