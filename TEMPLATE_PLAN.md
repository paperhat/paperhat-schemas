# Codex Template System Update Plan

## Problem Statement

The Codex specification requires every concrete document to declare exactly one
root Concept (`specifications/languages/codex-spec/spec/1.0.0/index.cdx:13238`)
and every Entity to declare exactly one `id` trait
(`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12874`) whose value
is an IRI Value
(`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12894`), and forbids
Codex-conforming tools from synthesizing identity
(`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12904`). The
`template.cdx` files currently under
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

Citations below are evidence as of plan authorship. They are reproduced for
context only. Every later phase MUST regenerate its own current evidence
before using any file count, file list, diagnostic, processor behavior, or
specification claim:

- `find /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas -type f -name template.cdx | wc -l`
  returned 174 on 2026-05-02.
- The Codex specification requires every concrete document to declare
  exactly one root Concept
  (`specifications/languages/codex-spec/spec/1.0.0/index.cdx:13238`).
- The Codex specification requires every Entity to declare exactly one
  `id` trait
  (`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12874`).
- The value of an `id` trait must be an IRI Value
  (`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12894`).
- The Codex specification forbids Codex-conforming tools from synthesizing
  an `id` trait
  (`specifications/languages/codex-spec/spec/1.0.0/index.cdx:12904`).

## Working Boundaries

Plan-wide editable scope:

- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`

Every other path is out of scope for plan-wide edits. Each phase declares
its own In-Scope Path Fence and Out-Of-Scope Path Fence in its phase
specification; a phase fence may expand the editable scope for the
duration of that phase's execution and may declare its own read scope.
The plan as a whole has no read scope; reads are governed per phase.

## Cross-Phase Invariants

- File and template inventories must be generated from current repository state
  in the phase that uses them.
- Processor work must follow the governing Codex specification, not the other
  way around.
- Schema package template updates must wait until the Codex template semantics
  are specified.

## Governance

Three workspace-level gates apply to phases that touch implementation code,
`.cdx` files, or schema-package files. This section names each gate once with
its normative source; later phases reference the gate by label (G1, G2, G3)
instead of restating it.

### G1. Implementation evidence is evidence-only

`AGENTS.md:21`: "Treat existing Rust repositories under
`/Users/guy/Workspace/@paperhat/implementations/` as temporary maintenance
surfaces, not normative design sources for specifications, schemas, foundries,
diagnostics, or generated implementations."

`AGENTS.md:64-65` extends the same evidence-only status to generated `*.md`
projections, `CHECK_RESULTS.json`, `specifications/**/plans/`, memory entries,
summaries, and prior answers; design-authority citation, following, reliance,
or use of those sources is forbidden.

A phase that reads files under `implementations/` (or any other source listed
in `AGENTS.md:64-65`) MUST label its findings about those sources
"evidence-only" in the phase report and MUST NOT cite them as normative design
authority for the work the phase produces.

### G2. Codex CLI evidence gate for `.cdx` edits

`AGENTS.md:7`: ".cdx edit plans require the Codex CLI evidence gate in
`/Users/guy/Workspace/@paperhat/SPEC_AUTHORING_PROTOCOL.md`; .cdx edit plans
that bypass that gate are forbidden."

`SPEC_AUTHORING_PROTOCOL.md:92` defines `### Gate 0: Codex CLI Evidence`:
before drafting instructions that edit a `.cdx` file, or before directly
editing a `.cdx` file, run the real Codex CLI on every `.cdx` file the prompt
or edit touches; include the literal Codex CLI output in the edit plan or
completion report; address every reported diagnostic. The Python verifier,
regex output, prior answer, memory entry, or summarized diagnostic list is
NOT a substitute for Codex CLI evidence.

A phase that plans `.cdx` edits MUST run the Codex CLI on every affected
`.cdx` file before the edit plan is drafted, MUST include the literal output
in the phase report's `Codex CLI Evidence` section (per `## Phase Artifacts`
§Report Body item 14), and MUST NOT bypass the gate on the basis of any
adjacent evidence.

