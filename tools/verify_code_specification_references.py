#!/usr/bin/env python3
"""Emit deterministic reference and identity evidence for code specifications."""

from __future__ import annotations

import argparse
import collections
import dataclasses
import re
import sys
from pathlib import Path


LOOKUP_TOKEN_PATTERN = re.compile(r"^~[a-z][A-Za-z0-9]*$")
ATTRIBUTE_PATTERN = re.compile(
    r"([A-Za-z_][A-Za-z0-9_:.-]*)="
    r"(?:\"([^\"]*)\"|`([^`]*)`|(\[[^\]]*\])|([^\s>]+))",
    re.DOTALL,
)
TAG_PATTERN = re.compile(
    r"<(/?)([A-Za-z_][A-Za-z0-9_:.-]*)([^<>]*?)(/?)>",
    re.DOTALL,
)

CODE_SPECIFICATION_REFERENCE_TRAITS = frozenset(
    {
        "accessor",
        "appliesToParameter",
        "appliesToType",
        "belongsToType",
        "boundConstant",
        "compareField",
        "delegateField",
        "diagnosticType",
        "diagnosticVariant",
        "diagnosticVariants",
        "elementType",
        "expectedDiagnostic",
        "failureFamilyType",
        "forVariant",
        "grammarReference",
        "mapsToField",
        "operation",
        "parameterToCheck",
        "prohibitedConstant",
        "producesType",
        "producesVariant",
        "referencedTypeParameter",
        "returnType",
        "returnsConstant",
        "returnsField",
        "sourceLineNumberType",
        "sourceParameter",
        "specRequirement",
        "targetField",
        "validationRule",
        "valueType",
        "wrapsType",
    }
)

WORKSPACE_DOCUMENT_ROOTS = (
    "implementations",
    "schemas/paperhat-schemas",
    "specifications",
)

PROBLEM_STATUSES = frozenset(
    {
        "ambiguous",
        "duplicate_id",
        "duplicate_key",
        "external_or_missing",
        "forbidden_id",
        "invalid_lookup_token",
        "missing_id",
        "unresolved",
        "wrong_concept",
    }
)

REPORT_COLUMNS = (
    "record_type",
    "status",
    "slice",
    "file",
    "line",
    "path",
    "holder_concept",
    "trait",
    "value",
    "member",
    "target_policy",
    "candidate_count",
    "candidates",
    "evidence_rule",
)


class VerificationError(RuntimeError):
    """Raised when the verifier cannot load its authorities."""


@dataclasses.dataclass(frozen=True)
class Element:
    """One parsed Codex element start tag."""

    concept: str
    attributes: dict[str, str]
    line: int
    path: tuple[str, ...]


@dataclasses.dataclass(frozen=True)
class Candidate:
    """One local key or id candidate in a code specification."""

    concept: str
    line: int
    path: tuple[str, ...]
    id_value: str
    key_value: str
    name_value: str


@dataclasses.dataclass(frozen=True)
class ConceptDefinition:
    """Schema-derived concept identity rule."""

    concept: str
    entity_eligibility: str


@dataclasses.dataclass(frozen=True)
class SlicePolicy:
    """One explicit reference slice target policy."""

    holder_concept: str
    trait: str
    target_concepts: tuple[str, ...]

    @property
    def name(self) -> str:
        """Return the stable slice name."""

        return f"{self.holder_concept}:{self.trait}"


@dataclasses.dataclass(frozen=True)
class ReportRow:
    """One machine-readable verifier row."""

    record_type: str
    status: str
    slice_name: str
    file: str
    line: int
    path: str
    holder_concept: str
    trait: str
    value: str
    member: str
    target_policy: str
    candidate_count: int
    candidates: str
    evidence_rule: str

    def as_tsv(self) -> str:
        """Render the row as one TSV line."""

        values = [
            self.record_type,
            self.status,
            self.slice_name,
            self.file,
            str(self.line),
            self.path,
            self.holder_concept,
            self.trait,
            self.value,
            self.member,
            self.target_policy,
            str(self.candidate_count),
            self.candidates,
            self.evidence_rule,
        ]
        return "\t".join(sanitize_cell(value) for value in values)


