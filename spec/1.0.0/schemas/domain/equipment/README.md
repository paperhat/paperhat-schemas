Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Equipment

Kitchen and general-purpose equipment, with canonical name, category, and optional descriptive and measurement children.

## When to Use

Use `Equipment` to author a reusable equipment entity that can be referenced from recipes and other consuming schemas. The package covers a canonical name, a broad category, optional description, optional measurements, and optional tags.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Equipment | Semantic (Entity) | ForbidsContent | `desc:Description`, `measure:Measure`, `tags:Tags` | The root equipment entity. |

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | Canonical authored name. |
| category | $EnumeratedToken | no | Equipment category. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| measure | `codex:domain:measure` |
| tags | `codex:domain:tags` |

## Design Notes

- `Equipment` is intentionally broad enough to cover cookware, utensils, appliances, and serving tools.
- Measurements remain child concepts so the package does not flatten dimensions into local traits.
- Tags remain external so recipe-specific classification can compose over the same equipment entity.

---

**End of Equipment v1.0.0**
