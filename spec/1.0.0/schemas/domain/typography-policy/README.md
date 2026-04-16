Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Typography Policy

Authored spacing, paragraph, and accessibility policy objects for Colophon. Defines spacing policies, paragraph policies, and typography accessibility policies as durable authored rule documents.

## When to Use

Use this package to author durable rule objects that govern spacing, paragraph composition, and typographic accessibility for Colophon. `paperhat-typography-policy` defines the policy objects themselves. It projects spacing governance, paragraph break and hyphenation governance, and typographic accessibility floors as authored documents. It does not bind those policies to a specific project object by reference, and it does not contain derived layout results or audit bundles.

## Concepts

| Concept | Entity | Description |
|---|---|---|
| SpacingPolicy | yes | First-class authored spacing policy carrying leading, baseline grid, paragraph spacing, and measure governance. |
| ParagraphPolicy | yes | First-class authored paragraph policy carrying alignment, hyphenation, and widow/orphan governance. |
| TypographyAccessibilityPolicy | yes | First-class authored typography accessibility policy carrying minimum size, leading, and measure floors. |

## Traits

| Trait | Type | Required On | Description |
|---|---|---|---|
| name | $Text | SpacingPolicy, ParagraphPolicy, TypographyAccessibilityPolicy | Human-readable policy name. |
| bodyLeading | $Text | SpacingPolicy | Body text leading value as an absolute point value or relative ratio string. |
| headingLeading | $Text | SpacingPolicy | Heading text leading value as an absolute point value or relative ratio string. |
| captionLeading | $Text | SpacingPolicy | Caption text leading value as an absolute point value or relative ratio string. |
| codeLeading | $Text | SpacingPolicy | Code text leading value as an absolute point value or relative ratio string. |
| baselineGridUnit | $Text | SpacingPolicy | Baseline grid unit as a point value string. |
| paragraphSpacing | $Text | SpacingPolicy | Inter-paragraph spacing as a point value string. |
| paragraphIndent | $Text | no | First-line paragraph indent as a point or em value string. |
| defaultMeasure | $Text | no | Default line measure as a character-width unit string. |
| minimumMeasure | $Text | no | Minimum line measure as a character-width unit string. |
| maximumMeasure | $Text | no | Maximum line measure as a character-width unit string. |
| spacingPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for a spacing policy. |
| defaultAlignment | $EnumeratedToken | ParagraphPolicy | Default text alignment. Allowed values: `$Left`, `$Right`, `$Center`, `$Justified`. |
| headingAlignment | $EnumeratedToken | ParagraphPolicy | Heading text alignment. Allowed values: `$Left`, `$Right`, `$Center`, `$Justified`. |
| minimumBeforeBreak | $NonNegativeInteger | ParagraphPolicy | Minimum number of lines before a page or column break. |
| minimumAfterBreak | $NonNegativeInteger | ParagraphPolicy | Minimum number of lines after a page or column break. |
| maximumConsecutiveHyphens | $NonNegativeInteger | ParagraphPolicy | Maximum number of consecutive hyphenated lines. |
| minimumWidowLines | $NonNegativeInteger | ParagraphPolicy | Minimum number of lines at the top of a page or column after a break. |
| minimumOrphanLines | $NonNegativeInteger | ParagraphPolicy | Minimum number of lines at the bottom of a page or column before a break. |
| justificationMethod | $Text | no | Justification algorithm name or identifier string. |
| paragraphPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for a paragraph policy. |
| minimumBodySize | $Text | TypographyAccessibilityPolicy | Minimum body text size as a point value string. |
| minimumCaptionSize | $Text | TypographyAccessibilityPolicy | Minimum caption text size as a point value string. |
| minimumLeadingRatio | $Text | TypographyAccessibilityPolicy | Minimum leading ratio as a decimal string. |
| minimumMeasureCharacters | $NonNegativeInteger | TypographyAccessibilityPolicy | Minimum line measure in characters. |
| maximumMeasureCharacters | $NonNegativeInteger | TypographyAccessibilityPolicy | Maximum line measure in characters. |
| minimumScaleLevelDifference | $Text | no | Minimum typographic scale level difference between adjacent hierarchy levels as a decimal string. |
| typographyAccessibilityPolicyStatus | $EnumeratedToken | no | Lifecycle or governance status for a typography accessibility policy. |

## Children

| Parent | Child | Source | Description |
|---|---|---|---|
| SpacingPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the spacing policy. |
| ParagraphPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the paragraph policy. |
| TypographyAccessibilityPolicy | description:Description | `paperhat:domain:description` | Human-readable descriptive text for the typography accessibility policy. |

## Constraints

`SpacingPolicy` requires `name`, `bodyLeading`, `headingLeading`, `captionLeading`, `codeLeading`, `baselineGridUnit`, and `paragraphSpacing`.

`ParagraphPolicy` requires `name`, `defaultAlignment`, `headingAlignment`, `minimumBeforeBreak`, `minimumAfterBreak`, `maximumConsecutiveHyphens`, `minimumWidowLines`, and `minimumOrphanLines`.

`TypographyAccessibilityPolicy` requires `name`, `minimumBodySize`, `minimumCaptionSize`, `minimumLeadingRatio`, `minimumMeasureCharacters`, and `maximumMeasureCharacters`.

`defaultAlignment` and `headingAlignment` accept exactly one of `$Left`, `$Right`, `$Center`, or `$Justified`.

Leading values (`bodyLeading`, `headingLeading`, `captionLeading`, `codeLeading`) are `$Text` strings carrying either absolute point values or relative ratios. The consuming application parses them using typography-spec types.

Size and ratio values (`minimumBodySize`, `minimumCaptionSize`, `minimumLeadingRatio`, `minimumScaleLevelDifference`) are `$Text` strings carrying decimal values.

## Imports

| Namespace | Schema | Purpose |
|---|---|---|
| description | `paperhat:domain:description` | Provides descriptive text for authored policy objects. |

## Design Notes

- This package projects authored typography governance rules directly as durable Codex documents.
- Concrete policy attachment belongs in higher-level composer packages such as `paperhat-colophon-project`, where project-local governance objects and policy objects coexist in one document.
- Leading, size, and ratio values use `$Text` because they carry string representations of decimal or point values. The consuming application parses these strings using the types defined in `typography-spec`.
- Derived layout results, accessibility audit reports, and governance bundles are intentionally absent. They belong in result-bundle packages.

---

**End of Typography Policy v1.0.0**
