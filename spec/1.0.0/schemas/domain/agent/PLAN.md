# Agent Schema Package Plan

Status: PLANNING
Scope: `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/`

This document is a durable planning artifact for the future `agent` schema package. It is not an edit-ready `.cdx` executor prompt. A later `.cdx` edit plan MUST run the Codex CLI evidence gate required by `/Users/guy/Workspace/@paperhat/SPEC_AUTHORING_PROTOCOL.md` before drafting or editing any `.cdx` file.

## Evidence Basis

- `AGENTS.md:5-7` requires current-task reads of the Paperhat session and specification authoring protocols before Paperhat planning and `.cdx` work.
- `AGENTS.md:27-35` requires `.cdx` as the source of truth, `MUST` / `MUST NOT` modalities, closed selection dimensions, and closure refresh after schema edits.
- `SPEC_AUTHORING_PROTOCOL.md:35-53` requires explicit structural coverage for public surface, validation, grammar, operation semantics, conformance, dependencies, target choices, generated tests, diagnostics, and documentation.
- `SPEC_AUTHORING_PROTOCOL.md:92-111` requires Codex CLI evidence before `.cdx` edit prompts or `.cdx` edits.
- `CLAUDE.md:3-9` establishes current Claude output as a discovery shim that must read `AGENTS.md`, must not contain independent Paperhat policy, and must defer to `AGENTS.md` on conflict.
- `governance-document/schema.cdx:178-193` shows `GovernanceRequirement` uses `specbase:modality` narrowed to `$Must` / `$MustNot`.
- `specification-foundation/schema.cdx:417-424` defines `specbase:modality`; there is no `govdoc:Modality` enum in the checked-in governance document schema.
- `governance-document/schema.cdx:219-357` already defines governance authority, conflict, boundary, and restatement concepts.
- `governance-document/schema.cdx:359-391` defines governance section/source reference concepts, with resolution constraints at `governance-document/schema.cdx:476-528`.

## Path Fence

In scope for the future `agent` package authoring batch:

- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/manifest.cdx`
- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/schema.cdx`
- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/localizations/en.cdx`
- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/examples/`
- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/templates/`
- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/README.md`

Out of scope for the initial `domain/agent` authoring batch:

- `/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/view/agent-projection/`
- Generated `AGENTS.md` and `CLAUDE.md`
- Root `AGENTS.md` and `CLAUDE.md`
- `CHECK_RESULTS.json`
- `/Users/guy/Workspace/@paperhat/implementations/`
- `/Users/guy/Workspace/@paperhat/tools/`
- `/Users/guy/Workspace/@paperhat/websites/`

## Design Decisions

1. Create `agent` as a domain package at `schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent/`.
2. Use `namespace="agent"` and `packageName="paperhat-agent"`.
3. Import `govdoc` for reusable governance concepts.
4. Import `specbase` directly for `specbase:modality`; do not refer to `govdoc:Modality`.
5. Import `text`, `list`, and `cite` for paragraph, list, and citation content.
6. Do not import `composition` in v1. Define a local `AgentInclude` because v1 assembly needs agent-specific fragment references, precedence, and duplicate behavior.
7. Do not create or edit `view/agent-projection` in this batch. Projection belongs in a later view package after the source schema is inventoried and accepted.
8. Do not define `$Custom` target file output in v1. V1 target files are exactly `$AgentsMd` and `$ClaudeMd`.
9. Do not use audience filtering in v1. An `AgentFile` chooses its output by explicit `targetFileKind` and explicit `AgentAssembly`.
10. Do not import `code` in v1. Verbatim command text is carried in `RequiredClause` / `ForbiddenClause` content unless a later inventory proves block-level code semantics are required.
11. V1 duplicate behavior is rejection, not replacement. `ReplaceByKey` is deferred until diagnostics and weakening/supersession semantics are specified.
12. `CLAUDE.md` generation is represented by a dedicated shim concept, not a normal full router.

## Required Package Artifacts

Create these files:

