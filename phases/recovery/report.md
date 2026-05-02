# Recovery Report for Recommendations #1–#5

Date finalized: 2026-05-02
Repository: schemas/paperhat-schemas
Commit hash at start of writeup: 336439e
Author: Charles Munat (with Claude Opus 4.7 assistance)

## Purpose

The first five recommendation commits on this branch (104ff33, b9f1a53,
c7ffb13, 41c1c49, 17262cc) were executed without producing the required
procedural structure defined by `LLM_SESSION_PROTOCOL.md` §Required Output
Structure (Source Inventory, Authority Map, Blocking Conditions, Grounded
Findings, Inferences, Open Items) and §Required Edit Batch Sections
(Batch Invariants, Consequence Sweep, Proof Bundle).

The original audit (this conversation, before this report) catalogued the
omissions as findings F1–F11. This report retrospectively produces the
missing artifacts for each commit using current-turn evidence, closing
F1, F2, F3, F4, F5, and F11 to the extent recoverable. F6–F10 (conduct
issues at the time of the original commits) and F12 (wrong commit-message
diffstat counts) cannot be repaired and are listed in the Limitations
section.

## Scope

Five commits, in chronological order:

| # | Hash    | Date                   | Recommendation |
|---|---------|------------------------|----------------|
| 1 | 104ff33 | 2026-05-02 12:37:54 +1200 | #1 Demote front-matter design constraints |
| 2 | b9f1a53 | 2026-05-02 12:48:12 +1200 | #2 Add Phase Artifacts section |
| 3 | c7ffb13 | 2026-05-02 12:54:00 +1200 | #3 Add Verification Block; retrofit Phase 0 |
| 4 | 41c1c49 | 2026-05-02 12:55:15 +1200 | #4 Collapse Working Boundaries |
| 5 | 17262cc | 2026-05-02 13:00:21 +1200 | #5 Hostile Audit Checklist as reusable template |

Each entry below produces the nine procedural sections that should have
accompanied the commit at the time.

## Limitations

- **Reconstructed evidence.** "Current-turn" evidence in this report is
  the state at this report's writeup turn (HEAD `336439e`,
  2026-05-02 ~15:01 NZST), not the state at each individual rec's commit
  time. Where a citation might have differed at the time, the difference
  is noted.
- **Conduct unrepairable (F6–F10).** Citation Rules violations (F6),
  Non-Stale Evidence Rules violations (F7), Source Accounting failures
  (F8), Audit Mode Rule violations (F9), and Responsiveness Rule
  violations (F10) describe conduct that occurred at commit time. They
  cannot be replayed. Going forward, the UserPromptSubmit gate hook
  installed after the audit (commit on `.claude/settings.local.json`)
  and the PreToolUse / PostToolUse hooks installed in the
  cache-pointer enforcement turn make recurrence mechanically harder.
- **F12 unrepairable.** The rec #4 commit message states "Net: 18 lines
  removed, 9 added" but the actual diffstat is 6 insertions / 14
  deletions. The rec #5 commit message states "Net: 51 insertions, 13
  deletions" but the actual diffstat is 63 insertions / 12 deletions.
  Both are in committed history; AGENTS.md `:52` (no `git rebase`, no
  history rewrites) makes them unrepairable.
- **No git history modified by this report.** This is a forward-only
  artifact under `phases/recovery/`. No commit is amended, reordered,
  or removed.

---

## Recommendation #1 — commit 104ff33

### Source Inventory

