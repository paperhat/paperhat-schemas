Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Color Governance

Deterministic color-governance primitives for Prism. Defines color systems, palettes, palette members, token sets, tokens, and semantic roles above retained substrate color values.

## When to Use

Use this package to author durable semantic grouping and role-governance state for retained colors. `paperhat-color-governance` defines how a governed color system is organized. It does not define accessibility policy, proof policy, audit bundles, or Prism project assembly. Those belong in adjacent packages.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| ColorSystem | yes | Top-level governed color domain containing palettes, token sets, and semantic roles. |
| Palette | yes | Ordered collection of retained color values with stable membership identity. |
| PaletteMember | yes | One stable palette entry carrying a retained color value. |
| TokenSet | yes | Ordered collection of published or publishable color-bearing tokens. |
| Token | yes | One stable named token carrying a retained color value and a semantic-role reference. |
| SemanticRole | yes | One stable governed role such as brand, surface, text, border, action, status, data-visualization, focus, or disabled. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| name | $Text | ColorSystem, Palette, TokenSet | Human-readable name for the governed object. |
| colorSystemKind | $EnumeratedToken | no | Open classification for a ColorSystem. |
| colorSystemStatus | $EnumeratedToken | no | Lifecycle or governance status for a ColorSystem. |
| paletteKind | $EnumeratedToken | no | Palette classification. Allowed values: `$Brand`, `$Semantic`, `$Neutral`, `$Diagnostic`. |
| paletteStatus | $EnumeratedToken | no | Lifecycle or governance status for a Palette. |
| key | $LookupToken | PaletteMember, Token, SemanticRole | Stable document-scoped lookup key. |
| label | $Text | PaletteMember, Token, SemanticRole | Human-readable display label. |
| colorValue | $Color | PaletteMember, Token | Retained substrate color value. |
| paletteMemberStatus | $EnumeratedToken | no | Lifecycle or governance status for a PaletteMember. |
| publicationIntent | $EnumeratedToken | TokenSet, Token | Publication-target intent. Allowed values: `$Css`, `$ApplicationTokens`, `$PrintSwatches`. |
| tokenSetStatus | $EnumeratedToken | no | Lifecycle or governance status for a TokenSet. |
| semanticRole | $Iri (reference trait) | Token | Reference to the SemanticRole governed by the token. |
| tokenKind | $EnumeratedToken | no | Open classification for a Token. |
| tokenStatus | $EnumeratedToken | no | Lifecycle or governance status for a Token. |
| roleType | $EnumeratedToken | SemanticRole | Base semantic role type. Allowed values: `$Brand`, `$Surface`, `$Text`, `$Border`, `$Action`, `$Status`, `$DataVisualization`, `$Focus`, `$Disabled`. |
| parentRole | $Iri (reference trait) | no | Optional reference to a parent SemanticRole for role-graph structure. |
| roleStatus | $EnumeratedToken | no | Lifecycle or governance status for a SemanticRole. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| ColorSystem | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the color system. |
| ColorSystem | Palette | local | One or more ordered palettes inside the governed system. |
| ColorSystem | SemanticRole | local | One or more governed semantic roles inside the system. |
| ColorSystem | TokenSet | local | Optional token sets for publication or application use. |
| Palette | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the palette. |
| Palette | PaletteMember | local | One or more ordered palette members. |
| TokenSet | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the token set. |
| TokenSet | Token | local | One or more ordered tokens. |
| SemanticRole | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the role. |

## Constraints

| Identifier | Description |
|---|---|
| token-reference-trait-allowed | `Token` allows only `semanticRole` as a reference trait. |
| token-reference-singleton | `Token` declares at most one reference trait. |
| token-semantic-role-target-type | `Token.semanticRole` targets `SemanticRole`. |
| token-semantic-role-must-resolve | `Token.semanticRole` resolves. |
| semantic-role-reference-trait-allowed | `SemanticRole` allows only `parentRole` as a reference trait. |
| semantic-role-reference-singleton | `SemanticRole` declares at most one reference trait. |
| semantic-role-parent-role-target-type | `SemanticRole.parentRole` targets `SemanticRole`. |
| semantic-role-parent-role-must-resolve | `SemanticRole.parentRole` resolves. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| description | `paperhat:domain:description` | Provides descriptive text for color systems, palettes, token sets, and semantic roles. |

## Design Notes

- `PaletteMember`, `Token`, and `SemanticRole` are entities because Prism requires stable identity for review, diff, reference, and governance work.
- This package keeps retained color values as `$Color` substrate values. It does not redefine color parsing, canonicalization, or gamut semantics.
- Policy objects are intentionally absent. Accessibility policy, proof policy, repair policy, and other rule-governing objects belong in `paperhat-color-policy`.
- `Token` carries a direct retained color value rather than a palette-member reference. This keeps publication-facing token semantics explicit and avoids making palettes the hidden authority for token color assignment.
- `SemanticRole.parentRole` gives the first version a role-graph hook without forcing a separate role-graph package.

---

**End of Color Governance v1.0.0**