### G3. Closure-hash refresh after schema-package edits

`AGENTS.md:35`: "After edits under
`/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/`, run `python3 -B
/Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/tools/refresh_repository_closure.py`
instead of hand-editing `closureHash` or `SchemaImport reference` digests."

A phase that edits any file under `schemas/paperhat-schemas/` MUST run the
closure refresh tool after every edit, MUST include the tool's output in the
phase report (a no-drift output for closure-neutral edits, or the actual drift
output otherwise), and MUST NOT hand-edit `closureHash` values or
`SchemaImport reference` digests.

### Phase invocation map

| Phase | Gates that apply |
|---|---|
| Phase 0. Evidence Baseline And Scope Lock | none — Batch Invariants forbid `.cdx`, schema-package, and processor edits |
| Phase 1. Template Corpus Audit | none expected (audit-only); G3 if any closure-affecting edit appears |
| Phase 2. Codex Specification Surface Audit | none expected (read-only audit) |
| Phase 3. Template Semantic Model | none expected (design only); downstream phases inherit |
| Phase 4. Codex Specification Edit Plan | G2 (the phase plans `.cdx` edits to the Codex specification) |
| Phase 5. Bootstrap Schema Edit Plan | G2 (if `.cdx` edits), G3 (if any schema-package file is touched) |
| Phase 6. Processor Implementation Plan | G1 (processor implementation work is evidence-only for the specifications it implements) |
| Phase 7. Schema Package Template Update Plan | G2 (the phase edits `.cdx` template files), G3 (the phase edits schema-package files) |
| Phase 8. Conformance And Completion Proof Plan | none expected (verification only); cite evidence sources but do not invoke gates |

Each phase's Definition Of Done MUST list the applicable gates and prove
satisfaction in the phase report.

## Current-Turn Evidence Rule

Any file count, file path, specification line, or command output cited
anywhere in `TEMPLATE_PLAN.md` MUST be regenerated in the current revision
and cited as `(file:line)` for files or `(command, run YYYY-MM-DD)` for
command output. Stale numbers in checklists are forbidden.

The rule binds the Problem Statement, the Current Evidence Seed, every
phase opener, every phase report (including the report header, every
Grounded Finding, every Verification Block output, every evidence table,
and every Progress Checklist item), and every artifact under
`schemas/paperhat-schemas/phases/`. It applies to revisions of
`TEMPLATE_PLAN.md` itself: any edit that introduces a new factual claim
about repository state or specification content MUST carry its citation
in the same revision.

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

The report body must use the union of the following sections, in this order.
Sections that do not apply must say `NONE` with a current-evidence reason;
sections must not be omitted or reordered.

From `LLM_SESSION_PROTOCOL.md` §Required Output Structure:

1. Source Inventory
2. Authority Map
3. Blocking Conditions
4. Grounded Findings
5. Inferences
6. Open Items

For substantial edit batches, also from `LLM_SESSION_PROTOCOL.md`
§Required Output Structure:

7. Batch Invariants — before edits
8. Consequence Sweep — after edits

From `LLM_SESSION_PROTOCOL.md` §Completion Report Contract:

9. Proof Bundle
10. Bespoke Logic Remaining
11. Underspecified Areas
12. Unresolved Contradictions
13. Sources Accounted For

For phases that touch `.cdx` files, also from `SPEC_AUTHORING_PROTOCOL.md`
§Completion Report Contract:

14. Codex CLI Evidence
15. Missing Conformance Coverage

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
- The `command:` and `step:` fields must always be concrete: a real shell
  command and a real Phase step or DoD bullet, respectively. A block whose
  command or step is unknown must not be listed in the Verification Block;
  track it under the phase's `### Open Verification Items` section until
  both fields can be filled.
