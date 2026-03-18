Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Material

A material or substance from which objects are made, with canonical name, aliases, category, physical characteristics, and sustainability traits.

## When to Use

Use `Material` to author a reusable material entity referenced by products, equipment, and other consuming schemas. The package covers a canonical name, alternate names, material category, optional color and finish, sustainability flags, optional location, optional measurements, and optional tags.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Material | Semantic (Entity) | ForbidsContent | `desc:Description`, `Aliases` (0..1), `loc:Location`, `measure:Measure`, `tags:Tags` | The root material entity. |
| Aliases | Structural | ForbidsContent | `Alias` | Unordered collection of alternate names. |
| Alias | Semantic | RequiresContent (Flow) | -- | An alternate name with optional language context. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | Canonical authored name. |
| category | $EnumeratedToken | no | Material category. |
| color | $Color | no | Typical or defining color. |
| finish | $EnumeratedToken | no | Surface finish. |
| recyclable | $Boolean | no | Whether the material is recyclable. |
| biodegradable | $Boolean | no | Whether the material is biodegradable. |
| language | $EnumeratedToken | no | Language of the alias. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| tags | `paperhat:domain:tags` |
| measure | `paperhat:domain:measure` |
| loc | `paperhat:domain:location` |

## Design Notes

- `Material` is entity-centered and does not flatten location, measurement, or tagging semantics into local traits.
- `Aliases` is unordered and duplicate-free.
- `recyclable` and `biodegradable` capture simple sustainability facts without forcing a larger lifecycle model into this package.

---

**End of Material v1.0.0**