- `manifest.cdx`
- `schema.cdx`
- `README.md`
- `localizations/en.cdx`
- `examples/workspace-router/example.cdx`
- `examples/claude-shim/example.cdx`
- `examples/repo-fragment/example.cdx`
- `examples/fragment-assembly/example.cdx`
- `templates/basic/template.cdx`
- `templates/fragment/template.cdx`

## Schema Imports

Planned schema imports:

- `govdoc` -> `paperhat:domain:governance-document`
- `specbase` -> `paperhat:domain:specification-foundation`
- `text` -> `paperhat:domain:text`
- `list` -> `paperhat:domain:list`
- `cite` -> `paperhat:domain:citation`

`SchemaImport reference` values MUST be computed or refreshed by the repository closure tooling. They MUST NOT be guessed or hand-edited.

## Public Type Inventory

Candidate local concepts:

- `AgentFile`: root entity for one generated instruction target.
- `AgentDiscoveryShim`: structural concept for the `CLAUDE.md` discovery shim.
- `AgentAssembly`: entity describing deterministic fragment inclusion.
- `AgentInclude`: structural child that references one fragment and declares precedence.
- `AgentFragment`: reusable rule fragment.
- `AgentSection`: ordered section within a fragment.
- `AgentRequirement`: agent-specific requirement with structured required/forbidden clauses.
- `RequiredClause`: flow-content required half of a rule.
- `ForbiddenClause`: flow-content forbidden half of a rule.
- `AgentPathFence`: in-scope or out-of-scope path fence.
- `AgentPath`: value-like workspace path or path pattern.
- `AgentAuthoritySource`: source citation or authority pointer.

Imported child concepts allowed where appropriate:

- `govdoc:GovernanceAuthorityRule`
- `govdoc:GovernanceConflictRule`
- `govdoc:GovernanceBoundary`
- `govdoc:GovernanceRestatementRule`
- `govdoc:GovernanceSectionReference`
- `govdoc:GovernanceSourceClause`
- `text:Paragraph`
- `list:OrderedList`
- `list:UnorderedList`
- `cite:Citation`

## Trait Inventory

Candidate local traits:

- `name`: `$Text`
- `targetFileKind`: `$EnumeratedToken`
- `assembly`: `$Iri`, reference trait to `AgentAssembly`
- `fragment`: `$Iri`, reference trait to `AgentFragment`
- `key`: `$LookupToken`
- `title`: `$Text`
- `precedence`: `$Number`
- `fragmentScope`: `$EnumeratedToken`
- `appliesToPath`: `$Text`
- `requirementForm`: `$EnumeratedToken`
- `sectionKind`: `$EnumeratedToken`
- `mergePolicy`: `$EnumeratedToken`
- `pathFenceKind`: `$EnumeratedToken`
- `pathPattern`: `$EnumeratedToken`
- `authorityRole`: `$EnumeratedToken`
- `target`: `$Iri`
- `lineRange`: `$Text`
- `note`: `$Text`

Imported trait use:

- `specbase:modality`, narrowed at `AgentRequirement` to `$Must` / `$MustNot`.

## Closed Selection Dimensions

Local enumerated value sets:

- `TargetFileKind`: `$AgentsMd`, `$ClaudeMd`
- `FragmentScope`: `$Workspace`, `$Repository`, `$TaskScoped`
- `RequirementForm`: `$RequiredOnly`, `$ForbiddenOnly`, `$RequiresAndForbids`
- `PathFenceKind`: `$InScope`, `$OutOfScope`
- `AuthorityRole`: `$Normative`, `$Derivative`, `$Supplemental`, `$Legacy`
- `AgentSectionKind`: `$SourceFiles`, `$Authority`, `$PathSet`, `$SpecificationRules`, `$SessionGates`, `$GitSafety`, `$InstructionChecks`, `$EvidenceOnlySources`, `$DirectoryLayout`
- `MergePolicy`: `$AppendByPrecedence`, `$RejectOnDuplicate`
- `PathPattern`: `$AbsoluteWorkspacePath`, `$RepositoryRelativePath`, `$GlobPattern`

## Concept Rules

`AgentFile`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `name`.
- MUST require `targetFileKind`.
- MUST allow one `AgentAssembly` when `targetFileKind=$AgentsMd`.
- MUST require one `AgentDiscoveryShim` and forbid `AgentAssembly` when `targetFileKind=$ClaudeMd`.

