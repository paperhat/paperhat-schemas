Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Speed

A closed vocabulary of units of measurement for speed and velocity.

## Purpose

Constrains `$EnumeratedToken` traits that represent speed units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to speed units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$KilometersPerHour`, `$MetersPerSecond`, `$Knot`). Labels carry the standard symbol or abbreviation (e.g., `km/h`, `m/s`, `kn`).

## Scope

This vocabulary includes metric units (meters per second, kilometers per hour), imperial and customary units (miles per hour, feet per second), nautical units (knot), and the Mach number. It excludes specialized scientific velocity units not in common use.

**End of Units of Speed v1.0.0**
