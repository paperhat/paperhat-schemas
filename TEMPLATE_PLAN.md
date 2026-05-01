# Template Migration Plan

Status: planning document only. No template files have been renamed by this
plan.

This plan is not self-authorizing. The executor prompt that launches Phase A
must explicitly grant every cross-repository read, cross-repository edit, Codex
CLI invocation, and concurrent-work lock listed below.

## Verified Starting Facts

Current facts verified on 1 May 2026:

- `git ls-files | rg '(^|/)template\.cdx$' | wc -l` in
  `schemas/paperhat-schemas` returns `174`.
- `git ls-files | rg '\.tcdx$' | wc -l` in `schemas/paperhat-schemas` returns
  `0`.
- `git status --short` in `schemas/paperhat-schemas` returns only
  `?? TEMPLATE_PLAN.md`.
- stale-reference grep across `specifications/` with `rg --no-ignore` returns
  18 line hits in exactly these 8 files outside `schemas/paperhat-schemas`:
  - `specifications/applications/lexis-spec/spec/1.0.0/AI_CONVENTIONS.md`
  - `specifications/applications/lexis-spec/tests/test_structural_check.py`
  - `specifications/applications/lexis-spec/tools/structural_check.py`
  - `specifications/applications/lexis-spec/plans/specification-schema-preflight.md`
  - `specifications/applications/lexis-spec/plans/poc/step-1-report.md`
  - `specifications/applications/lexis-spec/plans/implementation-program/composition-definition-update-priority-note.md`
  - `specifications/applications/lexis-spec/plans/implementation-program/legal-package-graph-repair-decision-note.md`
  - `specifications/applications/prism-spec/plans/executable-remediation-plan.md`
- The local Codex CLI exists at
  `implementations/languages/codex/target/release/codex` and supports
  `canonicalize`.
- `codex canonicalize` returns nonzero on parse failure when its exit code is
  captured before any pipeline, and returns zero for a valid template.
- `codex validate --schema ...` is not a reliable Phase A evidence command:
  a trial against `domain/code-specification/templates/basic/template.cdx`
  failed on schema-import availability before template validation. Phase A uses
  `codex canonicalize` evidence instead.

## Purpose

Concrete `.cdx` files are Codex documents. They are eligible for normal Codex
parsing, identity, reference, import, and closure rules.

Template files are not concrete documents. Applications use them as boilerplate
that a user or generator fills in later. A template may intentionally omit
document identifiers, entity identifiers, references, names, or content required
in concrete `.cdx`.

Phase A separates those surfaces mechanically:

- `.cdx` remains the extension for concrete Codex documents.
- `.tcdx` becomes the extension for Codex template source.

Phase A does not define template syntax, implement a template processor, edit
template contents, or regenerate rendered concrete documents. Those are Phase B.

## Required Executor Prompt Grants

The executor prompt must explicitly grant all items in this section. If any
grant is missing, the executor must refuse Phase A and report the missing grant.

1. Edit grant for `schemas/paperhat-schemas/`.
2. Edit grant for these exact files outside `schemas/paperhat-schemas/`:
   - `specifications/applications/lexis-spec/spec/1.0.0/AI_CONVENTIONS.md`
   - `specifications/applications/lexis-spec/tests/test_structural_check.py`
   - `specifications/applications/lexis-spec/tools/structural_check.py`
   - `specifications/applications/lexis-spec/plans/specification-schema-preflight.md`
   - `specifications/applications/lexis-spec/plans/poc/step-1-report.md`
   - `specifications/applications/lexis-spec/plans/implementation-program/composition-definition-update-priority-note.md`
   - `specifications/applications/lexis-spec/plans/implementation-program/legal-package-graph-repair-decision-note.md`
   - `specifications/applications/prism-spec/plans/executable-remediation-plan.md`
3. Read-only grant for stale-reference grep across `specifications/` using
   `rg --no-ignore`.
4. Invocation grant for the already-built Codex CLI binary at
   `implementations/languages/codex/target/release/codex`. This is an invocation
   grant only; editing `implementations/` remains forbidden.
5. Strict canonicalize-failure rule: any `codex canonicalize` failure in Batch 3
   stops Phase A before the rename. Phase A has no continuation flag,
   per-template exception file, or "known failure" bypass.
6. Parallel-work lock grant covering the full repository roots listed in
   "Parallel-Work Coordination".

