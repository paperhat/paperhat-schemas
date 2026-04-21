# Code Specification

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines a language-agnostic schema for authoring code specifications in Codex. A code specification is the single normative source for any Paperhat product: substrate libraries, extension libraries, application workbenches, foundries, language processors, stores, solvers, and graphical, terminal, and command-line interfaces. It declares product types, primitive types, sum types, named constants, operations, validation rules, formal surface grammars, normative requirements, terminology definitions, external references, module descriptions, and conformance cases. The same document generates human-readable documentation through Lexis media foundries and executable implementations in every target language through Nexus code foundries. All field types reference Paperhat canonical type identifiers, preserving type identity from specification through RDF to generated code with zero erasure.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| CodeSpecification | Semantic | MustNotBeEntity | ForbidsContent | ProductType, PrimitiveType, SumType, NamedConstant, ConstructionOperation, AccessorOperation, UniformAccessorOperation, ValidationRule, grammar:Grammar, ConstructionTestCase, RejectionTestCase, InequalityTestCase, OrderingTestCase, OperationConformanceCase, InteropModule, ModuleDescription, NormativeRequirement, TermDefinition, ExternalReference | Root container for a complete code specification. |
| ProductType | Semantic | MustBeEntity | ForbidsContent | Field (1+), CanonicalOrderingRule (0–1), TypeParameter (0+) | A type whose instances carry all fields simultaneously. Projected as a struct in Rust, a record in Haskell. |
| PrimitiveType | Semantic | MustBeEntity | ForbidsContent | — | An atomic type whose instances are indivisible values rather than records or variants. Projected as a native atomic value according to `representationKind`. |
| SumType | Semantic | MustBeEntity | ForbidsContent | Variant (1+), CanonicalOrderingRule (0–1), TypeParameter (0+) | A type whose instances carry exactly one variant at a time. Projected as an enum in Rust, a data type in Haskell. |
| Variant | Semantic | MustNotBeEntity | ForbidsContent | Field (0+) | A variant of a sum type. Carries either named fields or wraps a single unnamed value. |
| Field | Semantic | MustNotBeEntity | ForbidsContent | — | A named, typed field belonging to a product type or a sum type variant. |
| TypeParameter | Semantic | MustNotBeEntity | ForbidsContent | — | A type parameter declared on a product type or sum type. |
| NamedConstant | Semantic | MustBeEntity | ForbidsContent | — | A named constant value with a canonical type identifier. |
| CanonicalOrderingRule | Structural | MustNotBeEntity | ForbidsContent | ComparisonStep (0+), WithinVariantRule (0+) | Defines the canonical total ordering for a type. For sum types, same-variant comparison uses field-order rules for fielded variants, wrapped-value comparison for wrapped variants, and equality for unit variants. |
| WithinVariantRule | Structural | MustNotBeEntity | ForbidsContent | ComparisonStep (1+) | Defines the field comparison order within one field-bearing variant of a sum type. |
| ComparisonStep | Semantic | MustNotBeEntity | ForbidsContent | — | A single step in a comparison chain: compare the values of a specific field. |
| ConstructionOperation | Semantic | MustBeEntity | ForbidsContent | OperationParameter (0+), ConstantBinding (0+), Precondition (0+), ProhibitionPrecondition (0–1), ValueMapping (0–1), behavior:Calculation (0–1) | A pure operation that produces a value of a specific type. Constructors, parsers, planners, evaluators, transitions, formatters, and other deterministic operations all use this concept. `producesVariant` identifies the produced variant when the result type is a sum type. For `PrimitiveType` targets, an optional `behavior:Calculation` child defines the produced primitive value. |
| OperationParameter | Semantic | MustNotBeEntity | ForbidsContent | — | A parameter accepted by an operation. |
| ConstantBinding | Semantic | MustNotBeEntity | ForbidsContent | — | Binds a constant value to a target field during construction. |
| Precondition | Semantic | MustNotBeEntity | ForbidsContent | — | A validation-rule precondition on an operation parameter. |
| ProhibitionPrecondition | Semantic | MustNotBeEntity | ForbidsContent | — | A precondition that prohibits a parameter from equaling a specific constant. |
| ValueMapping | Semantic | MustNotBeEntity | ForbidsContent | — | Maps a boolean parameter to text values for the lexical form field. |
| AccessorOperation | Semantic | MustBeEntity | ForbidsContent | AccessorArm (1+) | An accessor operation that returns different values per variant of a sum type. |
| UniformAccessorOperation | Semantic | MustBeEntity | ForbidsContent | — | An accessor operation that returns a field with a stable name from a product type or from every variant of a sum type that exposes that field. |
| AccessorArm | Semantic | MustNotBeEntity | ForbidsContent | — | One arm of a variant accessor: specifies what a specific variant returns. |
| ValidationRule | Semantic | MustBeEntity | ForbidsContent | behavior:Validation (0–1) | A named validation rule with a behavior expression tree as the single normative definition. The code foundry generates a validation function from the expression tree. The media foundry generates a human-readable description from the expression tree. |
| ConstructionTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+), ExpectedAccessorResult (0+) | A test that constructs a value and asserts accessor results. |
| RejectionTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+) | A test that asserts an operation rejects invalid input. |
| InequalityTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestValue (2) | A test that asserts two constructed values are not equal. |
| OrderingTestCase | Semantic | MustNotBeEntity | ForbidsContent | TestValue (2) | A test that asserts one constructed value is less than another. |
| TestValue | Semantic | MustNotBeEntity | ForbidsContent | TestArgument (0+) | A value constructed for use in a test case. |
| TestArgument | Semantic | MustNotBeEntity | ForbidsContent | — | An argument passed to an operation in a test case. |
| ExpectedAccessorResult | Semantic | MustNotBeEntity | ForbidsContent | — | An expected result from calling an accessor on a constructed value. |
| OperationConformanceCase | Semantic | MustNotBeEntity | ForbidsContent | OperationArgument (0+), ExpectedOperationValue (0–1), ExpectedDiagnosticValue (0–1) | A test that invokes any operation with exact typed arguments and asserts one exact success value or one exact diagnostic value. |
| OperationArgument | Semantic | MustNotBeEntity | RequiresContent | — | One typed argument supplied to an operation conformance case. The content is the canonical Codex literal or canonical Codex fragment for the argument value. Product values use the product tag; primitive fields may be attributes; complex fields use field-named child wrappers. Sum values use the selected variant tag. Wrapped variants contain one child fragment for the wrapped value. Ordered list fields use one field-named wrapper containing the ordered child fragments. |
| ExpectedOperationValue | Semantic | MustNotBeEntity | RequiresContent | — | The exact success value expected from an operation conformance case. The content is the canonical Codex literal or canonical Codex fragment for the returned value. Product, sum, wrapped-variant, and ordered-list encoding follow the same canonical fragment rules defined for OperationArgument. |
| ExpectedDiagnosticValue | Semantic | MustNotBeEntity | RequiresContent | — | The exact diagnostic value expected from an operation conformance case. The content is the canonical Codex fragment for the returned diagnostic value. Product, sum, wrapped-variant, and ordered-list encoding follow the same canonical fragment rules defined for OperationArgument. |
| InteropModule | Semantic | MustNotBeEntity | ForbidsContent | — | A language-specific interop module. Foundries for the target language generate the interop code; other foundries ignore it. |
| ModuleDescription | Structural | MustNotBeEntity | ForbidsContent | — | Describes a source module in the generated code. The foundry uses module descriptions to generate module-level documentation comments. |
| NormativeRequirement | Semantic | MustBeEntity | ForbidsContent | — | A normative requirement that governs the specification as a whole or defines a cross-cutting policy, behavioral mandate, or contract clause not tied to a specific type or operation. |
| TermDefinition | Semantic | MustBeEntity | ForbidsContent | — | A formal terminology definition that establishes the precise meaning of a term used throughout the specification. |
| ExternalReference | Semantic | MustNotBeEntity | ForbidsContent | — | A reference to an external standard, specification, or resource that this code specification depends on or cites. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| behavior | `paperhat:behavior:expression` | Provides the `Calculation` and `Validation` expression containers for construction-operation and validation-rule behavior expression trees. |
| grammar | `paperhat:domain:formal-grammar` | Provides exact surface-grammar containers and production rules for syntax-governed specifications. |