- A `TODO(<reason>)` marker may attach to the `purpose:`,
  `expected output shape:`, or `acceptance criterion:` field when those
  fields depend on a separate forthcoming fix; the marker keeps the
  outstanding work visible until the fix lands.

## Hostile Audit Template

Every phase's `### Hostile Audit Checklist` consists of:

1. The Universal Hostile Audit Questions defined below, in their full
   present-tense form.
2. Phase-specific additions appended after the universal questions.

A phase that determines a Universal Hostile Audit Question is vacuously
satisfied by its own Batch Invariants must mark that question
`N/A — <invariant citation>` rather than omit it. The full universal list
must remain visible so reviewers can see what was excluded and why.

### Universal Hostile Audit Questions

The phase fails its hostile audit if the answer to any of these questions
is yes:

- Does the phase use remembered file lists, prior command output,
  summaries, memory entries, or any other evidence not regenerated in the
  current turn?
- Does the phase assert Codex behavior, schema constraint, processor
  behavior, specification requirement, verifier behavior, command
  behavior, acceptance criterion, or completion status without a current
  `file:line` citation against the governing source? (Per
  `LLM_SESSION_PROTOCOL.md` §Citation Rules.)
- Does the phase treat processor code, generated `*.md` projections,
  `CHECK_RESULTS.json`, prior plans, or memory entries as normative
  design authority?
- Does the phase propose `.cdx` edits without running the Codex CLI
  evidence gate on every affected `.cdx` file?
- Does the phase make a design decision that pre-empts a later phase or
  substitutes for evidence the phase has not yet gathered?
- Does the phase contain a Verification Block command whose acceptance
  criterion cannot be evaluated by reading the command's output alone?
- Does the phase contain a finding that lacks a current `file:line` or
  current command citation?
- Does the phase read or edit a path outside its declared In-Scope Path
  Fence, or edit a path inside its declared Out-Of-Scope Path Fence?
- Does the phase advance to the next phase without explicit human
  approval?

### Phase-Specific Additions

Each phase appends additional questions targeting the work specific to
that phase. Phase-specific additions follow the same present-tense form
and the same yes-fails convention.

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

This phase is bound by `## Current-Turn Evidence Rule`.

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
   - concept instances declaring an `id` trait whose value is a literal IRI rather than a parameter
   - concept instances missing an `id` trait whose Concept is governed by `MustBeEntity`
   - annotations preceding the root Concept
   - documents with multiple top-level Concepts
   - prose-only `instructions` traits
6. Read current Codex processor entry points for parsing, value parsing,
   identity validation, schema validation, canonicalization, command dispatch,
   and import resolution.
7. Produce an evidence table mapping each observed template problem to the
   Codex specification surface that must be updated.
8. Hostile-audit the evidence table for stale source use, missing files,
   unsupported claims, and hidden design decisions.

### Definition Of Done

Phase 0 is accepted only when:

- The phase report path is `schemas/paperhat-schemas/phases/phase-0/report.md`
  (path 1 per `## Phase Artifacts`); all generated artifacts live in
  `schemas/paperhat-schemas/phases/phase-0/`.
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

- command: `find schemas/paperhat-schemas/spec/1.0.0/schemas -type f -path '*/templates/*/template.cdx'`
  purpose: Generate the current template corpus file list.
  step: Step 4 (Generate a current template corpus file list).
  expected output shape: One workspace-relative file path per line, each path ending in `/templates/<variant>/template.cdx`.
  acceptance criterion: (a) Every output line matches the literal pattern `*/templates/*/template.cdx` (one variant directory between `templates/` and `template.cdx`, exactly one path per template directory); and (b) the line count equals the count returned by the cross-check command `find schemas/paperhat-schemas/spec/1.0.0/schemas -type f -name template.cdx | wc -l`. If the two counts disagree, some `template.cdx` exists outside the expected `*/templates/*/template.cdx` shape and Phase 0 must report the deviation in its Grounded Findings before continuing.

