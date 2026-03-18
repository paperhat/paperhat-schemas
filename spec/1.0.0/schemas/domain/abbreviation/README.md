# Abbreviation

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines three semantically distinct shortened-form concepts for technical specifications: general abbreviations (e.g. "etc.", "approx."), initialisms (letter-by-letter, e.g. "U.S.A.", "HTML"), and acronyms (pronounced as words, e.g. "NASA", "LaTeX"). Each carries its short form, full expansion, and a stable key for cross-referencing. An AbbreviationList container collects them for structured list-of-abbreviations sections.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Abbreviation | Semantic | MustBeEntity | ForbidsContent | Description | General shortened form (e.g. "etc.", "approx.", "dept."). |
| Initialism | Semantic | MustBeEntity | ForbidsContent | Description | Shortened form spelled out letter by letter (e.g. "U.S.A.", "HTML", "CPU"). |
| Acronym | Semantic | MustBeEntity | ForbidsContent | Description | Shortened form pronounced as a word (e.g. "NASA", "LaTeX", "SCUBA"). Supports optional pronunciation trait. |
| AbbreviationList | Semantic | MustNotBeEntity | ForbidsContent | Abbreviation (1+), Initialism (1+), Acronym (1+) | Container for a list of abbreviations, initialisms, and acronyms. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing the abbreviated term. |
| `shortForm` | `$Text` | -- | The abbreviated form as written (e.g. "NASA", "U.S.A.", "etc."). |
| `expansion` | `$Text` | -- | The full expanded form (e.g. "National Aeronautics and Space Administration"). |
| `pronunciation` | `$Text` | -- | How the acronym is spoken aloud. Only meaningful for Acronym. |
| `label` | `$Text` | -- | Short display label for projection. |
| `language` | `$EnumeratedToken` | -- | Natural language of the abbreviation and its expansion. |
| `listTitle` | `$Text` | -- | Optional title for an AbbreviationList container. |

## Design Decisions

- Three distinct concepts rather than one concept with a "type" trait. The semantic difference between abbreviation, initialism, and acronym is meaningful: it affects how a projection layer handles the text (e.g. screen readers spell out initialisms but pronounce acronyms).
- `pronunciation` is only allowed on Acronym because initialisms are by definition spelled out and general abbreviations have conventional readings.
- All three are MustBeEntity so they are cross-referenceable from inline abbreviation usage elsewhere in the document.
- `shortForm` and `expansion` are both required traits. You cannot define an abbreviation without both pieces.
- AbbreviationList uses a union selector (`Abbreviation|Initialism|Acronym`) so all three types mix freely in a single list, which matches real specification practice.
- Description is allowed as a child for cases where the expansion alone is insufficient (e.g. explaining what an organization does, not just its name).