def sanitize_cell(value: str) -> str:
    """Make one value safe for TSV output."""

    return " ".join(value.replace("\t", " ").split())


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Verify deterministic reference and identity evidence for "
            "CodeSpecification documents. The tool is read-only."
        )
    )
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=None,
        help="Paperhat workspace root. Defaults to discovery from the current directory.",
    )
    parser.add_argument(
        "--schema-root",
        type=Path,
        default=None,
        help="Schema root containing schema.cdx files.",
    )
    parser.add_argument(
        "--file",
        action="append",
        type=Path,
        default=[],
        help="Specific CodeSpecification file to inspect. Can be repeated.",
    )
    parser.add_argument(
        "--slice",
        action="append",
        default=[],
        help=(
            "Reference slice in HolderConcept:trait=TargetConcept[,TargetConcept] "
            "form. Can be repeated."
        ),
    )
    parser.add_argument(
        "--gate-slice",
        action="store_true",
        help=(
            "Fail unless every declared slice has at least one row and every "
            "selected reference row resolves to one declared target concept."
        ),
    )
    parser.add_argument(
        "--show",
        choices=("all", "identity", "problems", "references", "slice", "summary"),
        default="problems",
        help="Rows to emit.",
    )
    parser.add_argument(
        "--fail-on",
        default="",
        help=(
            "Comma-separated statuses that produce a nonzero exit. "
            "Use 'problem' for the built-in problem status set."
        ),
    )
    return parser.parse_args()


def find_workspace_root(start_path: Path) -> Path:
    """Locate the Paperhat workspace root."""

    for candidate in [start_path, *start_path.parents]:
        if (candidate / "repos.manifest").is_file() and (candidate / "CLAUDE.md").is_file():
            return candidate.resolve()
    raise VerificationError(f"Could not locate workspace root from {start_path}")


def resolve_workspace_root(explicit_workspace_root: Path | None) -> Path:
    """Resolve the workspace root from arguments or the current directory."""

    if explicit_workspace_root is not None:
        return explicit_workspace_root.resolve()
    return find_workspace_root(Path.cwd().resolve())


def resolve_schema_root(
    workspace_root: Path,
    explicit_schema_root: Path | None,
) -> Path:
    """Resolve the schema root."""

    if explicit_schema_root is not None:
        schema_root = explicit_schema_root.resolve()
    else:
        schema_root = (
            workspace_root
            / "schemas/paperhat-schemas/spec/1.0.0/schemas"
        ).resolve()
    if not schema_root.is_dir():
        raise VerificationError(f"Schema root does not exist: {schema_root}")
    return schema_root


def parse_attributes(attribute_text: str) -> dict[str, str]:
    """Parse Codex-style start tag attributes."""

    attributes: dict[str, str] = {}
    for match in ATTRIBUTE_PATTERN.finditer(attribute_text):
        value = next(group for group in match.groups()[1:] if group is not None)
        attributes[match.group(1)] = value
    return attributes


def parse_elements(text: str) -> list[Element]:
    """Parse start tags and their concept paths from a Codex document."""

    stack: list[Element] = []
    elements: list[Element] = []

    for match in TAG_PATTERN.finditer(text):
        is_closing = bool(match.group(1))
        concept = match.group(2)
        attribute_text = match.group(3)
        is_self_closing = bool(match.group(4)) or attribute_text.rstrip().endswith("/")
        line = text.count("\n", 0, match.start()) + 1

        if is_closing:
            while stack:
                popped = stack.pop()
                if popped.concept == concept:
                    break
            continue

        attributes = parse_attributes(attribute_text)
        path = tuple([element.concept for element in stack] + [concept])
        element = Element(
            concept=concept,
            attributes=attributes,
            line=line,
            path=path,
        )
        elements.append(element)

        if not is_self_closing:
            stack.append(element)

    return elements


