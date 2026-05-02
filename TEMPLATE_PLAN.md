# Codex Template System Update Plan

## Problem Statement

The Codex specification requires every concrete document to declare exactly one
root Concept and every Entity to declare exactly one `id` trait whose value is
an IRI Value, and forbids Codex-conforming tools from synthesizing identity.
The 174 `template.cdx` files currently under
`schemas/paperhat-schemas/spec/1.0.0/schemas` cannot satisfy those rules as
concrete documents — they carry placeholder identifiers, omit required
identity, declare top-level annotations before the root, or otherwise depend on
data supplied when a template is used. Codex has no native notion of a
template, so these files are neither validatable as templates nor acceptable as
concrete documents. This plan determines, through evidence and review, what the
Codex template system must become and what changes are required across the
specification, the processors, and the schema package to support it without
weakening concrete-document identity.

## Current Evidence Seed

Current preparatory reads and commands for this plan revision show:

- Current discovery under `schemas/paperhat-schemas/spec/1.0.0/schemas`
  finds 174 `templates/*/template.cdx` files.
- The current Codex specification requires every concrete document to have
  exactly one root concept.
- The current Codex specification requires each entity to have exactly one
  `id` trait whose value is an IRI.
- The current Codex specification forbids Codex-conforming tools from
  synthesizing an `id` trait.

Every later phase must regenerate its own current evidence before using any
file count, file list, diagnostic, processor behavior, or specification claim.

## Working Boundaries

Current edit scope:

- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

Current read scope for preparatory planning:

- `AGENTS.md`
- `LLM_SESSION_PROTOCOL.md`
- `SPEC_AUTHORING_PROTOCOL.md`
- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`
- `specifications/languages/codex-spec/spec/1.0.0/index.cdx`
- `schemas/paperhat-schemas/spec/1.0.0/schemas/**/templates/**/template.cdx`
  discovery by current command

Current out-of-scope edit paths:

- every file other than `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

## Cross-Phase Invariants

- File and template inventories must be generated from current repository state
  in the phase that uses them.
- Processor work must follow the governing Codex specification, not the other
  way around.
- Schema package template updates must wait until the Codex template semantics
  are specified.

## Phase Artifacts

Each executed phase produces a phase report. Reports are normative: they are
the evidence that a phase met its Definition Of Done.

### Report Path Convention

A phase report must live at exactly one of the following locations, declared
in the phase's Definition Of Done before evidence collection begins:

1. `schemas/paperhat-schemas/phases/phase-<number>/report.md` — a per-phase
   directory that may also hold generated artifacts. Required for any phase
   whose evidence includes a generated file list, an evidence table that
   would inflate the plan file, processor entry-point citations, or a
   command transcript.
2. `schemas/paperhat-schemas/TEMPLATE_PLAN.md`, as an appendix titled
   `## Phase <number> Report. <name>` placed immediately after the phase's
   specification section. Permitted only when the report contains no
   generated artifacts.

### Report Header

Every phase report must begin with three lines before any section:

- phase number and name
- ISO 8601 date the report was finalized
- the `schemas/paperhat-schemas` commit hash at the start of evidence
  collection

### Report Body

The report body must use the Required Report Form defined in
`schemas/paperhat-schemas/TEMPLATE_PLAN_PLAN.md` (15 sections). Sections that
do not apply must say `NONE` with a current-evidence reason; sections must
not be omitted or reordered.

### Generated Artifacts

When a phase uses path 1, all generated artifacts referenced by the report
must live in the same `phases/phase-<number>/` directory. Recommended
filenames:

- `corpus-list.txt` — generated file inventory
- `evidence-table.md` — observation-to-specification mapping
- `commands.log` — verbatim command output transcripts
- `processor-evidence.md` — processor entry-point citations

When a phase uses path 2, no generated artifacts are permitted; if any are
needed, the phase must switch to path 1 before evidence collection begins.

### Stable Paths

Once committed, a report path and any path-1 artifact path must not be
renamed. Revisions must happen by editing the existing files and appending a
`## Revision History` section that cites the prior commit hash.

## Verification Block

Each phase's `### Verification Commands` section must use the Verification
Block form below. Prose lists are not permitted.

### Block Form

For every command the phase requires, the phase must include the following
fields in this order:

- `command:` — the exact shell command with all flags and paths; no
  variables, no ellipses, no "current equivalents of" hedging. If the
  command depends on a previously-generated artifact, that artifact's path
  is named here.
- `purpose:` — one sentence stating what the command verifies.
- `step:` — the phase step number or Definition Of Done bullet this command
  serves. A command with no upstream step or DoD bullet is forbidden;
  either add the step or remove the command.
