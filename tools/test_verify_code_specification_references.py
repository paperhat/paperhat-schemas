#!/usr/bin/env python3
"""Automated tests for code-specification reference evidence verification."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
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
        module_spec = importlib.util.spec_from_file_location(
            "verify_code_specification_references_under_test",
            cls.tool_path,
        )
        if module_spec is None or module_spec.loader is None:
            raise AssertionError(f"Could not load verifier tool: {cls.tool_path}")
        verifier_module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_spec.name] = verifier_module
        module_spec.loader.exec_module(verifier_module)
        cls.verifier = verifier_module

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

    def run_tool_in_workspace(
        self,
        files: dict[str, str],
        *extra_arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        """Run the verifier against a temporary multi-document workspace."""

        with tempfile.TemporaryDirectory(prefix="code_reference_workspace_") as directory:
            workspace_root = Path(directory)
            for relative_path, document_text in files.items():
                document_path = workspace_root / relative_path
                document_path.parent.mkdir(parents=True, exist_ok=True)
                document_path.write_text(document_text, encoding="utf-8")
            command = [
                "python3",
                "-B",
                str(self.tool_path),
                "--workspace-root",
                str(workspace_root),
                "--schema-root",
                str(
                    self.workspace_root
                    / "schemas/paperhat-schemas/spec/1.0.0/schemas"
                ),
                *extra_arguments,
            ]
            return subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
            )

    def test_default_discovery_only_reads_current_document_roots(self) -> None:
        """Default discovery must include only the current document roots."""

        document_text = """<CodeSpecification>
\t<ProductType key=~sample name="Sample" />
</CodeSpecification>
"""

        with tempfile.TemporaryDirectory(prefix="code_reference_workspace_") as directory:
            workspace_root = Path(directory)
            for relative_path in (
                "implementations/example/included.cdx",
                "specifications/example/included.cdx",
                "schemas/paperhat-schemas/example/included.cdx",
                "archive/example/excluded.cdx",
                "project/example/excluded.cdx",
                "schemas/other-schema-repository/example/excluded.cdx",
            ):
                document_path = workspace_root / relative_path
                document_path.parent.mkdir(parents=True, exist_ok=True)
                document_path.write_text(document_text, encoding="utf-8")

            command = [
                "python3",
                "-B",
                str(self.tool_path),
                "--workspace-root",
                str(workspace_root),
                "--schema-root",
                str(
                    self.workspace_root
                    / "schemas/paperhat-schemas/spec/1.0.0/schemas"
                ),
                "--show",
                "identity",
            ]
            result = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("implementations/example/included.cdx", result.stdout)
        self.assertIn("specifications/example/included.cdx", result.stdout)
        self.assertIn("schemas/paperhat-schemas/example/included.cdx", result.stdout)
        self.assertNotIn("archive/example/excluded.cdx", result.stdout)
        self.assertNotIn("project/example/excluded.cdx", result.stdout)
        self.assertNotIn(
            "schemas/other-schema-repository/example/excluded.cdx",
            result.stdout,
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

    def test_cross_file_id_target_resolves_with_evidence(self) -> None:
        """A URN reference can resolve to an id declared in another in-scope file."""

        files = {
            "specifications/source/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/Local key=~local name="Local">
\t\t<Field key=~external name="external" valueType=urn:test#type/External />
\t</ProductType>
</CodeSpecification>
""",
            "specifications/provider/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/External key=~external name="External" />
</CodeSpecification>
""",
        }

        result = self.run_tool_in_workspace(files, "--show", "references")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("resolved_without_target_policy", result.stdout)
        self.assertIn("urn:test#type/External", result.stdout)
        self.assertIn("IRI resolves by workspace id equality", result.stdout)

    def test_cross_file_id_miss_remains_external_or_missing(self) -> None:
        """A URN with no local or workspace id candidate remains external or missing."""

        files = {
            "specifications/source/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/Local key=~local name="Local">
\t\t<Field key=~missing name="missing" valueType=urn:test#type/Missing />
\t</ProductType>
</CodeSpecification>
""",
            "specifications/provider/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/External key=~external name="External" />
