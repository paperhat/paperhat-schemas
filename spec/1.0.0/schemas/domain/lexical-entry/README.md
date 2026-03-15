Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Lexical Entry

A lexical entry supporting full dictionary entries with multiple senses, parts of speech, etymology, inflected forms, and semantic relations.

## When to Use

Use `LexicalEntry` for lexicographic and dictionary-level content: entries with multiple senses, etymologies, inflected forms, and semantic relations to other terms. This is the schema for dictionaries, lexica, thesauri, and terminological databases.

Distinct from Definition (`paperhat:domain:definition`), which is a discourse primitive for formally defining a term. A Definition is a single definiendum-definiens pair. A LexicalEntry is a rich lexicographic structure.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| LexicalEntry | Semantic | $MustBeEntity | AllowsContentOrChildren (Flow) | Sense (0+), Etymology (0..1), LexicalForm (0+), LexicalRelation (0+) | The headword entry. Direct content holds a simple definition; Sense children hold structured multi-sense definitions. |
| Sense | Semantic | $MustNotBeEntity | RequiresContent (Flow) | UsageExample (0+) | One meaning of the term, optionally scoped by part of speech, register, or domain. Content is the definition text. |
| UsageExample | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | An illustrative sentence showing the term in context. |
| Etymology | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | The origin and historical development of the term. |
| LexicalForm | Semantic | $MustNotBeEntity | ForbidsContent | — | An inflected or alternate form of the headword. |
| LexicalRelation | Semantic | $MustNotBeEntity | ForbidsContent | — | A semantic relationship to another term. |

## LexicalEntry Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| term | $Text | yes | The headword or defined term. |
| key | $LookupToken | no | Machine-readable lookup key for Gloss cross-references, for example `~canonicalForm`. |

## Sense Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| partOfSpeech | $EnumeratedToken | no | Part of speech, for example `$Noun`, `$Verb`, `$Adjective`. Open vocabulary. |
| register | $EnumeratedToken | no | Usage register, for example `$Formal`, `$Informal`, `$Archaic`. Open vocabulary. |
| domain | $EnumeratedToken | no | Subject domain, for example `$Computing`, `$Law`, `$Medicine`. Open vocabulary. |

## LexicalForm Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| form | $Text | yes | The alternate form, for example "runs", "ran", "running". |
| formKind | $EnumeratedToken | no | The grammatical relationship to the headword, for example `$Plural`, `$PastTense`. Open vocabulary. |

## LexicalRelation Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| relatedTerm | $Text | yes | The related term as text. |
| relationKind | $EnumeratedToken | yes | The semantic relationship, for example `$Synonym`, `$Antonym`, `$Hypernym`. |
| target | $Iri | no | Entity reference to the related `LexicalEntry` if it exists in the corpus. |

## Constraints

- `LexicalEntry` requires either direct definition content or at least one `Sense` child.
- `LexicalRelation` allows only `target` as a reference trait.
- `LexicalRelation` must declare at most one reference trait.
- `LexicalRelation` target must resolve to an entity.
- `LexicalRelation` target must resolve.

## Design Notes

- `LexicalEntry` is an entity because defined terms are graph objects and must be referenceable across a corpus.
- `AllowsContentOrChildren` preserves both the simple glossary pattern and the structured multi-sense pattern.
- Follows OntoLex-Lemon conventions: LexicalEntry, LexicalForm, and LexicalRelation align with the W3C community standard for linguistic linked data.
- The schema is self-contained. Consuming schemas import one package and gain the full lexical-entry surface.

---

**End of Lexical Entry v1.0.0**
