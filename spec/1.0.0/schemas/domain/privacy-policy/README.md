Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Privacy Policy

A structured privacy policy document defining governing entities, covered targets, controllers, collection, use, sharing, retention, rights, privacy contact information, and related legal document references.

## When to Use

Use `PrivacyPolicy` for a real privacy policy document whose semantics must be machine-readable. The policy identifies its governing entity or entities, states what targets it covers, names controllers, states what data is collected, how that data is used, whether it is shared, how long it is retained, what rights data subjects have, and how privacy requests can be directed.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| PrivacyPolicy | Semantic (Entity) | ForbidsContent | docmeta:DocumentMetadata (0..1), jurisdiction:Jurisdiction, GoverningEntity (0..n), AppliesTo (0..n), RelatedDocument (0..n), Controller (1..n), DataCollection (1), DataUse (1), DataSharing (0..1), Retention (0..1), DataRights (1), PrivacyContact (0..1), notes:Notes (0..1) | Root privacy policy document. Requires `title`. |
| GoverningEntity | Structural | ForbidsContent | — | A referenced governing organization or other governing entity. Requires `target`. |
| AppliesTo | Structural | ForbidsContent | — | A referenced covered target such as a site, service, product, or application. Requires `target`. |
| RelatedDocument | Structural | ForbidsContent | — | A referenced related legal document. Requires `target` and `relationshipKind`. |
| Controller | Semantic | ForbidsContent | — | A referenced controller or responsible entity. Requires `target`. |
| DataCollection | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | What data is collected. |
| DataUse | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | How collected data is used. |
| DataSharing | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | How data is shared or disclosed. |
| Retention | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | How long data is retained. |
| DataRights | Semantic | ForbidsContent | text:Paragraph, list:OrderedList, list:UnorderedList, section:Section, notes:Notes | Rights available to data subjects. |
| PrivacyContact | Structural | ForbidsContent | contact:ContactPoint | Contact methods for privacy requests or complaints. |

## Imports

| Namespace | Schema |
|---|---|
| docmeta | `codex:domain:document-metadata` |
| jurisdiction | `codex:domain:jurisdiction` |
| contact | `codex:domain:contact-point` |
| text | `codex:domain:text` |
| list | `codex:domain:list` |
| section | `codex:domain:section` |
| notes | `codex:domain:notes` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The title of the privacy policy document. |
| target | $Iri | yes on GoverningEntity, AppliesTo, RelatedDocument, Controller | The referenced entity target. Marked as a reference trait. |
| governingRole | $EnumeratedToken | no on GoverningEntity | The governing role, such as `$Owner`, `$Operator`, or `$Publisher`. |
| scopeKind | $EnumeratedToken | no on AppliesTo | The covered target kind, such as `$Site`, `$Service`, `$Application`, or `$Product`. |
| relationshipKind | $EnumeratedToken | yes on RelatedDocument | The legal relationship kind, such as `$Supplements`, `$References`, `$PairedWith`, or `$GovernsWith`. |
| controllerKind | $EnumeratedToken | no on Controller | The controller classification, such as `$Primary`, `$Joint`, or `$Processor`. |

## Constraints

- `PrivacyPolicy` requires at least one `Controller`.
- `PrivacyPolicy` requires `DataCollection`, `DataUse`, and `DataRights`.
- `GoverningEntity`, `AppliesTo`, `RelatedDocument`, and `Controller` allow only `target` as a reference trait.
- Every `target` in those concepts must resolve to an entity.
- `PrivacyContact` must contain at least one `contact:ContactPoint`.

## Design Notes

- This schema models the policy itself, not its page layout.
- `Retention` is harmonized with the wider legal package set.
- Graph references are explicit so a policy can be connected to its governing entity, covered targets, and related legal documents without relying on prose links.
- `PrivacyContact` is separated from general document metadata so privacy-specific contact channels can be surfaced distinctly by foundries.

**End of Privacy Policy v1.0.0**
