# Maturity Levels: ISO

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the ISO/IEC document maturity levels as established by the ISO/IEC Directives, Part 1. Covers the full development lifecycle from preliminary work through to published International Standard or withdrawal.

## Maturity Stages

| Token | Label | Description |
|---|---|---|
| `$PreliminaryWorkItem` | preliminary-work-item | PWI: Preliminary stage before a formal new work item proposal. |
| `$NewWorkItemProposal` | new-work-item-proposal | NP/NWIP: Formal proposal for new work approved by the technical committee. |
| `$WorkingDraft` | working-draft | WD: Successive drafts developed within the working group. |
| `$CommitteeDraft` | committee-draft | CD: Draft circulated to the full technical committee for comment and ballot. |
| `$DraftInternationalStandard` | draft-international-standard | DIS: Draft circulated to all ISO member bodies for a five-month vote. |
| `$FinalDraftInternationalStandard` | final-draft-international-standard | FDIS: Final draft circulated for a two-month approval vote. |
| `$InternationalStandard` | international-standard | IS: Published International Standard. |
| `$TechnicalSpecification` | technical-specification | TS: Normative document published when consensus for IS is not yet achievable. |
| `$TechnicalReport` | technical-report | TR: Informative document containing information of a different kind from an IS or TS. |
| `$PubliclyAvailableSpecification` | publicly-available-specification | PAS: Specification published to respond to an urgent market need, with less consensus than a TS. |
| `$Withdrawn` | withdrawn | Standard or document formally withdrawn from the ISO catalogue. |

## Design Decisions

- Includes both the main standards track (PWI → NP → WD → CD → DIS → FDIS → IS) and the alternative deliverables (TS, TR, PAS) because specifications commonly carry these labels.
- ISO/IEC JTC 1 follows the same process; no separate JTC 1 vocabulary is needed.
- `Withdrawn` is a terminal state; systematic review also results in confirmation or revision, but those are process actions, not maturity labels.
