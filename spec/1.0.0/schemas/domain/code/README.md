Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Code

Computing notation for text spans and blocks: inline code, keyboard input, sample output, variables, and code blocks.

## When to Use

Use `CodeNotation` to define span-binding targets for computing-related text. Inline code concepts are Gloss span targets bound via `{~key}` or `{~key | label}` references. CodeBlock is a block-level content element placed by entity schemas.

## Concepts

### CodeNotation (Container)

Structural container for inline code notation definitions. Unordered, no duplicates.

### Span-Binding Concepts

These concepts forbid content. All require a `key` trait. All allow an optional `text` trait for Pattern B.

| Concept | Optional Traits | Description |
|---|---|---|
| Code | language | A span of computer code. The `language` trait identifies the programming language. |
| KeyboardInput | -- | Text representing what the user types (keyboard shortcuts, command input). |
| SampleOutput | -- | Text representing computer-generated output. |
| Variable | -- | A placeholder or variable name in instructional text. |

### Block-Level Concepts

| Concept | Required Traits | Optional Traits | Content | Description |
|---|---|---|---|---|
| CodeBlock | -- | key, language | The code text (whitespace preserved) | A block of computer code. Uses `whitespaceMode=$Preserve` to retain formatting. |

## Traits

| Trait | Type | Cardinality | Description |
|---|---|---|---|
| key | $LookupToken | Single | Gloss binding key for `{~key}` references. |
| text | $Text | Single | Display text for label-less Gloss references (Pattern B). |
| language | $EnumeratedToken | Single | Programming or markup language identifier (e.g. `$javascript`, `$python`, `$rust`). |

## Constraints

- CodeNotation must contain at least one child.

## Design Notes

- CodeBlock uses `whitespaceMode=$Preserve` because code formatting (indentation, line breaks) is semantically significant.
- CodeBlock is not a child of the CodeNotation container. It is a block-level content element placed by entity schemas.
- The `language` trait uses $EnumeratedToken so consuming schemas can constrain allowed values via a vocabulary of language identifiers.
- Code marks what something IS (computer code), not how it looks. The foundry decides rendering (monospace, syntax highlighting, etc.).

**End of Code v1.0.0**
