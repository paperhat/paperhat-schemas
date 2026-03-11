Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Citation

A structured bibliographic citation with ordered contributors (persons or organizations), publication metadata, and identifiers. Supports the full range from simple web references to complete academic bibliographic entries.

## When to Use

Use `Citation` to represent a reference to a published work with enough metadata for identification and retrieval. Citation is distinct from Reference (a typed entity pointer) and from Notes (footnote containers). Use Citation when you need bibliographic structure: authors, publication dates, publishers, page ranges, DOIs, ISBNs.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Citation | Semantic | $MayBeEntity | ForbidsContent | Contributor (1+, ordered), ident:Identifier (0+) | A bibliographic citation. Contributor order is document order — foundries render "et al" based on position. |
| Contributor | Semantic | $MustNotBeEntity | ForbidsContent | person:Person (0..1), org:Organization (0..1), ref:Reference (0..1) | A person or organization in a specific role on the cited work. Exactly one of Person, Organization, or Reference must be present. |

## Citation Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | Title of the cited work. |
| subtitle | $Text | no | Subtitle, if any. |
| citationKind | $EnumeratedToken | no | Classification token, e.g., `$book`, `$article`, `$chapter`, `$specification`, `$standard`, `$rfc`, `$website`, `$patent`, `$thesis`, `$dissertation`, `$conferenceProceeding`, `$report`, `$letter`, `$manuscript`, `$softwareDocumentation`. Open vocabulary. |
| containerTitle | $Text | no | Title of the containing work — the journal name for an article, the book title for a chapter, the conference name for a proceeding. |
| edition | $Text | no | Edition statement (e.g., "2nd ed.", "Revised edition"). |
| volume | $Text | no | Journal or book volume. |
| issue | $Text | no | Journal issue number. |
| number | $Text | no | Report number, RFC number, working paper number. |
| pageRange | $Text | no | Page range (e.g., "123-145"). |
| publicationPlace | $Text | no | City or region of publication (e.g., "Cambridge, MA"). |
| datePublished | $Date | no | Publication date. |
| dateAccessed | $Date | no | Date the resource was last accessed (for web resources). |
| language | $EnumeratedToken | no | Language of the cited work. Binds to `bcp-47-languages` vocabulary. |
| uri | $Url | no | URL to the cited work. |
| key | $LookupToken | no | Machine-readable lookup key for Gloss cross-references (e.g., `~rfc2119`). |

## Contributor Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| contributorKind | $EnumeratedToken | yes | The contributor's role, e.g., `$author`, `$editor`, `$translator`, `$compiler`, `$illustrator`, `$chair`, `$publisher`, `$seriesEditor`, `$forewordAuthor`. Open vocabulary. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| person | `paperhat:domain:person` | Person (with PersonName, ContactPoint, Identifier, Location children) |
| org | `paperhat:domain:organization` | Organization (with Description, ContactPoint, Identifier, Location, Tags children) |
| ident | `paperhat:domain:identifier` | Identifier (scheme + value for ISBN, DOI, ISSN, etc.) |
| ref | `paperhat:domain:reference` | Reference (entity pointer for linking to persons or organizations defined elsewhere) |

## Constraints

- `title` is required on Citation.
- `contributorKind` is required on Contributor.
- A Contributor must have exactly one of: a Person child, an Organization child, or a Reference child.

## Examples

### Simple RFC citation

```
<Citation
	title="Key words for use in RFCs to Indicate Requirement Levels"
	citationKind=$rfc
	number="2119"
	datePublished={1997-03}
	key=~rfc2119
	uri=url("https://www.rfc-editor.org/rfc/rfc2119")
>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="Scott" family="Bradner" />
		</person:Person>
	</Contributor>
</Citation>
```

### Multi-author book with publisher

```
<Citation
	title="Design Patterns"
	subtitle="Elements of Reusable Object-Oriented Software"
	citationKind=$book
	datePublished={1994-10-31}
	publicationPlace="Reading, MA"
	key=~gangOfFour
>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="Erich" family="Gamma" />
		</person:Person>
	</Contributor>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="Richard" family="Helm" />
		</person:Person>
	</Contributor>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="Ralph" family="Johnson" />
		</person:Person>
	</Contributor>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="John" family="Vlissides" />
		</person:Person>
	</Contributor>
	<Contributor contributorKind=$publisher>
		<org:Organization name="Addison-Wesley" />
	</Contributor>
	<ident:Identifier scheme=$isbn value="978-0-201-63361-0" />
</Citation>
```

### Organization as author with entity reference

```
<Citation
	title="WHO Guidelines on Hand Hygiene in Health Care"
	citationKind=$report
	datePublished={2009}
	key=~whoHandHygiene
>
	<Contributor contributorKind=$author>
		<ref:Reference target=who />
	</Contributor>
</Citation>
```

Here `target=who` points to an `<org:Organization id=who name="World Health Organization" />` entity defined elsewhere in the document.

### Journal article

```
<Citation
	title="Computing Machinery and Intelligence"
	citationKind=$article
	containerTitle="Mind"
	volume="59"
	issue="236"
	pageRange="433-460"
	datePublished={1950-10}
	key=~turingTest
>
	<Contributor contributorKind=$author>
		<person:Person>
			<pname:PersonName given="Alan" middle="Mathison" family="Turing" />
		</person:Person>
	</Contributor>
	<Contributor contributorKind=$publisher>
		<org:Organization name="Oxford University Press" />
	</Contributor>
	<ident:Identifier scheme=$doi value="10.1093/mind/LIX.236.433" />
</Citation>
```

## Design Notes

- **Contributors are entities, not text.** Authors, editors, and publishers are Persons or Organizations with real identity. This enables proper name rendering per locale, deduplication across citations, entity linking, and machine-readable bibliographic data.
- **Ordering is document order.** The first Contributor with `contributorKind=$author` is the first author. Foundries use position to render "et al" and to format author lists per citation style (APA, Chicago, MLA, etc.).
- **Publisher is a Contributor.** Rather than a separate concept, publisher is a Contributor with `contributorKind=$publisher`. This unifies the model — every entity associated with a cited work has the same structural pattern.
- **Three ways to identify a contributor.** Embed a Person (creates the entity inline), embed an Organization, or use Reference to point to an entity defined elsewhere. This covers external persons cited for the first time, internal persons already in the corpus, and institutional authors.
- **Identifier children for structured IDs.** DOI, ISBN, ISSN, PMID, etc. use the existing Identifier leaf with `scheme=$doi`, `scheme=$isbn`, etc. This avoids trait proliferation and reuses the established pattern.
- **`$MayBeEntity`** because citations in a bibliography section need stable identity for Gloss cross-references (`{~rfc2119 | RFC 2119}`), but inline citations in a footnote might not.

---

**End of Citation v1.0.0**
