Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Prism Result Bundle

Derived Prism workflow result documents. Defines durable `Proof`, `RepairSuggestion`, `ContrastPair`, `AuditReport`, `PublicationTargetMatrix`, and `ProvenanceTrace` snapshots.

## When to Use

Use this package to persist derived Prism workflow outputs as stable reviewable documents. `paperhat-prism-result-bundle` does not author color-governance truth, policy truth, or Prism project authority. It records derived proof results, repair proposals, evaluated contrast pairs, audit rollups, publication coverage matrices, and provenance traces as closed snapshots.

This package defines no templates.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| Proof | yes | Durable proof-result document carrying one proof subject, one or more ordered proof-target results, zero or more rendered proof artifacts, and one or more provenance-trace locators. |
| ProofTargetResult | no | Ordered proof-target result snapshot inside one Proof document. |
| ProofSubjectResult | no | Ordered proof-subject result snapshot inside one ProofTargetResult. |
| RenderedProofArtifactReference | no | Stable rendered-artifact witness for one proof target. |
| RepairSuggestion | yes | Durable repair-suggestion document carrying one exact request context, one exact suggestion, one or more ordered repair objectives, and one or more provenance-trace locators. |
| RepairObjective | no | Ordered repair-objective snapshot inside one RepairSuggestion document. |
| ContrastPair | yes | Durable evaluated accessibility pair carrying exact witness values and one or more provenance-trace locators. |
| AuditReport | yes | Durable audit-rollup document carrying ordered scope summaries and ordered direct violations. |
| AuditScopeSummary | no | Ordered per-scope audit summary inside one AuditReport. |
| AuditCategoryResult | no | Ordered per-category audit summary inside one AuditScopeSummary. |
| AuditViolation | no | Ordered direct audit violation inside one AuditReport. |
| PublicationTargetMatrix | yes | Durable publication-coverage matrix for one routed root selection. |
| CrossWorldCorrespondence | no | Ordered non-focal locator group for one semantic world. |
| PublicationTargetMatrixEntry | no | Ordered matrix entry describing one publication target. |
| ProvenanceTrace | yes | Durable source-first provenance trace for one selection root or artifact root. |
| ProvenanceTraceEntry | no | Ordered provenance-trace step entry. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| subjectArtifactKind | $EnumeratedToken | Proof | Exact proof subject kind. Allowed values: `$ColorValue`, `$Palette`, `$TokenSet`, `$TargetProfileColorPackage`. |
| subjectArtifactLocator | $Iri | Proof | Stable locator for the proof subject root artifact. |
| provenanceTraceArtifactLocator | $List<$Iri> | Proof, RepairSuggestion, ContrastPair, PublicationTargetMatrixEntry | One or more stable provenance-trace document locators in stored order. |
| proofTargetIdentifier | $Text | ProofTargetResult, RenderedProofArtifactReference | Exact authored proof-target identifier. |
| proofTargetSnapshot | $Text | ProofTargetResult | Canonical snapshot of the authored proof target. |
| proofTargetLabel | $Text | no | Human-readable proof-target label. |
| proofTargetResolutionState | $EnumeratedToken | ProofTargetResult | Exact proof-target resolution state. Allowed values: `$Resolved`, `$TargetProfileNotFound`, `$ProofMediumMismatch`. |
| resolvedTargetProfileDefinitionSnapshot | $Text | no | Canonical snapshot of the resolved target-profile definition. |
| outputColorTargetSnapshot | $Text | no | Canonical snapshot of the resolved output-color target. |
| opacityHandlingPolicySnapshot | $Text | no | Canonical snapshot of the resolved opacity-handling policy. |
| subjectCount | $Integer | ProofTargetResult | Exact subject-stream count. |
| admittedSubjectCount | $Integer | ProofTargetResult | Exact count of admitted retained outputs. |
| rejectedSubjectCount | $Integer | ProofTargetResult | Exact count of rejected or rendered-only outputs. |
| retainedComparisonWithinToleranceCount | $Integer | ProofTargetResult | Exact count of retained comparisons within tolerance. |
| retainedComparisonExceededToleranceCount | $Integer | ProofTargetResult | Exact count of retained comparisons above tolerance. |
| retainedComparisonNotComputableCount | $Integer | ProofTargetResult | Exact count of retained comparisons that were not computable. |
| proofRenderedEvidenceState | $EnumeratedToken | ProofTargetResult | Exact rendered-evidence state. Allowed values: `$NotRequired`, `$RequiredPending`, `$Present`, `$Failed`. |
| subjectIndex | $Integer | ProofSubjectResult | Zero-based subject position. |
| tokenSelectorIdentity | $Text | no | Exact token-selector identity when the subject shape is token-bearing. |
| effectiveSubjectColorState | $EnumeratedToken | ProofSubjectResult | Exact effective-subject state. Allowed values: `$Resolved`, `$Unresolved`. |
| effectiveSubjectColor | $Color | no | Exact effective subject color when resolved. |
| proofEvaluationColorState | $EnumeratedToken | ProofSubjectResult | Exact proof-evaluation color state. Allowed values: `$Derived`, `$AbsentByUnresolvedSubject`, `$AbsentByOpacityHandling`. |
| proofEvaluationColor | $Color | no | Exact proof-evaluation color when derived. |
| proofOutputAdmissionState | $EnumeratedToken | ProofSubjectResult | Exact output-admission state. Allowed values: `$AdmittedRetainedOutput`, `$RejectedUnresolvedSubject`, `$RejectedOpacityHandling`, `$RejectedOutputTarget`, `$RenderedOutputRequired`. |
| proofGamutState | $EnumeratedToken | ProofSubjectResult | Exact proof gamut state. Allowed values: `$NotApplicable`, `$InGamut`, `$OutOfGamutRejected`, `$OutOfGamutClipped`, `$OutOfGamutChromaReduced`, `$RenderedMappingRequired`, `$DeviceNative`. |
| proofOutputColor | $Color | no | Exact retained proof-output color when admitted. |
| proofRetainedComparisonOutcome | $EnumeratedToken | no | Exact retained-comparison outcome. Allowed values: `$WithinTolerance`, `$ExceedsTolerance`, `$NotComputable`. |
| retainedComparisonMetric | $Text | no | Exact retained Delta E metric token or numeric identifier. |
| retainedComparisonValue | $FiniteRealNumber | no | Exact retained-comparison witness value. |
| retainedComparisonTolerance | $FiniteRealNumber | no | Exact retained-comparison tolerance. |
| artifactKind | $Text | RenderedProofArtifactReference | Exact artifact-kind identifier. |
| artifactLocator | $Iri | RenderedProofArtifactReference, ProvenanceTraceEntry | Stable durable artifact locator. |
| renderingIntent | $EnumeratedToken | RenderedProofArtifactReference | Exact rendering intent. Allowed values: `$RelativeColorimetric`, `$AbsoluteColorimetric`, `$Perceptual`, `$Saturation`. |
| sourceOperationIdentifier | $Text | RenderedProofArtifactReference | Exact producing operation identifier. |
| repairRequestIdentifier | $Text | RepairSuggestion | Exact repair-request identifier. |
| subjectColor | $Color | RepairSuggestion | Exact direct subject color from the repair request. |
| repairSuggestionIdentifier | $Text | RepairSuggestion | Exact repair-suggestion identifier. |
| rank | $Integer | RepairSuggestion | Zero-based suggestion rank. |
| suggestedColor | $Color | RepairSuggestion | Exact suggested replacement color. |
| repairStrategyKind | $List<$EnumeratedToken> | RepairSuggestion | One or more exact repair strategy tokens in stored order. Allowed values: `$ChannelClamp`, `$OutputSpaceClip`, `$HuePreservingChromaReduction`, `$OklchLightnessSweep`, `$NeutralAxisBoundary`, `$ReferenceSegmentSearch`, `$PaletteMemberSelection`, `$OpacityForceOpaque`. |
| perceptualDistanceMetric | $EnumeratedToken | RepairSuggestion | Exact repair ranking metric. Allowed values: `$Ok`. |
| perceptualDistanceValue | $FiniteRealNumber | RepairSuggestion | Exact Delta E Ok distance to the effective subject color. |
| satisfiedRepairObjectiveIdentifier | $List<$Text> | RepairSuggestion | One or more satisfied repair-objective identifiers in request order. |
| repairObjectiveIdentifier | $Text | RepairObjective | Exact repair-objective identifier. |
| repairObjectiveKind | $EnumeratedToken | RepairObjective | Exact repair-objective kind. Allowed values: `$ChannelRange`, `$Gamut`, `$WcagContrastRatio`, `$ApcaContrast`, `$PerceptualDistance`, `$ExtensionPaletteMembership`, `$OutputTargetAdmission`, `$OpaqueBackground`. |
| governingSourceKind | $EnumeratedToken | RepairObjective | Exact governing source kind. Allowed values: `$ManualConstraint`, `$AccessibilityPolicyRule`, `$PaletteMembershipPolicyRule`, `$ProofTarget`, `$PublicationScope`. |
| governingSourceIdentifier | $Text | RepairObjective | Exact governing source identifier. |
| governingPolicyRuleIdentifier | $Text | no | Exact governing policy-rule identifier when one explicit rule owns the objective. |
| channelRangeConstraintSnapshot | $Text | no | Canonical snapshot of the governing channel-range constraint. |
| gamutConstraintSnapshot | $Text | no | Canonical snapshot of the governing gamut constraint. |
| contrastRatioConstraintSnapshot | $Text | no | Canonical snapshot of the governing contrast constraint. |
| referenceColor | $Color | no | Exact reference color for perceptual-distance objectives. |
| minimumAbsoluteLc | $FiniteRealNumber | no | Exact minimum absolute APCA Lc threshold when present. |
| repairContrastSubjectRole | $EnumeratedToken | no | Exact contrast subject role. Allowed values: `$Foreground`, `$Background`. |
| perceptualDistanceConstraintSnapshot | $Text | no | Canonical snapshot of the governing perceptual-distance constraint. |
| paletteSnapshot | $Text | no | Canonical snapshot of the governing palette. |
| paletteMembershipPolicySnapshot | $Text | no | Canonical snapshot of the governing palette-membership policy. |
| contrastPairIdentifier | $Text | ContrastPair | Exact evaluated contrast-pair identifier. |
| contrastPairOriginKind | $EnumeratedToken | ContrastPair | Exact pair origin kind. Allowed values: `$OrderedInputPair`, `$PalettePair`. |
| leftColor | $Color | ContrastPair | Exact left retained color. |
| rightColor | $Color | ContrastPair | Exact right retained color. |
| leftArtifactLocator | $Iri | no | Stable locator of the left governed source when present. |
| rightArtifactLocator | $Iri | no | Stable locator of the right governed source when present. |
| leftOrdinal | $Integer | ContrastPair | Zero-based left ordinal in the governing pair domain. |
| rightOrdinal | $Integer | ContrastPair | Zero-based right ordinal in the governing pair domain. |
| governingAccessibilityPolicySnapshot | $Text | ContrastPair | Canonical snapshot of the governing accessibility policy. |
| apcaPolicyRuleIdentifier | $Text | no | Exact APCA rule identifier when present. |
| minimumApcaLc | $FiniteRealNumber | no | Exact APCA threshold when present. |
| apcaAbsoluteLc | $FiniteRealNumber | no | Exact APCA witness value when admitted. |
| apcaEvaluationState | $EnumeratedToken | ContrastPair | Exact APCA evaluation state. Allowed values: `$Satisfied`, `$Violated`, `$NotRequested`. |
| wcagPolicyRuleIdentifier | $Text | no | Exact WCAG rule identifier when present. |
| minimumWcagContrastRatio | $FiniteRealNumber | no | Exact WCAG threshold when present. |
| wcagContrastRatio | $FiniteRealNumber | no | Exact WCAG witness value when admitted. |
| wcagEvaluationState | $EnumeratedToken | ContrastPair | Exact WCAG evaluation state. Allowed values: `$Satisfied`, `$Violated`, `$NotRequested`. |
| primaryConstraintCategory | $EnumeratedToken | no | First violated audit category in exact prominence order when present. Allowed values: `$AccessibilityFailure`, `$ResolutionContextInsufficient`, `$PublicationTargetNotRepresentable`, `$ProofCoverageMissing`, `$GamutFailure`, `$RoleUnassigned`, `$PrecisionWarning`. |
| auditReportIdentifier | $Text | AuditReport | Exact audit-report identifier. |
| auditRootScopeKind | $EnumeratedToken | AuditReport | Exact root audit scope kind. Allowed values: `$ColorSystem`, `$Palette`, `$TokenSet`, `$TokenSelectorIdentity`, `$ColorValue`, `$CssDeclaredColor`. |
| rootScopeArtifactLocator | $Iri | AuditReport | Exact root scope locator. |
| auditScopeKind | $EnumeratedToken | AuditScopeSummary, AuditViolation | Exact audit scope kind. Allowed values: `$ColorSystem`, `$Palette`, `$TokenSet`, `$TokenSelectorIdentity`, `$ColorValue`, `$CssDeclaredColor`. |
| scopeArtifactLocator | $Iri | AuditScopeSummary, AuditViolation | Exact scope artifact locator. |
| auditConstraintCategory | $EnumeratedToken | AuditCategoryResult, AuditViolation | Exact audit constraint category. Allowed values: `$AccessibilityFailure`, `$ResolutionContextInsufficient`, `$PublicationTargetNotRepresentable`, `$ProofCoverageMissing`, `$GamutFailure`, `$RoleUnassigned`, `$PrecisionWarning`. |
| auditConstraintState | $EnumeratedToken | AuditCategoryResult | Exact audit constraint state. Allowed values: `$Satisfied`, `$Violated`, `$NotApplicable`. |
| violationCount | $Integer | AuditCategoryResult | Exact direct-plus-descendant violation count. |
| firstViolationCode | $Text | no | Exact first violation code when the count is greater than zero. |
| prominenceRank | $Integer | AuditViolation | Zero-based prominence rank. |
| violationCode | $Text | AuditViolation | Exact direct violation code. |
| publicationScopeKey | $LookupToken | AuditViolation, PublicationTargetMatrixEntry | Exact governing publication-scope key. |
| publicationTargetMatrixIdentifier | $Text | PublicationTargetMatrix | Exact publication-target-matrix identifier. |
| selectionKind | $EnumeratedToken | PublicationTargetMatrix, ProvenanceTrace | Exact selection kind. Allowed values: `$ColorSelection`, `$PaletteSelection`, `$TokenSetSelection`, `$RoleSelection`, `$ContrastPairSelection`, `$TargetProfileSelection`, `$ArtifactSelection`, `$GovernancePackSelection`, `$SemanticDifferenceSelection`, `$ProvenanceSelection`, `$CssDeclaredColorSelection`, `$CssDeclaredResolutionContextSelection`. |
| selectionWorld | $EnumeratedToken | CrossWorldCorrespondence, PublicationTargetMatrix, ProvenanceTrace | Exact selection world. Allowed values: `$AuthoredSemanticWorld`, `$ResolvedColorWorld`, `$PublishedArtifactWorld`. |
| focalArtifactLocator | $Iri | PublicationTargetMatrix, ProvenanceTrace | Exact root focal artifact locator. |
| artifactLocatorSequence | $List<$Iri> | CrossWorldCorrespondence, PublicationTargetMatrixEntry | Stored artifact locators in exact order. `CrossWorldCorrespondence` requires one or more values. `PublicationTargetMatrixEntry` admits zero or more values. |
| publicationTargetKind | $EnumeratedToken | PublicationTargetMatrixEntry | Exact publication target family. Allowed values: `$Css`, `$DesignTokensCommunityGroup`, `$StyleDictionary`, `$TargetProfile`. |
| publicationIntent | $EnumeratedToken | PublicationTargetMatrixEntry | Exact authored publication intent. Allowed values: `$Css`, `$ApplicationTokens`, `$PrintSwatches`, `$Proof`, `$Report`, `$Governance`. |
| targetMedium | $EnumeratedToken | no | Exact target medium when present. Allowed values: `$Web`, `$Print`, `$Presentation`, `$Document`, `$Ebook`. |
| targetProfileIdentifier | $Text | no | Exact target-profile identifier when present. |
| proofTargetOrdinal | $Integer | no | Exact proof-target ordinal when present. |
| publicationRepresentabilityState | $EnumeratedToken | PublicationTargetMatrixEntry | Exact representability state. Allowed values: `$Representable`, `$NotRepresentable`. |
| proofCoverageState | $EnumeratedToken | PublicationTargetMatrixEntry | Exact proof-coverage state. Allowed values: `$NotRequired`, `$Covered`, `$MissingProofPolicyBinding`, `$MissingProofTarget`, `$MissingTargetMedium`, `$MissingTargetProfileCatalog`, `$TargetProfileNotFound`, `$ProofMediumMismatch`. |
| publicationDiagnosticCode | $List<$Text> | no | Zero or more publication or proof diagnostic codes in stored order. |
| publicationArtifactAvailabilityState | $EnumeratedToken | PublicationTargetMatrixEntry | Exact publication artifact availability state. Allowed values: `$NotProduced`, `$Produced`. |
| provenanceTraceIdentifier | $Text | ProvenanceTrace | Exact provenance-trace identifier. |
| provenanceTraceRootKind | $EnumeratedToken | ProvenanceTrace | Exact provenance-trace root kind. Allowed values: `$SelectionRoot`, `$ArtifactRoot`. |
| traceEntryIndex | $Integer | ProvenanceTraceEntry | Zero-based source-first trace index. |
| provenanceTraceEntryKind | $EnumeratedToken | ProvenanceTraceEntry | Exact provenance-trace entry kind. Allowed values: `$AuthoredArtifact`, `$PolicyArtifact`, `$TargetProfileArtifact`, `$ContextArtifact`, `$Operation`, `$DiagnosticArtifact`, `$DerivedArtifact`, `$PublishedArtifact`. |
| semanticWorld | $EnumeratedToken | no | Exact semantic world for non-operation trace entries. Allowed values: `$AuthoredSemanticWorld`, `$ResolvedColorWorld`, `$PublishedArtifactWorld`. |
| operationIdentifier | $Text | no | Exact operation identifier for operation trace entries. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| Proof | ProofTargetResult | local | One or more ordered proof-target results. |
| Proof | RenderedProofArtifactReference | local | Zero or more rendered proof-artifact witnesses. |
| ProofTargetResult | ProofSubjectResult | local | Zero or more ordered proof-subject results. |
| RepairSuggestion | RepairObjective | local | One or more ordered repair-objective snapshots from the governing request. |
| AuditReport | AuditScopeSummary | local | One or more ordered audit scope summaries. |
| AuditReport | AuditViolation | local | Zero or more ordered direct violations. |
| AuditScopeSummary | AuditCategoryResult | local | Exactly seven ordered category results in exact prominence order. |
| PublicationTargetMatrix | CrossWorldCorrespondence | local | Zero or more root correspondence groups. |
| PublicationTargetMatrix | PublicationTargetMatrixEntry | local | Zero or more ordered publication-target entries. |
| ProvenanceTrace | CrossWorldCorrespondence | local | Zero or more root correspondence groups when the root kind is `SelectionRoot`. |
| ProvenanceTrace | ProvenanceTraceEntry | local | One or more ordered provenance-trace entries. |

