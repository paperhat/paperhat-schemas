Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# IANA Time Zone Database Identifiers

A closed vocabulary of canonical time zone identifiers from the IANA Time Zone Database (also known as tzdata or the Olson database).

## Purpose

Constrains `$EnumeratedToken` traits that represent time zones to well-known, unambiguous identifiers. Preferred over UTC offsets because they account for daylight saving time transitions and long-term rule changes.

## Token format

Tokens use an underscore-delimited form derived from the canonical `Area/Location` identifier (e.g., `$America_NewYork`, `$Europe_London`, `$Asia_Tokyo`). Each underscore-separated segment uses PascalCase. Multi-word location names within a segment are merged into PascalCase (e.g., IANA `New_York` becomes `NewYork`). Labels provide the original IANA identifier for reference.

## Scope

This vocabulary includes a curated set of commonly used IANA identifiers. It is
not the full semantic domain of the Paperhat `Timezone` type; it is a schema
vocabulary for enumerated-token use. It includes `$Etc_UTC` because
`Etc/UTC` is an IANA identifier. It excludes alias identifiers, bare `UTC`,
bare `Z`, numeric offsets, POSIX-style identifiers, and zones that differ only
by archived rule sets.

**End of IANA Time Zone Database Identifiers v1.0.0**
