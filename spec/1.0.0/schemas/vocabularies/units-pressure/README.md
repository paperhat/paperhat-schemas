Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Pressure

A closed vocabulary of units of measurement for pressure and stress.

## Purpose

Constrains `$EnumeratedToken` traits that represent pressure units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to pressure units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Kilopascal`, `$Atmosphere`, `$PoundsPerSquareInch`). Labels carry the standard symbol or abbreviation (e.g., `kPa`, `atm`, `psi`).

## Scope

This vocabulary includes SI units (pascal, kilopascal, megapascal), bar-family units (bar, millibar), atmospheric and mercury-column units (atmosphere, torr, millimeter of mercury, inch of mercury), and imperial units (pounds per square inch). It excludes archaic or specialized units not in common modern use.

**End of Units of Pressure v1.0.0**
