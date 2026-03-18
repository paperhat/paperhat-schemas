Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Organizational Unit

A named subdivision within an organization, such as a department, division, team, bureau, or working group. Organizational Unit represents the structural building block of an organization's internal hierarchy.

## When to Use

Use `OrganizationalUnit` to represent a named internal subdivision of an organization. Examples include departments (Engineering, Marketing), divisions (North America Division), teams (Platform Team), bureaus, or working groups. OrganizationalUnit is an entity (`$MustBeEntity`) and is referenceable from other schemas. It is distinct from Organization (the top-level institution) and Role (a function held by a person).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The unit name (e.g., "Engineering", "North America Division", "Platform Team"). |
| unitKind | $EnumeratedToken | no | Classification token, e.g., `$Department`, `$Division`, `$Team`, `$Bureau`, `$WorkingGroup`, `$Committee`, `$Office`. Open vocabulary. |
| parentUnit | $Iri | no | Reference to the parent OrganizationalUnit in a hierarchy. Marked as a reference trait (`isReferenceTrait=true`). |

## Constraints

`name` is required. An organizational unit without a name is empty.

## Design Notes

- OrganizationalUnit is an entity (`$MustBeEntity`) because subdivisions need stable identity for cross-references. Role assignments, Projects, and other schemas reference an OrganizationalUnit by entity IRI.
- `parentUnit` allows modeling of hierarchical organization structures (e.g., a Team within a Department within a Division) without requiring a separate hierarchy schema.
- This is a pure leaf with no imports and no children. Higher-level organizational composers (Stage 4) will compose OrganizationalUnit as a child of Organization alongside Role, ContactPoint, and Location.
- `unitKind` is `$EnumeratedToken` rather than `$Text` because unit types are machine-readable classifiers. Display labels belong in the consuming schema's localization bundle.

---

**End of Organizational Unit v1.0.0**
