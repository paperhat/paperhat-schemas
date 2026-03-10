Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# Units of Digital Data

A closed vocabulary of units of measurement for digital data storage and transfer rate.

## Purpose

Constrains `$EnumeratedToken` traits that represent data size or data rate units. Used by the Measure schema's `unit` trait when a consuming schema restricts allowed values to data units.

## Token format

Tokens use fully spelled out PascalCase names (e.g., `$Gigabyte`, `$Mebibyte`, `$MegabitsPerSecond`). Labels carry the standard symbol or abbreviation (e.g., `GB`, `MiB`, `Mbps`).

## Scope

This vocabulary includes decimal storage units (byte, kilobyte, megabyte, gigabyte, terabyte, petabyte), binary storage units (kibibyte, mebibyte, gibibyte, tebibyte, pebibyte), the bit, and transfer rate units (bits per second, kilobits per second, megabits per second, gigabits per second). It excludes nibbles, words, and archaic storage units.

**End of Units of Digital Data v1.0.0**
