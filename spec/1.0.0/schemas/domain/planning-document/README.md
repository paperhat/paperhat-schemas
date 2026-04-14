Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# PlanningDocument

A strategic planning document with titled sections, milestones, dependencies, deadlines, budgets, release schedules, and temporal projections — a project plan, commercial strategy, roadmap, or operational plan.

## When to Use

Use `PlanningDocument` as the root concept for any strategic or operational planning artifact: a project plan, release roadmap, commercial strategy, dogfooding plan, go-to-market schedule, or domain pack specification. The schema composes milestones, dependencies, deadlines, budgets, releases, products, and narrative sections into a coherent document with temporal projections.

## Concepts

### PlanningDocument

The root document concept. Entity with stable identity.

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The document title. |
| planningDocumentKind | $EnumeratedToken | no | Classification: `$ProjectPlan`, `$CommercialStrategy`, `$Roadmap`, `$OperationalPlan`, `$DogfoodingPlan`, `$DomainPackSpecification`. Open vocabulary. |
| planningDocumentStatus | $EnumeratedToken | no | Lifecycle status: `$Draft`, `$Active`, `$Approved`, `$Superseded`, `$Archived`. Open vocabulary. |

### Phase

A named phase within a planning document. Entity with stable identity. Phases contain the same child types as the root document (milestones, dependencies, budgets, releases, sections, narrative) scoped to that phase.

| Trait | Type | Required | Description |
|---|---|---|---|
| title | $Text | yes | The phase title. |
| phaseStatus | $EnumeratedToken | no | Lifecycle status: `$Planned`, `$Active`, `$Completed`, `$Deferred`. Open vocabulary. |

## Children (both PlanningDocument and Phase)

| Child | Schema | Description |
|---|---|---|
| audience:Audience | paperhat-audience | Target audience for the plan. |
| budget:Budget | paperhat-budget | Financial plans. |
| budgetLine:BudgetLine | paperhat-budget-line | Individual budget line items. |
| deadline:Deadline | paperhat-deadline | Temporal obligations. |
| dependency:Dependency | paperhat-dependency | Directional dependency relationships. |
| desc:Description | paperhat-description | Prose description. |
| docmeta:DocumentMetadata | paperhat-document-metadata | Authorship, dates, versioning (root only, max 1). |
| milestone:Milestone | paperhat-milestone | Named target achievements. |
| narrative:Narrative | paperhat-narrative | Extended prose content. |
| product:Product | paperhat-product | Products described in the plan. |
| release:Release | paperhat-release | Versioned release milestones. |
| section:Section | paperhat-section | Titled content sections. |
| series:SeriesInformation | paperhat-series | Series membership (root only). |
| tags:Tags | paperhat-tags | Freeform categorization. |
| temporal:TemporalAnnotations | paperhat-temporal | Keyed temporal values. |
| work:Work | paperhat-work | Authorship and licensing (root only, max 1). |

## Imports

| Namespace | Schema |
|---|---|
| audience | paperhat-audience |
| budget | paperhat-budget |
| budgetLine | paperhat-budget-line |
| deadline | paperhat-deadline |
| dependency | paperhat-dependency |
| desc | paperhat-description |
| docmeta | paperhat-document-metadata |
| milestone | paperhat-milestone |
| narrative | paperhat-narrative |
| product | paperhat-product |
| release | paperhat-release |
| section | paperhat-section |
| series | paperhat-series |
| tags | paperhat-tags |
| temporal | paperhat-temporal |
| work | paperhat-work |

## Design Notes

- `PlanningDocument` is the first Paperhat "composer" schema for planning artifacts. It wires together 16 imported leaf schemas into a coherent document structure.
- `Phase` is a locally-defined concept (not imported) that provides temporal and organizational grouping within a plan. Phases are entities because they have stable identity ("Phase 1: Ship") and are referenced by dependency relationships.
- BudgetLine children are allowed at both the root and phase level, enabling both plan-level and phase-level budget detail.
- Dependency children at the root level express cross-phase dependencies. Dependency children within a phase express intra-phase dependencies.
- Ordered collection rules preserve the authored sequence of phases and sections.
- This schema does not import Obligation, ReviewCycle, Recurrence, ComplianceStatus, ScenarioModel, or other governance/workflow schemas. Those are wired by higher-level composers for governance plans and operational documents.

---

**End of PlanningDocument v1.0.0**