## Traits

| Trait | Value Type | Priority | Description |
|---|---|---|---|
| `key` | `$LookupToken` | Primary | Stable lookup key for cross-referencing. |
| `title` | `$Text` | Primary | Title of the code specification. |
| `version` | `$SemanticVersion` | Primary | Semantic version of the specification. |
| `license` | `$Text` | Primary | License identifier for the specification. |
| `description` | `$Text` | Secondary | Human-readable description. |
| `longDescription` | `$Text` | Secondary | Extended human-readable description. |
| `contentTransformer` | `$Iri` | Primary | IRI of the content transformer that generates human-readable documentation from this code specification. Lexis runs the transformer before composition. |
| `name` | `$Text` | Primary | Name of a type, variant, field, operation, or constant. |
| `testName` | `$Text` | Primary | Name of a test case. |
| `exported` | `$Boolean` | Primary | Whether the construct is part of the public interface. |
| `position` | `$NonNegativeInteger` | Primary | Ordinal position within a parent container. |
| `parameterName` | `$Text` | Secondary | The parameter name associated with an operation conformance argument. |
| `valueType` | `$Iri` | Primary | Canonical type identifier for a field, constant, argument value, or expected result value. |
| `elementType` | `$Iri` | Secondary | Canonical type identifier for elements within a collection-typed field. |
| `wrapsType` | `$Iri` | Primary | The single type that a newtype variant wraps. |
| `capabilities` | `$List<$EnumeratedToken>` | Primary | Type capabilities (Equality, Hashing, Cloning, CanonicalOrdering, Debugging). |
| `representationKind` | `$EnumeratedToken` | Primary | Primitive representation category (Boolean, Text, Integer, NonNegativeInteger, Decimal). |
| `specSection` | `$Text` | Secondary | Section reference within the governing specification. |
| `specRequirement` | `$LookupToken` | Secondary | Requirement identifier within the governing specification. |
| `strategy` | `$EnumeratedToken` | Primary | Ordering strategy. `FieldByFieldComparison` and `DelegateToField` apply to product types. `VariantThenFieldComparison` applies to sum types. |
| `delegateField` | `$LookupToken` | Primary | The field to delegate comparison to when strategy is DelegateToField. |
| `compareField` | `$LookupToken` | Primary | The field whose values are compared in this comparison step. |
| `forVariant` | `$LookupToken` | Primary | The variant this rule or arm applies to. |
| `producesType` | `$Iri` | Primary | Canonical type identifier of the type this operation produces. |
| `producesVariant` | `$LookupToken` | Primary | The produced variant when the result type is a sum type. |
| `fallible` | `$Boolean` | Primary | Whether the operation returns a diagnostic result instead of total success. |
| `diagnosticVariant` | `$LookupToken` | Primary | The diagnostic variant returned by a fallible operation or exact diagnostic expectation. |
| `diagnosticType` | `$Iri` | Primary | Canonical type identifier of the diagnostic type associated with the specification. |
| `optional` | `$Boolean` | Primary | Whether a field or operation result is optional. |
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
| `validationPattern` | `$RegularExpression` | Primary | Regular expression pattern for pattern-based validation rules (convenience shorthand; the behavior expression tree is the normative definition). |
| `value` | `$Text` | Primary | The literal value of a constant or test argument. |
| `operation` | `$LookupToken` | Primary | The construction operation invoked in a test case. |
| `accessor` | `$LookupToken` | Primary | The accessor whose result is asserted in an expected result. |
| `expectedValue` | `$Text` | Primary | The expected string representation of an accessor result. |
| `expectedFailureContaining` | `$Text` | Primary | A substring that the rejection error message is expected to contain. |
| `role` | `$EnumeratedToken` | Primary | The role of a test value (Left, Right, Lesser, Greater). |
| `conditionalOn` | `$Text` | Primary | The language or platform condition that activates this interop module. |
| `targetLibrary` | `$Text` | Primary | The external library or framework this interop module targets. |
| `modality` | `$EnumeratedToken` | Primary | The normative modality of a requirement (Must, MustNot). |
| `rationale` | `$Text` | Secondary | The reasoning behind a normative requirement. |
| `term` | `$Text` | Primary | The term being defined in a term definition. |
| `label` | `$Text` | Primary | Human-readable label for an external reference. |
| `uri` | `$Iri` | Primary | The IRI or URN of a referenced external resource. |