`AgentDiscoveryShim`:

- MUST be `$Structural`.
- MUST be `$MustNotBeEntity`.
- MUST encode the four current shim behaviors: read `AGENTS.md`; contain no independent policy; do not duplicate shared rules; defer to `AGENTS.md` on conflict.

`AgentAssembly`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `mergePolicy`.
- MUST require at least one `AgentInclude`.
- MUST preserve include order as semantically significant.

`AgentInclude`:

- MUST be `$Structural`.
- MUST be `$MustNotBeEntity`.
- MUST require `fragment`.
- MUST require `precedence`.

`AgentFragment`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `key`.
- MUST require `fragmentScope`.
- MUST require `appliesToPath` unless `fragmentScope=$Workspace`.
- MUST contain at least one `AgentSection`.

`AgentSection`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `key`, `title`, and `sectionKind`.
- MUST use ordered collection semantics.
- MUST allow local agent rule concepts and imported governance/text/list/citation concepts listed above.

`AgentRequirement`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `key`.
- MUST require `specbase:modality` narrowed to `$Must` / `$MustNot`.
- MUST require `requirementForm`.
- MUST use `RequiredClause` and `ForbiddenClause` children instead of renderer-invented prose splitting.

`RequiredClause` and `ForbiddenClause`:

- MUST be `$Structural`.
- MUST be `$MustNotBeEntity`.
- MUST require flow content.

`AgentPathFence`:

- MUST be `$Structural`.
- MUST be `$MustNotBeEntity`.
- MUST require `pathFenceKind`.
- MUST contain at least one `AgentPath`.

`AgentPath`:

- MUST be `$ValueLike`.
- MUST be `$MustNotBeEntity`.
- MUST require content.
- MUST allow `pathPattern`.

`AgentAuthoritySource`:

- MUST be `$Semantic`.
- MUST be `$MustBeEntity`.
- MUST require `authorityRole`.
- MUST require `target`.
- MUST allow `lineRange` and `note`.

## Constraint Inventory

Required constraints:

- `AgentFile` with `targetFileKind=$AgentsMd` requires one `AgentAssembly`.
- `AgentFile` with `targetFileKind=$ClaudeMd` requires one `AgentDiscoveryShim` and forbids `AgentAssembly`.
- `AgentRequirement requirementForm=$RequiredOnly` requires exactly one `RequiredClause` and forbids `ForbiddenClause`.
- `AgentRequirement requirementForm=$ForbiddenOnly` requires exactly one `ForbiddenClause` and forbids `RequiredClause`.
- `AgentRequirement requirementForm=$RequiresAndForbids` requires exactly one `RequiredClause` and exactly one `ForbiddenClause`.
- `AgentRequirement specbase:modality` is restricted to `$Must` / `$MustNot`.
- `AgentFragment fragmentScope=$Workspace` permits absent `appliesToPath`.
- `AgentFragment fragmentScope=$Repository` or `$TaskScoped` requires `appliesToPath`.
- `AgentInclude fragment` must resolve to `AgentFragment`.
- `AgentFile assembly` must resolve to `AgentAssembly`.
- `AgentAuthoritySource target` must resolve when `authorityRole=$Normative`.
- `AgentSection key` must be unique within one `AgentFragment`.
- Assembled `(sectionKey, requirementKey)` duplicates must be rejected in v1.
- Assembly ordering must be deterministic by `precedence`, then fragment key, then source order inside ordered collections.
- `AgentPath` must match the selected `PathPattern`.
- Local path fences must not escape their fragment `appliesToPath`.

## Diagnostic Inventory

Diagnostic names and IRIs are NOT defined in this plan. Before authoring diagnostics, read `/Users/guy/Workspace/@paperhat/diagnostics.md` in the current task and define typed diagnostics for at least:

- duplicate assembled section/rule key
- unresolved fragment reference
- unresolved assembly reference
- unresolved normative authority target
- invalid workspace path
- path fence escapes fragment scope
- Claude target contains non-shim policy
- unsupported target file kind
- unsupported merge policy

