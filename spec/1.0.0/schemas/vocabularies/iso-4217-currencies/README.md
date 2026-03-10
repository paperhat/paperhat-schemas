Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0
Editor: Charles F. Munat

# ISO 4217 Currency Codes

A closed vocabulary of active currency codes from the ISO 4217 standard.

## Purpose

Constrains `$EnumeratedToken` traits that represent currencies to the set of internationally recognized currency codes. Referenced by leaf schemas such as MonetaryAmount (`currency`) and Offer (`priceCurrency`).

## Token format

Tokens use the three-letter alphabetic code (e.g., `$USD`, `$EUR`, `$JPY`). Labels provide the human-readable currency name as defined by the standard.

## Scope

This vocabulary includes active circulating currencies. It excludes inactive codes, supranational currencies (except `$EUR`), precious metals (XAU, XAG), testing codes (XTS), and fund codes.

**End of ISO 4217 Currency Codes v1.0.0**
