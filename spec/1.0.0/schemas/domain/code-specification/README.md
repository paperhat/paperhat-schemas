# Code Specification

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines a language-agnostic schema for authoring code specifications in Codex. A code specification declares product types, sum types, named constants, construction and accessor operations, validation rules, and test cases. The same document generates human-readable documentation through Lexis media foundries and executable code through Nexus code foundries. All field types reference Paperhat canonical type identifiers, preserving type identity from specification through RDF to generated code with zero erasure.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| CodeSpecification | Semantic | MustNotBeEntity | ForbidsContent | ProductType, SumType, NamedConstant, ConstructionOperation, AccessorOperation, UniformAccessorOperation, ValidationRule, ConstructionTestCase, RejectionTestCase, InequalityTestCase, OrderingTestCase, InteropModule | Root container for a complete code specification. |
| ProductType | Semantic | MustBeEntity | ForbidsContent | Field (1+), CanonicalOrderingRule (0–1) | A type whose instances carry all fields simultaneously. Projected as a struct in Rust, a record in Haskell. |
| SumType | Semantic | MustBeEntity | ForbidsContent | Variant (1+), CanonicalOrderingRule (0–1) | A type whose instances carry exactly one variant at a time. Projected as an enum in Rust, a data type in Haskell. |
| Variant | Semantic | MustNotBeEntity | ForbidsContent | Field (0+) | A variant of a sum type. Carries either named fields or wraps a single unnamed value. |
| Field | Semantic | MustNotBeEntity | ForbidsContent | — | A named, typed field belonging to a product type or a sum type variant. |
| NamedConstant | Semantic | MustBeEntity | ForbidsContent | — | A named constant value with a canonical type identifier. |
| CanonicalOrderingRule | Structural | MustNotBeEntity | ForbidsContent | ComparisonStep (0+), WithinVariantRule (0+) | Defines the canonical total ordering for a type. |
| WithinVariantRule | Structural | MustNotBeEntity | ForbidsContent | ComparisonStep (1+) | Defines the field comparison order within a specific variant of a sum type. |
| ComparisonStep | Semantic | MustNotBeEntity | ForbidsContent | — | A single step in a comparison chain: compare the values of a specific field. |
| ConstructionOperation | Semantic | MustBeEntity | ForbidsContent | OperationParameter (0+), ConstantBinding (0+), Precondition (0–1), ProhibitionPrecondition (0–1), ValueMapping (0–1) | An operation that constructs a value of a specific type and variant. |
| OperationParameter | Semantic | MustNotBeEntity | ForbidsContent | — | A parameter accepted by an operation. |
| ConstantBinding | Semantic | MustNotBeEntity | ForbidsContent | — | Binds a constant value to a target field during construction. |
| Precondition | Semantic | MustNotBeEntity | ForbidsContent | — | A validation-rule precondition on an operation parameter. |
| ProhibitionPrecondition | Semantic | MustNotBeEntity | ForbidsContent | — | A precondition that prohibits a parameter from equaling a specific constant. |
| ValueMapping | Semantic | MustNotBeEntity | ForbidsContent | — | Maps a boolean parameter to text values for the lexical form field. |
| AccessorOperation | Semantic | MustBeEntity | ForbidsContent | AccessorArm (1+) | An accessor operation that returns different values per variant of a sum type. |
| UniformAccessorOperation | Semantic | MustBeEntity | ForbidsContent | — | An accessor operation that returns the same-named field from every variant of a sum type. |
| AccessorArm | Semantic | MustNotBeEntity | ForbidsContent | — | One arm of a variant accessor: specifies what a specific variant returns. |
| ValidationRule | Semantic | MustBeEntity | ForbidsContent | — | A named validation rule with formal semantics. The foundry generates a validation function; conformance tests verify correctness. |
| ConstructionTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+), ExpectedAccessorResult (0+) | A test that constructs a value and asserts accessor results. |
| RejectionTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+) | A test that asserts an operation rejects invalid input. |
| InequalityTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestValue (2) | A test that asserts two constructed values are not equal. |
| OrderingTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestValue (2) | A test that asserts one constructed value is less than another. |
| TestValue | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+) | A value constructed for use in a test case. |
| TestArgument | Semantic | MustNotBeEntity | ForbidsContent | — | An argument passed to an operation in a test case. |
| ExpectedAccessorResult | Semantic | MustNotBeEntity | ForbidsContent | — | An expected result from calling an accessor on a constructed value. |
| InteropModule | Semantic | MustNotBeEntity | ForbidsContent | — | A language-specific interop module. Foundries for the target language generate the interop code; other foundries ignore it. |

## Imports

This schema has no imports. It is entirely self-contained.

## Traits