### Open Verification Items

These items belong in Phase 0's Verification Block once their preconditions
are met. They are listed here, not in the block, because the
`## Verification Block` discipline requires concrete `command:` and `step:`
fields:

- Step 5 audit commands. The Step 5 categories are now neutral
  observables (rewritten by recommendation #11). Concrete enumeration
  still requires Codex-aware tooling that can parse `template.cdx`
  files for concept structure, `id` trait values, schema bindings to
  `MustBeEntity`, top-level Concept counts, annotation position
  relative to the root Concept, and `instructions` trait kinds. Those
  observations cannot be expressed as one-line shell commands; they
  invoke the Codex CLI per the Codex CLI evidence gate (Governance
  §G2, which Phase 0 invokes for `.cdx` reads even though Phase 0
  Batch Invariants forbid `.cdx` edits). The Phase 0 executor will
  invoke the Codex CLI per category and record findings directly in
  the Phase 0 report's Grounded Findings section; per-category
  Verification Block entries are written into the report rather than
  into this template plan.
- Closure verification. The closure refresh command
  (`python3 -B …/tools/refresh_repository_closure.py`) was previously
  listed but has no aligned Phase 0 step: Phase 0's Batch Invariants
  forbid the `.cdx`, manifest, and schema-import edits this command
  exists to verify. The command belongs in phases that perform those
  edits (recommendation #9 will scope it accordingly). Phase 0 does not
  invoke the closure refresh.

### Current Evidence Snapshot

The rows below were verified on 2026-05-02 (plan authorship). On the day
Phase 0 is reviewed or executed, every row MUST be re-run and the result
recorded in the Phase 0 report's Grounded Findings; the authorship-time
value is a baseline, not a fact carried forward. Staleness is visible
because each row carries an explicit citation command or path.

| Claim | Source-citation |
|---|---|
| Template corpus under `schemas/paperhat-schemas/spec/1.0.0/schemas` contains N `template.cdx` files (authorship-time baseline: N = 174). | `find /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/spec/1.0.0/schemas -type f -name template.cdx \| wc -l` |
| Codex specification's root-Concept, id-trait, id-IRI, and no-synthesis rules bind every concrete document. | `specifications/languages/codex-spec/spec/1.0.0/index.cdx:13238`, `:12874`, `:12894`, `:12904` (re-run via `sed -n` to confirm each line still matches the seed wording). |

If a row's citation re-run produces a different current value or wording,
Phase 0 MUST cite the new value in its report and update the seed and
this Snapshot table in the same revision (per `## Current-Turn Evidence
Rule`).

### Progress Checklist

- [ ] `diagnostics.md` has been read for Phase 0 diagnostic planning.
- [ ] Current template corpus file list has been generated and preserved in the
      Phase 0 report.
- [ ] Current template corpus audit has been completed.
- [ ] Current Codex processor evidence has been read.
- [ ] Evidence table has been produced.
- [ ] Hostile audit has passed.
- [ ] Human approval has been given before Phase 1 expansion.

### Hostile Audit Checklist

This checklist applies the Universal Hostile Audit Questions defined in
`## Hostile Audit Template` plus the Phase 0 additions below. The phase
fails its hostile audit if any answer is yes.

The Universal Hostile Audit Questions all apply to Phase 0 except:

- "Does the phase propose `.cdx` edits without running the Codex CLI
  evidence gate on every affected `.cdx` file?" — N/A: Phase 0 Batch
  Invariants forbid `.cdx` edits, template corpus edits, and Codex
  processor edits.

Phase 0 additions:

- Does the phase omit any `template.cdx` file present in the current
  repository from the generated template corpus list?
- Does the phase leave any template problem category named in Step 5
  without current `file:line` evidence?

## Phase 3. Template Semantic Model

Status: not yet expanded. The phase will be specified after Phases 1 and 2
pass hostile audit.

This phase is bound by `## Current-Turn Evidence Rule`.

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
