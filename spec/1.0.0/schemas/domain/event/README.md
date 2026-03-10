Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Event

An occurrence happening at a certain time and place — a concert, conference, lecture, festival, lexis, or community gathering.

## When to Use

Use `Event` to represent any named occurrence with a time dimension: scheduled happenings, recurring meetings, performances, sporting events, or ceremonies. Events are entities (`$MustBeEntity`) and can be referenced from other schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The name of the event. |
| startDate | $Date | no | When the event begins. |
| endDate | $Date | no | When the event ends. For single-day events, omit or set equal to startDate. |
| eventStatus | $EnumeratedToken | no | Scheduling status, e.g. `$scheduled`, `$cancelled`, `$postponed`, `$rescheduled`. |
| eventAttendanceMode | $EnumeratedToken | no | Attendance mode, e.g. `$offline`, `$online`, `$mixed`. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `codex:domain:description` | Free-text description of the event. |
| loc:Location | `codex:domain:location` | Venue name, city, region, country. |
| geo:GeographicLocation | `codex:domain:geographic-location` | Precise coordinates of the venue. |
| contact:ContactPoint | `codex:domain:contact-point` | Organizer or box-office contact info. |
| ident:Identifier | `codex:domain:identifier` | Event IDs, ticket barcodes, registration codes. |
| offer:Offer | `codex:domain:offer` | Ticket pricing, availability, and conditions. |
| dur:Duration | `codex:domain:duration` | Length of the event. |
| rating:Rating | `codex:domain:rating` | Aggregate reviews or ratings. |
| money:MonetaryAmount | `codex:domain:monetary-amount` | Admission cost when not expressed via Offer. |
| tags:Tags | `codex:domain:tags` | Freeform categorization. |
| work:Work | `codex:domain:work` | Authorship, licensing, provenance. |
| schedule:OperatingSchedule | `codex:domain:operating-schedule` | Recurring schedule information. |
| audience:Audience | `codex:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `codex:domain:accessibility` | Accessibility information. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| loc | `codex:domain:location` |
| geo | `codex:domain:geographic-location` |
| contact | `codex:domain:contact-point` |
| ident | `codex:domain:identifier` |
| offer | `codex:domain:offer` |
| dur | `codex:domain:duration` |
| rating | `codex:domain:rating` |
| money | `codex:domain:monetary-amount` |
| tags | `codex:domain:tags` |
| work | `codex:domain:work` |
| schedule | `codex:domain:operating-schedule` |
| audience | `codex:domain:audience` |
| a11y | `codex:domain:accessibility` |

## Design Notes

- Event composes 14 leaf concepts, validating the leaf-first architecture: leaves designed independently compose naturally into entity-level schemas.
- Performer and organizer relationships (references to Person or Organization) will be modeled once the cross-entity Reference pattern is established.
- The `eventStatus` and `eventAttendanceMode` traits use open `$EnumeratedToken` values. These are candidates for future vocabulary packages once the token sets stabilize.
- Media attachment uses the `media-reference` schema package.

**End of Event v1.0.0**
