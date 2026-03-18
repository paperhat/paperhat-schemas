Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# GeographicLocation

A precise geographic position on Earth, expressed as decimal latitude and longitude with optional elevation.

## When to Use

Use `GeographicLocation` when you need exact coordinates rather than named places: map pins, GPS waypoints, survey points, sensor placements, flight paths. For named locations with administrative subdivisions (city, region, country), use `Location` instead.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| latitude | $Number | yes | Decimal degrees latitude. Positive values are north of the equator; negative values are south. Range: −90 to 90. |
| longitude | $Number | yes | Decimal degrees longitude. Positive values are east of the prime meridian; negative values are west. Range: −180 to 180. |
| elevation | $Number | no | Elevation in meters above mean sea level. Negative values indicate below sea level. |

## Design Notes

- Both `latitude` and `longitude` are required. A coordinate without both axes is meaningless.
- Coordinates use decimal degrees (WGS 84), the universal standard for web and data interchange.
- Elevation is optional because most use cases only need a 2D position.
- Distinct from `Location`, which captures named places with administrative hierarchy. A consuming schema uses both: `Location` for the human-readable name and `GeographicLocation` for the machine-readable coordinates.

**End of GeographicLocation v1.0.0**
