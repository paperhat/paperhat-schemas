Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Electrical Measurement

A closed vocabulary of units of measurement for electrical quantities.

## Purpose

Constrains `$EnumeratedToken` traits that represent electrical units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to electrical units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Milliampere`, `$Kilovolt`, `$Microfarad`). Labels carry the standard symbol or abbreviation (e.g., `mA`, `kV`, `uF`).

## Scope

This vocabulary includes current units (ampere, milliampere, microampere), voltage units (volt, millivolt, kilovolt), resistance units (ohm, kilohm, megohm), capacitance units (farad, microfarad, nanofarad, picofarad), inductance units (henry, millihenry), conductance units (siemens), charge units (coulomb, ampere-hour, milliampere-hour). It excludes archaic or specialized units not in common modern use.

**End of Units of Electrical Measurement v1.0.0**
