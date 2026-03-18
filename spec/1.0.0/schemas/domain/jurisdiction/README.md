Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Jurisdiction

A named legal or regulatory jurisdiction — a country, state, province, supranational body, or treaty area under which laws, policies, or regulations apply.

## When to Use

Use `Jurisdiction` to attach legal or regulatory scope to policies, contracts, organizations, or any concept that operates within a defined legal boundary. Jurisdiction is a leaf concept with no imports, designed to be composed into higher-level schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The jurisdiction name (e.g., "New Zealand", "European Union", "State of California"). |
| jurisdictionKind | $EnumeratedToken | no | Classification token, e.g., `$country`, `$state`, `$province`, `$territory`, `$supranational`, `$treaty`, `$municipality`, `$federalDistrict`. Open vocabulary. |
| countryCode | $EnumeratedToken | no | ISO 3166-1 alpha-2 country code when applicable (e.g., `$NZ`, `$US`, `$DE`). Binds to the `iso-3166-countries` vocabulary. |
| subdivisionCode | $Text | no | ISO 3166-2 subdivision code when applicable (e.g., "US-CA", "DE-BY"). Text because subdivision codes include the country prefix and the full ISO 3166-2 set is too large for a vocabulary package. |

## Constraints

`name` is required. A Jurisdiction without a name is ambiguous.

## Design Notes

- `$MustNotBeEntity` because Jurisdiction is a descriptor attached to policies, contracts, and organizations — not a standalone referenceable object. If a jurisdiction needs to be referenced across documents, a future revision promotes it to `$MayBeEntity`.
- `countryCode` binds to the existing `iso-3166-countries` vocabulary, providing machine-readable country identification.
- `subdivisionCode` is `$Text` rather than `$EnumeratedToken` because ISO 3166-2 has thousands of subdivision codes and a vocabulary package for all of them is not warranted.
- Supranational jurisdictions (e.g., European Union, ASEAN) use `jurisdictionKind=$supranational` with no country code.

---

**End of Jurisdiction v1.0.0**
