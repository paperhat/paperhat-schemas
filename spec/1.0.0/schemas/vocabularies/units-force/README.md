Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Force

A closed vocabulary of units of measurement for force.

## Purpose

Constrains `$EnumeratedToken` traits that represent force units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to force units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Newton`, `$PoundForce`, `$KilogramForce`). Labels carry the standard symbol or abbreviation (e.g., `N`, `lbf`, `kgf`).

## Scope

This vocabulary includes SI units (newton, kilonewton, meganewton), CGS units (dyne), and gravitational and imperial units (kilogram-force, pound-force, poundal). It excludes archaic or specialized units not in common modern use.

**End of Units of Force v1.0.0**
