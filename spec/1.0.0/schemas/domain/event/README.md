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
| desc:Description | `paperhat:domain:description` | Free-text description of the event. |
| loc:Location | `paperhat:domain:location` | Venue name, city, region, country. |
| geo:GeographicLocation | `paperhat:domain:geographic-location` | Precise coordinates of the venue. |
| contact:ContactPoint | `paperhat:domain:contact-point` | Organizer or box-office contact info. |
| ident:Identifier | `paperhat:domain:identifier` | Event IDs, ticket barcodes, registration codes. |
| offer:Offer | `paperhat:domain:offer` | Ticket pricing, availability, and conditions. |
| dur:Duration | `paperhat:domain:duration` | Length of the event. |
| rating:Rating | `paperhat:domain:rating` | Aggregate reviews or ratings. |
| money:MonetaryAmount | `paperhat:domain:monetary-amount` | Admission cost when not expressed via Offer. |
| tags:Tags | `paperhat:domain:tags` | Freeform categorization. |
| work:Work | `paperhat:domain:work` | Authorship, licensing, provenance. |
| schedule:OperatingSchedule | `paperhat:domain:operating-schedule` | Recurring schedule information. |
| audience:Audience | `paperhat:domain:audience` | Target audience metadata. |
| a11y:Accessibility | `paperhat:domain:accessibility` | Accessibility information. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| loc | `paperhat:domain:location` |
| geo | `paperhat:domain:geographic-location` |
| contact | `paperhat:domain:contact-point` |
| ident | `paperhat:domain:identifier` |
| offer | `paperhat:domain:offer` |
| dur | `paperhat:domain:duration` |
| rating | `paperhat:domain:rating` |
| money | `paperhat:domain:monetary-amount` |
| tags | `paperhat:domain:tags` |
| work | `paperhat:domain:work` |
| schedule | `paperhat:domain:operating-schedule` |
| audience | `paperhat:domain:audience` |
| a11y | `paperhat:domain:accessibility` |

## Design Notes

- Event composes 14 leaf concepts, validating the leaf-first architecture: leaves designed independently compose naturally into entity-level schemas.
- Performer and organizer relationships (references to Person or Organization) will be modeled once the cross-entity Reference pattern is established.
- The `eventStatus` and `eventAttendanceMode` traits use open `$EnumeratedToken` values. These are candidates for future vocabulary packages once the token sets stabilize.
- Media attachment uses the `media-reference` schema package.

**End of Event v1.0.0**
