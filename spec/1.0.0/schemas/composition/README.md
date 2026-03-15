Status: NORMATIVE
Lock State: UNLOCKED
Version: 1.0.0

# Composition

A graph-native composition schema rooted in `Document`. Composition defines the semantic output graph for one run. It organizes referenced content that lives elsewhere and constrains which realization classes a run is intended to support.

## When to Use

Use `Document` when an authored run needs to gather content from multiple documents or entities, organize that content into semantic artifacts, bind selected material to views, and declare semantic relationships among the resulting artifacts.

## Concepts

| Concept | Kind | Content | Children | Description |
|---|---|---|---|---|
| Document | Semantic (Entity) | ForbidsContent | `text:Title` (1), `desc:Description` (0..1), `Import` (1..n), `Artifact` (1..n), `Relationship` (0..n), `Condition` (0..n) | Root composition document for one run. Trait: `realization`. |
| Import | Semantic (Entity) | ForbidsContent | -- | Declares an imported source surface. Traits: `target`, `importKind`. |
| Artifact | Semantic (Entity) | ForbidsContent | `text:Title` (0..1), `desc:Description` (0..1), `Selection` (0..n), `Collection` (0..n), `Binding` (0..n) | Declares one composed semantic artifact. Traits: `category`, `realization`, `priority`, `audience`. |
| Selection | Semantic (Entity) | ForbidsContent | `Filter` (0..1) | Declares a selection over imported material. Without a Filter, selects all entities from the source. With a Filter, selects only entities for which the Behavior predicate expression evaluates to true. Traits: `source`. |
| Filter | Structural (non-entity) | ForbidsContent | Behavior expression nodes | Contains a Behavior predicate expression that evaluates against each candidate entity from the Selection's source. The expression evaluates with each candidate as the context entity. |
| Collection | Semantic (Entity) | ForbidsContent | `text:Title` (0..1) | Declares a curated named set of members. Traits: `members`, `organization`, `orderingKey`. |
| Binding | Semantic (Entity) | ForbidsContent | -- | Binds source material or a collection to a view. Traits: `source`, `view`, `bindingIntent`, `realization`. |
| Relationship | Semantic (Entity) | ForbidsContent | -- | Declares a semantic relationship edge between composed artifacts or collections. Traits: `source`, `target`, `relationshipKind`, `weight`, `condition`. |
| Condition | Semantic (Entity) | ForbidsContent | Behavior expression nodes | Declares a reusable condition for graph activation or exclusion. The Behavior predicate expression is authored as child elements. Trait: `effect`. |

## Imports

| Namespace | Schema |
|---|---|
| desc | `paperhat:domain:description` |
| text | `paperhat:domain:text` |

## Trait Vocabularies

| Trait | Meaning |
|---|---|
| realization | Realization classes the document, artifact, or binding is intended to support. |
| importKind | Kind of imported source: `Document`, `Entity`, `Collection`, `Schema`, `Repository`. |
| category | Semantic category of an artifact. |
| organization | Organization mode for a collection: `Ordered` (member list order), `Unordered` (no defined order), `Chronological` (sorted by `orderingKey` trait chronologically), `Alphabetical` (sorted by `orderingKey` trait alphabetically), `Hierarchical` (nesting defines levels; `orderingKey` defines intra-level order). |
| orderingKey | IRI of the trait used for sorting. Required when `organization` is `Chronological`, `Alphabetical`, or `Hierarchical`. Not used for `Ordered` or `Unordered`. |
| bindingIntent | Purpose of a view binding such as `Primary`, `Summary`, or `Detail`. |
| relationshipKind | Semantic graph relationship such as `References`, `Groups`, or `Governs`. |
| effect | Condition effect such as `Include`, `Exclude`, or `Activate`. |

## Design Notes

- Composition is semantic and graph-native.
- Composition MUST NOT encode headers, footers, dropdowns, sidebars, widget slots, or page sections.
- Foundries interpret composition semantics and adaptive-plan outputs into concrete realization choices.
- `Relationship` is reified as an entity so graph edges can be weighted and conditioned directly.
- `Selection` uses Behavior predicate expressions for filtering. Without a `Filter` child, all entities from the source are selected. With a `Filter`, only matching entities are selected. The Behavior expression evaluates with each candidate entity as the evaluation context.
- `Collection` membership is explicit through `members`, not inferred from layout order. `Collection` is for curated named sets; `Selection` is for dynamic filtered subsets.
- `Condition` expressions are Behavior predicate trees authored as child elements, not text strings.
- `Binding` attaches selected semantic material to a `ViewDefinition` surface without turning the view into the pipeline root.

---

**End of Composition v1.0.0**