## Enumerated Value Sets

| Set | Values | Description |
|---|---|---|
| Capability | Equality, Hashing, Cloning, CanonicalOrdering, Debugging | Type-level capabilities that a product type or sum type declares. |
| PrimitiveRepresentationKind | Boolean, Text, Integer, NonNegativeInteger, Decimal | Primitive representation categories for atomic types. |
| OrderingStrategy | FieldByFieldComparison, VariantThenFieldComparison, DelegateToField | Strategies for defining the canonical total ordering of a type. |
| TestValueRole | Left, Right, Lesser, Greater | The role a test value plays in a comparison or inequality test case. |
| Modality | Must, MustNot | The normative modality of a requirement. |

## Constraints

| Constraint | Target | Rule |
|---|---|---|
| variant-fields-or-wraps | Variant | A variant carries either named fields or wraps a single type, not both. |
| accessor-arm-returns-one | AccessorArm | An accessor arm returns either a field or a constant, not both. |
| operation-conformance-has-one-expected | OperationConformanceCase | An operation conformance case expects either one success value or one diagnostic value. |
| primitive-construction-operation-shape | ConstructionOperation | A construction operation that produces a primitive type uses `behavior:Calculation`, must not use `producesVariant`, and must not use ConstantBinding or ValueMapping. |
| field-by-field-ordering-shape | CanonicalOrderingRule | `FieldByFieldComparison` is valid only under `ProductType`, must not use `delegateField`, and must not contain `WithinVariantRule`. |
| variant-then-field-ordering-shape | CanonicalOrderingRule | `VariantThenFieldComparison` is valid only under `SumType`, must not use `delegateField`, and must not contain top-level `ComparisonStep` children. |
| delegate-ordering-shape | CanonicalOrderingRule | `DelegateToField` is valid only under `ProductType`, requires `delegateField`, and must not contain `ComparisonStep` or `WithinVariantRule`. |

