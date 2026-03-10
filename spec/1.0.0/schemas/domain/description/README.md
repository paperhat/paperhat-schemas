Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Description

A dual-mode description: plain text for simple cases, or paragraphs and lists for structured descriptions.

## When to Use

Use `Description` wherever content needs a "what is this?" block. For simple cases, put plain text directly as content. For richer descriptions, use children mode with paragraphs and lists.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Description | Semantic | AllowsContentOrChildren (Flow) | text:Paragraph, list:OrderedList, list:UnorderedList | Content mode = plain text. Children mode = paragraphs + lists. |

## Imports

| Namespace | Schema |
|---|---|
| text | `codex:domain:text` |
| list | `codex:domain:list` |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| language | $EnumeratedToken | no | Language of the description text. |

## Design Notes

- Description uses `AllowsContentOrChildren` to support both simple (single-string) and structured (multi-paragraph, lists) use cases without separate concept variants.
- Content mode is plain text. Children mode composes Paragraph and list concepts from their respective schemas.

**End of Description v1.0.0**
