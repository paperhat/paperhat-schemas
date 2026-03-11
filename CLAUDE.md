# Paperhat Schemas — AI Reference

## What This Repository Is

This repository is the canonical universal Paperhat schema corpus.

It contains reusable schema packages that are not owned by Lexis. Lexis consumes these schemas. It does not define them.

## Codex Authority Rule

When checking parser behavior, canonical surface output, digest values, schema imports, validation, or reconstruction, the real Codex command-line interface is the authority.

Rules:

1. Real `.cdx` files on disk MUST be checked with the real Codex command-line interface.
2. Canonical surface output and digest values from the real Codex command-line interface override bridge or fallback tooling whenever they disagree.
3. `SchemaImport` references MUST resolve through the real Codex command-line interface over the real repository tree.
4. If local manifest tooling disagrees with the real Codex command-line interface, the mismatch MUST be reported and repaired. It MUST NOT be ignored.
5. Schema and corpus work for active Lexis integration MUST follow `/Users/guy/Workspace/@paperhat/specifications/lexis-spec/plans/implementation-program/codex-active-closure-conformance-policy.md`.

## Architectural Rule

Model semantic truth first.

Do not create page-shaped, widget-shaped, or presentation-shaped schemas when a semantic schema or composed structure already covers the need.

## Package Boundary Rule

These schemas are universal. They are not Lexis-specific. Do not introduce `lexis-` package naming or Lexis-owned semantics into this repository.