- `expected output shape:` — what a successful run looks like in concrete
  terms (line count bound, prefix, presence of token, absence of token,
  exit status, stat counts). Not a summary; a recognizable shape that the
  acceptance criterion can be evaluated against.
- `acceptance criterion:` — the predicate that, if true of the actual
  output, passes the check. The criterion must be evaluable by reading the
  command output alone, without further interpretation.

### Block Discipline

- The phase's Verification Block must list every command needed to
  discharge the Definition Of Done; commands not listed in the block are
  not part of the phase's verification surface.
- A command whose acceptance criterion cannot be written without
  hand-waving signals a mis-scoped command; either narrow the command or
  narrow the step.
- Working directory is the workspace root
  (`/Users/guy/Workspace/@paperhat`) unless the block declares otherwise.
- A command pending a separate fix may be left in the block with a
  `TODO(recommendation #N)` marker on the affected field, so the
  misalignment is visible until that recommendation is applied.

## Phase Sequence

The plan is built and executed in small reviewed batches. Only Phase 0 is
specified for execution in this revision.

1. Phase 0. Evidence Baseline And Scope Lock
2. Phase 1. Template Corpus Audit
3. Phase 2. Codex Specification Surface Audit
4. Phase 3. Template Semantic Model
5. Phase 4. Codex Specification Edit Plan
6. Phase 5. Bootstrap Schema Edit Plan
7. Phase 6. Processor Implementation Plan
8. Phase 7. Schema Package Template Update Plan
9. Phase 8. Conformance And Completion Proof Plan

Each later phase is expanded only after the previous phase passes hostile
audit.

## Phase 0. Evidence Baseline And Scope Lock

Status: draft for hostile audit.

### Purpose

Create the current-source evidence baseline needed before designing or editing
the Codex template system. This phase does not design template syntax, edit
`.cdx` files, edit processor code, or update schema package templates.

### In-Scope Path Fence

Read-only:

- `AGENTS.md`
- `LLM_SESSION_PROTOCOL.md`
- `SPEC_AUTHORING_PROTOCOL.md`
- `diagnostics.md`
- `specifications/languages/codex-spec/spec/1.0.0/**`
- `schemas/paperhat-schemas/**`
- `implementations/languages/codex/**`

Editable:

- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

### Out-Of-Scope Path Fence

Edits are out of scope for every path except
`schemas/paperhat-schemas/TEMPLATE_PLAN.md`.

### Batch Invariants

- No `.cdx` file is edited.
- No template corpus file is edited.
- No Codex processor file is edited.
- No schema manifest hash or schema import reference is hand-edited.
- No file list is accepted unless generated by a current command.
- No processor behavior is treated as normative authority.
- No Codex semantic requirement is asserted without a current Codex
  specification citation.

### Steps

1. Read current governing instructions: `AGENTS.md`,
   `LLM_SESSION_PROTOCOL.md`, and `SPEC_AUTHORING_PROTOCOL.md`.
2. Read current diagnostic authoring rules before any diagnostic model or
   diagnostic behavior is planned.
3. Read current Codex specification sections governing document roots, entity
   identity, trait values, canonicalization, validation, schema loading, and
   bootstrapping.
4. Generate a current template corpus file list from
   `schemas/paperhat-schemas/spec/1.0.0/schemas`.
5. Audit the current template corpus for:
   - top-level annotations before template content
   - multiple top-level concepts
   - missing entity identity
   - hard-coded identity that must vary per use
   - references to identity that must be bound consistently at instantiation
   - prose instructions that must become structured template data
6. Read current Codex processor entry points for parsing, value parsing,
   identity validation, schema validation, canonicalization, command dispatch,
   and import resolution.
7. Produce an evidence table mapping each observed template problem to the
   Codex specification surface that must be updated.
8. Hostile-audit the evidence table for stale source use, missing files,
   unsupported claims, and hidden design decisions.

### Definition Of Done

Phase 0 is accepted only when:

- Every required source is listed with `READ` status in the report.
- The template corpus file list is generated in the current phase.
- Every audited template finding cites current file and line evidence.
- Every Codex semantic claim cites the current Codex specification.
- Every processor claim is labeled evidence-only unless backed by the Codex
  specification.
- The evidence table has no rows derived from remembered inventory or prior
  command output.
- The hostile audit reports no stale evidence, unsupported claim, missing
  source, ungrounded identifier, or hidden design choice.
- The human approves Phase 1 expansion.

### Verification Commands

The Verification Block below uses the form defined in `## Verification Block`.

