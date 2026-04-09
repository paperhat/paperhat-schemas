Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Color Policy

Authored accessibility and proof policy objects for Prism. Defines accessibility policies, contrast requirements, simulation conditions, proof policies, and proof targets.

## When to Use

Use this package to author durable rule objects that govern accessibility evaluation and target-medium proofing for Prism. `paperhat-color-policy` defines the policy objects themselves. It does not bind those policies to a specific project object by reference, and it does not contain derived repair suggestions, proofs, or audit bundles.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| AccessibilityPolicy | yes | First-class accessibility policy object for one Prism scope level. |
| ContrastRequirement | yes | Stable authored contrast rule for one semantic role-type pair. |
| SimulationCondition | no | Required simulation mode to include during accessibility evaluation. |
| ProofPolicy | yes | First-class proofing policy object for one Prism scope level. |
| ProofTarget | yes | Stable authored proof target describing one medium, color space, and comparison mode. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| name | $Text | AccessibilityPolicy, ProofPolicy | Human-readable policy name. |
| scopeLevel | $EnumeratedToken | AccessibilityPolicy, ProofPolicy | Intended Prism scope level. Allowed values: `$Project`, `$ColorSystem`, `$Palette`, `$TokenSet`, `$Token`. |
| accessibilityPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for an accessibility policy. |
| complianceStandard | $EnumeratedToken | no | Declared compliance standard, such as WCAG profile or institutional rule set. |
| contrastComputationMode | $EnumeratedToken | no | Declared contrast-computation mode. Allowed values: `$WcagRelativeLuminance`, `$ApcaW3`. |
| key | $LookupToken | ContrastRequirement, ProofTarget | Stable document-scoped lookup key. |
| minimumContrastRatio | $FiniteRealNumber | ContrastRequirement | Minimum acceptable contrast ratio. |
| foregroundSemanticRoleType | $EnumeratedToken | ContrastRequirement | Governing foreground semantic role type. Allowed values: `$Surface`, `$Text`, `$Border`, `$Icon`, `$Link`, `$Action`, `$Focus`, `$Overlay`, `$DataVisualization`, `$Brand`, `$Status`, `$Disabled`. |
| backgroundSemanticRoleType | $EnumeratedToken | ContrastRequirement | Governing background semantic role type. Allowed values: `$Surface`, `$Text`, `$Border`, `$Icon`, `$Link`, `$Action`, `$Focus`, `$Overlay`, `$DataVisualization`, `$Brand`, `$Status`, `$Disabled`. |
| label | $Text | ContrastRequirement, ProofTarget | Human-readable display label. |
| contrastContext | $EnumeratedToken | no | Context classification. Allowed values: `$NormalText`, `$LargeText`, `$NonText`. |
| contrastRequirementStatus | $EnumeratedToken | no | Lifecycle or governance status for a contrast requirement. |
| simulationMode | $EnumeratedToken | SimulationCondition | Simulation mode required during evaluation. Allowed values: `$Protanopia`, `$Deuteranopia`, `$Tritanopia`. |
| simulationConditionStatus | $EnumeratedToken | no | Lifecycle or governance status for a simulation condition. |
| proofPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for a proof policy. |
| targetMedium | $EnumeratedToken | ProofTarget | Declared proof target medium. |
| proofColorSpace | $EnumeratedToken | no | Declared proof color space. |
| gamutMappingMode | $EnumeratedToken | no | Declared gamut-mapping mode. Allowed values: `$None`, `$Perceptual`, `$Clip`, `$ChromaReduction`. |
| proofComparisonMode | $EnumeratedToken | no | Declared proof comparison mode. |
| renderingIntent | $EnumeratedToken | no | Declared rendering intent. |
| toleranceDeltaE | $FiniteRealNumber | no | Declared acceptable color-difference tolerance. |
| proofTargetStatus | $EnumeratedToken | no | Lifecycle or governance status for a proof target. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| AccessibilityPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the accessibility policy. |
| AccessibilityPolicy | ContrastRequirement | local | One or more authored contrast requirements. |
| AccessibilityPolicy | SimulationCondition | local | Optional simulation conditions to include during accessibility evaluation. |
| ProofPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the proof policy. |
| ProofPolicy | ProofTarget | local | One or more authored proof targets. |

## Constraints

`AccessibilityPolicy` requires at least one `ContrastRequirement`.

`ProofPolicy` requires at least one `ProofTarget`.

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| description | `paperhat:domain:description` | Provides descriptive text for authored policy objects. |

## Design Notes

- This package is intentionally portable. Policies declare scope level and semantic role types rather than binding themselves directly to one specific `ColorSystem`, `Palette`, or `TokenSet`.
- Concrete policy attachment belongs in higher-level composer packages such as `paperhat-prism-project`, where project-local governance objects and policy objects coexist in one document.
- Contrast rules target semantic role types rather than specific role entities. This keeps authored policy reusable across multiple governed color systems that share the Prism base role vocabulary.
- Derived `RepairSuggestion`, `Proof`, `AuditReport`, and governance bundles are intentionally absent. They belong in `paperhat-prism-result-bundle`.

---

**End of Color Policy v1.0.0**
