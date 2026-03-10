Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Location

A named geographic or fictional location with optional administrative subdivisions.

**Package:** `paperhat-location`
**Schema ID:** `codex:domain:location`

---

## When to Use

Use `Location` whenever you need to represent a place such as a city, a country, a fictional realm, or any other named location. `Location` is deliberately simpler than a full mailing-address concept; it captures where something is, not how to route mail there.

A single entity can have multiple `Location` instances to capture birthplaces, residences, workplaces, settings, and other location roles. The `locationKind` trait distinguishes those roles.

`Location` is a leaf concept with no concept dependencies. It is designed to be composed into higher-level schemas such as `Person`, `Organization`, `Food`, and `Event`.

---

## Traits

### locationKind

A token classifying the role this location plays for its parent entity. Common values include `$birthPlace`, `$residence`, `$workplace`, `$deathPlace`, `$hometown`, and `$setting`.

This vocabulary is open. A consuming schema can constrain accepted values.

### name

A descriptive name for the location. Use this for specific places that do not decompose cleanly into administrative parts.

### locality

The city, town, or village.

### region

The state, province, territory, or other administrative subdivision.

### country

The country or sovereign entity. This trait uses `$EnumeratedToken`, which keeps the surface consistent with the rest of the package's tokenized administrative traits while still permitting open authored values.

---

## Constraints

At least one of `name`, `locality`, `region`, or `country` must be present. A `Location` with only `locationKind` and no actual location information is invalid.

---

## Design Notes

A full mailing-address concept serves a different purpose and remains separate. `Location` answers a simpler question: where is this.

`locationKind` describes the role the location plays for its parent entity. The place itself remains the same place regardless of role.

**End of Location v1.0.0**