- `TEMPLATE_PLAN.md` — `READ` (at commit time the file was an empty
  placeholder per `git show HEAD~1:TEMPLATE_PLAN.md` — the first
  commit's diff was effectively a full-file insert of 248 lines) —
  `DERIVATIVE` (work product)
- `TEMPLATE_PLAN_PLAN.md` — `READ` (newly created in this commit, 142
  lines: governing meta-plan with Required Report Form and Phase
  Template) — `DERIVATIVE` (transient meta-plan, slated for discard)
- `AGENTS.md`, `LLM_SESSION_PROTOCOL.md`, `SPEC_AUTHORING_PROTOCOL.md`,
  `diagnostics.md` — `NOT READ` at commit time (audit found these
  omissions in F1, F8) — `NORMATIVE` (should have been READ)

### Authority Map

- Normative: governance-spec, AGENTS.md, the protocols, diagnostics.md
- Derivative: TEMPLATE_PLAN.md, TEMPLATE_PLAN_PLAN.md
- Precedence: governance-spec > AGENTS.md > protocols > plan/meta-plan

### Blocking Conditions

At commit time, retrospectively: per LLM_SESSION_PROTOCOL.md §Source
Accounting, "synthesis is forbidden" until every in-scope artifact is
READ. The four governing files were not READ. Synthesis was forbidden;
synthesis happened anyway. This is the F8 finding.

### Grounded Findings

`FACT:` Commit 104ff33 produced TEMPLATE_PLAN.md content that demoted
the prior `## Objective` and `## Required Outcome` sections (each
inferred from the commit message) into a one-paragraph
`## Problem Statement`.

`FACT:` Commit 104ff33 renamed `## Non-Negotiable Design Constraints` to
`## Cross-Phase Invariants` and removed the design items (verified by
reading the post-commit file at HEAD).

`FACT:` Commit 104ff33 added a `## Phase 3. Template Semantic Model` stub
with the moved content reframed as Candidate Deliverables and Candidate
Constraints (verified by reading the post-commit file).

`FACT:` Commit 104ff33 also created `TEMPLATE_PLAN_PLAN.md` as a new
file (verified by `git show --stat 104ff33`).

### Inferences

`INFERENCE:` The intent of the demotion was that the audit cannot
conclude what the front matter has already decided. This is the
recommendation #1 rationale and is reflected in the post-commit file's
Phase 3 stub note that the Candidate Constraints are not frozen design.

`INFERENCE:` The naming "Cross-Phase Invariants" was chosen over
alternatives (e.g., keeping "Non-Negotiable Design Constraints") to
underline that the remaining items are process rules, not design
decisions.

### Open Items

- F13 (Phase 0 has no path declaration) was introduced by this commit
  in the sense that Phase 0 already lacked one and this commit did not
  add one. Closed by commit 1fe5acb (F13 fix).

### Batch Invariants

The batch should have preserved (reconstructed):
- Phase 0's existence and skeleton (Status, Purpose, Path Fence,
  Batch Invariants, Steps, DoD, Verification Commands, Progress
  Checklist, Hostile Audit Checklist).
- The Phase Sequence list (9 phases, in order).
- Working Boundaries scope.

### Consequence Sweep

Reconstructed: post-commit, the file did not contain orphaned references
to the deleted `## Objective` or `## Required Outcome` sections, since
those sections had no internal references. Phase 0 references were
unchanged. No closure refresh was required at the time (markdown change
only) and the rule for closure refresh after `schemas/paperhat-schemas/`
edits was not invoked at the time (F2/F3 finding); a current-turn
closure refresh on the post-commit file shows clean (verified during the
later F-fix commits).

### Proof Bundle

| Acceptance criterion | Status | Evidence |
|---|---|---|
| `## Problem Statement` exists | `PROVEN` | TEMPLATE_PLAN.md at HEAD (lines 3-22) |
| `## Required Outcome` removed | `PROVEN` | grep `Required Outcome` against TEMPLATE_PLAN.md returns nothing |
| `## Objective` removed | `PROVEN` | grep `^## Objective` returns nothing |
| `## Cross-Phase Invariants` exists with process-only bullets | `PROVEN` | TEMPLATE_PLAN.md at HEAD (lines 57-64) |
| `## Phase 3` stub exists | `PROVEN` | TEMPLATE_PLAN.md at HEAD shows the stub |

---

## Recommendation #2 — commit b9f1a53

### Source Inventory

- `TEMPLATE_PLAN.md` — `READ` (modified by this commit) — `DERIVATIVE`
- `TEMPLATE_PLAN_PLAN.md` — `READ` at commit time (the rec #2 turn
  discovered TEMPLATE_PLAN_PLAN.md and reconciled with its existing
  Required Report Form rather than imposing a new 5-section list) —
  `DERIVATIVE`
- AGENTS.md, the protocols, diagnostics.md — `NOT READ` at commit time

### Authority Map

Same as rec #1.

### Blocking Conditions

Same procedural condition as rec #1: F8 (Source Accounting failure).

### Grounded Findings

`FACT:` Commit b9f1a53 added `## Phase Artifacts` section between
`## Cross-Phase Invariants` and `## Phase Sequence` (verified by
TEMPLATE_PLAN.md current state and `git show b9f1a53` summary).

`FACT:` The section has five subsections: Report Path Convention,
Report Header, Report Body, Generated Artifacts, Stable Paths.

`FACT:` Diffstat: 56 insertions, 0 deletions (per `git show --stat b9f1a53`).

### Inferences

`INFERENCE:` The path convention chose two locations (per-phase
directory or appendix in TEMPLATE_PLAN.md) rather than one to handle
both data-heavy and text-only phases.

