Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Project

A named initiative, effort, or body of work with identity — a software project, specification effort, research program, or any other bounded endeavor that has contributors, artifacts, and a lifecycle.

## When to Use

Use `Project` to represent any bounded endeavor: a software project, a specification effort, a research program, a publication series, or an infrastructure initiative. Projects are entities (`$MustBeEntity`) and can be referenced from other schemas. Project is distinct from Product (a commercial offering) and Organization (an institution).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The project name (e.g., "Codex", "Lexis", "Praxis"). |
| projectKind | $EnumeratedToken | no | Classification token, e.g., `$software`, `$specification`, `$research`, `$publication`, `$infrastructure`, `$standard`. Open vocabulary. |
| repositoryUrl | $Url | no | Primary source repository URL (e.g., GitHub). |
| websiteUrl | $Url | no | Project website URL. |
| projectStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$active`, `$archived`, `$planning`, `$completed`, `$suspended`, `$deprecated`. Open vocabulary. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `codex:domain:description` | Free-text project description. |
| ident:Identifier | `codex:domain:identifier` | External identifiers (DOI, registry IDs, package registry names). |
| tags:Tags | `codex:domain:tags` | Freeform categorization. |
| work:Work | `codex:domain:work` | Authorship, licensing, dates, versioning. |
| temporal:Temporal | `codex:domain:temporal` | Project start date, end date, milestones. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `codex:domain:description` |
| ident | `codex:domain:identifier` |
| tags | `codex:domain:tags` |
| work | `codex:domain:work` |
| temporal | `codex:domain:temporal` |

## Design Notes

- Project is an entity (`$MustBeEntity`) because it needs stable identity for cross-references. Organization, Role, and other schemas reference Projects by entity IRI.
- Repository is a trait (`repositoryUrl`) rather than a separate concept, because a repository URL is a single value. If a project has multiple repositories, use `Identifier` children with `scheme=$repository` for the additional URLs.
- Role assignments are not children of Project in this leaf schema. Role is composed as a child by higher-level schemas (Stage 4 organizational composers) that bring Project and Role together.
- The import set follows the standard leaf composition pattern used by Event, Organization, and similar entity schemas.

---

**End of Project v1.0.0**
