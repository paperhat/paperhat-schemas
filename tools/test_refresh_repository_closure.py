#!/usr/bin/env python3
"""Automated tests for the repository closure refresh tool."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ZERO_HASH = "0" * 64


class RefreshRepositoryClosureTest(unittest.TestCase):
    """End-to-end tests for repository closure refresh orchestration."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace_root = Path(__file__).resolve().parents[3]
        cls.tool_path = (
            cls.workspace_root
            / "schemas/paperhat-schemas/tools/refresh_repository_closure.py"
        )
        cls.import_check_tool = (
            cls.workspace_root
            / "specifications/applications/lexis-spec/tools/normalize_schema_import_references.py"
        )
        cls.manifest_check_tool = (
            cls.workspace_root
            / "specifications/applications/lexis-spec/tools/normalize_manifests.py"
        )
        cls.codex_binary = (
            cls.workspace_root
            / "implementations/languages/codex/target/debug/codex"
        )

        for required_path in [
            cls.tool_path,
            cls.import_check_tool,
            cls.manifest_check_tool,
            cls.codex_binary,
        ]:
            if not required_path.is_file():
                raise AssertionError(f"Missing required test path: {required_path}")

    def canonical_document_hash(self, document_path: Path) -> str:
        """Compute the canonical document hash through the real Codex CLI."""

        result = subprocess.run(
            [str(self.codex_binary), "canonicalize", str(document_path)],
            check=False,
            capture_output=True,
        )
        if result.returncode != 0:
            stderr = result.stderr.decode("utf-8", errors="replace").strip()
            raise AssertionError(
                f"Codex canonicalize failed for {document_path}: {stderr}"
            )
        return hashlib.sha256(result.stdout).hexdigest()

    def run_python_tool(
        self,
        tool_path: Path,
        *arguments: str | Path,
    ) -> subprocess.CompletedProcess[str]:
        """Run one Python tool and capture text output."""

        command = [
            "python3",
            "-B",
            str(tool_path),
            *[str(argument) for argument in arguments],
        ]
        return subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )

    def write_text(self, path: Path, text: str) -> None:
        """Write one UTF-8 file, creating parent directories first."""

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def make_repository_root(self) -> Path:
        """Create a temporary repository root for testing."""

        repository_root = Path(tempfile.mkdtemp(prefix="refresh_repository_closure_"))
        self.addCleanup(shutil.rmtree, repository_root)
        return repository_root

    def write_leaf_package(
        self,
        repository_root: Path,
        package_directory_name: str,
        package_name: str,
        schema_text: str,
    ) -> None:
        """Write one leaf package with a stale manifest closure hash."""

        package_root = (
            repository_root
            / "spec/1.0.0/schemas/domain"
            / package_directory_name
        )
        self.write_text(package_root / "schema.cdx", schema_text)
        self.write_text(
            package_root / "manifest.cdx",
            "\n".join(
                [
                    "<DomainPackageManifest",
                    '\tauthor="Test"',
                    f'\tclosureHash="{ZERO_HASH}"',
                    '\tcopyright="Copyright 2026 Test"',
                    f'\tdescription="{package_name}"',
                    '\tlicense="Apache-2.0"',
                    f'\tpackageName="{package_name}"',
                    '\tpackageVersion="1.0.0"',
                    '\tprimaryDocument="schema.cdx"',
                    '\trequiredCodexVersion=">=1.0.0 <2.0.0"',
                    '\trequiredLexisVersion=">=1.0.0 <2.0.0"',
                    "/>",
                    "",
                ]
            ),
        )

    def write_dependent_package(
        self,
        repository_root: Path,
        package_directory_name: str,
        package_name: str,
        dependency_name: str,
        schema_text: str,
    ) -> None:
        """Write one dependent package with stale dependency closure hashes."""

        package_root = (
            repository_root
            / "spec/1.0.0/schemas/domain"
            / package_directory_name
        )
        self.write_text(package_root / "schema.cdx", schema_text)
        self.write_text(
            package_root / "manifest.cdx",
            "\n".join(
                [
                    "<DomainPackageManifest",
                    '\tauthor="Test"',
                    f'\tclosureHash="{ZERO_HASH}"',
                    '\tcopyright="Copyright 2026 Test"',
                    f'\tdescription="{package_name}"',
                    '\tlicense="Apache-2.0"',
                    f'\tpackageName="{package_name}"',
                    '\tpackageVersion="1.0.0"',
                    '\tprimaryDocument="schema.cdx"',
                    '\trequiredCodexVersion=">=1.0.0 <2.0.0"',
                    '\trequiredLexisVersion=">=1.0.0 <2.0.0"',
                    ">",
                    "\t<PackageDependency",
                    f'\t\tpackageName="{dependency_name}"',
                    f'\t\tclosureHash="{ZERO_HASH}"',
                    '\t\tversionRange=">=1.0.0 <2.0.0"',
                    "\t/>",
                    "</DomainPackageManifest>",
                    "",
                ]
            ),
        )

    def write_root_manifest(self, repository_root: Path) -> None:
        """Write a root repository manifest with a stale closure hash."""

        self.write_text(
            repository_root / "manifest.cdx",
            "\n".join(
                [
                    "<LexisRepositoryManifest",
                    '\tauthor="Test"',
                    f'\tclosureHash="{ZERO_HASH}"',
                    '\tcopyright="Copyright 2026 Test"',
                    '\tdescription="Test repository"',
                    '\tlicense="Apache-2.0"',
                    '\trepositoryName="test-repository"',
                    '\trepositoryVersion="1.0.0"',
                    '\trequiredCodexVersion=">=1.0.0 <2.0.0"',
                    '\trequiredLexisVersion=">=1.0.0 <2.0.0"',
                    ">",
                    '\t<RepositoryPackageEntry packageFamily="domain" packageName="test-package-a" packagePath="spec/1.0.0/schemas/domain/package-a" />',
                    "",
                    '\t<RepositoryPackageEntry packageFamily="domain" packageName="test-package-b" packagePath="spec/1.0.0/schemas/domain/package-b" />',
                    "",
                    '\t<RepositoryPackageEntry packageFamily="domain" packageName="test-package-c" packagePath="spec/1.0.0/schemas/domain/package-c" />',
                    "</LexisRepositoryManifest>",
                    "",
                ]
            ),
        )

    def make_two_pass_repository(self) -> Path:
        """Create a repository that requires two SchemaImport normalization passes."""

        repository_root = self.make_repository_root()

        package_a_root = repository_root / "spec/1.0.0/schemas/domain/package-a"
        package_b_root = repository_root / "spec/1.0.0/schemas/domain/package-b"
        package_c_root = repository_root / "spec/1.0.0/schemas/domain/package-c"

        package_a_original_text = "\n".join(
            [
                "<Schema",
                '\tauthoringMode=$SimplifiedMode',
                '\tcompatibilityClass=$Initial',
                '\tdescription="Package A original."',
                "\tid=urn:test:package-a",
                '\tnamespace="a"',
                '\ttitle="Package A"',
                '\tversion="1.0.0"',
                '\tversionScheme=$SemanticVersion',
                "/>",
                "",
            ]
        )
        self.write_text(package_a_root / "schema.cdx", package_a_original_text)
        package_a_original_hash = self.canonical_document_hash(
            package_a_root / "schema.cdx"
        )

        package_a_current_text = package_a_original_text.replace(
            "Package A original.",
            "Package A current.",
        )
        self.write_leaf_package(
            repository_root=repository_root,
            package_directory_name="package-a",
            package_name="test-package-a",
            schema_text=package_a_current_text,
        )

        package_b_schema_text = "\n".join(
            [
                "<Schema",
                '\tauthoringMode=$SimplifiedMode',
                '\tcompatibilityClass=$Initial',
                '\tdescription="Package B."',
                "\tid=urn:test:package-b",
                '\tnamespace="b"',
                '\ttitle="Package B"',
                '\tversion="1.0.0"',
                '\tversionScheme=$SemanticVersion',
                ">",
                "\t<SchemaImports>",
                f"\t\t<SchemaImport namespace=\"a\" reference=urn:cdx:sha256:{package_a_original_hash} />",
                "\t</SchemaImports>",
                "</Schema>",
                "",
            ]
        )
        self.write_dependent_package(
            repository_root=repository_root,
            package_directory_name="package-b",
            package_name="test-package-b",
            dependency_name="test-package-a",
            schema_text=package_b_schema_text,
        )
        package_b_original_hash = self.canonical_document_hash(
            package_b_root / "schema.cdx"
        )

        package_c_schema_text = "\n".join(
            [
                "<Schema",
                '\tauthoringMode=$SimplifiedMode',
                '\tcompatibilityClass=$Initial',
                '\tdescription="Package C."',
                "\tid=urn:test:package-c",
                '\tnamespace="c"',
                '\ttitle="Package C"',
                '\tversion="1.0.0"',
                '\tversionScheme=$SemanticVersion',
                ">",
                "\t<SchemaImports>",
                f"\t\t<SchemaImport namespace=\"b\" reference=urn:cdx:sha256:{package_b_original_hash} />",
                "\t</SchemaImports>",
                "</Schema>",
                "",
            ]
        )
        self.write_dependent_package(
            repository_root=repository_root,
            package_directory_name="package-c",
            package_name="test-package-c",
            dependency_name="test-package-b",
            schema_text=package_c_schema_text,
        )

        self.write_root_manifest(repository_root)
        return repository_root

    def test_refresh_repository_closure_converges_multi_pass_import_drift(self) -> None:
        """The wrapper must iterate SchemaImport normalization to a fixed point."""

        repository_root = self.make_two_pass_repository()

        result = self.run_python_tool(
            self.tool_path,
            "--root",
            repository_root,
            "--max-schema-import-passes",
            "4",
        )
        import_check_result = self.run_python_tool(
            self.import_check_tool,
            "--check",
            "--root",
            repository_root,
        )
        manifest_check_result = self.run_python_tool(
            self.manifest_check_tool,
            "--check",
            "--root",
            repository_root,
        )
        root_manifest_text = (repository_root / "manifest.cdx").read_text(
            encoding="utf-8"
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "SchemaImport normalization passes applied: 2",
            result.stdout,
        )
        self.assertIn(
            "SchemaImport check: No SchemaImport reference drift detected.",
            result.stdout,
        )
        self.assertIn(
            "Manifest check: No manifest normalization drift detected.",
            result.stdout,
        )
        self.assertEqual(import_check_result.returncode, 0, import_check_result.stderr)
        self.assertEqual(
            manifest_check_result.returncode,
            0,
            manifest_check_result.stderr,
        )
        self.assertNotIn(f'closureHash="{ZERO_HASH}"', root_manifest_text)


if __name__ == "__main__":
    unittest.main()
