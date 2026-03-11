Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Cookie Policy

A structured cookie policy document defining governing entities, covered targets, cookie categories, controls, third-party use, retention semantics, defined terms, and related legal document references.

## When to Use

Use `CookiePolicy` for a document that explains how a service uses cookies or comparable client-side storage. This schema models semantic categories, controls, graph references, and defined terms rather than any specific page or consent-banner layout.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| CookiePolicy | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), jurisdiction:Jurisdiction, GoverningEntity (0..n), AppliesTo (0..n), RelatedDocument (0..n), Definitions (0..1), CookieCategory (1..n), CookieControl (0..1), ThirdPartyUse (0..1), Retention (0..1), notes:Notes (0..1) | Root cookie policy document. Requires `title`. |
| GoverningEntity | Structural | ForbidsContent | — | A referenced governing organization or other governing entity. Requires `target`. |
| AppliesTo | Structural | ForbidsContent | — | A referenced covered target such as a site, service, product, or application. Requires `target`. |
| RelatedDocument | Structural | ForbidsContent | — | A referenced related legal document. Requires `target` and `relationshipKind`. |
| Definitions | Structural | ForbidsContent | term:TermEntry (1..n) | Formal defined terms used by the cookie policy. |
| CookieCategory | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | A cookie category such as essential, analytics, or marketing. Requires `category`. |
| CookieControl | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | How users can control or disable cookie behavior. |
| ThirdPartyUse | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Third-party cookie or storage usage. |
| Retention | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Duration or retention semantics for cookie-related storage. |

## Imports

| Namespace | Schema |
|---|---|
| docmeta | `paperhat:domain:document-metadata` |
| jurisdiction | `paperhat:domain:jurisdiction` |
| text | `paperhat:domain:text` |
| list | `paperhat:domain:list` |
| section | `paperhat:domain:section` |
| notes | `paperhat:domain:notes` |
| term | `paperhat:domain:term-entry` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the cookie policy document. |
| category | $EnumeratedToken | yes on CookieCategory | The cookie category token, such as `$Essential`, `$Analytics`, `$Preferences`, or `$Marketing`. |
| target | $Iri | yes on GoverningEntity, AppliesTo, RelatedDocument | The referenced entity target. Marked as a reference trait. |
| governingRole | $EnumeratedToken | no on GoverningEntity | The role of the governing entity, such as `$Owner`, `$Operator`, or `$Publisher`. |
| scopeKind | $EnumeratedToken | no on AppliesTo | The covered target kind, such as `$Site`, `$Service`, `$Application`, or `$Product`. |
| relationshipKind | $EnumeratedToken | yes on RelatedDocument | The legal relationship kind, such as `$Supplements`, `$References`, `$PairedWith`, or `$GovernsWith`. |

## Constraints

- `CookiePolicy` requires at least one `CookieCategory`.
- Every `CookieCategory` requires its `category` trait.
- `Definitions` must contain at least one `term:TermEntry`.
- `GoverningEntity`, `AppliesTo`, and `RelatedDocument` allow only `target` as a reference trait.
- Every `target` in those concepts must resolve to an entity.

## Design Notes

- This schema models cookie semantics, not consent-banner layout.
- Graph references are explicit so a cookie policy can connect to governing entities, covered targets, and related legal documents without relying on prose links.
- Defined terms are explicit through `term:TermEntry` instead of being buried in prose paragraphs.
- Jurisdictions are explicit children because the applicable regulatory frame can vary by region.

**End of Cookie Policy v1.0.0**
