#!/usr/bin/env python3
"""Refresh SchemaImport references and manifest closure hashes for one repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_MAX_SCHEMA_IMPORT_PASSES = 32


class RefreshRepositoryClosureError(RuntimeError):
    """Raised when repository closure refresh cannot complete cleanly."""


@dataclass(frozen=True)
class CommandResult:
    """Captured result from one subprocess invocation."""

    command: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str


def default_repository_root() -> Path:
    """Return the paperhat-schemas repository root for this script."""

    return Path(__file__).resolve().parents[1]


def workspace_root() -> Path:
    """Return the Paperhat workspace root that hosts the sanctioned tools."""

    return Path(__file__).resolve().parents[3]


def lexis_tool_path(tool_name: str) -> Path:
    """Resolve one Lexis manifest-normalization tool by file name."""

    tool_path = (
        workspace_root()
        / "specifications"
        / "applications"
        / "lexis-spec"
        / "tools"
        / tool_name
    )
    if not tool_path.is_file():
        raise RefreshRepositoryClosureError(f"Missing Lexis tool: {tool_path}")
    return tool_path


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=default_repository_root(),
        help="Repository root directory to refresh (default: paperhat-schemas).",
    )
    parser.add_argument(
        "--max-schema-import-passes",
        type=int,
        default=DEFAULT_MAX_SCHEMA_IMPORT_PASSES,
        help=(
            "Maximum SchemaImport normalization passes before failing "
            "(default: 32)."
        ),
    )
    return parser.parse_args()


def run_python_tool(script_path: Path, *arguments: str | Path) -> CommandResult:
    """Run one Python tool and capture its result."""

    command = (
        sys.executable,
        "-B",
        str(script_path),
        *[str(argument) for argument in arguments],
    )
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
    )
    return CommandResult(
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def format_command_result(result: CommandResult) -> str:
    """Format one subprocess result for failure reporting."""

    stdout = result.stdout.strip() or "(no stdout)"
    stderr = result.stderr.strip() or "(no stderr)"
    command_text = " ".join(result.command)
    return (
        f"command: {command_text}\n"
        f"exit code: {result.returncode}\n"
        f"stdout:\n{stdout}\n"
        f"stderr:\n{stderr}"
    )


def require_success(result: CommandResult, context: str) -> None:
    """Require a zero exit status and raise a detailed error otherwise."""

    if result.returncode != 0:
        raise RefreshRepositoryClosureError(
            f"{context}\n{format_command_result(result)}"
        )


def run_schema_import_check(repository_root: Path) -> CommandResult:
    """Run the sanctioned SchemaImport drift check."""

    return run_python_tool(
        lexis_tool_path("normalize_schema_import_references.py"),
        "--check",
        "--root",
        repository_root,
    )


def run_schema_import_fix(repository_root: Path) -> CommandResult:
    """Run one sanctioned SchemaImport normalization pass."""

    return run_python_tool(
        lexis_tool_path("normalize_schema_import_references.py"),
        "--root",
        repository_root,
    )


def run_manifest_check(repository_root: Path) -> CommandResult:
    """Run the sanctioned manifest drift check."""

    return run_python_tool(
        lexis_tool_path("normalize_manifests.py"),
        "--check",
        "--root",
        repository_root,
    )


def run_manifest_fix(repository_root: Path) -> CommandResult:
    """Run the sanctioned manifest normalization pass."""

    return run_python_tool(
        lexis_tool_path("normalize_manifests.py"),
        "--root",
        repository_root,
    )


def iterate_schema_import_normalization(
    repository_root: Path,
    max_schema_import_passes: int,
) -> tuple[int, CommandResult]:
    """Iterate SchemaImport normalization until the check reaches a fixed point."""

    applied_passes = 0
    while True:
        check_result = run_schema_import_check(repository_root)
        if check_result.returncode == 0:
            return applied_passes, check_result

        if applied_passes >= max_schema_import_passes:
            raise RefreshRepositoryClosureError(
                "SchemaImport normalization did not converge before the pass limit.\n"
                f"applied passes: {applied_passes}\n"
                f"{format_command_result(check_result)}"
            )

        fix_result = run_schema_import_fix(repository_root)
        require_success(
            fix_result,
            "SchemaImport normalization pass failed.",
        )
        applied_passes += 1


def single_line_output(result: CommandResult) -> str:
    """Return one human-readable line from a command result."""

    for stream_text in [result.stdout, result.stderr]:
        stripped_text = stream_text.strip()
        if stripped_text:
            return stripped_text.splitlines()[0]
    return "(no output)"


def main() -> int:
    """Refresh repository closure state and verify it reaches zero drift."""

    arguments = parse_arguments()
    repository_root = arguments.root.resolve()
    if arguments.max_schema_import_passes < 0:
        raise RefreshRepositoryClosureError(
            "--max-schema-import-passes must be zero or greater."
        )
    if not repository_root.is_dir():
        raise RefreshRepositoryClosureError(
            f"Repository root does not exist: {repository_root}"
        )

    schema_import_passes, final_schema_import_check = iterate_schema_import_normalization(
        repository_root,
        arguments.max_schema_import_passes,
    )

    manifest_fix_result = run_manifest_fix(repository_root)
    require_success(
        manifest_fix_result,
        "Manifest normalization failed.",
    )

    verified_schema_import_check = run_schema_import_check(repository_root)
    require_success(
        verified_schema_import_check,
        "Final SchemaImport drift check failed after normalization.",
    )

    verified_manifest_check = run_manifest_check(repository_root)
    require_success(
        verified_manifest_check,
        "Final manifest drift check failed after normalization.",
    )

    print(f"Repository root: {repository_root}")
    print(f"SchemaImport normalization passes applied: {schema_import_passes}")
    print(f"Manifest normalization: {single_line_output(manifest_fix_result)}")
    print(f"SchemaImport check: {single_line_output(verified_schema_import_check)}")
    print(f"Manifest check: {single_line_output(verified_manifest_check)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RefreshRepositoryClosureError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
