Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Food

A food or comestible, with canonical name, aliases, category, sensory profile, nutritional information, availability, and varieties.

## When to Use

Use `Food` to define a food entity that can be referenced by recipes and other consuming schemas. The package supports a canonical name, alternate names, category, nutritional information, availability, location, sensory profile, and named varieties.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Food | Semantic (Entity) | ForbidsContent | `desc:Description`, `Aliases` (0..1), `Varieties` (0..1), `nutrition:NutritionInformation` (0..1), `loc:Location`, `sensory:SensoryProfile` (0..1), `tags:Tags` | The root food entity. |
| Aliases | Structural | ForbidsContent | `Alias` | Unordered collection of alternate names. |
| Alias | Semantic | RequiresContent (Flow) | -- | An alternate name with optional language and region context. |
| Varieties | Structural | ForbidsContent | `Variety` | Unordered collection of named varieties. |
| Variety | Semantic | ForbidsContent | `desc:Description` | A named variety of the food. |

## Traits

| Trait | Type | Used by | Description |
|---|---|---|---|
| name | $Text | `Food`, `Variety` | Canonical authored name. |
| category | $EnumeratedToken | `Food` | Food category. |
| availability | $Range<$MonthDay> | `Food` | Seasonal or annual availability range. |
| shelfLife | $Duration | `Food` | Typical shelf-life duration. |
| language | $EnumeratedToken | `Alias` | Language of the alias. |
| region | $Text | `Alias` | Regional context for the alias. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| nutrition | `codex:domain:nutrition-information` |
| tags | `codex:domain:tags` |
| loc | `codex:domain:location` |
| sensory | `codex:domain:sensory-profile` |

## Design Notes

- `Food` stays entity-centered and does not flatten sensory or nutrition semantics into local traits.
- `Location` captures origin or place semantics through child composition, not through a local `origin` trait.
- `SensoryProfile` captures taste, aroma, and mouthfeel through child composition, not through a local `flavorProfile` trait.
- `availability` captures seasonality through a typed range surface.
- `Varieties` and `Aliases` are unordered and duplicate-free.

---

**End of Food v1.0.0**