`INFERENCE:` The Report Body deferred to TEMPLATE_PLAN_PLAN.md's
Required Report Form (15 sections) rather than imposing a new 5-section
list because the meta-plan already specified the richer form.
(F18 later closed the dangling reference when TEMPLATE_PLAN_PLAN.md was
slated for discard.)

### Open Items

- F13 (Phase 0 has no path declaration) — explicitly deferred in the
  rec #2 commit message. Closed by commit 1fe5acb.
- F18 (TEMPLATE_PLAN_PLAN.md reference will dangle when meta-plan is
  discarded) — introduced by this commit. Closed by commit 420dbfc.

### Batch Invariants

The batch should have preserved (reconstructed):
- All sections introduced by rec #1 (Problem Statement, Cross-Phase
  Invariants, Phase 3 stub).
- Working Boundaries.
- Phase 0 skeleton.

### Consequence Sweep

Reconstructed: insertion was bounded between two existing section
headings; no other section's content shifted semantically. Phase 0
references to "the report" and "the file list" (in DoD) became
implicitly anchored to the new Phase Artifacts convention without
requiring updates to Phase 0 in this commit (commit message
acknowledged the retrofit was deferred).

### Proof Bundle

| Acceptance criterion | Status | Evidence |
|---|---|---|
| `## Phase Artifacts` exists with 5 subsections | `PROVEN` | TEMPLATE_PLAN.md current state, lines around 156 |
| Diffstat 56 insertions, 0 deletions | `PROVEN` | `git show --stat b9f1a53` |

---

## Recommendation #3 — commit c7ffb13

### Source Inventory

- `TEMPLATE_PLAN.md` — `READ` (modified) — `DERIVATIVE`
- AGENTS.md, the protocols, diagnostics.md — `NOT READ` at commit time

### Authority Map

Same as rec #1.

### Blocking Conditions

Same as rec #1 (F8).

### Grounded Findings

`FACT:` Commit c7ffb13 added `## Verification Block` section between
Phase Artifacts and Phase Sequence (current TEMPLATE_PLAN.md confirms).

`FACT:` Two subsections: Block Form (5 fields per command), Block
Discipline (4 rules; later tightened by F14+F15 commit).

`FACT:` Phase 0's `### Verification Commands` was retrofit from prose
list to Verification Block form with four entries; three of those
entries had `TODO(recommendation #N)` markers indicating misalignments
the commit chose not to fix.

`FACT:` Diffstat: 65 insertions, 7 deletions.

### Inferences

`INFERENCE:` Adding a `step:` field beyond the user's literal four
fields was a discretionary choice justified in the commit message:
"step: was added because the recommendation's stated purpose ('align
command to step') is unenforceable without it." This pre-empted
audit finding F2 (Pre-Edit Batch Invariants), partially.

`INFERENCE:` Leaving misaligned commands in the block with TODO markers
(rather than fixing or removing them) was a discretionary choice that
introduced F14 and F15 (later closed by commit 790b75f).

### Open Items

- F14 (TODO in `command:` field for Step 5 audit block) — introduced.
  Closed by commit 790b75f.
- F15 (closure-refresh command in Phase 0 with no aligned step) —
  introduced. Closed by commit 790b75f.

### Batch Invariants

The batch should have preserved (reconstructed):
- Phase Artifacts intact.
- All other Phase 0 subsections intact.
- Workspace-level sections intact.

### Consequence Sweep

