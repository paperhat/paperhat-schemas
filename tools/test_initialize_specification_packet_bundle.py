#!/usr/bin/env python3
"""Automated tests for packet-bundle initialization."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class InitializeSpecificationPacketBundleTest(unittest.TestCase):
    """End-to-end tests for the packet-bundle scaffold tool."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace_root = Path(__file__).resolve().parents[3]
        cls.tool_path = (
            cls.workspace_root
            / "schemas/paperhat-schemas/tools/initialize_specification_packet_bundle.py"
        )
        cls.codex_binary = (
            cls.workspace_root
            / "implementations/languages/codex/target/debug/codex"
        )

        for required_path in [cls.tool_path, cls.codex_binary]:
            if not required_path.is_file():
                raise AssertionError(f"Missing required test path: {required_path}")

    def make_temporary_directory(self) -> Path:
        """Create a temporary directory for bundle initialization."""

        directory_path = Path(
            tempfile.mkdtemp(prefix="initialize_specification_packet_bundle_")
        )
        self.addCleanup(shutil.rmtree, directory_path)
        return directory_path

    def run_tool(
        self,
        *arguments: str | Path,
    ) -> subprocess.CompletedProcess[str]:
        """Run the scaffold tool and capture text output."""

        command = [
            "python3",
            "-B",
            str(self.tool_path),
            *[str(argument) for argument in arguments],
        ]
        return subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
        )

    def canonicalize(self, document_path: Path) -> subprocess.CompletedProcess[str]:
        """Canonicalize one generated Codex document through the real Codex CLI."""

        return subprocess.run(
            [str(self.codex_binary), "canonicalize", str(document_path)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_initialize_packet_bundle_creates_parseable_registry_and_packet(self) -> None:
        """The tool must create one minimal parseable packet bundle."""

        output_root = self.make_temporary_directory() / "bundle"

        result = self.run_tool(
            "--output-root",
            output_root,
            "--packet-id",
            "rdf-001",
            "--target-specification",
            "paperhat-rdf",
            "--owner-section",
            "Section 4.2 IRI lowering",
            "--constructs",
            "IriNode; CanonicalOrderingRule",
        )

        registry_path = output_root / "packet-registry.cdx"
        packet_path = output_root / "packets/rdf-001.cdx"
        registry_text = registry_path.read_text(encoding="utf-8")
        packet_text = packet_path.read_text(encoding="utf-8")
        registry_canonicalize_result = self.canonicalize(registry_path)
        packet_canonicalize_result = self.canonicalize(packet_path)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Initialized packet bundle:", result.stdout)
        self.assertTrue(registry_path.is_file())
        self.assertTrue(packet_path.is_file())
        self.assertIn('packetId="rdf-001"', registry_text)
        self.assertIn('packetDocumentReference="packets/rdf-001.cdx"', registry_text)
        self.assertIn('constructs="IriNode; CanonicalOrderingRule"', registry_text)
        self.assertIn('packetId="rdf-001"', packet_text)
        self.assertIn('ownerSection="Section 4.2 IRI lowering"', packet_text)
        self.assertEqual(
            registry_canonicalize_result.returncode,
            0,
            registry_canonicalize_result.stderr,
        )
        self.assertEqual(
            packet_canonicalize_result.returncode,
            0,
            packet_canonicalize_result.stderr,
        )

    def test_initialize_packet_bundle_rejects_nonempty_output_directory(self) -> None:
        """The tool must refuse to write into a nonempty directory."""

        output_root = self.make_temporary_directory()
        existing_path = output_root / "existing.txt"
        existing_path.write_text("occupied\n", encoding="utf-8")

        result = self.run_tool(
            "--output-root",
            output_root,
            "--packet-id",
            "rdf-001",
            "--target-specification",
            "paperhat-rdf",
            "--owner-section",
            "Section 4.2 IRI lowering",
            "--constructs",
            "IriNode; CanonicalOrderingRule",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("output root must be empty", result.stderr)

    def test_initialize_packet_bundle_rejects_unsafe_attribute_text(self) -> None:
        """The tool must reject quoted attribute text instead of emitting invalid Codex."""

        output_root = self.make_temporary_directory() / "bundle"

        result = self.run_tool(
            "--output-root",
            output_root,
            "--packet-id",
            "rdf-001",
            "--target-specification",
            "paperhat-rdf",
            "--owner-section",
            'Section "4.2" IRI lowering',
            "--constructs",
            "IriNode; CanonicalOrderingRule",
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("owner section must not contain double quotes", result.stderr)


if __name__ == "__main__":
    unittest.main()
