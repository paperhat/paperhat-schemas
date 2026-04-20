#!/usr/bin/env python3
"""Automated tests for schema package closure verification tooling."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class VerifySchemaPackageClosureTest(unittest.TestCase):
    """End-to-end tests for the closure verifier CLI."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace_root = Path(__file__).resolve().parents[3]
        cls.tool_path = (
            cls.workspace_root
            / "schemas/paperhat-schemas/tools/verify_schema_package_closure.py"
        )
        cls.codex_binary = (
            cls.workspace_root
            / "implementations/languages/codex/target/release/codex"
        )
        cls.description_package = (
            cls.workspace_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description"
        )

        if not cls.tool_path.is_file():
            raise AssertionError(f"Missing verifier tool: {cls.tool_path}")
        if not cls.codex_binary.is_file():
            raise AssertionError(f"Missing Codex binary: {cls.codex_binary}")
        if not cls.description_package.is_dir():
            raise AssertionError(
                f"Missing description package: {cls.description_package}"
            )

    def run_tool(self, *arguments: str | Path) -> subprocess.CompletedProcess[str]:
        """Run the verifier CLI and capture its output."""

        command = [
            "python3",
            "-B",
            str(self.tool_path),
            "--codex-binary",
            str(self.codex_binary),
            *[str(argument) for argument in arguments],
        ]
        return subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )

    def make_temp_workspace(self) -> Path:
        """Create a minimal temporary workspace for closure-tool testing."""

        temporary_root = Path(tempfile.mkdtemp(prefix="schema_closure_test_"))
        (temporary_root / "repos.manifest").write_text("", encoding="utf-8")
        (temporary_root / "CLAUDE.md").write_text("", encoding="utf-8")

        schemas_root = temporary_root / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain"
        schemas_root.mkdir(parents=True, exist_ok=True)

        for package_name in ["description", "text", "list"]:
            shutil.copytree(
                self.workspace_root
                / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain"
                / package_name,
                schemas_root / package_name,
            )

        self.addCleanup(shutil.rmtree, temporary_root)
        return temporary_root

    def test_description_package_matches_real_manifest(self) -> None:
        """The unchanged description package must verify cleanly."""

        result = self.run_tool(self.description_package)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("status: MATCH", result.stdout)
        self.assertIn(
            "stored closureHash:   1d52385bd993afa202cdda224e86fce0da4a104de6bbf26a1910b5d74cc7b04c",
            result.stdout,
        )

    def test_write_manifest_repairs_stale_root_closure_hash(self) -> None:
        """Write mode must repair a stale root manifest closure hash."""

        temporary_root = self.make_temp_workspace()
        manifest_path = (
            temporary_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description/manifest.cdx"
        )
        original_manifest_text = manifest_path.read_text(encoding="utf-8")
        stale_manifest_text = original_manifest_text.replace(
            'closureHash="1d52385bd993afa202cdda224e86fce0da4a104de6bbf26a1910b5d74cc7b04c"',
            'closureHash="0000000000000000000000000000000000000000000000000000000000000000"',
            1,
        )
        manifest_path.write_text(stale_manifest_text, encoding="utf-8")

        update_result = self.run_tool(
            "--write-manifest",
            temporary_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description",
        )
        reread_manifest_text = manifest_path.read_text(encoding="utf-8")
        verify_result = self.run_tool(
            temporary_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description",
        )

        self.assertEqual(update_result.returncode, 0, update_result.stderr)
        self.assertIn("status: UPDATED", update_result.stdout)
        self.assertIn(
            'closureHash="1d52385bd993afa202cdda224e86fce0da4a104de6bbf26a1910b5d74cc7b04c"',
            reread_manifest_text,
        )
        self.assertEqual(verify_result.returncode, 0, verify_result.stderr)
        self.assertIn("status: MATCH", verify_result.stdout)

    def test_package_dependency_hash_mismatch_is_rejected(self) -> None:
        """Bad PackageDependency closure hashes must fail verification."""

        temporary_root = self.make_temp_workspace()
        manifest_path = (
            temporary_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description/manifest.cdx"
        )
        manifest_text = manifest_path.read_text(encoding="utf-8")
        broken_manifest_text = manifest_text.replace(
            'closureHash="cd2819edcdfd0f1f6506ced617b55588e882dad2c30665ede6355cd9b9b3a805"',
            'closureHash="ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"',
            1,
        )
        manifest_path.write_text(broken_manifest_text, encoding="utf-8")

        result = self.run_tool(
            temporary_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas/domain/description",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn(
            "PackageDependency closureHash does not match the imported package manifest",
            result.stderr,
        )


if __name__ == "__main__":
    unittest.main()