- command: `git -C schemas/paperhat-schemas status --short`
  purpose: Identify any dirty paths in the schemas repository before and after edits.
  step: Phase 0 Batch Invariants (no unrelated paths edited; only `TEMPLATE_PLAN.md` is editable).
  expected output shape: Two-character status codes followed by repository-relative file paths, one per line; output may be empty.
  acceptance criterion: Every output line names a path inside the editable scope declared by Phase 0; any path outside that scope must have been explicitly accepted by the planner before the next phase step proceeds.

- command: `rg --files schemas/paperhat-schemas/spec/1.0.0/schemas`
  purpose: Generate the current template corpus file list.
  step: Step 4 (Generate a current template corpus file list).
  expected output shape: One workspace-relative file path per line.
  acceptance criterion: TODO(recommendation #10) — the listed command lists every schema file, not just templates, so it does not satisfy Step 4. The replacement command must restrict output to `*/templates/*/template.cdx`; the criterion will then be that every output line ends with `/template.cdx` and the line count equals the count returned by an independent `find` against the same scope.

- command: TODO(recommendation #11)
  purpose: Audit the generated template corpus for the categories named in Step 5.
  step: Step 5 (audit current template corpus).
  expected output shape: TODO(recommendation #11) — depends on the rewritten neutral-observable categories.
  acceptance criterion: TODO(recommendation #11).

- command: `python3 -B /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/tools/refresh_repository_closure.py`
  purpose: Verify schema closure has no drift after schema or manifest edits.
  step: TODO(recommendation #9) — Phase 0 Batch Invariants forbid the `.cdx`, manifest, and schema-import edits this command exists to verify; the command does not align with any Phase 0 step or Definition Of Done bullet.
  expected output shape: Plain text ending with `No SchemaImport reference drift detected.` and `No manifest normalization drift detected.` when no drift exists.
  acceptance criterion: TODO(recommendation #9) — the command must be removed from Phase 0; closure-neutral edits do not require closure verification.

### Progress Checklist

- [x] Current template corpus discovery counted 174 `template.cdx` files.
- [x] Current Codex root and identity constraints were read for seed evidence.
- [ ] `diagnostics.md` has been read for Phase 0 diagnostic planning.
- [ ] Current template corpus file list has been generated and preserved in the
      Phase 0 report.
- [ ] Current template corpus audit has been completed.
- [ ] Current Codex processor evidence has been read.
- [ ] Evidence table has been produced.
- [ ] Hostile audit has passed.
- [ ] Human approval has been given before Phase 1 expansion.

### Hostile Audit Checklist

The Phase 0 hostile audit must fail the phase if any answer is yes:

- Did the phase use remembered file lists or prior command output?
- Did the phase omit any generated template corpus file?
- Did the phase treat processor code as normative design authority?
- Did the phase assert Codex behavior without current specification citation?
- Did the phase propose `.cdx` edits without Codex CLI evidence?
- Did the phase design syntax before completing the corpus and specification
  audits?
- Did the phase leave any template problem category without file and line
  evidence?
- Did the phase advance to Phase 1 without explicit human approval?

## Phase 3. Template Semantic Model

Status: not yet expanded. The phase will be specified after Phases 1 and 2
pass hostile audit.

### Candidate Deliverables

Phase 3 is expected to produce, as findings earned by the corpus audit
(Phase 1) and the Codex specification surface audit (Phase 2):

- A Codex-native template root model.
- A way to describe typed required data for template use.
- A way to represent required entity identity inside template bodies without
  weakening concrete entity identity.
- Template validation that checks both template structure and the contained
  Codex shape.
- Instantiation rules that bind required template data before concrete
  validation.
- Canonicalization rules for template documents.
- Concrete validation rules that continue to reject missing, malformed, or
  synthesized entity identity.
- A specification of the processor support that Phase 6 must implement
  (parsing, validating, canonicalizing, and instantiating template documents).
- A specification of the schema package template updates that Phase 7 must
  apply.
- A specification of the conformance evidence that Phase 8 must produce,
  proving that template-valid and concrete-valid are distinct validation
  states.

### Candidate Constraints

Phase 3's design must respect, unless evidence justifies revision:

- Templates are Codex documents.
- Template validity and concrete document validity are distinct validation
  states.
- Template validation requires a typed obligation wherever concrete validation
  would require data that is supplied at template use time.
- Template identity obligations are fulfilled before concrete validation.
- Template instructions are structured Codex data, not processor-specific
  prose.

These items are starting candidates only. Phase 3 may add, remove, or reshape
them based on what Phases 1 and 2 find. Nothing in this list is a frozen design
constraint that overrides phase findings.