def read_text(path: Path) -> str:
    """Read UTF-8 text."""

    return path.read_text(encoding="utf-8")


def schema_namespace(schema_elements: list[Element]) -> str:
    """Return the namespace declared by a schema document."""

    if not schema_elements or schema_elements[0].concept != "Schema":
        raise VerificationError("Schema document does not start with <Schema>")
    namespace = schema_elements[0].attributes.get("namespace")
    if namespace is None:
        raise VerificationError("Schema document is missing namespace")
    return namespace


def qualify_concept_name(namespace: str, name: str) -> str:
    """Qualify imported schema concept names the way code specifications use them."""

    if namespace == "codeSpecification":
        return name
    return f"{namespace}:{name}"


def load_concept_definitions(schema_root: Path) -> dict[str, ConceptDefinition]:
    """Load concept identity rules from schema documents."""

    definitions: dict[str, ConceptDefinition] = {}
    for schema_path in sorted(schema_root.rglob("schema.cdx")):
        elements = parse_elements(read_text(schema_path))
        if not elements or elements[0].concept != "Schema":
            continue
        namespace = schema_namespace(elements)
        for element in elements:
            if element.concept != "ConceptDefinition":
                continue
            name = element.attributes.get("name")
            entity_eligibility = element.attributes.get("entityEligibility")
            if name is None or entity_eligibility is None:
                continue
            concept = qualify_concept_name(namespace, name)
            definitions[concept] = ConceptDefinition(
                concept=concept,
                entity_eligibility=entity_eligibility,
            )
    return definitions


def load_explicit_reference_policies(
    schema_root: Path,
) -> dict[str, tuple[str, ...]]:
    """Load explicit ReferenceConstraint target policies keyed by trait name."""

    policies: dict[str, set[str]] = collections.defaultdict(set)
    for schema_path in sorted(schema_root.rglob("schema.cdx")):
        elements = parse_elements(read_text(schema_path))
        for element in elements:
            if element.concept != "ReferenceConstraint":
                continue
            trait_name = element.attributes.get("traitName")
            concept_selector = element.attributes.get("conceptSelector")
            if trait_name is None or concept_selector is None:
                continue
            policies[trait_name].add(concept_selector)
    return {
        trait_name: tuple(sorted(concepts))
        for trait_name, concepts in sorted(policies.items())
    }


def discover_code_specification_files(workspace_root: Path) -> list[Path]:
    """Find CodeSpecification documents under in-scope workspace roots."""

    ignored_parts = {
        ".git",
        "__pycache__",
        "target",
        "node_modules",
        ".venv",
    }
    files: list[Path] = []
    for root_name in WORKSPACE_DOCUMENT_ROOTS:
        document_root = workspace_root / root_name
        if not document_root.is_dir():
            continue
        for path in sorted(document_root.rglob("*.cdx")):
            relative_parts = path.resolve().relative_to(workspace_root).parts
            directory_parts = relative_parts[:-1]
            if any(
                part in ignored_parts or part.startswith(".")
                for part in directory_parts
            ):
                continue
            try:
                text = read_text(path)
            except UnicodeDecodeError:
                continue
            if re.search(r"<CodeSpecification\b", text):
                files.append(path)
    return files


def relative_path(path: Path, workspace_root: Path) -> str:
    """Return a workspace-relative path when possible."""

    try:
        return str(path.resolve().relative_to(workspace_root))
    except ValueError:
        return str(path)


def make_candidate(element: Element) -> Candidate:
    """Create a candidate record from an element."""

    return Candidate(
        concept=element.concept,
        line=element.line,
        path=element.path,
        id_value=element.attributes.get("id", ""),
        key_value=element.attributes.get("key", ""),
        name_value=element.attributes.get("name", ""),
    )


