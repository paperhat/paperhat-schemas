Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# MediaReference

A reference to a media resource such as an image, video, or audio file, with optional format and dimension details.

## When to Use

Use `MediaReference` wherever an entity needs to attach or link to media: product photos, event promotional images, organization logos, recipe dish photos, person avatars, or audio/video content.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| url | $Iri | no | URL of the media resource. |
| mediaKind | $EnumeratedToken | no | Kind of media, e.g. `$image`, `$video`, `$audio`, `$document`. |
| encodingFormat | $Text | no | MIME type, e.g. "image/png", "video/mp4". |
| caption | $Text | no | Human-readable description or alt text. |
| width | $Number | no | Width in pixels. |
| height | $Number | no | Height in pixels. |
| contentSize | $Text | no | File size, e.g. "4.2MB". |

## Design Notes

- All traits are optional because different contexts need different subsets. The "at least one" constraint prevents empty MediaReference elements.
- `url` is an IRI reference, not plain text, to enable tooling to validate and resolve the link.
- `contentSize` is $Text rather than $Number because it typically includes a unit suffix (e.g. "4.2MB", "320KB").
- MediaReference describes the physical artifact (URL, format, dimensions). For authorship and versioning metadata, compose with the Work concept.
- `caption` doubles as alt text for images and descriptive text for audio/video.

**End of MediaReference v1.0.0**
