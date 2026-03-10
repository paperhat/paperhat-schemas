Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# NutritionInformation

Nutritional facts per serving, expressed as child concepts that wrap typed measurement leaves.

## When to Use

Use `NutritionInformation` wherever an entity has nutritional data: recipes with per-serving nutrition, food entities with nutrition facts, or any other authored object that needs a structured nutritional surface.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| NutritionInformation | Semantic | ForbidsContent | `ServingSize` (0..1), `Calories` (0..1), `FatContent` (0..1), `ProteinContent` (0..1), `CarbohydrateContent` (0..1), `FiberContent` (0..1), `SugarContent` (0..1), `SodiumContent` (0..1) | Root nutritional container. |
| ServingSize | Semantic | ForbidsContent | `massmeasure:MassMeasure` (0..1), `volumemeasure:VolumeMeasure` (0..1) | The serving size surface. |
| Calories | Semantic | ForbidsContent | `energymeasure:EnergyMeasure` (1) | Calories per serving. |
| FatContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Fat per serving. |
| ProteinContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Protein per serving. |
| CarbohydrateContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Carbohydrates per serving. |
| FiberContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Fiber per serving. |
| SugarContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Sugar per serving. |
| SodiumContent | Semantic | ForbidsContent | `massmeasure:MassMeasure` (1) | Sodium per serving. |

## Imports

| Namespace | Schema |
|---|---|
| energymeasure | `codex:domain:paperhat-energy-measure` |
| massmeasure | `codex:domain:paperhat-mass-measure` |
| volumemeasure | `codex:domain:paperhat-volume-measure` |

## Constraints

| Constraint | Rule |
|---|---|
| NutritionInformation requires nutrient content | Every `NutritionInformation` instance must contain at least one child concept. |

## Design Notes

- The package uses typed measurement leaves instead of bare numeric traits.
- `ServingSize` remains flexible by allowing mass or volume measurement children.
- Macronutrients and sodium use mass measurement children.
- Calories use an energy measurement child.

---

**End of NutritionInformation v1.0.0**
