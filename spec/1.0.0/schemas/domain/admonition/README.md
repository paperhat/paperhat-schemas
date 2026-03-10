Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Admonition

Callout-level semantic markers for informational notices, warnings, dangers, critical alerts, tips, and general notices.

## When to Use

Use `Admonitions` to define callout-level span-binding targets. Each admonition concept is a semantic marker indicating the significance level of the bound text. Bound from Gloss spans via `{~key}` or `{~key | label}` references.

## Concepts

### Admonitions (Container)

Structural container for admonition definitions. Unordered, no duplicates.

### Admonition Concepts

All concepts forbid content. All require a `key` trait. All allow optional `text` and `title` traits.

| Concept | Description |
|---|---|
| Informational | General informational callout. |
| Warning | Caution about potential issues or unintended consequences. |
| Danger | Serious risk of harm, data loss, or irreversible action. |
| Critical | Highest severity: system failure, safety hazard, or security breach. |
| Notice | General notice requiring attention but not implying risk. |
| Tip | Helpful suggestion, best practice, or shortcut. |

## Traits

| Trait | Type | Cardinality | Description |
|---|---|---|---|
| key | $LookupToken | Single | Gloss binding key for `{~key}` references. |
| text | $Text | Single | Display text for label-less Gloss references (Pattern B). |
| title | $Text | Single | Optional heading for the callout when rendered as a block. |

## Constraints

- Admonitions must contain at least one child.

## Design Notes

- Admonition concepts are semantic markers, not block containers. The foundry decides rendering (inline highlight, sidebar callout, icon, etc.).
- The `title` trait allows a custom heading. If absent, the foundry uses the concept name (e.g. "Warning") as the default heading.
- Severity increases: Informational < Notice < Tip < Warning < Danger < Critical. This ordering is a rendering hint, not a constraint.

**End of Admonition v1.0.0**
