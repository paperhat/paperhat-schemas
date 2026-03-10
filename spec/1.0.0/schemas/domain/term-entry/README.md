Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Term Entry

A lexical term entry that scales from a simple glossary definition to a full dictionary entry with multiple senses, parts of speech, etymology, inflected forms, and semantic relations.

## When to Use

Use `TermEntry` whenever a document needs defined terms: specification glossaries, policy definition sections, contract definitions, dictionaries, encyclopedic indexes, or any context requiring formal term-definition pairs. For a simple key-value definition, write the definition text as content directly on TermEntry. For structured multi-sense entries, use Sense children.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| TermEntry | Semantic | $MayBeEntity | AllowsContent (Flow) | Sense (0+), Etymology (0..1), TermForm (0+), TermRelation (0+) | The headword entry. Content holds a simple definition; Sense children hold structured multi-sense definitions. |
| Sense | Semantic | $MustNotBeEntity | RequiresContent (Flow) | UsageExample (0+) | One meaning of the term, optionally scoped by part of speech, register, or domain. Content is the definition text. |
| UsageExample | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | An illustrative sentence showing the term in context. |
| Etymology | Semantic | $MustNotBeEntity | RequiresContent (Flow) | — | The origin and historical development of the term. |
| TermForm | Semantic | $MustNotBeEntity | ForbidsContent | — | An inflected or alternate form of the headword. |
| TermRelation | Semantic | $MustNotBeEntity | ForbidsContent | — | A semantic relationship to another term. |

## TermEntry Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| term | $Text | yes | The headword or defined term. |
| key | $LookupToken | no | Machine-readable lookup key for Gloss cross-references (e.g., `~canonicalForm`). |

## Sense Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| partOfSpeech | $EnumeratedToken | no | Part of speech, e.g., `$noun`, `$verb`, `$adjective`, `$adverb`, `$preposition`, `$conjunction`, `$pronoun`, `$interjection`, `$determiner`, `$article`, `$participle`. Open vocabulary. |
| register | $EnumeratedToken | no | Usage register, e.g., `$formal`, `$informal`, `$archaic`, `$technical`, `$slang`, `$literary`, `$colloquial`, `$vulgar`, `$dialectal`. Open vocabulary. |
| domain | $EnumeratedToken | no | Subject domain, e.g., `$computing`, `$law`, `$medicine`, `$linguistics`, `$music`, `$botany`, `$chemistry`. Open vocabulary. |

## TermForm Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| form | $Text | yes | The alternate form (e.g., "ran", "running", "mice"). |
| formKind | $EnumeratedToken | no | The grammatical relationship to the headword, e.g., `$plural`, `$singular`, `$pastTense`, `$presentParticiple`, `$pastParticiple`, `$comparative`, `$superlative`, `$thirdPersonSingular`, `$gerund`, `$diminutive`, `$abbreviation`, `$feminine`, `$masculine`, `$neuter`. Open vocabulary. |

## TermRelation Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| relatedTerm | $Text | yes | The related term as text. |
| relationKind | $EnumeratedToken | yes | The semantic relationship, e.g., `$synonym`, `$antonym`, `$homonym`, `$homophone`, `$hypernym`, `$hyponym`, `$meronym`, `$holonym`, `$seeAlso`. |
| target | $Iri | no | Entity reference to the related TermEntry if it exists in the document. Marked as a reference trait (`isReferenceTrait=true`). |

## Constraints

- `term` is required on TermEntry.
- `form` is required on TermForm.
- `relatedTerm` and `relationKind` are both required on TermRelation.

## Usage Spectrum

### Simple glossary (key-value)

```
<TermEntry term="canonical form">The normalized representation of a value after all processing rules have been applied.</TermEntry>
```

### Specification glossary (with lookup key)

```
<TermEntry term="canonical form" key=~canonicalForm>The normalized representation of a value after all processing rules have been applied.</TermEntry>
```

### Full dictionary entry

```
<TermEntry term="run">
	<Sense partOfSpeech=$verb>
		To move swiftly on foot so that both feet leave the ground during each stride.
		<UsageExample>She runs five kilometers every morning.</UsageExample>
		<UsageExample>The children ran across the field.</UsageExample>
	</Sense>
	<Sense partOfSpeech=$verb register=$informal>
		To manage or operate.
		<UsageExample>He runs a small bakery on the corner.</UsageExample>
	</Sense>
	<Sense partOfSpeech=$noun>
		An act or instance of running.
		<UsageExample>She went for a run before breakfast.</UsageExample>
	</Sense>
	<TermForm form="runs" formKind=$thirdPersonSingular />
	<TermForm form="ran" formKind=$pastTense />
	<TermForm form="running" formKind=$presentParticiple />
	<Etymology>From Middle English runnen, from Old English rinnan and Old Norse rinna.</Etymology>
	<TermRelation relatedTerm="sprint" relationKind=$synonym />
	<TermRelation relatedTerm="walk" relationKind=$antonym />
</TermEntry>
```

## Design Notes

- `$MayBeEntity` on TermEntry because glossary terms in specifications need stable identity for Gloss cross-references, while simple inline definitions do not.
- AllowsContent on TermEntry enables the simple key-value pattern. For structured entries, use Sense children instead. A consuming schema can constrain to one pattern or the other.
- No imports. All sub-concepts are local to this schema. This keeps it self-contained while still being importable — a Specification or Policy schema imports the whole package and gets all six concepts.
- Pronunciation is handled by importing `linguistic-annotation` as a sibling in the consuming schema, not here. That keeps concerns separate.
- The existing `specification` schema has its own internal `Definition` concept. Once this shared leaf exists, a future unlocked revision of the specification schema could migrate to importing this package. The specification schema is UNLOCKED, so this is possible without breaking locked contracts.

---

**End of Term Entry v1.0.0**
