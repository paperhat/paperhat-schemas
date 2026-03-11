Status: NORMATIVE
Lock State: LOCKED
Version: 1.0.0

# Person

A person, real or fictional, composed from leaf concepts for names, contact points, identifiers, and locations.

## When to Use

Use `Person` to represent any human being — an author, a character, a well-known figure, a contributor, or anyone who needs identity within a document. Person is an entity (`$MustBeEntity`) and can be referenced from other schemas.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| gender | $Text | no | Free-text gender identity. Codex does not impose a controlled vocabulary. |
| birthDate | $Date | no | Date of birth. For uncertain dates, use the best known date or omit. |
| deathDate | $Date | no | Date of death. Omit for living persons. |

## Children

| Child | Schema | Description |
|---|---|---|
| pname:PersonName | `paperhat:domain:person-name` | Names for this person. Multiple instances with different `nameKind` values support legal names, birth names, aliases, stage names, etc. |
| contact:ContactPoint | `paperhat:domain:contact-point` | Contact methods. Use `contactKind` to distinguish work, personal, emergency roles. |
| ident:Identifier | `paperhat:domain:identifier` | External identifiers (passport, ORCID, SSN). |
| loc:Location | `paperhat:domain:location` | Associated locations (birthplace, residence, workplace). |

## Imports

| Namespace | Schema |
|---|---|
| pname | `paperhat:domain:person-name` |
| contact | `paperhat:domain:contact-point` |
| ident | `paperhat:domain:identifier` |
| loc | `paperhat:domain:location` |

## Constraints

- At least one `pname:PersonName` child is required.

## Design Notes

- Person is an entity; PersonName is not. A PersonName is a value — it describes a name but has no independent identity. A Person is an individual who can be referenced from citations, attributions, or character lists.
- No Description or biography trait. Biographical prose belongs in a document *about* the person, not *inside* the Person entity.
- Media attachment uses the `media-reference` schema package.

---

**End of Person v1.0.0**
