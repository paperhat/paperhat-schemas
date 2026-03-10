Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Rating

A numeric rating on a defined scale.

## When to Use

Use `Rating` wherever a scored evaluation is needed: product reviews, recipe difficulty, restaurant stars, course quality, event satisfaction. The scale is explicit — authors declare what the best and worst values are, so "4 out of what?" is never ambiguous.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| ratingValue | $Number | yes | The actual rating. |
| bestRating | $Number | no | The highest possible value on the scale. Convention is 5 if omitted. |
| worstRating | $Number | no | The lowest possible value on the scale. Convention is 1 if omitted. |
| ratingKind | $EnumeratedToken | no | What aspect is being rated, e.g. `$overall`, `$quality`, `$difficulty`, `$taste`, `$value`. Consuming schemas may constrain the allowed values. |

## Design Notes

- Only `ratingValue` is required. When `bestRating` and `worstRating` are omitted, the conventional interpretation is a 1-to-5 scale, but consuming schemas should make their scale explicit via documentation or constraints.
- Multiple ratings on different aspects can be expressed by composing several Rating children, each with a distinct `ratingKind`.
- Rating is the natural building block for a future Review composer (Rating + Description + Reference to author + date).

---

**End of Rating v1.0.0**
