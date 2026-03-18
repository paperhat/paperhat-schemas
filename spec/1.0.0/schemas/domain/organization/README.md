Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Organization

An organization with identity — a company, nonprofit, government body, educational institution, or any other named collective entity.

## When to Use

Use `Organization` to represent any named entity that is not a person: corporations, charities, government agencies, universities, clubs, or bands. Organizations are entities (`$MustBeEntity`) and are referenceable from other schemas.

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
| desc:Description | `paperhat:domain:description` | Free-text description of the organization. |
| contact:ContactPoint | `paperhat:domain:contact-point` | Email addresses, phone numbers, websites. |
| ident:Identifier | `paperhat:domain:identifier` | Tax IDs, registration numbers, stock tickers. |
| loc:Location | `paperhat:domain:location` | Headquarters, branches, registered addresses. |
| tags:Tags | `paperhat:domain:tags` | Freeform categorization. |
| work:Work | `paperhat:domain:work` | Authorship, licensing, provenance. |
| schedule:OperatingSchedule | `paperhat:domain:operating-schedule` | Business hours and recurring schedules. |
| audience:Audience | `paperhat:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `paperhat:domain:accessibility` | Accessibility information. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| contact | `paperhat:domain:contact-point` |
| ident | `paperhat:domain:identifier` |
| loc | `paperhat:domain:location` |
| tags | `paperhat:domain:tags` |
| work | `paperhat:domain:work` |
| schedule | `paperhat:domain:operating-schedule` |
| audience | `paperhat:domain:audience` |
| a11y | `paperhat:domain:accessibility` |

## Design Notes

- Organization names are modeled as a required trait rather than a child concept. Unlike person names (which have complex decomposition into given/family/middle/title), organization names are single strings.
- Organization-to-Person relationships (employment, membership) will be modeled once the cross-entity Reference pattern is established.
- Media attachment uses the `media-reference` schema package.

---

**End of Organization v1.0.0**
