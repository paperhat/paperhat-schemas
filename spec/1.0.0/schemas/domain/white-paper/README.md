Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# White Paper

A structured, argument-driven long-form document for technical or policy white papers. Composes imported building blocks for metadata, narrative structure, document structure, footnotes, and series membership.

## When to Use

Use `WhitePaper` when the document must present a central thesis, develop that thesis across ordered sections of continuous prose, and provide explicit footnoted references to source material. This schema is for analytical technical writing grounded in specifications, standards, or research. For shorter, less structured prose, consider `Essay`.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| WhitePaper | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), series:SeriesInfo (0..1), documentstructure:Abstract (1), narrative:Narrative (1), documentstructure:Conclusion (0..1), notes:Notes (0..1) | Root white paper entity. Requires title and coreThesis traits. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| docmeta | `paperhat:domain:document-metadata` | DocumentMetadata (composes Work, Description, Summary, Tags, Audience, Person, PersonName, ContactPoint, Identifier, Location) |
| narrative | `paperhat:domain:narrative` | Narrative (composes Section, Paragraph; Section further composes Rubric, Description, OrderedList, UnorderedList, Notes) |
| notes | `paperhat:domain:notes` | Notes, Note (keyed footnotes and endnotes) |
| series | `paperhat:domain:series` | SeriesInfo (series title, position, track) |
| documentstructure | `paperhat:domain:document-structure` | Abstract, Conclusion |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the white paper. |
| coreThesis | $Text | yes | The central thesis statement of the paper. |

All other metadata (author, dates, status, license, version, tags, audience) belongs inside `DocumentMetadata` via the `Work`, `Tags`, `Audience`, and other leaf concepts.

## Design Notes

- The schema follows the same structural pattern as `Essay`: a root entity composing DocumentMetadata, a body container (Narrative), and Notes. The additions are `Abstract`, `Conclusion`, `SeriesInfo`, and the `coreThesis` trait.
- `Abstract` and `Conclusion` are imported from `paperhat-document-structure` as reusable document-structure concepts. `Abstract` has a distinct rhetorical function from `Summary`: it frames a thesis for academic and technical readers rather than describing what something says. `Conclusion` synthesises findings rather than argues, and the schema enforces at most one.
- Body content lives inside `Narrative`, which holds `Section` children in reading order. Each Section composes `Rubric` (for headings), `Paragraph`, `Description`, `OrderedList`, `UnorderedList`, nested `Section`, and section-scoped `Notes`.
- Footnotes use the `Notes`/`Note` schema with `LookupToken` keys (e.g., `key=~canonicalForm`). Display numbering is a rendering concern handled by the foundry. Document-level endnotes go in a `Notes` child of `WhitePaper`; section-scoped footnotes go in a `Notes` child of the relevant `Section`.
- Series membership (track, position, series title) uses the reusable `SeriesInfo` concept from `paperhat:domain:series`.
- White papers are continuous prose with footnoted references, not structurally decomposed arguments. The schema does not define argument primitives (claims, evidence, counterpositions) because those are rhetorical patterns within prose, not structural units.

---

**End of White Paper v1.0.0**
