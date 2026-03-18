Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Role

A named function or capacity that a person or organization holds, such as author, editor, maintainer, or approver. Role represents the abstract function independent of who fills it or where it is assigned.

## When to Use

Use `Role` to assign a named function to a person or organization within a context. Role is a leaf concept designed to be composed as a child of higher-level schemas such as Organization, Project, or any entity that needs role assignments. The `roleKind` trait is an open `$EnumeratedToken` at the leaf level; importing schemas constrain it via `AllowedValues` to the role tokens valid in their context.

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| roleKind | $EnumeratedToken | yes | The role token. Open vocabulary at leaf level. Importing schemas constrain via `AllowedValues`. Common values: `$author`, `$editor`, `$maintainer`, `$reviewer`, `$approver`, `$contributor`, `$owner`, `$director`, `$officer`. |
| holder | $Iri | no | Reference to the Person or Organization entity filling this role. Marked as a reference trait (`isReferenceTrait=true`). |
| scope | $Text | no | Free-text description of what the role covers (e.g., "Codex specification", "all Lexis schemas"). |

## Constraints

`roleKind` is required. A Role without a kind is empty.

## Design Notes

- Role is a pure leaf with no imports and no children.
- `roleKind` is `$EnumeratedToken` rather than `$Text` because roles are machine-readable classifiers. Display labels (e.g., "Editor", "Lead Maintainer") belong in the consuming schema's localization bundle, not in the Role instance.
- `holder` is an optional reference trait. When a Role is composed as a child of an Organization or Project, the holder links to the person filling the role. When a Role describes a template position (e.g., "the Editor role requires..."), holder is omitted.
- Responsibility and authority are expressed via `roleKind` and `scope`, not as sub-concepts. A `$maintainer` with `scope="Codex specification"` captures both the function and its boundary.

---

**End of Role v1.0.0**
