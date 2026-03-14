# Maturity Levels: OASIS

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the OASIS specification maturity levels as established by the OASIS Standards Process. Covers the Committee Specification track, the OASIS Standard track, and the Committee Note track.

## Maturity Stages

| Token | Label | Description |
|---|---|---|
| `$WorkingDraft` | working-draft | In-progress document developed by an OASIS Technical Committee. |
| `$CommitteeSpecificationDraft` | committee-specification-draft | CSD: Draft approved by the TC for public review. |
| `$CommitteeSpecification` | committee-specification | CS: Approved by the TC after public review; may be submitted as a Candidate OASIS Standard. |
| `$CandidateOasisStandard` | candidate-oasis-standard | COS: Committee Specification submitted for OASIS-wide membership ballot. |
| `$OasisStandard` | oasis-standard | OS: Approved by OASIS membership ballot as a full OASIS Standard. |
| `$CommitteeNote` | committee-note | Non-normative informational document published by a TC. |
| `$CommitteeNoteDraft` | committee-note-draft | Draft of a Committee Note, published for review. |
| `$ErrataApproved` | errata-approved | Approved errata document correcting a published specification. |
| `$Rescinded` | rescinded | Standard or specification formally rescinded by OASIS. |

## Design Decisions

- The OASIS process has a clear escalation path: WD → CSD → CS → COS → OS. Each stage represents a distinct approval gate.
- Committee Notes are a separate non-normative track but are included because they are a formal OASIS deliverable type.
- `ErrataApproved` is included as a maturity label because OASIS publishes errata as distinct tracked documents.
- `Rescinded` is the OASIS term for formal withdrawal of a standard.
