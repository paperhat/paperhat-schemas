Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Energy and Power

A closed vocabulary of units of measurement for energy, work, heat, and power.

## Purpose

Constrains `$EnumeratedToken` traits that represent energy or power units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to energy or power units. Energy and power are combined in one vocabulary because they are closely related dimensions and frequently appear together in domain schemas.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$KilowattHour`, `$BritishThermalUnit`, `$Horsepower`). Labels carry the standard symbol or abbreviation (e.g., `kWh`, `BTU`, `hp`).

## Scope

This vocabulary includes SI energy units (joule, kilojoule, megajoule, gigajoule), thermal units (calorie, kilocalorie, British thermal unit, therm), electrical energy units (watt-hour, kilowatt-hour, megawatt-hour), mechanical energy units (foot-pound, erg, electronvolt), SI power units (watt, kilowatt, megawatt, gigawatt), and mechanical power units (horsepower, metric horsepower, foot-pounds per second, British thermal units per hour). It excludes archaic or specialized units not in common modern use.

**End of Units of Energy and Power v1.0.0**
