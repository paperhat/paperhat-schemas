Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Media Asset

A discrete media file or object with identity, such as an image, video, audio recording, or document file, carrying technical metadata about the asset itself.

## When to Use

Use `MediaAsset` to represent a media file as a first-class entity with stable identity. Examples include a company logo, a product photograph, a podcast episode recording, or a specification PDF. MediaAsset is an entity (`$MustBeEntity`) and is referenceable from other schemas by IRI. It is distinct from MediaReference (an inline pointer to a media resource without identity) and Figure (a presentational wrapper for media within a document).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The asset name (e.g., "Company Logo", "Product Hero Image", "Episode 42 Recording"). |
| assetKind | $EnumeratedToken | no | Classification token, e.g., `$Image`, `$Video`, `$Audio`, `$Document`, `$Spreadsheet`, `$Presentation`. Open vocabulary. |
| url | $Url | no | The canonical URL where the asset is stored or served. |
| encodingFormat | $MediaType | no | The MIME type of the asset (e.g., `image/png`, `video/mp4`, `audio/mpeg`). |
| altText | $Text | no | Alternative text description for accessibility. |

## Constraints

`name` is required. A media asset without a name is empty.

## Design Notes

- MediaAsset is an entity (`$MustBeEntity`) because assets need stable identity for cross-references. A product page, organization profile, or project references the same logo asset by IRI rather than embedding duplicate MediaReference elements.
- This is a pure leaf with no imports and no children. Higher-level composers will compose MediaAsset with Description, Tags, Work (for authorship/licensing), and other leaf schemas as needed.
- MediaReference remains the correct choice for inline media pointers within documents. MediaAsset is for when the media file itself is the subject being described and needs to be referenceable.
- `encodingFormat` uses `$MediaType` (MIME type) consistent with the same trait on MediaReference.

---

**End of Media Asset v1.0.0**
