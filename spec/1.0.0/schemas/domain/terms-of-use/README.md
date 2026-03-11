Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Terms Of Use

A structured terms of use document defining governing entities, covered targets, legal definitions, permitted use, prohibited use, disclaimers, liability limits, termination, governing law, related legal documents, and contact information.

## When to Use

Use `TermsOfUse` for the contractual or quasi-contractual terms governing use of a service, site, application, or product. This schema models the semantic parts of the terms rather than any page layout.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| TermsOfUse | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), jurisdiction:Jurisdiction, GoverningEntity (0..n), AppliesTo (0..n), RelatedDocument (0..n), Definitions (0..1), Acceptance (1), PermittedUse (1), ProhibitedUse (0..1), Disclaimer (0..1), LimitationOfLiability (0..1), Termination (0..1), GoverningLaw (0..1), TermsContact (0..1), notes:Notes (0..1) | Root terms document. Requires `title`. |
| GoverningEntity | Structural | ForbidsContent | — | A referenced governing organization or other governing entity. Requires `target`. |
| AppliesTo | Structural | ForbidsContent | — | A referenced covered target such as a site, service, product, or application. Requires `target`. |
| RelatedDocument | Structural | ForbidsContent | — | A referenced related legal document. Requires `target` and `relationshipKind`. |
| Definitions | Structural | ForbidsContent | term:TermEntry (1..n) | Formal defined terms used by the legal document. |
| Acceptance | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | The user acceptance basis. |
| PermittedUse | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Allowed uses of the service. |
| ProhibitedUse | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Forbidden conduct or misuse. |
| Disclaimer | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Warranty or service disclaimers. |
| LimitationOfLiability | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Liability limitations. |
| Termination | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Suspension or termination conditions. |
| GoverningLaw | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Governing law and dispute framing. |
| TermsContact | Structural | ForbidsContent | contact:ContactPoint | Contact methods for terms-related notices. |

## Imports

| Namespace | Schema |
|---|---|
| docmeta | `paperhat:domain:document-metadata` |
| jurisdiction | `paperhat:domain:jurisdiction` |
| contact | `paperhat:domain:contact-point` |
| text | `paperhat:domain:text` |
| list | `paperhat:domain:list` |
| section | `paperhat:domain:section` |
| notes | `paperhat:domain:notes` |
| term | `paperhat:domain:term-entry` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the terms document. |
| target | $Iri | yes on GoverningEntity, AppliesTo, RelatedDocument | The referenced entity target. Marked as a reference trait. |
| governingRole | $EnumeratedToken | no on GoverningEntity | The governing role, such as `$Owner`, `$Operator`, or `$Publisher`. |
| scopeKind | $EnumeratedToken | no on AppliesTo | The covered target kind, such as `$Site`, `$Service`, `$Application`, or `$Product`. |
| relationshipKind | $EnumeratedToken | yes on RelatedDocument | The legal relationship kind, such as `$Supplements`, `$References`, `$PairedWith`, or `$GovernsWith`. |

## Constraints

- `TermsOfUse` requires `Acceptance` and `PermittedUse`.
- `Definitions` must contain at least one `term:TermEntry`.
- `GoverningEntity`, `AppliesTo`, and `RelatedDocument` allow only `target` as a reference trait.
- Every `target` in those concepts must resolve to an entity.
- `TermsContact` must contain at least one `contact:ContactPoint`.

## Design Notes

- Defined terms are explicit through `term:TermEntry` instead of being buried in prose paragraphs.
- Graph references are explicit so terms can connect to governing entities, covered targets, and related legal documents without relying on prose links.
- Terms sections preserve internal order through paragraphs, lists, nested sections, and notes.
- `TermsContact` is separate from general metadata so notice channels can be surfaced distinctly by foundries.

**End of Terms Of Use v1.0.0**