## Constraints

`Proof` requires at least one `provenanceTraceArtifactLocator` list member and at least one `ProofTargetResult`.

`RepairSuggestion` requires at least one `RepairObjective`, at least one `repairStrategyKind` list member, at least one `satisfiedRepairObjectiveIdentifier` list member, and at least one `provenanceTraceArtifactLocator` list member.

`ContrastPair` requires at least one `provenanceTraceArtifactLocator` list member.

`AuditScopeSummary` requires exactly seven `AuditCategoryResult` children in the exact category order: `AccessibilityFailure`, `ResolutionContextInsufficient`, `PublicationTargetNotRepresentable`, `ProofCoverageMissing`, `GamutFailure`, `RoleUnassigned`, `PrecisionWarning`.

`CrossWorldCorrespondence` requires at least one `artifactLocatorSequence` list member.

`PublicationTargetMatrix` admits only `selectionKind` values `ColorSelection`, `PaletteSelection`, and `TokenSetSelection`.

`PublicationTargetMatrixEntry` requires at least one `provenanceTraceArtifactLocator` list member.

When `provenanceTraceRootKind` is `$ArtifactRoot`, `selectionKind` and `selectionWorld` are absent.

When `provenanceTraceEntryKind` is `$Operation`, `semanticWorld` and `artifactLocator` are absent and `operationIdentifier` is present.

