#!/usr/bin/env python3
"""Automated tests for code-specification reference evidence verification."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


class VerifyCodeSpecificationReferencesTest(unittest.TestCase):
    """End-to-end tests for the reference verifier command-line interface."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace_root = Path(__file__).resolve().parents[3]
        cls.tool_path = (
            cls.workspace_root
            / "schemas/paperhat-schemas/tools/verify_code_specification_references.py"
        )
        if not cls.tool_path.is_file():
            raise AssertionError(f"Missing verifier tool: {cls.tool_path}")

    def run_tool(
        self,
        document_text: str,
        *extra_arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        """Run the verifier against one temporary CodeSpecification document."""

        with tempfile.TemporaryDirectory(prefix="code_reference_verifier_") as directory:
            document_path = Path(directory) / "example.cdx"
            document_path.write_text(document_text, encoding="utf-8")
            command = [
                "python3",
                "-B",
                str(self.tool_path),
                "--workspace-root",
                str(self.workspace_root),
                "--file",
                str(document_path),
                *extra_arguments,
            ]
            return subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_single_lookup_token_target_resolves_with_evidence(self) -> None:
        """A reference with exactly one matching key must resolve mechanically."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~value name="value" />
\t</ProductType>

\t<ValidationRule
\t\tid=urn:test#validation/nonEmpty
\t\tkey=~nonEmpty
\t\tname="nonEmpty"
\t\tappliesToType=urn:test#type/Sample
\t/>

\t<ConstructionOperation
\t\tid=urn:test#operation/constructSample
\t\tkey=~constructSample
\t\tname="constructSample"
\t\tproducesType=urn:test#type/Sample
\t>
\t\t<OperationParameter key=~input name="input" mapsToField=~value />
\t\t<Precondition validationRule=~nonEmpty appliesToParameter=~input />
\t</ConstructionOperation>
</CodeSpecification>
"""

        result = self.run_tool(document_text, "--show", "references")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("resolved_without_target_policy", result.stdout)
        self.assertIn("lookup token resolves by exact key equality", result.stdout)
        self.assertIn("line=", result.stdout)

    def test_duplicate_key_makes_reference_ambiguous(self) -> None:
        """Duplicate keys must prevent deterministic reference resolution."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~input name="value" />
\t</ProductType>

\t<ConstructionOperation
\t\tid=urn:test#operation/constructSample
\t\tkey=~constructSample
\t\tname="constructSample"
\t\tproducesType=urn:test#type/Sample
\t>
\t\t<OperationParameter key=~input name="input" />
\t\t<Precondition appliesToParameter=~input />
\t</ConstructionOperation>
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--show",
            "problems",
            "--fail-on",
            "ambiguous,duplicate_key",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate_key", result.stdout)
        self.assertIn("ambiguous", result.stdout)
        self.assertIn("key values must be unique in a document", result.stdout)

    def test_entity_identity_rules_are_reported(self) -> None:
        """Missing and forbidden id attributes must be reported from schema rules."""

        document_text = """<CodeSpecification>
\t<grammar:Grammar key=~surfaceGrammar notation=$Custom>
\t\t<grammar:ProductionRule key=~surfaceRule ruleName="surface">
\t\t\tsurface ::= value
\t\t</grammar:ProductionRule>
\t</grammar:Grammar>

\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field id=urn:test#field/value key=~value name="value" />
\t</ProductType>
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--show",
            "identity",
            "--fail-on",
            "missing_id,forbidden_id",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("missing_id", result.stdout)
        self.assertIn("$MustBeEntity concept has no id attribute", result.stdout)
        self.assertIn("forbidden_id", result.stdout)
        self.assertIn("$MustNotBeEntity concept has an id attribute", result.stdout)

    def test_invalid_lookup_token_can_fail_the_gate(self) -> None:
        """Invalid lookup-token spelling must be gateable."""

        document_text = """<CodeSpecification>
\t<ConstructionTestCase testName="case" operation=~NotLowercase />
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--show",
            "problems",
            "--fail-on",
            "invalid_lookup_token",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid_lookup_token", result.stdout)
        self.assertIn("lookup token syntax", result.stdout)


if __name__ == "__main__":
    unittest.main()
