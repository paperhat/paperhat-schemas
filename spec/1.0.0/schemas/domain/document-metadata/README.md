Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Document Metadata

An unordered container for document metadata: authorship, descriptions, summaries, tags, audience, and other non-body information.

## When to Use

Use `DocumentMetadata` to collect the metadata of any document-like entity. It holds Work (authorship, dates, licensing), Description, Summary, Tags, audience information, contributor identities, and contact points. Pair it with `Narrative` to cleanly segregate unordered metadata from ordered body content.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| DocumentMetadata | Structural | ForbidsContent | work:Work, desc:Description, summary:Summary, tags:Tags, audience:Audience, person:Person, pname:PersonName, contact:ContactPoint, ident:Identifier, loc:Location | An unordered container. The order of metadata children carries no meaning. |

## Imports

| Namespace | Schema |
|---|---|
| work | `paperhat:domain:work` |
| desc | `paperhat:domain:description` |
| summary | `paperhat:domain:summary` |
| tags | `paperhat:domain:tags` |
| audience | `paperhat:domain:audience` |
| person | `paperhat:domain:person` |
| pname | `paperhat:domain:person-name` |
| contact | `paperhat:domain:contact-point` |
| ident | `paperhat:domain:identifier` |
| loc | `paperhat:domain:location` |

## Design Notes

- DocumentMetadata is unordered because metadata has no reading sequence. Author, publication date, tags, and description are all equally accessible regardless of position.
- The generous set of allowed children covers the metadata needs of most document types. Not every document will use all of them.
- Person and PersonName children support structured attribution (editors, translators, contributors) beyond the plain-text `author` trait on Work.
- Multiple Description or Summary children can coexist for multilingual documents, each with a different `language` trait.
- Media attachment uses the `media-reference` schema package.

**End of Document Metadata v1.0.0**
