# Design Annotation

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

A DesignAnnotation attaches SDL semantic roles, CDL constraints, and PDL adaptive rules to the elements declared by a ViewDefinition or composition. Each annotation targets one view or composition and declares the perceptual relationships that the foundry solver enforces at render time. Adaptive rules modify constraint weights and behaviors in response to runtime conditions such as viewport class, input mode, or accessibility profile.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| DesignAnnotation | Semantic | MustBeEntity | ForbidsContent | Title (1), Description (0–1), DesignElement (1+), DesignConstraint (0+), AdaptiveRule (0+) | Root annotation entity targeting a view definition or composition. |
| DesignElement | Structural | MustNotBeEntity | ForbidsContent | — | Assigns a semantic role to one element from the target view or composition. |
| DesignConstraint | Semantic | MustBeEntity | ForbidsContent | — | Declares a perceptual constraint (proximity, contrast, alignment, and others) between elements. |
| AdaptiveRule | Semantic | MustBeEntity | ForbidsContent | Predicate (1+), WeightOperation (0+), FreezeOperation (0+), RelaxOperation (0+), GuardOperation (0+) | Conditionally modifies constraint behavior in response to runtime variables. |
| Predicate | Structural | MustNotBeEntity | ForbidsContent | — | A single Boolean condition that the adaptive rule evaluates. |
| WeightOperation | Structural | MustNotBeEntity | ForbidsContent | — | Sets the weight of a target constraint when the rule fires. |
| FreezeOperation | Structural | MustNotBeEntity | ForbidsContent | — | Locks a target constraint at its current level when the rule fires. |
| RelaxOperation | Structural | MustNotBeEntity | ForbidsContent | — | Relaxes a target constraint by a specified number of ordinal steps when the rule fires. |
| GuardOperation | Structural | MustNotBeEntity | ForbidsContent | — | Prevents a target constraint from being relaxed below its current level when the rule fires. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Title |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `target` | `$Iri` | — | IRI of the view definition or composition this annotation targets. |
| `maxStructuralDelta` | `$Number` | — | Maximum structural delta budget for the annotation or adaptive rule. |
| `elementReference` | `$Text` | — | Reference to the composition or view element being annotated. |
| `role` | `$EnumeratedToken` | `$Rubric`, `$Body`, `$Caption`, `$Label`, `$Annotation`, `$DataValue`, `$Media`, `$Exhibit`, `$Container`, `$Group`, `$Relation`, `$List`, `$PrimaryAction`, `$SecondaryAction`, `$DestructiveAction`, `$Reference`, `$Input`, `$Toggle`, `$Search`, `$Control`, `$Success`, `$Caution`, `$Issue`, `$Progress`, `$Notice`, `$CostDisclosure`, `$RiskDisclosure`, `$ConsentGate`, `$LegalDisclosure`, `$IdentityDisclosure` | Semantic role assigned to the element. |
| `operator` | `$EnumeratedToken` | `$Proximity`, `$Contrast`, `$Alignment`, `$Repetition`, `$Separation`, `$Foregrounding`, `$Grouping`, `$NegativeSpace` | Perceptual operator this constraint applies. |
| `level` | `$EnumeratedToken` | `$ProximityTight`, `$ProximityNear`, `$ProximityFar`, `$ContrastSoft`, `$ContrastClear`, `$ContrastStrong`, `$AlignmentLoose`, `$AlignmentAligned`, `$AlignmentLocked`, `$RepetitionLoose`, `$RepetitionCohesive`, `$RepetitionLocked`, `$SeparationSubtle`, `$SeparationClear`, `$SeparationStrong`, `$ForegroundingSubtle`, `$ForegroundingProminent`, `$ForegroundingDominant`, `$GroupingLoose`, `$GroupingCohesive`, `$GroupingLocked`, `$NegativeSpaceMinimal`, `$NegativeSpaceBalanced`, `$NegativeSpaceGenerous` | Ordinal intensity level for the constraint operator. |
| `elements` | `$List<$Text>` | — | Element references the constraint applies to. |
| `relativeTo` | `$List<$Text>` | — | Element references the constraint is measured against. |
| `weight` | `$Number` | — | Relative importance weight for constraint solving. |
| `variable` | `$EnumeratedToken` | `$ViewportClass`, `$InputMode`, `$AccessibilityProfile`, `$Locale`, `$Intent`, `$Phase`, `$Density` | Runtime variable the predicate evaluates. |
| `comparison` | `$EnumeratedToken` | `$Equal`, `$NotEqual`, `$MemberOf` | Comparison operator for the predicate. |
| `value` | `$Text` | — | The value to compare against. |
| `constraintTarget` | `$Iri` | — | IRI of the constraint this operation targets. |
| `targetWeight` | `$Number` | — | The weight to assign to the target constraint. |
| `steps` | `$Number` | — | Number of ordinal steps to relax the target constraint. |
| `confidenceFloor` | `$Number` | — | Minimum confidence threshold for rule application. |

## Design Decisions

- DesignAnnotation is MustBeEntity so that DesignPackage members reference it by IRI and the adaptive plan compiler resolves it as a standalone document.
- DesignElement is Structural and MustNotBeEntity because it is a positional child within the annotation, not a standalone referenceable unit.
- DesignConstraint is MustBeEntity so that adaptive rule operations reference individual constraints by IRI.
- The `role` enumeration uses the 30 SDL semantic roles (post-revision). Roles declare what an element IS, not how it appears.
- The `level` enumeration pairs each operator with three ordinal intensities (e.g., ProximityTight/Near/Far), giving the constraint solver a discrete, bounded space to explore.
- AdaptiveRule children are typed operations (WeightOperation, FreezeOperation, RelaxOperation, GuardOperation) rather than a generic operation concept with a type trait. This makes the schema self-documenting and the required traits for each operation explicit.
