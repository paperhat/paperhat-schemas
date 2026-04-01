Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Localization Schema

System-level schema that defines the structure of localization bundles.

## Overview

Localization bundles provide human-readable labels and descriptions for schema elements (concepts, traits, tokens, and constraints) in any natural language. Schemas carry only identifiers; every display string comes from a localization bundle. No language is structurally privileged.

## Concepts

- **LocalizationBundle** — Root container. Targets one schema, one language. Traits: `schema` (IRI), `schemaVersion` (text), `language` (`$LanguageTag`).
- **ConceptLocalization** — Label for a concept name. No content.
- **TraitLocalization** — Label for a trait name. Optional prose description as content.
- **TokenLocalization** — Label for a vocabulary token. Optional prose description as content.
- **ConstraintLocalization** — Label for a constraint. Optional prose description as content.

Within one bundle, `identifier` values are unique within each localization concept type.

## Pluralization

All label-bearing concepts support CLDR plural categories via optional traits: `label` (singular/default), `labelZero`, `labelTwo`, `labelFew`, `labelMany`, `labelOther`. Authors populate only the categories their language requires.

## Grammatical Gender

`ConceptLocalization` and `TraitLocalization` carry an optional `grammaticalGender` trait for languages with grammatical gender agreement.

## Bundle Location

Bundles live inside each schema package at `localizations/<language>.cdx` (e.g., `localizations/en.cdx`). Localization files are excluded from the package closure hash.

## Fallback Chain

1. Exact locale match (e.g., `language-tag("fr-CA")`)
2. General language match (e.g., `language-tag("fr")`)
3. English (`language-tag("en")`) as the universal fallback

English bundles must always exist.

## Design Notes

See [Localization Resource Model](../../../notes/localization-resource-model/index.md) for the full design rationale.

**End of Localization Schema v1.0.0**
