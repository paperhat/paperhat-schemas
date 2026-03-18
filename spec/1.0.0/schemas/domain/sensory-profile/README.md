Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Sensory Profile

Compositional sensory characteristics of food and beverage items, covering taste, aroma, and mouthfeel for flavor modeling and substitution inference.

## When to Use

Use `SensoryProfile` to author a reusable sensory description attached to foods and other ingestible entities. The package captures sensory observations as structured notes across taste, aroma, and mouthfeel, with optional descriptive prose and optional intensity markers.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| SensoryProfile | Structural | ForbidsContent | `TasteNote`, `AromaNote`, `MouthfeelNote`, `desc:Description` (0..1) | Container for sensory observations. |
| TasteNote | Semantic | ForbidsContent | `desc:Description` (0..1) | A taste observation. |
| AromaNote | Semantic | ForbidsContent | `desc:Description` (0..1) | An aroma observation. |
| MouthfeelNote | Semantic | ForbidsContent | `desc:Description` (0..1) | A mouthfeel observation. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| taste | $EnumeratedToken | yes on `TasteNote` | The taste class for the note. |
| aroma | $EnumeratedToken | yes on `AromaNote` | The aroma class for the note. |
| mouthfeel | $EnumeratedToken | yes on `MouthfeelNote` | The mouthfeel class for the note. |
| intensity | $EnumeratedToken | no | Relative intensity of the note. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |

## Design Notes

- `SensoryProfile` is a compositional child structure, not an entity.
- Sensory meaning is split across three axes only: taste, aroma, and mouthfeel.
- `intensity` remains a lightweight modifier and does not attempt to model balance, persistence, or dominance.
- The package is designed to support later flavor and substitution reasoning without forcing a larger ontology into the first contract.

---

**End of Sensory Profile v1.0.0**