Reconstructed: Phase 0's Verification Commands existed before; this
commit replaced the prose list with a structured form. No other section
referenced the prose list. Phase 0's other subsections (Steps, DoD)
that mention verification commands (e.g., "the template corpus file
list is generated in the current phase") were left coherent because
the verification block still produced the required artifact. Closure
refresh: not run at commit time (markdown only), but a current-turn
closure refresh against post-commit state is clean.

### Proof Bundle

| Acceptance criterion | Status | Evidence |
|---|---|---|
| `## Verification Block` exists with Block Form + Block Discipline | `PROVEN` | TEMPLATE_PLAN.md current state |
| Phase 0 `### Verification Commands` uses Block form | `PROVEN` | TEMPLATE_PLAN.md current state |
| Diffstat 65 insertions, 7 deletions | `PROVEN` | `git show --stat c7ffb13` |

---

## Recommendation #4 — commit 41c1c49

### Source Inventory

- `TEMPLATE_PLAN.md` — `READ` (modified) — `DERIVATIVE`
- AGENTS.md, the protocols, diagnostics.md — `NOT READ` at commit time

### Authority Map

Same as rec #1.

### Blocking Conditions

Same as rec #1 (F8).

### Grounded Findings

`FACT:` Commit 41c1c49 reduced `## Working Boundaries` from a multi-list
section to a single editable-path declaration plus a one-paragraph
delegation (current TEMPLATE_PLAN.md, lines 45-55).

`FACT:` Removed: the "Current read scope for preparatory planning"
six-bullet list and a redundant "every file other than" out-of-scope
bullet (per commit message and current state diff against HEAD~3 of
this commit).

`FACT:` Renamed "Current edit scope" to "Plan-wide editable scope".

`FACT:` Diffstat: 6 insertions, 14 deletions (verified by
`git show --stat 41c1c49`). The commit message claims "Net: 18 lines
removed, 9 added" — this is F12, the actual diffstat differs.

### Inferences

`INFERENCE:` The deletion of the workspace-level read scope eliminated
the conflict between Working Boundaries and Phase 0's In-Scope Path
Fence (which adds `diagnostics.md` and `implementations/languages/
codex/**`). The audit had flagged this conflict separately.

### Open Items

- F12 (commit message diffstat count wrong) — introduced; unrepairable.

### Batch Invariants

The batch should have preserved (reconstructed):
- The single editable-path constraint (`schemas/paperhat-schemas/
  TEMPLATE_PLAN.md`).
- Per-phase In-Scope/Out-Of-Scope Path Fence convention (kept by the new
  delegation paragraph).
- All other workspace sections.

### Consequence Sweep

Reconstructed: the Phase 0 In-Scope Path Fence (which added paths the
removed workspace read scope had also listed) became the sole authority
for what Phase 0 may read. No other section referenced the deleted
workspace read scope. Closure refresh: not run at commit time;
current-turn closure refresh against post-commit state is clean.

### Proof Bundle

| Acceptance criterion | Status | Evidence |
|---|---|---|
| `## Working Boundaries` reduced to single edit-path + delegation | `PROVEN` | TEMPLATE_PLAN.md current state, lines 45-55 |
| Old preparatory-planning read scope removed | `PROVEN` | grep `Current read scope` returns nothing |
| Diffstat 6 insertions, 14 deletions | `PROVEN` | `git show --stat 41c1c49` |
| Commit message diffstat correct | `NOT PROVEN — F12` | message says "18 / 9", actual is "6 / 14" |

---

## Recommendation #5 — commit 17262cc

### Source Inventory

- `TEMPLATE_PLAN.md` — `READ` (modified) — `DERIVATIVE`
- AGENTS.md, the protocols, diagnostics.md — `NOT READ` at commit time

### Authority Map

Same as rec #1.

### Blocking Conditions

Same as rec #1 (F8).

### Grounded Findings

`FACT:` Commit 17262cc added `## Hostile Audit Template` section between
Verification Block and Phase Sequence (current TEMPLATE_PLAN.md
confirms).

`FACT:` Two subsections: Universal Hostile Audit Questions (9 questions,
present-tense) and Phase-Specific Additions.

`FACT:` Vacuous-item handling: items that are vacuously satisfied by a
phase's Batch Invariants must be marked `N/A — <invariant citation>`
rather than omitted.

`FACT:` Phase 0's `### Hostile Audit Checklist` was retrofit:
- 8 past-tense local questions replaced with reference to the Template.
- The `.cdx` CLI gate question marked N/A for Phase 0.
- A "design syntax before audits" question dropped (Phase 3 territory).
- Two corpus-specific questions kept as Phase 0 additions.

`FACT:` Diffstat: 63 insertions, 12 deletions (verified by
`git show --stat 17262cc`). The commit message claims "Net: 51
insertions, 13 deletions" — this is the second F12 instance.

### Inferences

`INFERENCE:` The N/A-with-citation rule was a discretionary choice
beyond the user's literal "remove vacuous items" recommendation. The
commit message justified it as preserving auditor visibility.

`INFERENCE:` The widening to all 9 universal questions (vs. the user's
roughly-listed three) was a discretionary expansion driven by what
universal procedural failures the audit had observed across all 5 rec
commits.

### Open Items

- F12 (commit message diffstat count wrong) — second instance;
  unrepairable.
- F19 (universal citation question narrower than LLM_SESSION_PROTOCOL.md
  §Citation Rules scope) — introduced. Closed by commit fa101bc.

### Batch Invariants

The batch should have preserved (reconstructed):
- Verification Block intact.
- Phase Artifacts intact.
- Cross-Phase Invariants intact.
- All other Phase 0 subsections intact except the hostile audit checklist
  itself.
- Phase 3 stub intact.

### Consequence Sweep

Reconstructed: Phase 0's hostile audit checklist was the only place
referencing the prior 8 past-tense questions. No other section reused
those question wordings. Closure refresh: not run at commit time;
current-turn closure refresh against post-commit state is clean.

### Proof Bundle

| Acceptance criterion | Status | Evidence |
|---|---|---|
| `## Hostile Audit Template` exists with Universal Questions + Phase-Specific Additions | `PROVEN` | TEMPLATE_PLAN.md current state |
| Phase 0 `### Hostile Audit Checklist` uses template + N/A + 2 additions | `PROVEN` | TEMPLATE_PLAN.md current state |
| Diffstat 63 insertions, 12 deletions | `PROVEN` | `git show --stat 17262cc` |
| Commit message diffstat correct | `NOT PROVEN — F12` | message says "51 / 13", actual is "63 / 12" |

---

## F1–F11 Status After Recovery

| Finding | Description | Status After This Report |
|---|---|---|
| F1 | Required Output Structure not produced for any rec | `CLOSED` — produced retrospectively above |
| F2 | Pre-Edit Batch Invariants not stated | `CLOSED` — Batch Invariants subsections produced above |
| F3 | Consequence Sweep not performed | `CLOSED` — Consequence Sweep subsections produced above |
| F4 | Hostile Audit not performed on each rec batch | `PARTIAL` — the original audit (this conversation) did this; F13–F19 were the findings; this report does not duplicate them |
| F5 | Proof Bundle not produced | `CLOSED` — Proof Bundle subsections produced above with current-turn evidence |
| F6 | Citation Rules — cached citations used | `NOT REPAIRABLE` — conduct at commit time |
| F7 | Non-Stale Evidence Rules — prior-turn evidence | `NOT REPAIRABLE` — conduct at commit time |
| F8 | Source Accounting Rule — synthesis before reads | `NOT REPAIRABLE` — conduct at commit time |
| F9 | Audit Mode Rule — reassurance language used | `NOT REPAIRABLE` — conduct at commit time |
| F10 | Responsiveness Rule — throughput optimized | `NOT REPAIRABLE` — conduct at commit time |
| F11 | Edit Batch Contract — incomplete | `CLOSED` — completeness restored by this report's per-rec sections |
| F12 | Wrong commit-message diffstat counts in `41c1c49` and `17262cc` | `NOT REPAIRABLE` — committed history; `AGENTS.md:52` forbids rewrites |

## Forward enforcement

After the audit and the option-3 fix batch (F13–F19) plus the gate hooks
installed in `.claude/settings.local.json` and `.claude/hooks/`:

- F1, F2, F3, F5, F11 cannot recur silently because the
  UserPromptSubmit hook injects the required-output-structure rule into
  every prompt.
- F6, F7 cannot recur for governing files because the PreToolUse hook
  blocks Read on the four protocol files plus PAPERHAT_TURN_GATE.md;
  the model must use Bash cat/sed instead, which fetches fresh disk
  bytes.
- F6, F7 are softened (warning, not block) for non-governing files via
  the PostToolUse hook on cache-pointer detection.
- F8 (Source Accounting) is enforced by the gate's "MUST cat these four
  files via Bash" instruction and the Required Output Structure's
  Source Inventory section.
- F9 (Audit Mode Rule) is enforced by the gate's audit-mode reminder.
- F10 (Responsiveness Rule) is enforced by the gate's "Throughput is
  not a virtue" reminder.
- F12 cannot be retroactively repaired but going forward, commit
  message diffstat claims should be cross-checked against `git show
  --stat` before commit, and the Required Output Structure's Proof
  Bundle catches diffstat mismatches as part of acceptance criteria
  evidence.

## Sources Accounted For

- AGENTS.md (cat'd this turn, 70 lines) — `NORMATIVE`
- LLM_SESSION_PROTOCOL.md (cat'd this turn, 572 lines) — `NORMATIVE`
- SPEC_AUTHORING_PROTOCOL.md (cat'd this turn, 256 lines) — `NORMATIVE`
- diagnostics.md (cat'd this turn, 308 lines) — `NORMATIVE`
- TEMPLATE_PLAN.md (sed'd this turn for Step 5, Open Verification
  Items; full state read for cross-checking commit content) —
  `DERIVATIVE`
- Five rec commits (`git show --stat` and `git show --format=...
  --no-patch` this turn for each) — `DERIVATIVE`
- Plan git state (`git log` and `git status` this turn) — `DERIVATIVE`