def index_candidates(
    elements: list[Element],
) -> tuple[dict[str, list[Candidate]], dict[str, list[Candidate]]]:
    """Index local id and key candidates."""

    id_candidates: dict[str, list[Candidate]] = collections.defaultdict(list)
    key_candidates: dict[str, list[Candidate]] = collections.defaultdict(list)

    for element in elements:
        candidate = make_candidate(element)
        if candidate.id_value:
            id_candidates[candidate.id_value].append(candidate)
        if candidate.key_value:
            key_candidates[candidate.key_value].append(candidate)

    return dict(id_candidates), dict(key_candidates)


def format_path(path: tuple[str, ...]) -> str:
    """Format a concept path."""

    return "/".join(path)


def format_candidate(candidate: Candidate) -> str:
    """Format a target candidate as compact evidence."""

    parts = [
        f"line={candidate.line}",
        f"concept={candidate.concept}",
        f"path={format_path(candidate.path)}",
    ]
    if candidate.id_value:
        parts.append(f"id={candidate.id_value}")
    if candidate.key_value:
        parts.append(f"key={candidate.key_value}")
    if candidate.name_value:
        parts.append(f"name={candidate.name_value}")
    return ";".join(parts)


def split_reference_members(value: str) -> tuple[str, ...]:
    """Split one reference trait value into one or more members."""

    stripped_value = value.strip()
    if stripped_value.startswith("[") and stripped_value.endswith("]"):
        inner_value = stripped_value[1:-1].strip()
        if not inner_value:
            return tuple()
        return tuple(member.strip() for member in inner_value.split(","))
    return (stripped_value,)


def target_policy_text(policy: tuple[str, ...] | None) -> str:
    """Format a target policy."""

    if policy is None:
        return "<unconfigured>"
    return ",".join(policy)


def parse_slice_policy(
    raw_value: str,
    reference_traits: frozenset[str],
    concept_definitions: dict[str, ConceptDefinition],
) -> SlicePolicy:
    """Parse one explicit slice policy."""

    if "=" not in raw_value:
        raise VerificationError(f"Slice is missing '=': {raw_value}")
    holder_and_trait, target_text = raw_value.split("=", 1)
    if ":" not in holder_and_trait:
        raise VerificationError(f"Slice is missing holder-trait separator: {raw_value}")
    holder_concept, trait = holder_and_trait.rsplit(":", 1)
    holder_concept = holder_concept.strip()
    trait = trait.strip()
    target_concepts = tuple(
        target.strip() for target in target_text.split(",") if target.strip()
    )

    if not holder_concept:
        raise VerificationError(f"Slice holder concept is empty: {raw_value}")
    if not trait:
        raise VerificationError(f"Slice trait is empty: {raw_value}")
    if trait not in reference_traits:
        raise VerificationError(f"Slice trait is not a reference trait: {trait}")
    if holder_concept not in concept_definitions:
        raise VerificationError(f"Slice holder concept is not declared: {holder_concept}")
    if not target_concepts:
        raise VerificationError(f"Slice has no target concepts: {raw_value}")
    for target_concept in target_concepts:
        if target_concept not in concept_definitions:
            raise VerificationError(
                f"Slice target concept is not declared: {target_concept}"
            )

    return SlicePolicy(
        holder_concept=holder_concept,
        trait=trait,
        target_concepts=target_concepts,
    )


def parse_slice_policies(
    raw_values: list[str],
    reference_traits: frozenset[str],
    concept_definitions: dict[str, ConceptDefinition],
) -> dict[tuple[str, str], SlicePolicy]:
    """Parse all explicit slice policies."""

    policies: dict[tuple[str, str], SlicePolicy] = {}
    for raw_value in raw_values:
        policy = parse_slice_policy(
            raw_value=raw_value,
            reference_traits=reference_traits,
            concept_definitions=concept_definitions,
        )
        key = (policy.holder_concept, policy.trait)
        if key in policies:
            raise VerificationError(f"Duplicate slice policy: {policy.name}")
        policies[key] = policy
    return policies


