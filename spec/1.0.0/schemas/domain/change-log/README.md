Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# ChangeLog

A record of changes to a versioned document or artifact — a chronological list of modifications with dates, authors, and descriptions.

## When to Use

Use `ChangeLog` to record the version history of a document, specification, or artifact. Each `ChangeLogEntry` child carries a version, date, optional author, and content describing the changes.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|

## Design Notes

- `ChangeLog` is `$Structural` and `$MustNotBeEntity` — a pure container for entries.
- `ChangeLogEntry` is `$Semantic` and `$MustNotBeEntity` — carries version, date, and content.
- `ChangeLogEntry` content is `$Flow` whitespace mode for the change description.
- Entries are ordered by the author (most recent first is a convention, not enforced by the schema).

---

**End of ChangeLog v1.0.0**
