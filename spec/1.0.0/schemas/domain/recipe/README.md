Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Recipe

A structured recipe for food or drink preparation, composed from reusable text and support schemas plus recipe-specific structural and semantic concepts.

## When to Use

Use `Recipe` to author any food or drink preparation procedure. Every recipe requires a title, an ingredient container, and ordered instructions. Timing, yield, equipment, advice, notes, nutrition, and audience material are optional.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Recipe | Semantic (Entity) | ForbidsContent | `text:Title` (1), `text:Teaser` (0..1), `desc:Description`, `Servings` (0..1), `Yield` (0..1), `Times` (0..1), `Ingredients` (1), `Equipment` (0..1), `Instructions` (1), `ServingSuggestions` (0..1), `tips:Tips`, `notes:Notes`, `tags:Tags`, `Source`, `work:Work`, `audience:Audience`, `nutrition:NutritionInformation` | The root recipe entity. |
| Servings | Semantic | ForbidsContent | -- | How many portions the recipe is intended to serve. Traits: `amount` (required), `unit`. |
| Yield | Semantic | ForbidsContent | `massmeasure:MassMeasure` (0..1), `volumemeasure:VolumeMeasure` (0..1) | The produced quantity when the result is better expressed as output amount rather than serving count. Traits: `amount` (required), `item`. |
| Times | Structural | ForbidsContent | `PreparationTime`, `CookingTime`, `RestingTime`, `SettingTime`, `TotalTime` | Timing container for the recipe. |
| PreparationTime | Semantic | ForbidsContent | `timemeasure:TimeMeasure` (1) | Time required before cooking or final combination begins. |
| CookingTime | Semantic | ForbidsContent | `timemeasure:TimeMeasure` (1) | Time spent cooking or actively heating. |
| RestingTime | Semantic | ForbidsContent | `timemeasure:TimeMeasure` (1) | Time the recipe must rest before the next stage or before serving. |
| SettingTime | Semantic | ForbidsContent | `timemeasure:TimeMeasure` (1) | Time required for chilling, setting, or firming. |
| TotalTime | Semantic | ForbidsContent | `timemeasure:TimeMeasure` (1) | Total elapsed time for the recipe. |
| Ingredients | Structural | ForbidsContent | `Ingredient`, `IngredientSet` | Unordered ingredient container for flat or grouped ingredient structures. |
| IngredientSet | Structural | ForbidsContent | `text:Title` (0..1), `Ingredient` (1..n) | A titled unordered ingredient set such as Sauce, Dressing, Base, or To serve. |
| Ingredient | Semantic | ForbidsContent | `massmeasure:MassMeasure` (0..1), `volumemeasure:VolumeMeasure` (0..1) | A single ingredient entry. Traits: `food` (required), `preparation`, `optional`, `toTaste`. |
| Equipment | Structural | ForbidsContent | `equip:Equipment` (1..n) | Unordered recipe-local equipment container. |
| Instructions | Structural | ForbidsContent | `Step` (1..n) | Ordered instruction sequence. |
| Step | Semantic | RequiresContent (Flow) | -- | A single instruction step. Trait: `optional`. |
| ServingSuggestions | Structural | ForbidsContent | `ServingSuggestion` (1..n) | Ordered recipe-specific serving guidance. |
| ServingSuggestion | Semantic | RequiresContent (Flow) | -- | A single serving suggestion. Trait: `language`. |
| Source | Semantic | RequiresContent (Flow) | -- | Attribution or adaptation prose for the recipe. |

## Imports

| Namespace | Schema |
|---|---|
| audience | `paperhat:domain:audience` |
| desc | `paperhat:domain:description` |
| equip | `paperhat:domain:equipment` |
| food | `paperhat:domain:food` |
| massmeasure | `paperhat:domain:paperhat-mass-measure` |
| notes | `paperhat:domain:notes` |
| nutrition | `paperhat:domain:nutrition-information` |
| tags | `paperhat:domain:tags` |
| text | `paperhat:domain:text` |
| timemeasure | `paperhat:domain:paperhat-time-measure` |
| tips | `paperhat:domain:tips` |
| volumemeasure | `paperhat:domain:paperhat-volume-measure` |
| work | `paperhat:domain:work` |

## Constraints

| Constraint | Rule |
|---|---|
| Recipe requires Title | Every `Recipe` must contain exactly one `text:Title` child. |
| Recipe requires Ingredients | Every `Recipe` must contain exactly one `Ingredients` child. |
| Recipe requires Instructions | Every `Recipe` must contain exactly one `Instructions` child. |
| Ingredients requires members | Every `Ingredients` container must contain at least one `Ingredient` or `IngredientSet`. |
| Times requires members | Every `Times` container must contain at least one time concept. |

## Design Notes

- Structured parts are modeled as concepts with explicit collection semantics, not flattened into local traits.
- `Ingredients`, `IngredientSet`, and `Equipment` are unordered and forbid duplicates.
- `Instructions` and `ServingSuggestions` are ordered and forbid duplicates.
- `tips:Tips` holds reusable ordered advice.
- `notes:Notes` holds referenced annotations.
- `ServingSuggestions` remains local to `recipe` because serving guidance is recipe semantics rather than a general-purpose advice leaf.
- `Times` gathers all recipe timing concepts into one exact home and avoids a drifting list of root-level timing children.
- `Source` remains flow-content attribution and adaptation prose until a separate attribution package is defined.

---

**End of Recipe v1.0.0**
