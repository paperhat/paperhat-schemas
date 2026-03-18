Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Project

A named initiative, effort, or body of work with identity — a software project, specification effort, research program, or any other bounded endeavor that has contributors, artifacts, and a lifecycle.

## When to Use

Use `Project` to represent any bounded endeavor: a software project, a specification effort, a research program, a publication series, or an infrastructure initiative. Projects are entities (`$MustBeEntity`) and are referenceable from other schemas. Project is distinct from Product (a commercial offering) and Organization (an institution).

## Traits

| Trait | Type | Required | Description |
|---|---|---|---|
| name | $Text | yes | The project name (e.g., "Codex", "Lexis", "Praxis"). |
| projectKind | $EnumeratedToken | no | Classification token, e.g., `$Software`, `$Specification`, `$Research`, `$Publication`, `$Infrastructure`, `$Standard`. Open vocabulary. |
| repositoryUrl | $Url | no | Primary source repository URL (e.g., GitHub). |
| websiteUrl | $Url | no | Project website URL. |
| projectStatus | $EnumeratedToken | no | Lifecycle status, e.g., `$Active`, `$Archived`, `$Planning`, `$Completed`, `$Suspended`, `$Deprecated`. Open vocabulary. |

## Children

| Child | Schema | Description |
|---|---|---|
| desc:Description | `paperhat:domain:description` | Free-text project description. |
| ident:Identifier | `paperhat:domain:identifier` | External identifiers (DOI, registry IDs, package registry names). |
| tags:Tags | `paperhat:domain:tags` | Freeform categorization. |
| work:Work | `paperhat:domain:work` | Authorship, licensing, dates, versioning. |
| temporal:TemporalAnnotations | `paperhat:domain:temporal` | Project start date, end date, milestones, and other keyed temporal annotations. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| ident | `paperhat:domain:identifier` |
| tags | `paperhat:domain:tags` |
| work | `paperhat:domain:work` |
| temporal | `paperhat:domain:temporal` |

## Design Notes

- Project is an entity (`$MustBeEntity`) because it needs stable identity for cross-references. Organization, Role, and other schemas reference Projects by entity IRI.
- Repository is a trait (`repositoryUrl`) rather than a separate concept, because a repository URL is a single value. If a project has multiple repositories, use `Identifier` children with `scheme=$Repository` for the additional URLs.
- Role assignments are not children of Project in this leaf schema. Role is composed as a child by higher-level schemas (Stage 4 organizational composers) that bring Project and Role together.
- The import set follows the standard leaf composition pattern used by Event, Organization, and similar entity schemas.

---

**End of Project v1.0.0**