## Grammar Inventory

The initial `agent` schema needs formal recognition rules for:

- workspace absolute path
- repository-relative path
- glob pattern
- line range
- generated target file name
- Markdown projection grammar, later in the projection package

The Markdown projection grammar is not part of the initial `domain/agent` package. It is deferred until the source package is accepted and the `ails` rule surface has been read.

## Example Requirements

`examples/workspace-router/example.cdx`:

- MUST model current root `AGENTS.md` as `AgentFile targetFileKind=$AgentsMd`.
- MUST include sections matching the current router headings.
- MUST use `AgentRequirement` for paired required/forbidden rules.

`examples/claude-shim/example.cdx`:

- MUST model current `CLAUDE.md` as `AgentFile targetFileKind=$ClaudeMd`.
- MUST use `AgentDiscoveryShim`.
- MUST NOT duplicate full workspace policy.

`examples/repo-fragment/example.cdx`:

- MUST contain an `AgentFragment` scoped below one repository path.
- MUST demonstrate `appliesToPath`.

`examples/fragment-assembly/example.cdx`:

- MUST include at least two fragments.
- MUST show deterministic ordering by precedence.
- MUST include an invalid duplicate-key companion case or documented rejection scenario.

## Template Requirements

`templates/basic/template.cdx`:

- Minimal `AgentFile targetFileKind=$AgentsMd`.
- One `AgentAssembly`.
- One `AgentInclude`.

`templates/fragment/template.cdx`:

- Minimal `AgentFragment`.
- One `AgentSection`.
- One `AgentRequirement`.

## Authoring Sequence

1. Re-read `AGENTS.md`, `LLM_SESSION_PROTOCOL.md`, and `SPEC_AUTHORING_PROTOCOL.md`.
2. Run the Codex CLI evidence gate required by `SPEC_AUTHORING_PROTOCOL.md` before drafting any `.cdx` edit prompt or editing `.cdx` files.
3. Read every imported schema from disk in the current turn.
4. Produce Gate 1 inventory: public type inventory, operation inventory, diagnostic inventory, grammar inventory, and cross-library dependency inventory.
5. Produce Gate 2 coverage: trace every public surface item to one structural home.
6. Author `schema.cdx` first with imports, concept definitions, trait definitions, enumerated sets, constraints, validators if needed, and explicit TODO markers only where the gate says unresolved work remains.
7. Author `manifest.cdx` with package metadata and dependencies.
8. Author `localizations/en.cdx` for every local concept and trait.
9. Author examples and templates.
10. Author README as supplemental projection documentation.
11. Run `python3 -B /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/tools/refresh_repository_closure.py`.
12. Run real Codex validation on `schema.cdx`, examples, and templates.
13. Inspect `git diff -- /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas/domain/agent`.
14. Read back changed sections from disk.
15. Perform hostile audit against the specification authoring protocol.

## Acceptance Criteria

- Every required package artifact exists.
- No `.cdx` file contains hand-guessed `closureHash` or `SchemaImport reference` digests.
- Every local concept, trait, and enumerated value is localized.
- Every user-selectable alternative is represented as a closed enumerated value set.
- No target output choice is open-ended.
- No assembly behavior is left to foundry discretion.
- No Claude target can carry independent workspace policy.
- Duplicate assembled requirements are rejected in v1.
- The package validates under the real Codex CLI.
- The closure refresh tool has been run after schema edits.

## Deferred Work

Deferred out of the initial `domain/agent` package:

- `view/agent-projection`
- Markdown byte-level projection grammar
- generated `AGENTS.md`
- generated `CLAUDE.md`
- `ails` acceptance fixtures
- replacement/override merge policy
- block-level command/code directive import

## Blocking Open Items

- Exact Codex CLI invocation for validating these package files must be established in the authoring task.
- `diagnostics.md` must be read before diagnostic IRIs/messages are authored.
- Exact workspace path grammar must be approved before `AgentPath` validation is locked.
- `ails` rule surface must be read before projection grammar or generated Markdown acceptance is locked.
- Import digests must be produced by tooling, not guessed.
