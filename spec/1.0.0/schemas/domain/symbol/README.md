# Symbol

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines three semantically distinct symbol concepts for technical specifications: general typographic symbols (e.g. "§", "†", "©"), math symbols with variable-binding semantics (e.g. "let τ denote round-trip latency"), and emoji with cultural context metadata. A SymbolTable container collects them for structured tables-of-symbols sections.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Symbol | Semantic | MustBeEntity | ForbidsContent | Description | A typographic or technical symbol with its Unicode codepoint, canonical name, and optional description. |
| MathSymbol | Semantic | MustBeEntity | ForbidsContent | Description | A symbol used as a mathematical variable or operator, with meaning binding, optional unit, and domain. Supports the "let X denote Y" pattern common in specifications. |
| Emoji | Semantic | MustBeEntity | ForbidsContent | Description | An emoji character with its canonical name, codepoint, and optional cultural context notes. |
| SymbolTable | Semantic | MustNotBeEntity | ForbidsContent | Symbol (1+), MathSymbol (1+), Emoji (1+) | Container for a table of symbols. Uses union selector so all three types can be mixed. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing the symbol. |
| `glyph` | `$Text` | -- | The visual symbol character(s) (e.g. "§", "τ", "🔒"). |
| `symbolName` | `$Text` | -- | Canonical name (e.g. "section sign", "Greek small letter tau"). |
| `codepoint` | `$Text` | -- | Unicode codepoint in U+ notation (e.g. "U+00A7"). |
| `meaning` | `$Text` | -- | What the math symbol denotes in this specification's context. Required for MathSymbol. |
| `unit` | `$Text` | -- | Unit of measurement if the math symbol represents a quantity (e.g. "ms", "bytes"). |
| `domain` | `$Text` | -- | Mathematical or scientific domain (e.g. "set theory", "thermodynamics"). |
| `culturalContext` | `$Text` | -- | Cultural or contextual notes on emoji meaning and usage. |
| `label` | `$Text` | -- | Short display label for projection. |
| `tableTitle` | `$Text` | -- | Optional title for a SymbolTable container. |

## Design Decisions

- Three distinct concepts because the metadata shapes differ meaningfully: MathSymbol has meaning/unit/domain, Emoji has culturalContext, and plain Symbol needs neither.
- `glyph` is required on all three because a symbol definition without the actual glyph is meaningless. `symbolName` is also required for accessibility and machine processing.
- `codepoint` is optional because some symbols are multi-character sequences (e.g. combined emoji) or the author may not know the codepoint.
- `meaning` is required on MathSymbol because the entire purpose of a math symbol definition is to bind a symbol to a meaning ("let τ denote..."). Without it, it's just a Symbol.
- `unit` and `domain` are optional on MathSymbol: not all math symbols represent quantities with units, and domain categorization is helpful but not essential.
- All three are MustBeEntity for cross-referencing: inline occurrences of a symbol elsewhere in the document can reference back to its definition.
- SymbolTable parallels AbbreviationList in the abbreviation schema — a container with a union selector and no duplicates.
