# Acknowledgments

- **Status**: NORMATIVE
- **Lock State**: UNLOCKED
- **Version**: 1.0.0

## Purpose

Defines structured, machine-readable acknowledgments for technical specifications. Participants are recorded with their names, affiliations, roles, and optional contact information. A ParticipantGroup concept supports the common pattern of grouping contributors by organizational role (e.g. "Working Group Members", "Ballot Group Members", "Reviewers"). Covers the acknowledgment patterns required by all major standards bodies.

## Concepts

| Concept | Kind | Entity | Content | Children | Description |
|---|---|---|---|---|---|
| Acknowledgments | Semantic | MustNotBeEntity | ForbidsContent | Participant (1+), ParticipantGroup, Description, Paragraph | Top-level container for all acknowledgments. |
| Participant | Semantic | MayBeEntity | ForbidsContent | Description | An individual contributor with name, affiliation, role, and contact information. |
| ParticipantGroup | Semantic | MustNotBeEntity | ForbidsContent | Participant (1+), Description | A named group of participants sharing a common role (e.g. "Working Group Members"). |

## Imports

| Namespace | Schema | Provides |
|---|---|---|
| desc | `paperhat:domain:description` | Description |
| text | `paperhat:domain:text` | Paragraph |

## Traits

| Trait | Value Type | Constrained | Description |
|---|---|---|---|
| `name` | `$Text` | -- | Full name of the participant. |
| `affiliation` | `$Text` | -- | Organization the participant represents. |
| `role` | `$EnumeratedToken` | ParticipantRole | Role in the specification development. |
| `email` | `$Text` | -- | Contact email address. |
| `uri` | `$Iri` | -- | Personal or organizational URI. |
| `key` | `$LookupToken` | -- | Stable lookup key for cross-referencing. |
| `label` | `$Text` | -- | Short display label. |
| `title` | `$Text` | -- | Optional title for the acknowledgments section. |
| `groupName` | `$Text` | -- | Name of the participant group. |
| `groupRole` | `$EnumeratedToken` | ParticipantRole | Default role for all participants in the group. |

## Enumerated Value Sets

### ParticipantRole (13 members)

| Member | Description |
|---|---|
| `Editor` | Primary editor of the specification. |
| `CoEditor` | Co-editor sharing editorial responsibility. |
| `Chair` | Chair of the working group or committee. |
| `CoChair` | Co-chair sharing leadership. |
| `Contributor` | Active contributor to the specification content. |
| `Reviewer` | Reviewed the specification and provided feedback. |
| `BallotGroupMember` | Member of the ballot group for formal approval. |
| `Observer` | Participated in an observer capacity. |
| `Secretary` | Secretary of the working group or committee. |
| `TechnicalContact` | Primary technical contact for the specification. |
| `ProjectLead` | Lead of the overall project. |
| `FormerEditor` | Previous editor no longer active. |
| `Acknowledgee` | General acknowledgment without a specific technical role. |

## Design Decisions

- `Participant` is MayBeEntity: participants who need cross-referencing (e.g. the editor referenced from the foreword) get entity IDs; minor acknowledgees do not.
- `ParticipantGroup` enables the common standards pattern of listing participants by group ("The following were members of the Working Group at the time of publication:"). The `groupRole` trait provides the default role for all members; individual Participant `role` traits can override it.
- `name` is a single `$Text` trait rather than importing the person-name schema. Acknowledgment sections typically list display names ("Jane Q. Smith, Acme Corp."), not structured name components. The person-name schema is available via document-metadata for richer person modeling where needed.
- `email` is `$Text` rather than a dedicated email type because Codex has no native email value type.
- `FormerEditor` is a distinct role because standards documents frequently list former editors separately (e.g. W3C specifications).
- `Acknowledgee` is the catch-all for people thanked without a specific technical role (e.g. "Thanks to John Doe for helpful discussions").
- The role vocabulary is open enough for all major standards bodies: IEEE uses BallotGroupMember, W3C uses Editor/Chair, IETF uses Contributor/Reviewer, ISO uses Secretary/TechnicalContact.
