Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Rubric

A structured heading block containing title, subtitle, teaser, and difficulty metadata.

## When to Use

Use `Rubric` at the top of a section, chapter, or document to declare its heading metadata. It provides a required title, optional subtitle, optional teaser, optional difficulty rating, and optional temporal traits.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Rubric | Structural | ForbidsContent | text:Title (1), Subtitle (0..1), text:Teaser (0..1), Difficulty (0..1) | The heading block. Requires exactly one Title. |
| Subtitle | Semantic | RequiresContent (Flow) | -- | A secondary title. Local to this schema because it is meaningless without a Title. |
| Difficulty | Semantic | ForbidsContent | -- | A scale+value pair describing content difficulty (e.g. grade level, categorical rating). |

## Imports

| Namespace | Schema |
|---|---|
| text | `paperhat:domain:text` |

## Traits

| Trait | On | Type | Required | Description |
|---|---|---|---|---|
| timeToRead | Rubric | $Duration | no | Estimated reading time. |
| publishedOn | Rubric | $Date | no | Publication date. |
| lastModifiedAt | Rubric | $DateTime | no | Last modification timestamp. |
| language | Subtitle | $EnumeratedToken | no | Language of the subtitle text. |
| scale | Difficulty | $EnumeratedToken | yes | The grading system, e.g. `$gradeLevel`, `$categorical`, `$numeric`. |
| value | Difficulty | $Text | yes | The difficulty value, e.g. `"4"` (grade level) or `$intermediate` (categorical). |

## Design Notes

- The name "Rubric" comes from the Latin *rubrica* (red heading) -- the traditional typographic term for a heading or caption in a manuscript.
- Subtitle is local because it has no meaning without a Title to accompany it.
- Difficulty is a concept (not just an enum) because grade-level systems like Flesch-Kincaid and Lexile produce numeric scores that need both a scale identifier and a value.

---

**End of Rubric v1.0.0**
