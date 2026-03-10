Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# BCP 47 Language Tags

A closed vocabulary of language identification tags from IETF BCP 47 (RFC 5646).

## Purpose

Constrains `$EnumeratedToken` traits that identify the natural language of text content. Used by any concept that carries human-readable text and needs to declare its language for rendering, sorting, accessibility, or export.

## Token format

Tokens use the BCP 47 tag directly (e.g., `$en`, `$fr`, `$zh-Hans`). Primary language subtags are lowercase ISO 639-1 codes. Regional and script subtags follow the standard hyphen-delimited form (e.g., `$en-US`, `$pt-BR`, `$zh-Hant`).

## Scope

This vocabulary includes a curated set of the most widely used language tags covering all major world languages, EU official languages, and key regional variants. The full BCP 47 registry contains thousands of subtag combinations; this vocabulary covers the primary tags needed for general-purpose content authoring. It excludes retired language codes, grandfathered tags, and private-use subtags.

**End of BCP 47 Language Tags v1.0.0**
