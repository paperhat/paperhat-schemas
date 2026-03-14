# Maturity Levels: IEEE

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines the IEEE Standards Association document maturity levels covering the full lifecycle from project authorization through publication and end-of-life.

## Maturity Stages

| Token | Label | Description |
|---|---|---|
| `$ProjectAuthorized` | project-authorized | PAR approved; working group authorized to develop the standard. |
| `$Draft` | draft | Working group draft under active development. |
| `$Balloting` | balloting | Draft submitted for sponsor ballot by IEEE-SA members. |
| `$Standard` | standard | Approved and published IEEE standard. |
| `$Corrigendum` | corrigendum | Published correction to an existing standard without changing its scope. |
| `$Amendment` | amendment | Published modification that adds to or changes an existing standard. |
| `$Superseded` | superseded | Replaced by a newer revision but still available for reference. |
| `$Withdrawn` | withdrawn | Removed from active status; no longer maintained or recommended. |

## Design Decisions

- `ProjectAuthorized` represents the PAR (Project Authorization Request) approval stage rather than the PAR submission itself, since PAR approval is the meaningful lifecycle gate.
- `Corrigendum` and `Amendment` are included as maturity labels because IEEE publishes these as distinct deliverables with their own document numbers.
- IEEE "Active" status is represented by `Standard`; the term "active" is a catalogue status, not a maturity label.
- IEEE standards have a 10-year review cycle; reaffirmation is a process action, not a separate maturity level.