## Design Decisions

- CodeSpecification is MustNotBeEntity because it is a root document container, not a referenceable entity. The types, operations, and constants within it are the entities.
- ProductType and SumType are separate concepts rather than one type with a discriminator trait. The structural differences (variants, field exclusivity, ordering semantics) are fundamental, not parametric.
- PrimitiveType exists separately from ProductType and SumType because atomic values are not records or tagged alternatives. Primitive construction is calculation-based and carries an explicit `representationKind` so host-language lowering remains exact.
- All field type references use `$Iri` pointing to Paperhat canonical type identifiers. This preserves type identity across the specification-to-code pipeline without lossy string matching.
- Validation rules carry a behavior expression tree (from the `paperhat:behavior:expression` schema) as the single normative definition. The code foundry generates validation functions from the expression tree. The media foundry generates human-readable descriptions from the expression tree. The `semantics` prose trait is removed. The `validationPattern` trait remains as a convenience shorthand for simple pattern-based rules, but the behavior expression is the normative authority when both are present.
- Surface-grammar definitions are imported from the formal-grammar schema rather than redefined locally. Code specifications use those grammar nodes when exact parser behavior is part of the normative contract.
- Test cases are first-class schema concepts, not external artifacts. This ensures that the specification and its tests are always co-located, versioned together, and processable by the same foundry pipeline.
- OperationConformanceCase exists alongside the constructor-focused legacy test cases because parser, formatter, planner, evaluator, and transition operations require exact typed arguments and exact structured outcomes that simple accessor assertions cannot express without guesswork.
- Canonical operation-conformance fragments use one uniform encoding rule: product values use the product tag, complex fields use field-named child wrappers, sum values use variant tags, wrapped variants contain the wrapped child fragment, and ordered list fields contain ordered child fragments inside one field-named wrapper.
- CanonicalOrderingRule supports three strategies to cover the common patterns: field-by-field comparison for product types, variant-then-field comparison for sum types, and single-field delegation for one named product field. For wrapped sum variants, `VariantThenFieldComparison` compares the wrapped values directly after variant-position comparison.
- InteropModule uses `conditionalOn` as a text string rather than a structured language enum. The set of target languages is open-ended and foundry-specific; the schema does not enumerate it.
- AccessorArm enforces a mutual exclusion constraint: it returns either a field or a constant, never both. This is enforced at the schema level through the `accessor-arm-returns-one` constraint rather than through separate concept types.
- NormativeRequirement is MustBeEntity because requirements have stable IRI identifiers used for cross-referencing, traceability, and conformance auditing. Requirements express cross-cutting policies, behavioral mandates, and contract clauses that are not structurally tied to a single type or operation.
- TermDefinition is MustBeEntity because definitions have stable IRI identifiers used for glossary generation and cross-referencing from requirement and type descriptions.
- ExternalReference is MustNotBeEntity because references are citation entries, not individually addressable semantic constructs. They appear in the generated references section and doc-comment links.
