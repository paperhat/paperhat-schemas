# Formal Grammar

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the structure for formal grammars embedded in technical specifications. Supports the major grammar notation families used in standards: IETF ABNF (RFC 5234), W3C EBNF, classic BNF, Parsing Expression Grammars (PEG), and custom notations. Each grammar is a container of named, cross-referenceable production rules whose bodies carry the notation-specific syntax as preserved-whitespace content.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Grammar | Semantic | MustBeEntity | ForbidsContent | ProductionRule (1+), Description, Paragraph | Container for a complete formal grammar. Declares the notation type and optional start symbol. |
| ProductionRule | Semantic | MustBeEntity | RequiresContent (Preserve) | Description, ProductionAlternative | A single production rule. Content carries the rule body in the grammar's notation. Cross-referenceable by key. |
| ProductionAlternative | Semantic | MustNotBeEntity | RequiresContent (Preserve) | -- | An alternative right-hand side for a production rule. Used when alternatives need individual annotation. |
| RuleReference | Semantic | MustNotBeEntity | ForbidsContent | -- | Inline cross-reference to a ProductionRule entity via reference trait. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing grammars and production rules. |
| `notation` | `$EnumeratedToken` | GrammarNotation | The formal notation used in this grammar. |
| `title` | `$Text` | -- | Human-readable title for the grammar. |
| `startSymbol` | `$Text` | -- | Name of the start production rule. |
| `ruleName` | `$Text` | -- | The nonterminal name of the production rule as it appears in the grammar notation. |
| `label` | `$Text` | -- | Short display label for projection. |
| `isTerminal` | `$Boolean` | -- | Whether this rule defines a terminal symbol. |
| `isStart` | `$Boolean` | -- | Whether this rule is the grammar's start symbol. |
| `target` | `$Iri` | reference | Reference to a ProductionRule entity. |

## Enumerated Value Sets

### GrammarNotation

| Member | Description |
|---|---|
| `ABNF` | Augmented Backus-Naur Form (RFC 5234). Standard for IETF protocol specifications. |
| `EBNF` | Extended Backus-Naur Form. Variants used by W3C (XML, XPath) and ISO 14977. |
| `BNF` | Classic Backus-Naur Form. |
| `PEG` | Parsing Expression Grammar. Unambiguous, prioritized-choice formalism. |
| `Custom` | A notation not covered by the standard options. The grammar description explains the custom notation. |

## Constraints

| Constraint | Target | Rule | Description |
|---|---|---|---|
| rule-reference-target-type | RuleReference | ReferenceTargetsConcept → ProductionRule | RuleReference target must resolve to a ProductionRule. |
| rule-reference-must-resolve | RuleReference | ReferenceMustResolve | RuleReference target must resolve to an existing entity. |

## Design Decisions

- Production rule bodies use `RequiresContent` with `$Preserve` whitespace mode because grammar notation is whitespace-sensitive (especially ABNF's continuation lines and EBNF's layout).
- `ProductionAlternative` is a separate concept (not just inline text) so that individual alternatives carry their own descriptions or annotations, which is common in specification grammars with prose explanations per alternative.
- `Grammar` is MustBeEntity so it is cross-referenceable from prose (e.g. "see Grammar G.1 for the message syntax").
- `ProductionRule` is MustBeEntity so RuleReference targets it. This supports the common pattern of hyperlinking nonterminal names to their definitions.
- `notation` is required on Grammar rather than optional because the rendering layer needs to know the notation family to format the grammar correctly.
- `startSymbol` is a text trait (not a reference) because it names a rule within the grammar's own scope. The `isStart` boolean on ProductionRule provides the complementary in-rule marker.
- The `Custom` notation value is an escape hatch for grammars that use a bespoke notation (e.g. railroad diagrams described textually, or domain-specific syntax).
