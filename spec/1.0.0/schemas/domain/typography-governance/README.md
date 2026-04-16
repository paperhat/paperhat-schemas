Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Typography Governance

Deterministic typography-governance primitives for Colophon. Defines typography systems, font families, font role bindings, font fallbacks, type scale definitions, scale mappings, and emphasis rules above retained substrate typographic values.

## When to Use

Use this package to author durable semantic grouping and role-governance state for retained typographic decisions. `paperhat-typography-governance` defines how a governed typography system is organized. It does not define accessibility policy, proof policy, audit bundles, or Colophon project assembly. Those belong in adjacent packages.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| TypographySystem | yes | Top-level governed typography domain containing font families, type scale definitions, font role bindings, scale mappings, emphasis rules, and font fallbacks. |
| FontFamily | yes | A governed typeface family entry carrying classification, foundry, and designer metadata. |
| FontRoleBinding | yes | Maps a semantic role to a font specification including family, weight, style, and OpenType feature settings. |
| OpenTypeFeatureSetting | no | One OpenType feature setting for a font role binding. |
| FontFallback | no | One entry in a fallback chain for a font role binding. |
| TypeScaleDefinition | yes | A governed modular type scale carrying base size, ratio, and level count. |
| ScaleMapping | no | Maps a semantic level name to a scale level index. |
| EmphasisRule | yes | Maps a CDL emphasis level to typographic treatment including weight, style, small caps, and underline. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| name | $Text | TypographySystem, FontFamily, TypeScaleDefinition | Human-readable name for the governed object. |
| typographySystemStatus | $EnumeratedToken | no | Lifecycle or governance status for a TypographySystem. |
| classification | $EnumeratedToken | FontFamily, FontFallback (optional) | Typeface classification. Allowed values: `$OldStyle`, `$Transitional`, `$Modern`, `$SlabSerif`, `$Grotesque`, `$NeoGrotesque`, `$Geometric`, `$Humanist`, `$Monospace`, `$Script`, `$Display`. |
| foundry | $Text | no | Type foundry that produced the font family. |
| designerName | $Text | no | Name of the typeface designer. |
| fontFamilyStatus | $EnumeratedToken | no | Lifecycle or governance status for a FontFamily. |
| key | $LookupToken | FontRoleBinding, EmphasisRule | Stable document-scoped lookup key. |
| role | $Text | FontRoleBinding | Semantic role name that the font role binding satisfies. |
| fontFamily | $Text | FontRoleBinding, FontFallback | Font family name referenced by the binding or fallback entry. |
| weight | $NonNegativeInteger | no | Font weight value for the binding or emphasis rule. |
| style | $EnumeratedToken | no | Font style for the binding or emphasis rule. Allowed values: `$Upright`, `$Italic`, `$Oblique`. |
| label | $Text | no | Human-readable display label. |
| fontRoleBindingStatus | $EnumeratedToken | no | Lifecycle or governance status for a FontRoleBinding. |
| featureTag | $Text | OpenTypeFeatureSetting | Four-character OpenType feature tag. |
| enabled | $Boolean | OpenTypeFeatureSetting | Whether the OpenType feature is enabled. |
| position | $NonNegativeInteger | FontFallback | Zero-based position of the fallback entry in the fallback chain. |
| baseSize | $Text | TypeScaleDefinition | Base font size for the type scale, carried as arbitrary-precision decimal text. |
| ratio | $Text | TypeScaleDefinition | Scale ratio for the type scale, carried as arbitrary-precision decimal text. |
| levels | $NonNegativeInteger | TypeScaleDefinition | Number of levels in the type scale. |
| typeScaleStatus | $EnumeratedToken | no | Lifecycle or governance status for a TypeScaleDefinition. |
| semanticLevel | $Text | ScaleMapping | Semantic level name mapped to a scale level index. |
| scaleLevel | $Integer | ScaleMapping | Scale level index (zero-based, negative values represent sub-base levels). |
| emphasisLevel | $Text | EmphasisRule | CDL emphasis level name that the rule governs. |
| useSmallCaps | $Boolean | no | Whether the emphasis rule activates small caps. |
| useUnderline | $Boolean | no | Whether the emphasis rule activates underline. |
| emphasisRuleStatus | $EnumeratedToken | no | Lifecycle or governance status for an EmphasisRule. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| TypographySystem | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the typography system. |
| TypographySystem | FontFamily | local | One or more governed font family entries. |
| TypographySystem | TypeScaleDefinition | local | Exactly one governed modular type scale. |
| TypographySystem | FontRoleBinding | local | One or more font role bindings mapping semantic roles to font specifications. |
| TypographySystem | ScaleMapping | local | One or more scale mappings from semantic level names to scale level indices. |
| TypographySystem | EmphasisRule | local | Zero or more emphasis rules mapping CDL emphasis levels to typographic treatment. |
| TypographySystem | FontFallback | local | Zero or more fallback chain entries. |
| FontFamily | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the font family. |
| FontRoleBinding | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the font role binding. |
| FontRoleBinding | OpenTypeFeatureSetting | local | Zero or more OpenType feature settings for the binding. |
| TypeScaleDefinition | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the type scale definition. |
| EmphasisRule | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the emphasis rule. |

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| description | `paperhat:domain:description` | Provides descriptive text for typography systems, font families, font role bindings, type scale definitions, and emphasis rules. |

## Design Notes

- `FontFamily`, `FontRoleBinding`, `TypeScaleDefinition`, and `EmphasisRule` are entities because Colophon requires stable identity for review, diff, reference, and governance work.
- `OpenTypeFeatureSetting`, `FontFallback`, and `ScaleMapping` are structural (non-entity) because they are positional or value-bearing children without independent identity.
- `baseSize` and `ratio` use `$Text` rather than a numeric type because they carry arbitrary-precision decimal values as strings, preserving exact authored precision without floating-point loss.
- `scaleLevel` uses `$Integer` (not `$NonNegativeInteger`) because negative scale levels represent sub-base sizes such as captions and footnotes.
- This package keeps typographic governance above substrate font values. It does not define font file loading, glyph rendering, or layout engine semantics.
- Policy objects are intentionally absent. Accessibility policy, proof policy, and other rule-governing objects belong in adjacent packages.

---

**End of Typography Governance v1.0.0**
