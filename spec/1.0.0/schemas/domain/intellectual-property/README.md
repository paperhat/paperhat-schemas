# Intellectual Property

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines structured intellectual property declarations for technical specifications. Covers copyright notices, trademarks (unregistered, service marks, and registered), patents with standards-essential licensing commitments, and license grants with SPDX identifiers. An IPNotice container collects all IP declarations into a single machine-readable section. Essential for standards documents where IP disclosure is mandatory (W3C, IETF, ISO, IEEE, OASIS all require IP sections).

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Copyright | Semantic | MustBeEntity | ForbidsContent | Description | Copyright declaration with holder, year or year range, optional jurisdiction and work identification. |
| Trademark | Semantic | MustBeEntity | ForbidsContent | Description | Unregistered trademark (™). |
| ServiceMark | Semantic | MustBeEntity | ForbidsContent | Description | Service mark (℠) for services rather than goods. |
| RegisteredTrademark | Semantic | MustBeEntity | ForbidsContent | Description | Registered trademark (®) with required registration number. |
| Patent | Semantic | MustBeEntity | ForbidsContent | Description | Patent declaration with number, holder, dates, and optional licensing commitment for standards-essential patents. |
| LicenseGrant | Semantic | MustBeEntity | ForbidsContent | Description, Paragraph | License grant with licensor, type, optional licensee, scope, terms URI, and SPDX identifier. |
| IPNotice | Semantic | MustNotBeEntity | ForbidsContent | Copyright, Trademark, ServiceMark, RegisteredTrademark, Patent, LicenseGrant (1+), Description, Paragraph | Container for all IP declarations in a specification. |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `holder` | `$Text` | -- | Copyright holder or patent holder name. |
| `year` | `$Text` | -- | Copyright year or start of year range. |
| `yearEnd` | `$Text` | -- | End year of a copyright year range. |
| `jurisdiction` | `$Text` | -- | Legal jurisdiction. |
| `work` | `$Text` | -- | The copyrighted work being covered. |
| `mark` | `$Text` | -- | The trademark text. |
| `owner` | `$Text` | -- | Owner of the mark. |
| `registrationNumber` | `$Text` | -- | Official registration number. |
| `niceClass` | `$Text` | -- | Nice Classification class number. |
| `patentNumber` | `$Text` | -- | Official patent number. |
| `filingDate` | `$Text` | -- | Patent filing date. |
| `grantDate` | `$Text` | -- | Patent grant date. |
| `licensingCommitment` | `$EnumeratedToken` | LicensingCommitment | Patent licensing commitment for standards-essential patents. |
| `licensor` | `$Text` | -- | Entity granting the license. |
| `licensee` | `$Text` | -- | Entity receiving the license. Omit for universal grants. |
| `licenseType` | `$EnumeratedToken` | LicenseType | Classification of the license. |
| `scope` | `$Text` | -- | What the license covers. |
| `termsUri` | `$Iri` | -- | IRI to the full license text. |
| `spdxIdentifier` | `$Text` | -- | SPDX license identifier (e.g. "Apache-2.0", "MIT"). |
| `label` | `$Text` | -- | Short display label. |
| `noticeTitle` | `$Text` | -- | Optional title for an IP notice section. |

## Enumerated Value Sets

### LicensingCommitment (7 members)

Standards-essential patent licensing commitments as used by W3C, IETF, ISO, IEEE, and OASIS.

| Member | Description |
|---|---|
| `RAND` | Reasonable And Non-Discriminatory terms. |
| `FRAND` | Fair, Reasonable And Non-Discriminatory terms (European usage). |
| `RoyaltyFree` | No royalties required. |
| `RANDRoyaltyFree` | RAND terms with zero royalty (W3C Patent Policy default). |
| `Reciprocal` | License granted on condition of reciprocal licensing. |
| `Unencumbered` | No known patent claims; available without licensing. |
| `Undeclared` | Patent holder has not made a licensing declaration. |

### LicenseType (8 members)

| Member | Description |
|---|---|
| `OpenSource` | Any OSI-approved open source license. |
| `Proprietary` | Proprietary/commercial license. |
| `CreativeCommons` | Creative Commons license family. |
| `PublicDomain` | Dedicated to the public domain (CC0, Unlicense, etc.). |
| `FOSS` | Free and Open Source Software license. |
| `Permissive` | Permissive open source (MIT, BSD, Apache-2.0, etc.). |
| `Copyleft` | Copyleft license (GPL, LGPL, MPL, etc.). |
| `Custom` | A license not covered by the standard categories. |

## Design Decisions

- Trademark, ServiceMark, and RegisteredTrademark are three distinct concepts because they carry different legal weight and render different symbols (™, ℠, ®). RegisteredTrademark requires a registrationNumber; the others allow it optionally.
- `year` and `yearEnd` are `$Text` rather than `$Integer` to accommodate historical conventions like "2020-2026" in the year field itself, and to avoid type system issues with four-digit years.
- `filingDate` and `grantDate` are `$Text` rather than a date type because Codex does not have a native date value type; ISO 8601 strings are the convention.
- `niceClass` refers to the Nice Classification (International Classification of Goods and Services) used worldwide for trademark registration.
- `LicensingCommitment` covers the major patent policy frameworks: RAND (IETF/ISO/IEEE), FRAND (European standard), RoyaltyFree (W3C default), and variations.
- `spdxIdentifier` on LicenseGrant enables machine-readable license identification using the industry-standard SPDX License List.
- `IPNotice` is the section-level container paralleling ConformanceClause, AbbreviationList, SymbolTable, etc.
- All IP concepts are MustBeEntity so they are cross-referenceable from the body of the specification (e.g. "as required by Patent P-1234...").