## Path Fence

Phase A edit scope:

- `schemas/paperhat-schemas/TEMPLATE_PLAN.md`
- `schemas/paperhat-schemas/tools/template_migration/**`
- `schemas/paperhat-schemas/tools/test_verify_code_specification_references.py`
- `schemas/paperhat-schemas/tools/verify_code_specification_references.py`, only
  if a failing test proves a discovery change is needed
- `schemas/paperhat-schemas/spec/1.0.0/schemas/**/templates/**/template.cdx`,
  renamed to `template.tcdx`
- `schemas/paperhat-schemas/spec/1.0.0/schemas/roadmap.md`
- the exact 8 external files listed in "Required Executor Prompt Grants"

Phase A out of scope for edits:

- `$WORKSPACE_ROOT/implementations/**`
- `$WORKSPACE_ROOT/tools/**`; this is the workspace-root tools directory and
  does not include `schemas/paperhat-schemas/tools/template_migration/**`
- `archive/**`
- `project/**`
- root instruction files, including `AGENTS.md`, `CLAUDE.md`,
  `LLM_SESSION_PROTOCOL.md`, and `SPEC_AUTHORING_PROTOCOL.md`
- `*-OBSOLETE*` files
- any Codex processor implementation
- any new branch, tag, worktree, submodule, or gitlink
- any `specifications/**` file not listed in the exact 8-file grant

Phase A read-only verification commands outside the edit scope:

```bash
rg -n --no-ignore 'template\.cdx' "$WORKSPACE_ROOT/specifications" -g '!**/.git/**' -g '!**/__pycache__/**' -g '!**/target/**' -g '!**/node_modules/**'
```

No other workspace-wide read is part of Phase A.

## Workspace Root Resolution

