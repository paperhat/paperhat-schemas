Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Term Entry

A lexical term entry that scales from a simple glossary definition to a full dictionary entry with multiple senses, parts of speech, etymology, inflected forms, and semantic relations.

## When to Use

Use `TermEntry` whenever a document needs defined terms: specification glossaries, policy definition sections, contract definitions, dictionaries, encyclopedic indexes, or any context requiring formal term-definition pairs. For a simple key-value definition, write the definition text as direct content on `TermEntry`. For structured multi-sense entries, use `Sense` children.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| TermEntry | Semantic | $MustBeEntity | AllowsContentOrChildren (Flow) | Sense (0+), Etymology (0..1), TermForm (0+), TermRelation (0+) | The headword entry. Direct content holds a simple definition; Sense children hold structured multi-sense definitions. |
| Sense | Semantic | $MustNotBeEntity | RequiresContent (Flow) | UsageExample (0+) | One meaning of the term, optionally scoped by part of speech, register, or domain. Content is the definition text. |
| UsageExample | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | An illustrative sentence showing the term in context. |
| Etymology | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | The origin and historical development of the term. |
| TermForm | Semantic | $MustNotBeEntity | ForbidsContent | — | An inflected or alternate form of the headword. |
| TermRelation | Semantic | $MustNotBeEntity | ForbidsContent | — | A semantic relationship to another term. |

## TermEntry Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| term | $Text | yes | The headword or defined term. |
| key | $LookupToken | no | Machine-readable lookup key for Gloss cross-references, for example `~canonicalForm`. |

## Sense Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| partOfSpeech | $EnumeratedToken | no | Part of speech, for example `$Noun`, `$Verb`, `$Adjective`, `$Adverb`, `$Preposition`, `$Conjunction`, `$Pronoun`, `$Interjection`, `$Determiner`, `$Article`, `$Participle`. Open vocabulary. |
| register | $EnumeratedToken | no | Usage register, for example `$Formal`, `$Informal`, `$Archaic`, `$Technical`, `$Slang`, `$Literary`, `$Colloquial`, `$Vulgar`, `$Dialectal`. Open vocabulary. |
| domain | $EnumeratedToken | no | Subject domain, for example `$Computing`, `$Law`, `$Medicine`, `$Linguistics`, `$Music`, `$Botany`, `$Chemistry`. Open vocabulary. |

## TermForm Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| form | $Text | yes | The alternate form, for example "runs", "ran", "running", or "mice". |
| formKind | $EnumeratedToken | no | The grammatical relationship to the headword, for example `$Plural`, `$Singular`, `$PastTense`, `$PresentParticiple`, `$PastParticiple`, `$Comparative`, `$Superlative`, `$ThirdPersonSingular`, `$Gerund`, `$Diminutive`, `$Abbreviation`, `$Feminine`, `$Masculine`, `$Neuter`. Open vocabulary. |

## TermRelation Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| relatedTerm | $Text | yes | The related term as text. |
| relationKind | $EnumeratedToken | yes | The semantic relationship, for example `$Synonym`, `$Antonym`, `$Homonym`, `$Homophone`, `$Hypernym`, `$Hyponym`, `$Meronym`, `$Holonym`, `$SeeAlso`. |
| target | $Iri | no | Entity reference to the related `TermEntry` if it exists in the corpus. |

## Constraints

- `TermEntry` requires either direct definition content or at least one `Sense` child.
- `bodyMode` is required on every `TermEntry` instance because the concept allows either direct content or children.
- `form` is required on `TermForm`.
- `relatedTerm` and `relationKind` are both required on `TermRelation`.

## Usage Spectrum

### Simple glossary

```
<TermEntry
	id=urn:term:canonical-form
	term="canonical form"
	key=~canonicalForm
	bodyMode=$Content
>
	The normalized representation of a value after all processing rules have been applied.
</TermEntry>
```

### Full dictionary entry

```
<TermEntry
	id=urn:term:run
	term="run"
	bodyMode=$Children
>
	<Sense partOfSpeech=$Verb>
		To move swiftly on foot so that both feet leave the ground during each stride.
		<UsageExample>She runs five kilometers every morning.</UsageExample>
		<UsageExample>The children ran across the field.</UsageExample>
	</Sense>
	<Sense partOfSpeech=$Verb register=$Informal>
		To manage or operate.
		<UsageExample>He runs a small bakery on the corner.</UsageExample>
	</Sense>
	<Sense partOfSpeech=$Noun>
		An act or instance of running.
		<UsageExample>She went for a run before breakfast.</UsageExample>
	</Sense>
	<TermForm form="runs" formKind=$ThirdPersonSingular />
	<TermForm form="ran" formKind=$PastTense />
	<TermForm form="running" formKind=$PresentParticiple />
	<Etymology>From Middle English runnen, from Old English rinnan and Old Norse rinna.</Etymology>
	<TermRelation relatedTerm="sprint" relationKind=$Synonym />
	<TermRelation relatedTerm="walk" relationKind=$Antonym />
</TermEntry>
```

## Design Notes

- `TermEntry` is an entity because defined terms are graph objects and must be referenceable across a corpus.
- `AllowsContentOrChildren` preserves both the simple glossary pattern and the structured multi-sense pattern.
- The schema is self-contained. Consuming schemas import one package and gain the full term-entry surface.
- The existing `specification` schema has its own internal `Definition` concept. This shared package remains the reusable lexical-entry surface.

---

**End of Term Entry v1.0.0**
