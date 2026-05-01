# Template Inventory Notes

Status: inventory-only note. The former `.tcdx` migration plan has been
removed. This file does not authorize template renames, a separate template
extension, template processor work, cross-repository edits, or template-content
changes.

## Verified Inventory

Current facts verified on 1 May 2026:

- `git ls-files | rg '(^|/)template\.cdx$' | wc -l` in
  `schemas/paperhat-schemas` returns `174`.
- `git ls-files | rg '\.tcdx$' | wc -l` in `schemas/paperhat-schemas` returns
  `0`.
- `git status --short` in `schemas/paperhat-schemas` returned only
  `?? TEMPLATE_PLAN.md`.
- Stale-reference grep across `specifications/` with `rg --no-ignore` returned
  18 line hits in exactly these 8 files outside `schemas/paperhat-schemas`:
  - `specifications/applications/lexis-spec/spec/1.0.0/AI_CONVENTIONS.md`
  - `specifications/applications/lexis-spec/tests/test_structural_check.py`
  - `specifications/applications/lexis-spec/tools/structural_check.py`
  - `specifications/applications/lexis-spec/plans/specification-schema-preflight.md`
  - `specifications/applications/lexis-spec/plans/poc/step-1-report.md`
  - `specifications/applications/lexis-spec/plans/implementation-program/composition-definition-update-priority-note.md`
  - `specifications/applications/lexis-spec/plans/implementation-program/legal-package-graph-repair-decision-note.md`
  - `specifications/applications/prism-spec/plans/executable-remediation-plan.md`
- The local Codex CLI existed at
  `implementations/languages/codex/target/release/codex` and supported
  `canonicalize`.
- `codex canonicalize` returned nonzero on parse failure when its exit code was
  captured before any pipeline, and returned zero for a valid template.
- `codex validate --schema ...` was not a reliable template-inventory evidence
  command in the earlier audit: a trial against
  `domain/code-specification/templates/basic/template.cdx` failed on
  schema-import availability before template validation.

## Use

These facts are retained only as inventory awareness for the future first-class
Codex template design. They are not a migration plan.
