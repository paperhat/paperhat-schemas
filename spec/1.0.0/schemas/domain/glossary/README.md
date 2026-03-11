# Glossary Schema

The glossary package defines concise glossary entries for specifications, documentation, and other corpora that bind a term to a definition.

## Schema Identifier

- `paperhat:domain:glossary`

## Concepts

- `GlossaryEntry`

## Traits

- `term`
- `key`

## Semantics

`GlossaryEntry` is a semantic entry that binds a term to a required definition body.

`term` carries the displayed term text.

`key` permits stable lookup-token references where a corpus uses keyed glossary references.
