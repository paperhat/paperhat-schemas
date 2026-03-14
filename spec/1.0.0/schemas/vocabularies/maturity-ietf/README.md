# Maturity Levels: IETF

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the IETF document maturity levels as established by RFC 2026 (Internet Standards Process) and updated by RFC 6410 (which collapsed the three-stage Standards Track to two stages) and RFC 9280 (RFC Editor model).

## Maturity Stages

| Token | Label | Description |
|---|---|---|
| `$InternetDraft` | internet-draft | Work-in-progress document, not yet an RFC. Expires after six months. |
| `$ProposedStandard` | proposed-standard | Standards Track entry point; technically sound and community-reviewed. |
| `$InternetStandard` | internet-standard | Full Standard (STD); demonstrated interoperability and widespread deployment. |
| `$BestCurrentPractice` | best-current-practice | BCP document codifying community consensus on operational or process matters. |
| `$Informational` | informational | Published for general information; no IETF consensus required. |
| `$Experimental` | experimental | Protocol or procedure published for experimentation and evaluation. |
| `$Historic` | historic | Formerly valid specification, reclassified as no longer recommended. |

## Design Decisions

- `DraftStandard` is omitted: RFC 6410 eliminated the Draft Standard maturity level in 2011. The two-stage model (Proposed Standard → Internet Standard) is current practice.
- `Historic` uses the IETF spelling (not "Historical") to match the official RFC classification.
- `InternetDraft` is included even though I-Ds are not RFCs, because specification authors need to express this pre-publication maturity level.
- `BestCurrentPractice` is a distinct maturity level in the IETF process, not a Standards Track stage.