Every shell script computes the workspace root from the
`schemas/paperhat-schemas` working tree:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
```

Executable command text must use `"$WORKSPACE_ROOT"` instead of hard-coded
absolute workspace paths.

## Parallel-Work Coordination

Phase A holds an exclusive logical lock on these full git repositories:

- `schemas/paperhat-schemas`
- `specifications/applications/lexis-spec`
- `specifications/applications/prism-spec`

No other LLM may read, write, stage, commit, test, or otherwise operate inside
those three repositories while Phase A is running. Parallel work may proceed
only outside those repository roots.

The lock exists because Phase A edits and commits in all three repositories. A
lock on individual files is not enough in a shared working tree.

Branches, worktrees, tags, submodules, `git switch -c`, and `git checkout -b`
remain forbidden.

## Phase A Invariants

- Do not edit template contents.
- Do not define placeholder syntax.
- Do not implement or invoke a `tcdx` processor.
- Do not edit Codex implementation source.
- Do not hand-edit closure hashes.
- Do not create branches, tags, worktrees, submodules, or gitlinks.
- Do not read or rely on `*-OBSOLETE*` files.
- Preserve concrete `.cdx` verifier behavior except proven `.tcdx` exclusion.
- Use path-scoped staging and commits in each touched repository.
- Stop at any gate failure. Do not continue to later batches.

## Phase A Deliverables

Schemas repo deliverables:

- `TEMPLATE_PLAN.md`
- `tools/template_migration/capture_codex_canonicalize.sh`
- `tools/template_migration/rename_templates.sh`
- `tools/template_migration/gate.sh`
- `tools/template_migration/baseline/template-cdx-inventory.txt`
- `tools/template_migration/baseline/tcdx-inventory.txt`
- `tools/template_migration/baseline/concrete-reference-summary.txt`
- `tools/template_migration/baseline/concrete-reference-problems-in-scope.tsv`
- `tools/template_migration/baseline/codex-canonicalize/summary.tsv`
- per-template Codex CLI stdout/stderr under
  `tools/template_migration/baseline/codex-canonicalize/`
- `tools/template_migration/evidence/stale-reference-rewrite.tsv`
- migrated `template.tcdx` files
- updated `spec/1.0.0/schemas/roadmap.md`
- verifier test/code edits only if required by Batch 5

Lexis-spec deliverables:

- updated `spec/1.0.0/AI_CONVENTIONS.md`
- updated `tests/test_structural_check.py`
- updated `tools/structural_check.py`
- updated Lexis planning files listed in the 8-file grant

Prism-spec deliverables:

- updated `plans/executable-remediation-plan.md`

Phase A must not produce:

- template fixtures
- placeholder syntax
- a template processor
- rendered `.cdx` files
- closure hash changes caused by the rename

## Batch 0: Plan Checkpoint

Scope:

- Commit this plan only in `schemas/paperhat-schemas`.
- No scripts.
- No renames.
- No cross-repo edits.

Commands:

```bash
git status --short
git add TEMPLATE_PLAN.md
git diff --cached --check
git commit -m "Add Phase A template migration plan"
git status --short
```

Definition of done:

- Pre-commit status is exactly `?? TEMPLATE_PLAN.md`.
- Commit contains only `TEMPLATE_PLAN.md`.
- Post-commit status is clean in `schemas/paperhat-schemas`.

## Batch 1: Capture Baseline Inventory

Scope:

- Create durable baseline evidence under
  `schemas/paperhat-schemas/tools/template_migration/baseline/`.
- No scripts.
- No renames.
- No Lexis/Prism edits.

Commands:

```bash
git status --short
[ ! -e tools/template_migration/baseline ] || { echo "baseline already exists"; exit 1; }
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
mkdir -p tools/template_migration/baseline
git ls-files | rg '(^|/)template\.cdx$' | sort > tools/template_migration/baseline/template-cdx-inventory.txt
git ls-files | rg '\.tcdx$' | sort > tools/template_migration/baseline/tcdx-inventory.txt
test "$(wc -l < tools/template_migration/baseline/template-cdx-inventory.txt | tr -d ' ')" = "174"
test "$(wc -l < tools/template_migration/baseline/tcdx-inventory.txt | tr -d ' ')" = "0"
python3 tools/verify_code_specification_references.py --workspace-root "$WORKSPACE_ROOT" --show summary > tools/template_migration/baseline/concrete-reference-summary.txt
python3 tools/verify_code_specification_references.py --workspace-root "$WORKSPACE_ROOT" --show problems | awk -F'\t' 'NR==1 || $4 ~ /^schemas\/paperhat-schemas\//' | sort > tools/template_migration/baseline/concrete-reference-problems-in-scope.tsv
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --check
git add tools/template_migration/baseline/template-cdx-inventory.txt tools/template_migration/baseline/tcdx-inventory.txt tools/template_migration/baseline/concrete-reference-summary.txt tools/template_migration/baseline/concrete-reference-problems-in-scope.tsv
git diff --cached --check
git commit -m "Capture template migration baseline"
git status --short
```

Definition of done:

- Starting `git status --short` is clean in `schemas/paperhat-schemas`.
- `template-cdx-inventory.txt` has exactly `174` rows.
- `tcdx-inventory.txt` has exactly `0` rows.
- In-scope concrete verifier problem baseline is captured from current tree
  state.
- Tests pass with exit `0`.
- Commit contains only baseline inventory and verifier baseline files.
- Post-commit status is clean in `schemas/paperhat-schemas`.

## Batch 2: Add Migration Scripts

Scope:

- Add scripts under `schemas/paperhat-schemas/tools/template_migration/`.
- Use the committed Batch 1 baseline for script checks.
- No Codex canonicalize sweep.
- No renames.
- No Lexis/Prism edits.

Required scripts:

- `capture_codex_canonicalize.sh`
- `rename_templates.sh`
- `gate.sh`

`capture_codex_canonicalize.sh` contract:

- Reads `tools/template_migration/baseline/template-cdx-inventory.txt`.
- Aborts if the inventory does not contain exactly `174` rows.
- Aborts if `tools/template_migration/baseline/codex-canonicalize/` already
  exists.
- Resolves the Codex CLI binary at
  `"$WORKSPACE_ROOT/implementations/languages/codex/target/release/codex"`.
- Supports `--check` mode that validates the baseline inventory, verifies the
  Codex CLI binary exists and `canonicalize --help` exits zero, confirms the
  output directory does not exist, and performs no template canonicalization.
- Runs `codex canonicalize "$template_path"` for each template.
- Captures stdout, stderr, and exit code for each template under a deterministic
  evidence path:
  - evidence key is `sha256(template_path)` using lowercase hexadecimal
  - evidence directory is
    `tools/template_migration/baseline/codex-canonicalize/files/<evidence-key>/`
  - files inside that directory are `stdout.txt`, `stderr.txt`, and
    `exit-code.txt`
- Writes `summary.tsv` with columns:
  `template_path`, `evidence_key`, `evidence_dir`, `exit_code`, `status`,
  `first_output_line`.
- `first_output_line` is the first line of stderr when stderr is non-empty;
  otherwise it is the first line of stdout.
- Uses `PASS` only when exit code is `0` and neither stdout nor stderr contains
  a Codex diagnostic record. Any nonzero exit code or diagnostic record is
  `FAIL`.
- Does not edit any template.

`rename_templates.sh` contract:

- Reads `tools/template_migration/baseline/template-cdx-inventory.txt`.
- Requires exactly `174` inventory rows.
- Asserts current tracked `template.cdx` count still equals `174` immediately
  before the move loop.
- Aborts if any inventory source path is missing.
- Aborts if any target `template.tcdx` already exists.
- Aborts if Codex canonicalize evidence is missing.
- If Codex canonicalize evidence contains `FAIL`, aborts. There is no
  continuation flag in Phase A.
- Uses `git mv` for all 174 template renames.
- Replaces `template.cdx` with `template.tcdx` using fixed-string replacement
  only in:
  - `spec/1.0.0/schemas/roadmap.md`
  - the exact 8 external files listed in the executor grant
- Writes `tools/template_migration/evidence/stale-reference-rewrite.tsv` with
  columns `file`, `before_count`, `after_count`, and `status`.
- The rewrite TSV includes one row for `spec/1.0.0/schemas/roadmap.md` and one
  row for each exact external file listed in the executor grant.
- The script also prints the rewrite TSV to stdout after writing it.
- Does not edit template contents.
- Supports `--check` mode with no file mutations; `--check` validates the
  inventory, current tracked counts, source path existence, and target absence
  but does not require Codex canonicalize evidence.

`gate.sh` contract:

- Parses `--pre-rename`; no other argument is accepted.
- In `--pre-rename` mode:
  - expects 174 tracked `template.cdx`
  - expects 0 tracked `.tcdx`
  - skips post-rename stale-reference checks
- In default post-rename mode:
  - expects 0 tracked `template.cdx`
  - expects 174 tracked `template.tcdx`
  - fails if `roadmap.md` contains `template.cdx`
  - fails if any of the exact 8 external files contains `template.cdx`
  - fails if any non-allowlisted in-repo file contains `template.cdx`
  - the in-repo stale-reference allowlist is exactly:
    - `TEMPLATE_PLAN.md`
    - `tools/template_migration/capture_codex_canonicalize.sh`
    - `tools/template_migration/rename_templates.sh`
    - `tools/template_migration/gate.sh`
    - `tools/template_migration/baseline/**`
    - `tools/template_migration/evidence/**`
- Compares in-scope verifier problems by row identity against
  `baseline/concrete-reference-problems-in-scope.tsv`. The comparison is scoped
  to rows whose file column starts with `schemas/paperhat-schemas/`; rows with
  status `missing_id` are ignored for the delta; any row present in the current
  non-`missing_id` problem set but absent from the baseline fails.
- Runs closure refresh as workspace compliance, but detects drift by comparing
  `git diff --binary HEAD --` before and after refresh so both staged and
  unstaged mid-state changes are included:
  - save `git diff --binary HEAD --` to a temporary file
  - run `python3 tools/refresh_repository_closure.py`
  - save `git diff --binary HEAD --` again
  - fail if the two patch files differ
- Runs `git diff --check`.

Commands:

```bash
git status --short
# Create the three scripts from the contracts above before running them.
chmod +x tools/template_migration/capture_codex_canonicalize.sh tools/template_migration/rename_templates.sh tools/template_migration/gate.sh
bash -n tools/template_migration/capture_codex_canonicalize.sh tools/template_migration/rename_templates.sh tools/template_migration/gate.sh
tools/template_migration/capture_codex_canonicalize.sh --check
tools/template_migration/rename_templates.sh --check
tools/template_migration/gate.sh --pre-rename
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --check
git add tools/template_migration/capture_codex_canonicalize.sh tools/template_migration/rename_templates.sh tools/template_migration/gate.sh
git diff --cached --check
git commit -m "Add template migration scripts"
git status --short
```

Definition of done:

- Scripts exist before they are invoked.
- Scripts are executable before they are invoked.
- `capture_codex_canonicalize.sh --check`,
  `rename_templates.sh --check`, and `gate.sh --pre-rename` are implemented and
  tested against the committed Batch 1 baseline.
- The closure-refresh drift detector runs during `gate.sh --pre-rename` and
  proves that refresh does not alter the current patch.
- Tests pass with exit `0`.
- Commit contains only the three scripts.
- Post-commit status is clean in `schemas/paperhat-schemas`.

## Batch 3: Capture Codex Evidence

Scope:

- Create durable Codex canonicalize evidence under
  `schemas/paperhat-schemas/tools/template_migration/baseline/codex-canonicalize/`.
- No renames.
- No Lexis/Prism edits.

Commands:

```bash
git status --short
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
CODEX_CLI="$WORKSPACE_ROOT/implementations/languages/codex/target/release/codex"
test -x "$CODEX_CLI"
"$CODEX_CLI" canonicalize --help >/tmp/template-migration-codex-canonicalize-help.txt
tools/template_migration/capture_codex_canonicalize.sh
awk 'END { exit (NR - 1 == 174) ? 0 : 1 }' tools/template_migration/baseline/codex-canonicalize/summary.tsv
FAIL_ROWS="$(awk -F'\t' 'NR > 1 && $3 == "FAIL" { print }' tools/template_migration/baseline/codex-canonicalize/summary.tsv)"
if [ -n "$FAIL_ROWS" ]; then printf '%s\n' "$FAIL_ROWS"; exit 1; fi
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --check
git add tools/template_migration/baseline/codex-canonicalize/
git diff --cached --check
git commit -m "Capture template canonicalize evidence"
git status --short
```

Definition of done:

- Starting `git status --short` is clean in `schemas/paperhat-schemas`.
- The Codex CLI binary exists, is executable, and `canonicalize --help` exits
  `0`.
- `codex-canonicalize/summary.tsv` has exactly `174` data rows.
- If any summary row has `FAIL`, Phase A stops before rename and reports the
  failure rows. Strict Phase A has no continuation path.
- Tests pass with exit `0`.
- Commit contains only Codex canonicalize evidence.

## Batch 4: Rename Templates And Stale References

Scope:

- Rename 174 template files in `schemas/paperhat-schemas`.
- Update `roadmap.md`.
- Update exactly the 8 external files listed in the executor grant.
- Do not edit template contents.

Preconditions:

- `schemas/paperhat-schemas`, `lexis-spec`, and `prism-spec` statuses are clean.
- Batch 1 baseline evidence is committed.
- Batch 3 Codex canonicalize evidence is committed and contains no `FAIL` rows.

Commands:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
git status --short
git -C "$WORKSPACE_ROOT/specifications/applications/lexis-spec" status --short
git -C "$WORKSPACE_ROOT/specifications/applications/prism-spec" status --short
tools/template_migration/rename_templates.sh
tools/template_migration/gate.sh
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --name-status
git diff --check
git add -A spec/1.0.0/schemas tools/template_migration/evidence/stale-reference-rewrite.tsv
git diff --cached --check
git commit -m "Rename schema templates to tcdx"
git status --short
```

Lexis verification:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
cd "$WORKSPACE_ROOT/specifications/applications/lexis-spec"
python3 -m unittest tests/test_structural_check.py
git status --short
git diff --check
git add spec/1.0.0/AI_CONVENTIONS.md tests/test_structural_check.py tools/structural_check.py plans/specification-schema-preflight.md plans/poc/step-1-report.md plans/implementation-program/composition-definition-update-priority-note.md plans/implementation-program/legal-package-graph-repair-decision-note.md
git diff --cached --check
git commit -m "Update Lexis template extension references"
git status --short
```

Prism verification:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
cd "$WORKSPACE_ROOT/specifications/applications/prism-spec"
git status --short
git diff --check
git add plans/executable-remediation-plan.md
git diff --cached --check
git commit -m "Update Prism template extension references"
git status --short
```

Definition of done:

- `git diff --name-status` in `schemas/paperhat-schemas` shows 174 renames from
  `template.cdx` to `template.tcdx`.
- No tracked `template.cdx` remains in `schemas/paperhat-schemas`.
- Exactly 174 tracked `template.tcdx` files exist.
- `spec/1.0.0/schemas/roadmap.md` contains no `template.cdx`.
- All 8 external files contain no `template.cdx`.
- `lexis-spec/tools/structural_check.py` uses `templates/*/template.tcdx`.
- `python3 -m unittest tests/test_structural_check.py` passes in `lexis-spec`.
- Schema repo tests pass.
- `gate.sh` passes.
- `git diff --check` passes in every touched repo.
- Before/after grep evidence proves the fixed-string substitution changed only
  `template.cdx` to `template.tcdx` in the planned files, and that evidence is
  stored in `tools/template_migration/evidence/stale-reference-rewrite.tsv`.
- Commit separately in each touched repo:
  - `schemas/paperhat-schemas`: renames plus roadmap update
  - `specifications/applications/lexis-spec`: Lexis updates
  - `specifications/applications/prism-spec`: Prism plan update

## Batch 5: Concrete Verifier Exclusion Test

Scope:

- Add/update verifier tests proving `.tcdx` files are not discovered as
  concrete `.cdx`.
- Modify verifier discovery code only if the test fails first.

Commands:

```bash
git status --short
python3 -m unittest tools/test_verify_code_specification_references.py
tools/template_migration/gate.sh
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --check
git add tools/test_verify_code_specification_references.py tools/verify_code_specification_references.py
git diff --cached --check
git commit -m "Verify templates are excluded from concrete scans"
git status --short
```

Definition of done:

- Test proves `.tcdx` exclusion.
- Ordinary `.cdx` discovery remains covered.
- Tests pass.
- `gate.sh` passes.
- Commit contains only verifier test/code changes.

## Batch 6: Final Audit

Scope:

- No semantic edits.
- Run final evidence commands.

Commands:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
tools/template_migration/gate.sh
git ls-files | rg '(^|/)template\.cdx$'
git ls-files | rg '(^|/)template\.tcdx$' | wc -l
rg -n 'template\.cdx' "$WORKSPACE_ROOT/schemas/paperhat-schemas" -g '!**/.git/**'
rg -n --no-ignore 'template\.cdx' "$WORKSPACE_ROOT/specifications" -g '!**/.git/**' -g '!**/__pycache__/**' -g '!**/target/**' -g '!**/node_modules/**'
python3 tools/verify_code_specification_references.py --workspace-root "$WORKSPACE_ROOT" --show summary
python3 -m unittest tools/test_verify_code_specification_references.py tools/test_verify_schema_package_closure.py tools/test_refresh_repository_closure.py
git diff --check
git status --short
```

