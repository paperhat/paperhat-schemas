Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Angle

A closed vocabulary of units of measurement for plane angle.

## Purpose

Constrains `$EnumeratedToken` traits that represent angle units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to angle units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Degree`, `$Radian`, `$ArcMinute`). Labels carry the standard symbol or abbreviation (e.g., `deg`, `rad`, `arcmin`).

## Scope

This vocabulary includes degree and its subdivisions (degree, arc minute, arc second), SI and mathematical units (radian, milliradian, turn), and the gradian. It excludes specialized navigation and surveying angle units not in common modern use.

**End of Units of Angle v1.0.0**
