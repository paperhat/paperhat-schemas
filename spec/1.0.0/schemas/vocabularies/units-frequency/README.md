Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Frequency

A closed vocabulary of units of measurement for frequency and periodic rate.

## Purpose

Constrains `$EnumeratedToken` traits that represent frequency units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to frequency units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Megahertz`, `$RevolutionsPerMinute`, `$BeatsPerMinute`). Labels carry the standard symbol or abbreviation (e.g., `MHz`, `rpm`, `bpm`).

## Scope

This vocabulary includes SI frequency units (hertz, kilohertz, megahertz, gigahertz, terahertz) and rotational and rhythmic rate units (revolutions per minute, beats per minute). It excludes specialized scientific frequency units not in common use.

**End of Units of Frequency v1.0.0**