</CodeSpecification>
""",
        }

        result = self.run_tool_in_workspace(files, "--show", "problems")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("external_or_missing", result.stdout)
        self.assertIn("urn:test#type/Missing", result.stdout)

    def test_cross_file_duplicate_id_is_reported(self) -> None:
        """Duplicate ids across files must surface as their own diagnostic."""

        files = {
            "specifications/first/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/Duplicate key=~first name="First" />
</CodeSpecification>
""",
            "specifications/second/spec/1.0.0/index.cdx": """<CodeSpecification>
\t<ProductType id=urn:test#type/Duplicate key=~second name="Second" />
</CodeSpecification>
""",
        }

        result = self.run_tool_in_workspace(
            files,
            "--show",
            "identity",
            "--fail-on",
            "cross_file_duplicate_id",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("cross_file_duplicate_id", result.stdout)
        self.assertIn("urn:test#type/Duplicate", result.stdout)
        self.assertIn("id values must be unique across workspace documents", result.stdout)

    def test_in_file_id_target_resolution_is_unchanged(self) -> None:
        """A local URN hit must keep using the existing per-file id evidence."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~value name="value" valueType=urn:test#type/Sample />
\t</ProductType>
</CodeSpecification>
"""

        result = self.run_tool(document_text, "--show", "references")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("resolved_without_target_policy", result.stdout)
        self.assertIn("IRI resolves by exact id equality", result.stdout)
        self.assertNotIn("IRI resolves by workspace id equality", result.stdout)

    def test_parser_indexes_ids_after_delimited_attribute_angle_brackets(self) -> None:
        """Delimited attribute values must not desynchronize element parsing."""

        document_text = """<CodeSpecification>
\t<ProductType
\t\tid=urn:test#type/LessThanTrigger
\t\tkey=~lessThanTrigger
\t\tname="LessThanTrigger"
\t\tdescription="A quoted range expression 0 <= h < 360."
\t>
\t\t<Field key=~lessThanField name="value" />
\t</ProductType>

\t<ProductType id=urn:test#type/AfterLessThan key=~afterLessThan name="AfterLessThan" />

\t<ProductType
\t\tid=urn:test#type/GreaterThanTrigger
\t\tkey=~greaterThanTrigger
\t\tname="GreaterThanTrigger"
\t\tdescription=`A backticked comparison x > y.`
\t>
\t\t<Field key=~greaterThanField name="value" />
\t</ProductType>

\t<ProductType id=urn:test#type/AfterGreaterThan key=~afterGreaterThan name="AfterGreaterThan" />

\t<ProductType
\t\tid=urn:test#type/BracketedValue
\t\tkey=~bracketedValue
\t\tname="BracketedValue"
\t\tcapabilities=[$Equality, $Hashing]
\t/>

\t<ProductType id=urn:test#type/AfterBracketed key=~afterBracketed name="AfterBracketed" />
</CodeSpecification>
"""

        elements = self.verifier.parse_elements(document_text)
        id_candidates, _ = self.verifier.index_candidates(elements)

        expected_ids = (
            "urn:test#type/LessThanTrigger",
            "urn:test#type/AfterLessThan",
            "urn:test#type/GreaterThanTrigger",
            "urn:test#type/AfterGreaterThan",
            "urn:test#type/BracketedValue",
            "urn:test#type/AfterBracketed",
        )
        for id_value in expected_ids:
            with self.subTest(id_value=id_value):
                self.assertIn(id_value, id_candidates)
                self.assertEqual(
                    id_candidates[id_value][0].path[0],
                    "CodeSpecification",
                )

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

    def test_slice_gate_passes_for_exact_declared_target(self) -> None:
        """A slice gate must pass when every row reaches one declared target."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~value name="value" />
\t</ProductType>

\t<ConstructionOperation
\t\tid=urn:test#operation/constructSample
\t\tkey=~constructSample
\t\tname="constructSample"
\t\tproducesType=urn:test#type/Sample
\t>
\t\t<OperationParameter key=~input name="input" mapsToField=~value />
\t</ConstructionOperation>
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--slice",
            "OperationParameter:mapsToField=Field",
            "--show",
            "slice",
            "--gate-slice",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OperationParameter:mapsToField", result.stdout)
        self.assertIn("resolved", result.stdout)
        self.assertIn("Field", result.stdout)

    def test_slice_gate_rejects_wrong_target_concept(self) -> None:
        """A slice gate must fail when the exact target has the wrong concept."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~value name="value" />
\t</ProductType>

\t<ConstructionOperation
\t\tid=urn:test#operation/constructSample
\t\tkey=~constructSample
\t\tname="constructSample"
\t\tproducesType=urn:test#type/Sample
\t>
\t\t<OperationParameter key=~input name="input" mapsToField=~value />
\t</ConstructionOperation>
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--slice",
            "OperationParameter:mapsToField=ValidationRule",
            "--show",
            "slice",
            "--gate-slice",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("wrong_concept", result.stdout)
        self.assertIn("SLICE_GATE_FAILED", result.stderr)

    def test_slice_gate_rejects_empty_slice(self) -> None:
        """A slice gate must fail when the configured slice inspects no rows."""

        document_text = """<CodeSpecification>
\t<ProductType id=urn:test#type/Sample key=~sample name="Sample">
\t\t<Field key=~value name="value" />
\t</ProductType>
</CodeSpecification>
"""

        result = self.run_tool(
            document_text,
            "--slice",
            "OperationParameter:mapsToField=Field",
            "--show",
            "slice",
            "--gate-slice",
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("SLICE_GATE_FAILED", result.stderr)
        self.assertIn("no reference rows inspected", result.stderr)


if __name__ == "__main__":
    unittest.main()
