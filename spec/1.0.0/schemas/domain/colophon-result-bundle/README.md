Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Colophon Result Bundle

Derived Colophon workflow result documents. Defines durable `RhythmAuditResult`, `MeasureAuditResult`, `AccessibilityAuditResult`, `EmphasisConsistencyAuditResult`, and `ProvenanceTraceLocator` snapshots.

## When to Use

Use this package to persist derived Colophon workflow outputs as stable reviewable documents. `paperhat-colophon-result-bundle` does not author typography governance truth, policy truth, or Colophon project authority. It records derived rhythm audit results, measure audit results, accessibility audit results, emphasis consistency audit results, and provenance traces as closed snapshots.

This package defines no templates.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| RhythmAuditResult | yes | Durable rhythm-audit result document carrying one audit identifier, pass state, element counts, zero or more rhythm violations, and one or more provenance-trace locators. |
| RhythmViolation | no | One rhythm violation entry inside one RhythmAuditResult document. |
| MeasureAuditResult | yes | Durable measure-audit result document carrying one audit identifier, pass state, element counts, zero or more measure violations, and one or more provenance-trace locators. |
| MeasureViolation | no | One measure violation entry inside one MeasureAuditResult document. |
| AccessibilityAuditResult | yes | Durable accessibility-audit result document carrying one audit identifier, pass state, check counts, zero or more accessibility violations, and one or more provenance-trace locators. |
| AccessibilityViolation | no | One accessibility violation entry inside one AccessibilityAuditResult document. |
| EmphasisConsistencyAuditResult | yes | Durable emphasis-consistency-audit result document carrying one audit identifier, pass state, rule counts, zero or more emphasis violations, and one or more provenance-trace locators. |
| EmphasisViolation | no | One emphasis-consistency violation entry inside one EmphasisConsistencyAuditResult document. |
| ProvenanceTraceLocator | no | Stable locator for one provenance trace. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| auditIdentifier | $Text | RhythmAuditResult, MeasureAuditResult, AccessibilityAuditResult, EmphasisConsistencyAuditResult | Exact audit identifier. |
| passed | $Boolean | RhythmAuditResult, MeasureAuditResult, AccessibilityAuditResult, EmphasisConsistencyAuditResult | Exact pass state. |
| totalElements | $NonNegativeInteger | RhythmAuditResult, MeasureAuditResult | Exact total element count. |
| alignedElements | $NonNegativeInteger | RhythmAuditResult | Exact count of elements aligned to the baseline grid. |
| auditDate | $Date | no | Date on which the audit was performed. |
| baselineGridUnit | $Text | no | Exact baseline grid unit used for the rhythm audit. |
| auditResultStatus | $EnumeratedToken | no | Exact audit result status. |
| role | $Text | RhythmViolation, MeasureViolation, AccessibilityViolation | Exact role of the violating element. |
| declaredLeading | $Text | RhythmViolation | Exact declared leading of the violating element. |
| nearestGridLine | $Text | RhythmViolation | Exact nearest grid line for the violating element. |
| violationDescription | $Text | RhythmViolation, MeasureViolation, AccessibilityViolation, EmphasisViolation | Exact violation description. |
| compliantElements | $NonNegativeInteger | MeasureAuditResult | Exact count of elements within measure bounds. |
| minimumMeasureBound | $Text | no | Exact minimum measure bound used for the measure audit. |
| maximumMeasureBound | $Text | no | Exact maximum measure bound used for the measure audit. |
| declaredMeasure | $Text | MeasureViolation | Exact declared measure of the violating element. |
| nearestBound | $Text | MeasureViolation | Exact nearest measure bound for the violating element. |
| totalChecks | $NonNegativeInteger | AccessibilityAuditResult | Exact total accessibility check count. |
| passedChecks | $NonNegativeInteger | AccessibilityAuditResult | Exact count of accessibility checks that passed. |
| checkKind | $EnumeratedToken | AccessibilityViolation | Exact accessibility check kind. Allowed values: `$MinimumSize`, `$MinimumLeading`, `$MinimumMeasure`, `$MaximumMeasure`, `$ScaleDifferentiation`. |
| declaredValue | $Text | AccessibilityViolation | Exact declared value of the violating element. |
| requiredValue | $Text | AccessibilityViolation | Exact required value for the accessibility check. |
| totalRules | $NonNegativeInteger | EmphasisConsistencyAuditResult | Exact total emphasis rule count. |
| distinguishableRules | $NonNegativeInteger | EmphasisConsistencyAuditResult | Exact count of distinguishable emphasis rules. |
| firstEmphasisLevel | $Text | EmphasisViolation | Exact first emphasis level in the indistinguishable pair. |
| secondEmphasisLevel | $Text | EmphasisViolation | Exact second emphasis level in the indistinguishable pair. |
| traceLocator | $Iri | ProvenanceTraceLocator | Stable locator for one provenance trace document. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| RhythmAuditResult | RhythmViolation | local | Zero or more rhythm violation entries. |
| RhythmAuditResult | ProvenanceTraceLocator | local | One or more provenance-trace locators. |
| MeasureAuditResult | MeasureViolation | local | Zero or more measure violation entries. |
| MeasureAuditResult | ProvenanceTraceLocator | local | One or more provenance-trace locators. |
| AccessibilityAuditResult | AccessibilityViolation | local | Zero or more accessibility violation entries. |
| AccessibilityAuditResult | ProvenanceTraceLocator | local | One or more provenance-trace locators. |
| EmphasisConsistencyAuditResult | EmphasisViolation | local | Zero or more emphasis-consistency violation entries. |
| EmphasisConsistencyAuditResult | ProvenanceTraceLocator | local | One or more provenance-trace locators. |

## Design Notes

- This package imports nothing and depends on nothing. It records durable result snapshots only.
- `RhythmAuditResult`, `MeasureAuditResult`, `AccessibilityAuditResult`, and `EmphasisConsistencyAuditResult` are top-level reviewable entities because Colophon review surfaces activate them directly.
- Violation concepts are structural children that record exact violation details without importing authored policy packages.
- `ProvenanceTraceLocator` carries a stable IRI reference to an external provenance trace document, keeping the result bundle self-contained.

**End of Colophon Result Bundle v1.0.0**