When `provenanceTraceEntryKind` is not `$Operation`, `semanticWorld` and `artifactLocator` are present and `operationIdentifier` is absent.

When `proofTargetResolutionState` is not `$Resolved`, `resolvedTargetProfileDefinitionSnapshot`, `outputColorTargetSnapshot`, and `opacityHandlingPolicySnapshot` are absent.

When `effectiveSubjectColorState` is not `$Resolved`, `effectiveSubjectColor` is absent.

When `proofEvaluationColorState` is not `$Derived`, `proofEvaluationColor` is absent.

When `proofOutputAdmissionState` is not `$AdmittedRetainedOutput`, `proofOutputColor` is absent.

## Design Notes

- This package imports nothing and depends on nothing. It records durable result snapshots only.
- Every cross-package object with one external semantic source is carried either by one exact stable artifact locator, one exact ordered locator list, or one exact snapshot trait.
- `Proof`, `RepairSuggestion`, and `ContrastPair` are top-level reviewable entities because Prism review and report surfaces activate them directly.
- `AuditReport`, `PublicationTargetMatrix`, and `ProvenanceTrace` remain separate top-level documents because Prism consumes them independently.
- `RepairObjective` remains local snapshot structure inside the result-bundle package so one repair suggestion keeps exact ordered request context without importing authored policy packages.
- `CrossWorldCorrespondence` is shared between `PublicationTargetMatrix` and `ProvenanceTrace` because both surfaces serialize the same non-focal locator grouping.

**End of Prism Result Bundle v1.0.0**