def classify_reference_member(
    member: str,
    policy: tuple[str, ...] | None,
    id_candidates: dict[str, list[Candidate]],
    key_candidates: dict[str, list[Candidate]],
) -> tuple[str, list[Candidate], str]:
    """Classify one reference member and return evidence."""

    if member.startswith("~"):
        if not LOOKUP_TOKEN_PATTERN.fullmatch(member):
            return "invalid_lookup_token", [], "lookup token syntax"
        candidates = key_candidates.get(member, [])
        evidence_rule = "lookup token resolves by exact key equality"
    elif member.startswith("urn:"):
        candidates = id_candidates.get(member, [])
        evidence_rule = "IRI resolves by exact id equality"
    else:
        return "invalid_reference_value", [], "reference value is not a lookup token or IRI"

    if not candidates:
        status = "external_or_missing" if member.startswith("urn:") else "unresolved"
        return status, [], evidence_rule

    if len(candidates) > 1:
        return "ambiguous", candidates, evidence_rule

    candidate = candidates[0]
    if policy is not None and candidate.concept not in policy:
        return "wrong_concept", candidates, evidence_rule

    if policy is None:
        return "resolved_without_target_policy", candidates, evidence_rule
    return "resolved", candidates, evidence_rule


def reference_rows_for_file(
    file_path: Path,
    workspace_root: Path,
    elements: list[Element],
    reference_traits: frozenset[str],
    policies: dict[str, tuple[str, ...]],
    slice_policies: dict[tuple[str, str], SlicePolicy],
) -> list[ReportRow]:
    """Build reference evidence rows for one file."""

    id_candidates, key_candidates = index_candidates(elements)
    rows: list[ReportRow] = []
    file_text = relative_path(file_path, workspace_root)

    for element in elements:
        for trait_name, value in sorted(element.attributes.items()):
            if trait_name not in reference_traits:
                continue
            members = split_reference_members(value)
            slice_policy = slice_policies.get((element.concept, trait_name))
            if slice_policy is None:
                policy = policies.get(trait_name)
                slice_name = ""
            else:
                policy = slice_policy.target_concepts
                slice_name = slice_policy.name
            if not members:
                rows.append(
                    ReportRow(
                        record_type="reference",
                        status="unresolved",
                        slice_name=slice_name,
                        file=file_text,
                        line=element.line,
                        path=format_path(element.path),
                        holder_concept=element.concept,
                        trait=trait_name,
                        value=value,
                        member="",
                        target_policy=target_policy_text(policy),
                        candidate_count=0,
                        candidates="",
                        evidence_rule="empty reference list has no target",
                    )
                )
                continue
            for member in members:
                status, candidates, evidence_rule = classify_reference_member(
                    member=member,
                    policy=policy,
                    id_candidates=id_candidates,
                    key_candidates=key_candidates,
                )
                rows.append(
                    ReportRow(
                        record_type="reference",
                        status=status,
                        slice_name=slice_name,
                        file=file_text,
                        line=element.line,
                        path=format_path(element.path),
                        holder_concept=element.concept,
                        trait=trait_name,
                        value=value,
                        member=member,
                        target_policy=target_policy_text(policy),
                        candidate_count=len(candidates),
                        candidates=" | ".join(
                            format_candidate(candidate) for candidate in candidates
                        ),
                        evidence_rule=evidence_rule,
                    )
                )

    return rows


