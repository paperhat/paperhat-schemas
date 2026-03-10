Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Temperature

A closed vocabulary of units of measurement for temperature.

## Purpose

Constrains `$EnumeratedToken` traits that represent temperature units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to temperature units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Celsius`, `$Fahrenheit`, `$Kelvin`). Labels carry the standard symbol (e.g., `C`, `F`, `K`).

## Scope

This vocabulary includes the four standard temperature scales: Celsius, Fahrenheit, Kelvin, and Rankine. It excludes historical scales (Delisle, Newton, Reaumur, Romer) not in common modern use.

**End of Units of Temperature v1.0.0**
