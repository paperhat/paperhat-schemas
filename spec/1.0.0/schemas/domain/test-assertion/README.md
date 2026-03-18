# Test Assertion

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines test assertions for verifying conformance to specification requirements. Each assertion is linked to a requirement by IRI reference, carries a test execution status, test method, severity classification, and structured children for preconditions, expected outcomes, and test procedures. A TestSuite container groups related assertions. This schema supports the W3C Test Assertion model and is general enough for any standards body's conformance testing framework.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| TestAssertion | Semantic | MustBeEntity | ForbidsContent | Precondition, ExpectedOutcome, TestProcedure, Description, Paragraph | A verifiable assertion linked to a requirement. Cross-referenceable by key. |
| Precondition | Semantic | MustNotBeEntity | ForbidsContent | Paragraph (1+, ordered) | Conditions that must hold before the test executes. |
| ExpectedOutcome | Semantic | MustNotBeEntity | ForbidsContent | Paragraph (1+, ordered) | The expected result if the implementation conforms. |
| TestProcedure | Semantic | MustNotBeEntity | ForbidsContent | Paragraph (1+, ordered) | Step-by-step procedure for executing the test. |
| TestSuite | Semantic | MustNotBeEntity | ForbidsContent | TestAssertion (1+), Description, Paragraph | Named container grouping related test assertions. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `requirementRef` | `$Iri` | reference | Reference to the requirement entity this assertion verifies. |
| `title` | `$Text` | -- | Human-readable title. |
| `status` | `$EnumeratedToken` | AssertionStatus | Current test execution status. |
| `testMethod` | `$EnumeratedToken` | TestMethod | How the assertion is verified. |
| `severity` | `$EnumeratedToken` | AssertionSeverity | Impact severity if the assertion fails. |
| `label` | `$Text` | -- | Short display label. |

## Enumerated Value Sets

### AssertionStatus (5 members)

| Member | Description |
|---|---|
| `Untested` | The assertion has not been executed. |
| `Pass` | The implementation satisfies the assertion. |
| `Fail` | The implementation does not satisfy the assertion. |
| `NotApplicable` | The assertion does not apply to this implementation. |
| `Error` | The test did not complete due to an error in the test environment. |

### TestMethod (4 members)

| Member | Description |
|---|---|
| `Automated` | Verified by automated test tooling. |
| `Manual` | Verified by human tester following the test procedure. |
| `Inspection` | Verified by visual inspection or document review. |
| `Analysis` | Verified by analytical reasoning or formal proof. |

### AssertionSeverity (4 members)

| Member | Description |
|---|---|
| `Critical` | Failure blocks conformance; must pass. |
| `Major` | Significant conformance impact; expected to pass. |
| `Minor` | Low conformance impact; desirable to pass. |
| `Informational` | Informational check only; does not affect conformance. |

## Constraints

| Constraint | Target | Rule | Description |
|---|---|---|---|
| requirement-ref-must-resolve | TestAssertion | ReferenceMustResolve | The requirementRef must resolve to an existing entity. |

## Design Decisions

- `requirementRef` is a reference trait (`isReferenceTrait=true`) so that the link from assertion to requirement is machine-verifiable. The constraint enforces that the target exists.
- No `ReferenceTargetsConcept` constraint on requirementRef because the Requirement concept is defined in variant schemas outside this schema's import closure.
- `Precondition`, `ExpectedOutcome`, and `TestProcedure` are separate concepts rather than traits because they each carry structured prose (one or more paragraphs), not simple scalar values.
- `TestSuite` is MustNotBeEntity (unlike TestAssertion) because suites are organizational groupings, not individually cross-referenceable test artifacts.
- `Error` in AssertionStatus is distinct from `Fail`: Error means the test infrastructure failed, not that the implementation failed.
- `Analysis` in TestMethod covers formal verification approaches used in safety-critical standards (e.g. DO-178C, IEC 61508).
- `AssertionSeverity` maps to common conformance testing practice where not all assertions carry equal weight.
