Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Tone

Emotional or tonal annotation on a text span, marking the intended feeling, mood, or voice of the passage.

## When to Use

Use `Tones` to annotate text spans with emotional or tonal metadata. Each Tone marks a passage with an intended emotion and optional intensity. Useful for creative writing, dialogue, accessibility (indicating emotional subtext), and sentiment analysis.

## Concepts

### Tones (Container)

Structural container for tone definitions. Unordered, no duplicates.

### Tone

An emotional or tonal marker. Bound from Gloss spans via `{~key}` or `{~key | label}` references.

| Trait | Type | Cardinality | Required | Description |
|---|---|---|---|---|
| key | $LookupToken | Single | yes | Gloss binding key. |
| emotion | $EnumeratedToken | Single | yes | The emotion or tonal quality (e.g. `$joy`, `$anger`, `$sarcasm`, `$melancholy`, `$urgency`). |
| text | $Text | Single | no | Display text for label-less Gloss references (Pattern B). |
| intensity | $EnumeratedToken | Single | no | How strongly the emotion is expressed (e.g. `$mild`, `$moderate`, `$strong`). |

## Constraints

- Tones must contain at least one Tone.

## Design Notes

- A single Tone concept with an `emotion` trait is preferred over separate concepts per emotion (Joy, Anger, etc.) because the set of emotions is open-ended and culturally variable.
- The `emotion` trait uses $EnumeratedToken so consuming schemas can constrain allowed values via a vocabulary, or authors can use freeform tokens.
- The `intensity` trait is a rendering hint. The foundry decides how (or whether) to visually distinguish intensity levels.
- Tone is a standalone schema. Authors either use it or not. It composes cleanly with any entity schema.

---

**End of Tone v1.0.0**