def duplicate_rows_for_file(
    file_path: Path,
    workspace_root: Path,
    candidates: dict[str, list[Candidate]],
    candidate_kind: str,
) -> list[ReportRow]:
    """Build duplicate id or key rows."""

    rows: list[ReportRow] = []
    file_text = relative_path(file_path, workspace_root)
    status = f"duplicate_{candidate_kind}"
    for value, duplicate_candidates in sorted(candidates.items()):
        if len(duplicate_candidates) < 2:
            continue
        first_candidate = duplicate_candidates[0]
        rows.append(
            ReportRow(
                record_type="identity",
                status=status,
                slice_name="",
                file=file_text,
                line=first_candidate.line,
                path=format_path(first_candidate.path),
                holder_concept=first_candidate.concept,
                trait=candidate_kind,
                value=value,
                member=value,
                target_policy="<not-applicable>",
                candidate_count=len(duplicate_candidates),
                candidates=" | ".join(
                    format_candidate(candidate) for candidate in duplicate_candidates
                ),
                evidence_rule=f"{candidate_kind} values must be unique in a document",
            )
        )
    return rows


def identity_rows_for_file(
    file_path: Path,
    workspace_root: Path,
    elements: list[Element],
    concept_definitions: dict[str, ConceptDefinition],
) -> list[ReportRow]:
    """Build identity evidence rows for one file."""

    id_candidates, key_candidates = index_candidates(elements)
    rows = [
        *duplicate_rows_for_file(file_path, workspace_root, id_candidates, "id"),
        *duplicate_rows_for_file(file_path, workspace_root, key_candidates, "key"),
    ]
    file_text = relative_path(file_path, workspace_root)

    for element in elements:
        definition = concept_definitions.get(element.concept)
        if definition is None:
            continue
        has_id = "id" in element.attributes
        if definition.entity_eligibility == "$MustBeEntity" and not has_id:
            rows.append(
                ReportRow(
                    record_type="identity",
                    status="missing_id",
                    slice_name="",
                    file=file_text,
                    line=element.line,
                    path=format_path(element.path),
                    holder_concept=element.concept,
                    trait="id",
                    value="",
                    member="",
                    target_policy="<not-applicable>",
                    candidate_count=0,
                    candidates="",
                    evidence_rule="$MustBeEntity concept has no id attribute",
                )
            )
        elif definition.entity_eligibility == "$MustNotBeEntity" and has_id:
            rows.append(
                ReportRow(
                    record_type="identity",
                    status="forbidden_id",
                    slice_name="",
                    file=file_text,
                    line=element.line,
                    path=format_path(element.path),
                    holder_concept=element.concept,
                    trait="id",
                    value=element.attributes.get("id", ""),
                    member=element.attributes.get("id", ""),
                    target_policy="<not-applicable>",
                    candidate_count=0,
                    candidates="",
                    evidence_rule="$MustNotBeEntity concept has an id attribute",
                )
            )

    return rows


def rows_for_file(
    file_path: Path,
    workspace_root: Path,
    concept_definitions: dict[str, ConceptDefinition],
    reference_traits: frozenset[str],
    policies: dict[str, tuple[str, ...]],
    slice_policies: dict[tuple[str, str], SlicePolicy],
) -> list[ReportRow]:
    """Build all verifier rows for one file."""

    elements = parse_elements(read_text(file_path))
    if not elements or elements[0].concept != "CodeSpecification":
        return []
    return [
        *identity_rows_for_file(
            file_path=file_path,
            workspace_root=workspace_root,
            elements=elements,
            concept_definitions=concept_definitions,
        ),
        *reference_rows_for_file(
            file_path=file_path,
            workspace_root=workspace_root,
            elements=elements,
            reference_traits=reference_traits,
            policies=policies,
            slice_policies=slice_policies,
        ),
    ]


def parse_fail_on(value: str) -> frozenset[str]:
    """Parse statuses that force a nonzero exit."""

    if not value.strip():
        return frozenset()
    statuses: set[str] = set()
    for raw_status in value.split(","):
        status = raw_status.strip()
        if not status:
            continue
        if status == "problem":
            statuses.update(PROBLEM_STATUSES)
        else:
            statuses.add(status)
    return frozenset(statuses)


