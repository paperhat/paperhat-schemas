# Codex Template Plan

## Working Purpose

This file is the active working plan for designing first-class Codex templates.
The plan advances by small reviewed phases. Each phase is added only after the
current phase text has been read back, checked against the governing session
rules, and subjected to hostile audit.

The design target is a Codex-native template model: templates remain parseable,
canonicalizable, and validatable through Codex, and instantiated documents pass
ordinary concrete Codex validation after required template data is supplied.

## Authority Boundary

This plan controls work sequencing and review discipline. Codex language
semantics belong in the governing Codex specification. Schema-package semantics
belong in their governing `.cdx` schemas. Processor behavior belongs in the
implementation only after the governing specification work identifies the exact
required behavior.

Implementation files, generated projections, verifier output, previous answers,
and remembered file lists are evidence only. Every phase derives its evidence
from current files and current commands run in that phase.

## Current Path Fence

Current edit scope:

- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

Current out-of-scope edit paths:

- every file other than `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

Future phase scopes must be named explicitly inside the phase before any read,
audit, edit, or verification work begins for that phase.

## Plan-Building Rules

1. Each phase is added in its own small batch.
2. Each batch begins with current-turn reads of `AGENTS.md`,
   `LLM_SESSION_PROTOCOL.md`, and `SPEC_AUTHORING_PROTOCOL.md`.
3. Each batch states its in-scope path fence and out-of-scope path fence before
   edits.
4. Each batch states batch invariants before edits.
5. Each batch uses current repository evidence only.
6. File inventories are generated from current commands in the batch that uses
   them.
7. Remembered file lists, previous reports, and prior command output are never
   accepted as inventory evidence.
8. Any phase that plans `.cdx` edits follows the Codex CLI evidence gate before
   the edit plan is drafted.
9. Any phase that authors or audits diagnostics reads `diagnostics.md` in that
   phase before diagnostic claims are made.
10. Any edit under `schemas/paperhat-schemas` is followed by
    `python3 -B /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/tools/refresh_repository_closure.py`.
11. Each phase has a Definition of Done before work begins.
12. Each phase has a progress checklist that is updated by evidence, not by
    intention.
13. Each phase ends with hostile audit before the next phase is added.
14. A second hostile audit is run when the first audit finds any omission,
    stale source, unsupported claim, scope error, or wording that weakens the
    approved direction.
15. Advancement stops immediately when an audit, evidence gate, command, or
    readback fails.

## Required Report Form

Every phase report uses this structure:

1. Source Inventory
2. Authority Map
3. Blocking Conditions
4. Grounded Findings
5. Inferences
6. Open Items
7. Batch Invariants
8. Consequence Sweep
9. Proof Bundle
10. Codex CLI Evidence
11. Bespoke Logic Remaining
12. Underspecified Areas
13. Missing Conformance Coverage
14. Unresolved Contradictions
15. Sources Accounted For

If a section does not apply to the current phase, the report says `NONE` for
that section and cites the reason from current evidence.

## Definition Of Done For Plan Additions

A plan addition is accepted only when all of these checks are satisfied:

- The current phase text has been read back from disk after editing.
- The exact diff for `TEMPLATE_PLAN.md` has been inspected.
- The `schemas/paperhat-schemas` repository status has been checked before and
  after the edit.
- The repository closure refresh command has passed after the edit.
- The report cites current-turn file and command evidence.
- Hostile audit reports no remaining failure.
- The human explicitly approves moving to the next phase.

## Phase Template

Each future phase uses this structure:

```text
## Phase <number>. <name>

Status:

Purpose:

In-Scope Path Fence:

Out-Of-Scope Path Fence:

Required Current Reads:

Batch Invariants:

Steps:

Definition Of Done:

Verification Commands:

Progress Checklist:

Hostile Audit Checklist:
```

## Progress

- [x] Preparatory material has been read back from disk.
- [x] Preparatory material diff has been inspected.
- [x] Repository closure refresh has passed after this edit.
- [ ] Hostile audit has reported no remaining failure for the preparatory
      material.
- [ ] Human approval has been given before Phase 1 is added.
