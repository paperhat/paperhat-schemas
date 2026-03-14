# Maturity Levels: W3C

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the W3C Recommendation Track maturity levels as revised by the W3C Process Document (2023). Includes the full Recommendation Track, Note Track, and Registry Track stages.

## Maturity Stages

| Token | Label | Description |
|---|---|---|
| `$WorkingDraft` | working-draft | First Public Working Draft or subsequent WD published for review. |
| `$CandidateRecommendation` | candidate-recommendation | Specification believed to be stable; inviting wide review and implementation experience. |
| `$CandidateRecommendationDraft` | candidate-recommendation-draft | In-progress update to a Candidate Recommendation, open for review. |
| `$CandidateRecommendationSnapshot` | candidate-recommendation-snapshot | Stable snapshot of a Candidate Recommendation capturing a specific state. |
| `$ProposedRecommendation` | proposed-recommendation | Submitted to the W3C Advisory Committee for final approval. |
| `$Recommendation` | recommendation | Endorsed by W3C as a Web standard. |
| `$Superseded` | superseded | Recommendation replaced by a newer version but still available. |
| `$Obsolete` | obsolete | Recommendation no longer considered relevant. |
| `$GroupNote` | group-note | Published W3C Group Note (informative, not on Recommendation Track). |
| `$DraftNote` | draft-note | Draft of a Group Note, published for review. |
| `$StatementNote` | statement-note | W3C Statement published as a Group Note with AC review. |
| `$RegistryReport` | registry-report | W3C Registry Track report tracking registered values. |
| `$DraftRegistryReport` | draft-registry-report | Draft of a Registry Report. |

## Design Decisions

- Includes the W3C Process 2023 split of Candidate Recommendation into Draft and Snapshot sub-stages.
- Note Track and Registry Track stages are included because W3C documents commonly carry these maturity labels and authors need to express them.
- `Superseded` and `Obsolete` are the official W3C end-of-life labels for Recommendations.