Lexis final verification:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
cd "$WORKSPACE_ROOT/specifications/applications/lexis-spec"
python3 -m unittest tests/test_structural_check.py
git diff --check
git status --short
```

Prism final verification:

```bash
WORKSPACE_ROOT="$(cd "$(git rev-parse --show-toplevel)/../.." && pwd)"
cd "$WORKSPACE_ROOT/specifications/applications/prism-spec"
git diff --check
git status --short
```

Definition of done:

- All touched repos have clean status after their commits.
- No tracked `template.cdx` files remain in `schemas/paperhat-schemas`.
- Exactly 174 tracked `template.tcdx` files exist.
- No stale `template.cdx` references remain outside allowlisted migration
  evidence and this plan.
- Concrete verifier summary has no unexpected in-scope worsening from baseline.
- Closure refresh produces no drift beyond the pre-refresh patch.
- All listed tests pass.

## Phase B: Deferred Work

Phase B requires a separate plan and authorization. Phase B covers:

- template placeholder syntax
- template fixtures
- template rendering
- `tcdx` processor architecture
- Codex checks for rendered fixture output
- future manifest behavior for template artifacts

None of those topics is part of Phase A.

## Final Evidence Package

The executor's final report must include:

- source inventory
- authority map
- blocking conditions
- grounded findings
- batch invariants
- consequence sweep
- every file edited, grouped by git repository
- every command run, exact command text, exit code, and result
- commit hash for every touched repository
- Codex canonicalize evidence summary row count and failure count
- Codex canonicalize evidence layout path and one sample `summary.tsv` row
- stale-reference rewrite TSV contents
- rename count from `git diff --name-status`
- final tracked `template.tcdx` count
- final stale-reference search output
- final concrete verifier summary
- closure-refresh drift comparison result
- Lexis structural-check test result
- remaining unverified risk
