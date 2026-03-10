Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Organization

An organization with identity — a company, nonprofit, government body, educational institution, or any other named collective entity.

## When to Use

Use `Organization` to represent any named entity that is not a person: corporations, charities, government agencies, universities, clubs, or bands. Organizations are entities (`$MustBeEntity`) and can be referenced from other schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The primary or legal name of the organization. |
| organizationKind | $EnumeratedToken | no | Classification token, e.g. `$corporation`, `$nonprofit`, `$government`, `$educational`. |
| foundingDate | $Date | no | When the organization was established. |
| dissolutionDate | $Date | no | When the organization ceased to exist. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `codex:domain:description` | Free-text description of the organization. |
| contact:ContactPoint | `codex:domain:contact-point` | Email addresses, phone numbers, websites. |
| ident:Identifier | `codex:domain:identifier` | Tax IDs, registration numbers, stock tickers. |
| loc:Location | `codex:domain:location` | Headquarters, branches, registered addresses. |
| tags:Tags | `codex:domain:tags` | Freeform categorization. |
| work:Work | `codex:domain:work` | Authorship, licensing, provenance. |
| schedule:OperatingSchedule | `codex:domain:operating-schedule` | Business hours and recurring schedules. |
| audience:Audience | `codex:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `codex:domain:accessibility` | Accessibility information. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| contact | `codex:domain:contact-point` |
| ident | `codex:domain:identifier` |
| loc | `codex:domain:location` |
| tags | `codex:domain:tags` |
| work | `codex:domain:work` |
| schedule | `codex:domain:operating-schedule` |
| audience | `codex:domain:audience` |
| a11y | `codex:domain:accessibility` |

## Design Notes

- Organization names are modeled as a required trait rather than a child concept. Unlike person names (which have complex decomposition into given/family/middle/title), organization names are single strings.
- Organization-to-Person relationships (employment, membership) will be modeled once the cross-entity Reference pattern is established.
- Media attachment uses the `media-reference` schema package.

---

**End of Organization v1.0.0**
