# Adaptive Plan

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

The adaptive plan is the self-contained artifact that the Lexis pipeline produces from design annotations and that the foundry consumes as its sole semantic input. It contains every element, constraint, perceptual invariant, accessibility requirement, and adaptation rule that the foundry needs to produce a conforming output. The foundry reads nothing else.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| AdaptivePlan | Semantic | MustBeEntity | ForbidsContent | Title (1), Description (0-1), AccessibilityConstraint (1+), AccessibilityThresholdOverride (0+), AdaptationPath (1+), Calculation (0+), Validation (0+), PerceptualInvariant (1+), PlanConstraint (1+), PlanElement (1+), ResolvedGlossReference (0+) | Root container for the compiled adaptive plan. |
| AccessibilityConstraint | Semantic | MustNotBeEntity | ForbidsContent | -- | Declares an accessibility requirement that applies to listed elements. |
| AccessibilityThresholdOverride | Semantic | MustBeEntity | ForbidsContent | -- | Replaces the default threshold for a specific operator at a specific ordinal level. |
| AdaptationPath | Semantic | MustBeEntity | ForbidsContent | PlanRule (0+) | Groups rules that produce a single adaptation result class (baseline, adapted, or constrained). |
| PerceptualInvariant | Semantic | MustNotBeEntity | ForbidsContent | -- | Declares a perceptual relationship among elements that the foundry preserves across all adaptation paths. |
| PlanElement | Semantic | MustBeEntity | ForbidsContent | -- | Represents one semantic element from the source composition or view, carrying its role, scope, and risk metadata. |
| ResolvedGlossReference | Semantic | MustNotBeEntity | ForbidsContent | -- | Carries the resolved display text for a gloss reference so the foundry does not need access to the glossary. |
| PlanConstraint | Semantic | MustBeEntity | ForbidsContent | -- | A spatial or visual constraint between elements, with solved and unsolved values from the constraint solver. |
| PlanRule | Semantic | MustBeEntity | ForbidsContent | PlanPredicate (1+), PlanWeightOperation (0+), PlanFreezeOperation (0+), PlanRelaxOperation (0+), PlanGuardOperation (0+) | A conditional rule inside an adaptation path that modifies constraint weights or freezes constraints based on predicates. |
| PlanPredicate | Structural | MustNotBeEntity | ForbidsContent | -- | A single boolean condition tested against a runtime variable. |
| PlanWeightOperation | Structural | MustNotBeEntity | ForbidsContent | -- | Sets a constraint's weight to a specific value when the parent rule fires. |
| PlanFreezeOperation | Structural | MustNotBeEntity | ForbidsContent | -- | Freezes a constraint at its current solved value when the parent rule fires. |
| PlanRelaxOperation | Structural | MustNotBeEntity | ForbidsContent | -- | Relaxes a constraint by a number of ordinal steps when the parent rule fires. |
| PlanGuardOperation | Structural | MustNotBeEntity | ForbidsContent | -- | Prevents a constraint from being relaxed below its current level when the parent rule fires. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| behavior | `paperhat:behavior:expression` | Calculation, Validation |
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Title |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `adaptationResultClass` | `$EnumeratedToken` | `$Baseline`, `$Adapted`, `$Constrained` | Classification of the adaptation path's output. |
| `adaptivePlanProjectionDefinitionClosureHash` | `$Text` | -- | SHA-256 hash of the projection definition closure that produced this plan. |
| `closureHash` | `$Text` | -- | SHA-256 hash of the entire plan closure. |
| `comparison` | `$EnumeratedToken` | `$Equal`, `$NotEqual`, `$MemberOf` | Comparison operator used in a predicate. |
| `compositionTarget` | `$Iri` | -- | IRI of the source composition this plan targets. |
| `confidenceFloor` | `$Number` | -- | Minimum confidence threshold below which the rule does not fire. |
| `constraintTarget` | `$Iri` | -- | IRI of the constraint that an operation targets. |
| `constraintType` | `$EnumeratedToken` | `$ContrastMinimum`, `$TargetSizeMinimum`, `$ReadingOrderPreservation`, `$LanguageMetadata`, `$StructuralRegionIdentification`, `$NonDecorativeAltText` | Category of accessibility constraint. |
| `contentHashAlgorithm` | `$EnumeratedToken` | `$SHA256` | Hash algorithm used for all content hashes in this plan. |
| `cumulativeDeltaLimit` | `$Number` | -- | Maximum total structural delta permitted across all adaptation paths. |
| `defaultThreshold` | `$Number` | -- | The default threshold value being overridden. |
| `derivedRiskLevel` | `$EnumeratedToken` | `$Standard`, `$Elevated`, `$Critical` | Risk level derived from the element's role and protection level. |
| `elementReference` | `$Text` | -- | Stable textual identifier for this element within the plan. |
| `elements` | `$List<$Text>` | -- | List of element references that this concept applies to. |
| `encodingCompatibility` | `$List<$EnumeratedToken>` | `$Position`, `$Size`, `$Value`, `$Shape`, `$Hue`, `$Texture`, `$Orientation` | Visual encoding channels compatible with this element's role. |
| `hardness` | `$EnumeratedToken` | `$Soft`, `$Hard` | Whether this constraint is relaxable (soft) or inviolable (hard). |
| `invariantType` | `$EnumeratedToken` | `$SemanticReadingOrder`, `$IntraGroupSeparation`, `$RoleEncodingStability`, `$FigureDominance`, `$ContainerBoundaryIntegrity` | Category of perceptual invariant. |
| `level` | `$EnumeratedToken` | 24 ordinal values (`$ProximityTight` through `$NegativeSpaceGenerous`) | Ordinal level of the constraint's design intent. |
| `lexisVersion` | `$Text` | -- | Lexis version that produced this plan. |
| `maxStructuralDelta` | `$Number` | -- | Maximum structural delta permitted for a single adaptation rule or the entire plan. |
| `operator` | `$EnumeratedToken` | `$Proximity`, `$Contrast`, `$Alignment`, `$Repetition`, `$Separation`, `$Foregrounding`, `$Grouping`, `$NegativeSpace` | Design operator governing this constraint or threshold override. |
| `ordinalLevel` | `$EnumeratedToken` | 24 ordinal values (`$ProximityTight` through `$NegativeSpaceGenerous`) | Ordinal level at which this threshold override applies. |
| `parentElement` | `$Iri` | -- | IRI of the parent element in the plan element hierarchy. |
| `protectionLevel` | `$EnumeratedToken` | `$Standard`, `$Elevated`, `$Protected` | Degree of protection against adaptation for this element. |
| `referenceTarget` | `$Iri` | -- | IRI of the glossary entry this reference resolves to. |
| `relativeTo` | `$List<$Text>` | -- | Element references that this constraint is measured relative to. |
| `replacementThreshold` | `$Number` | -- | The replacement threshold value for this operator at this ordinal level. |
| `resolvedDisplayText` | `$Text` | -- | Pre-resolved display text for the gloss reference. |
| `role` | `$EnumeratedToken` | 40 SDL roles (`$Rubric` through `$IdentityDisclosure`) | Semantic Design Language role assigned to this element. |
| `scope` | `$EnumeratedToken` | `$Composition`, `$View` | Whether this element originates from the composition or the view. |
| `sequentialIdentifierSignal` | `$Boolean` | -- | Whether this element participates in sequential identifier generation. |
| `solvedHardness` | `$EnumeratedToken` | `$Soft`, `$Hard` | Hardness of this constraint after solver processing. |
| `solvedLevel` | `$EnumeratedToken` | 24 ordinal values (`$ProximityTight` through `$NegativeSpaceGenerous`) | Ordinal level of this constraint after solver processing. |
| `solvedWeight` | `$Number` | -- | Weight of this constraint after solver processing. |
| `source` | `$EnumeratedToken` | `$Explicit`, `$RoleObligation` | Whether this constraint was authored explicitly or derived from a role obligation. |
| `sourceAnnotation` | `$Iri` | -- | IRI of the design annotation that produced this element or rule. |
| `sourceRole` | `$EnumeratedToken` | 40 SDL roles (`$Rubric` through `$IdentityDisclosure`) | SDL role that generated this constraint via role obligation. |
| `steps` | `$Number` | -- | Number of ordinal steps to relax a constraint. |
| `targetWeight` | `$Number` | -- | Weight value to assign to the targeted constraint when the rule fires. |
| `validationFamilies` | `$List<$EnumeratedToken>` | `$GroupingCoherence`, `$SalienceProportionality`, `$EntryClarity`, `$NavigationContinuity`, `$DisclosureIntegrity`, `$ProtectionCompleteness` | Validation families this constraint belongs to. |
| `value` | `$Text` | -- | Operand value in a predicate comparison. |
| `variable` | `$EnumeratedToken` | `$ViewportClass`, `$InputMode`, `$AccessibilityProfile`, `$Locale`, `$Intent`, `$Phase`, `$Density`, `$Confidence` | Runtime variable tested by a predicate. |
| `weight` | `$Number` | -- | Authored weight of this constraint before solver processing. |

## Design Decisions

- AdaptivePlan is MustBeEntity because foundries reference it by IRI as their sole input contract.
- PlanElement, PlanConstraint, PlanRule, AdaptationPath, and AccessibilityThresholdOverride are MustBeEntity because the foundry and solver reference them individually by IRI during layout resolution.
- AccessibilityConstraint, PerceptualInvariant, and ResolvedGlossReference are MustNotBeEntity because they are descriptive metadata consumed inline, not referenced individually.
- PlanPredicate, PlanWeightOperation, PlanFreezeOperation, PlanRelaxOperation, and PlanGuardOperation are Structural and MustNotBeEntity because they are positional children of PlanRule with no independent identity.
- The plan carries both unsolved (weight, level, hardness) and solved (solvedWeight, solvedLevel, solvedHardness) constraint values so the foundry has access to both the authored intent and the solver's resolution.
- Every IRI-typed trait (compositionTarget, sourceAnnotation, parentElement, constraintTarget, referenceTarget) references an external artifact or an entity within the plan, maintaining full provenance traceability from plan elements back to their source annotations.