| Trait | Value Type | Priority | Description |
|---|---|---|---|
| `key` | `$LookupToken` | Primary | Stable lookup key for cross-referencing. |
| `title` | `$Text` | Primary | Title of the code specification. |
| `version` | `$SemanticVersion` | Primary | Semantic version of the specification. |
| `license` | `$Text` | Primary | License identifier for the specification. |
| `description` | `$Text` | Secondary | Human-readable description. |
| `name` | `$Text` | Primary | Name of a type, variant, field, operation, or constant. |
| `testName` | `$Text` | Primary | Name of a test case. |
| `exported` | `$Boolean` | Primary | Whether the construct is part of the public interface. |
| `position` | `$NonNegativeInteger` | Primary | Ordinal position within a parent container. |
| `valueType` | `$Iri` | Primary | Canonical type identifier for a field or constant value. |
| `elementType` | `$Iri` | Secondary | Canonical type identifier for elements within a collection-typed field. |
| `wrapsType` | `$Iri` | Primary | The single type that a newtype variant wraps. |
| `capabilities` | `$List<$EnumeratedToken>` | Primary | Type capabilities (Equality, Hashing, Cloning, CanonicalOrdering, Debugging). |
| `specSection` | `$Text` | Secondary | Section reference within the governing specification. |
| `specRequirement` | `$LookupToken` | Secondary | Requirement identifier within the governing specification. |
| `strategy` | `$EnumeratedToken` | Primary | Ordering strategy (FieldByFieldComparison, VariantThenFieldComparison, DelegateToField). |
| `delegateField` | `$LookupToken` | Primary | The field to delegate comparison to when strategy is DelegateToField. |
| `compareField` | `$LookupToken` | Primary | The field whose values are compared in this comparison step. |
| `forVariant` | `$LookupToken` | Primary | The variant this rule or arm applies to. |
| `producesType` | `$Iri` | Primary | Canonical type identifier of the type this operation constructs. |
| `producesVariant` | `$LookupToken` | Primary | The variant this operation constructs. |
| `mapsToField` | `$LookupToken` | Secondary | The target field this parameter maps to during construction. |
| `targetField` | `$LookupToken` | Primary | The field that receives a constant binding or value mapping. |
| `boundConstant` | `$LookupToken` | Primary | The named constant bound to a field during construction. |
| `belongsToType` | `$Iri` | Primary | Canonical type identifier of the type this accessor belongs to. |
| `returnType` | `$Iri` | Primary | Canonical type identifier of the value this accessor returns. |
| `accessesFieldNamed` | `$Text` | Primary | The field name accessed uniformly across all variants. |
| `returnsField` | `$LookupToken` | Primary | The field this accessor arm returns. |
| `returnsConstant` | `$LookupToken` | Primary | The named constant this accessor arm returns. |
| `validationRule` | `$LookupToken` | Primary | The validation rule applied as a precondition. |
| `appliesToParameter` | `$LookupToken` | Primary | The operation parameter the precondition validates. |
| `appliesToType` | `$Iri` | Primary | Canonical type identifier the validation rule validates. |
| `failureMessage` | `$Text` | Primary | Human-readable error message when a precondition fails. |
| `parameterToCheck` | `$LookupToken` | Primary | The parameter checked by a prohibition precondition. |
| `prohibitedConstant` | `$LookupToken` | Primary | The constant value that the parameter is prohibited from equaling. |
| `whenTrue` | `$Text` | Primary | The text value mapped when a boolean parameter is true. |
| `whenFalse` | `$Text` | Primary | The text value mapped when a boolean parameter is false. |
| `semantics` | `$Text` | Primary | Formal semantic description of a validation rule. |
| `validationPattern` | `$RegularExpression` | Primary | Regular expression pattern for pattern-based validation rules. |
| `value` | `$Text` | Primary | The literal value of a constant or test argument. |
| `operation` | `$LookupToken` | Primary | The construction operation invoked in a test case. |
| `accessor` | `$LookupToken` | Primary | The accessor whose result is asserted in an expected result. |
| `expectedValue` | `$Text` | Primary | The expected string representation of an accessor result. |
| `expectedFailureContaining` | `$Text` | Primary | A substring that the rejection error message is expected to contain. |
| `role` | `$EnumeratedToken` | Primary | The role of a test value (Left, Right, Lesser, Greater). |
| `conditionalOn` | `$Text` | Primary | The language or platform condition that activates this interop module. |
| `targetLibrary` | `$Text` | Primary | The external library or framework this interop module targets. |

## Enumerated Value Sets

| Set | Values | Description |
|---|---|---|
| Capability | Equality, Hashing, Cloning, CanonicalOrdering, Debugging | Type-level capabilities that a product type or sum type declares. |
| OrderingStrategy | FieldByFieldComparison, VariantThenFieldComparison, DelegateToField | Strategies for defining the canonical total ordering of a type. |
| TestValueRole | Left, Right, Lesser, Greater | The role a test value plays in a comparison or inequality test case. |

## Constraints

| Constraint | Target | Rule |
|---|---|---|
| variant-fields-or-wraps | Variant | A variant carries either named fields or wraps a single type, not both. |
| accessor-arm-returns-one | AccessorArm | An accessor arm returns either a field or a constant, not both. |

## Design Decisions

- CodeSpecification is MustNotBeEntity because it is a root document container, not a referenceable entity. The types, operations, and constants within it are the entities.
- ProductType and SumType are separate concepts rather than one type with a discriminator trait. The structural differences (variants, field exclusivity, ordering semantics) are fundamental, not parametric.
- All field type references use `$Iri` pointing to Paperhat canonical type identifiers. This preserves type identity across the specification-to-code pipeline without lossy string matching.
- Validation rules carry formal `semantics` as prose text rather than an executable expression language. The foundry interprets semantics into language-specific validation code. A future version introduces a structured constraint expression language if the prose-based approach proves insufficient.
- Test cases are first-class schema concepts, not external artifacts. This ensures that the specification and its tests are always co-located, versioned together, and processable by the same foundry pipeline.
- CanonicalOrderingRule supports three strategies to cover the common patterns: field-by-field comparison for product types, variant-then-field comparison for sum types, and single-field delegation for wrapper types.
- InteropModule uses `conditionalOn` as a text string rather than a structured language enum. The set of target languages is open-ended and foundry-specific; the schema does not enumerate it.
- AccessorArm enforces a mutual exclusion constraint: it returns either a field or a constant, never both. This is enforced at the schema level through the `accessor-arm-returns-one` constraint rather than through separate concept types.