def filter_rows(rows: list[ReportRow], show: str) -> list[ReportRow]:
    """Apply output filtering."""

    if show == "all":
        return rows
    if show == "identity":
        return [row for row in rows if row.record_type == "identity"]
    if show == "references":
        return [row for row in rows if row.record_type == "reference"]
    if show == "slice":
        return [row for row in rows if row.slice_name]
    if show == "problems":
        return [row for row in rows if row.status in PROBLEM_STATUSES]
    if show == "summary":
        return []
    raise VerificationError(f"Unsupported show mode: {show}")


def slice_gate_failures(
    rows: list[ReportRow],
    slice_policies: dict[tuple[str, str], SlicePolicy],
) -> list[str]:
    """Return slice gate failure messages."""

    failures: list[str] = []
    if not slice_policies:
        return ["no slice policies were declared"]

    rows_by_slice: dict[str, list[ReportRow]] = collections.defaultdict(list)
    for row in rows:
        if row.slice_name:
            rows_by_slice[row.slice_name].append(row)

    for policy in slice_policies.values():
        slice_rows = rows_by_slice.get(policy.name, [])
        if not slice_rows:
            failures.append(f"{policy.name}: no reference rows inspected")
            continue
        for row in slice_rows:
            if row.status != "resolved":
                failures.append(
                    f"{policy.name}: {row.file}:{row.line} {row.trait} "
                    f"{row.member} status={row.status}"
                )

    return failures


def emit_slice_gate_failures(failures: list[str]) -> None:
    """Emit slice gate failures to standard error."""

    for failure in failures:
        print(f"SLICE_GATE_FAILED\t{failure}", file=sys.stderr)


def emit_rows(rows: list[ReportRow]) -> None:
    """Emit TSV rows."""

    print("\t".join(REPORT_COLUMNS))
    for row in rows:
        print(row.as_tsv())


def emit_summary(rows: list[ReportRow]) -> None:
    """Emit status counts."""

    status_counts = collections.Counter(row.status for row in rows)
    record_counts = collections.Counter(row.record_type for row in rows)
    for record_type, count in sorted(record_counts.items()):
        print(f"SUMMARY\trecord_type\t{record_type}\t{count}")
    for status, count in sorted(status_counts.items()):
        print(f"SUMMARY\tstatus\t{status}\t{count}")


def main() -> int:
    """Run the verifier."""

    arguments = parse_arguments()
    workspace_root = resolve_workspace_root(arguments.workspace_root)
    schema_root = resolve_schema_root(workspace_root, arguments.schema_root)
    concept_definitions = load_concept_definitions(schema_root)
    policies = load_explicit_reference_policies(schema_root)
    reference_traits = frozenset(
        sorted(CODE_SPECIFICATION_REFERENCE_TRAITS | frozenset(policies))
    )
    slice_policies = parse_slice_policies(
        raw_values=arguments.slice,
        reference_traits=reference_traits,
        concept_definitions=concept_definitions,
    )

    if arguments.file:
        files = [path.resolve() for path in arguments.file]
    else:
        files = discover_code_specification_files(workspace_root)

    all_rows: list[ReportRow] = []
    for file_path in files:
        all_rows.extend(
            rows_for_file(
                file_path=file_path,
                workspace_root=workspace_root,
                concept_definitions=concept_definitions,
                reference_traits=reference_traits,
                policies=policies,
                slice_policies=slice_policies,
            )
        )

    if arguments.show == "summary":
        emit_summary(all_rows)
    else:
        emit_rows(filter_rows(all_rows, arguments.show))

    fail_on_statuses = parse_fail_on(arguments.fail_on)
    if any(row.status in fail_on_statuses for row in all_rows):
        return 1
    if arguments.gate_slice:
        failures = slice_gate_failures(all_rows, slice_policies)
        if failures:
            emit_slice_gate_failures(failures)
            return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
