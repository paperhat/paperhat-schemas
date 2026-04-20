#!/usr/bin/env python3
"""Verify a schema package manifest closure hash against its primary document."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

MERKLE_NODE_TAG = b"CDX-MERKLE-NODE\0"
MERKLE_CLOSURE_TAG = b"CDX-MERKLE-CLOSURE\0"
CONTENT_HASH_URN_PREFIX = "urn:cdx:sha256:"
HEX_PATTERN = re.compile(r"^[0-9a-f]{64}$")


class VerificationError(RuntimeError):
    """Raised when closure verification cannot proceed or fails."""


@dataclass(frozen=True)
class PrimaryDocumentRecord:
    """Resolved primary document for a schema package."""

    document_hash: str
    manifest_path: Path
    primary_document_path: Path


@dataclass(frozen=True)
class TraceRecord:
    """Computed Merkle data for one visited document."""

    document_path: Path
    document_hash: str
    node_hash: str
    import_references: tuple[str, ...]


@dataclass(frozen=True)
class PackageDependencyRecord:
    """Declared package dependency from a package manifest."""

    package_name: str
    closure_hash: str


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Verify a schema package manifest closureHash against the Merkle closure "
            "of its primaryDocument and transitive SchemaImport graph."
        )
    )
    parser.add_argument(
        "target",
        type=Path,
        help="Path to a schema package directory or its manifest.cdx file.",
    )
    parser.add_argument(
        "--codex-binary",
        type=Path,
        default=None,
        help="Path to the Codex CLI binary used for canonicalize and identity.",
    )
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="Rewrite the root manifest closureHash after successful verification.",
    )
    return parser.parse_args()


def find_workspace_root(start_path: Path) -> Path:
    """Locate the Paperhat workspace root."""

    for candidate in [start_path, *start_path.parents]:
        if (candidate / "repos.manifest").is_file() and (candidate / "CLAUDE.md").is_file():
            return candidate
    raise VerificationError(
        f"Could not locate the Paperhat workspace root from {start_path}"
    )


def resolve_codex_binary(workspace_root: Path, explicit_path: Path | None) -> Path:
    """Resolve the Codex CLI binary path."""

    if explicit_path is not None:
        if explicit_path.is_file():
            return explicit_path
        raise VerificationError(f"Codex binary does not exist: {explicit_path}")

    candidate_paths = [
        workspace_root / "implementations/languages/codex/target/release/codex",
        workspace_root / "implementations/languages/codex/target/debug/codex",
    ]
    for candidate_path in candidate_paths:
        if candidate_path.is_file():
            return candidate_path

    discovered_path = shutil.which("codex")
    if discovered_path is not None:
        return Path(discovered_path)

    raise VerificationError(
        "Could not locate a Codex CLI binary. Use --codex-binary to provide one."
    )


def resolve_manifest_path(target_path: Path) -> Path:
    """Resolve the manifest path from a package directory or manifest path."""

    if target_path.is_file():
        if target_path.name != "manifest.cdx":
            raise VerificationError(
                f"Target file must be manifest.cdx, got {target_path}"
            )
        return target_path

    manifest_path = target_path / "manifest.cdx"
    if manifest_path.is_file():
        return manifest_path

    raise VerificationError(
        f"Could not find manifest.cdx under target path {target_path}"
    )


def read_text(path: Path) -> str:
    """Read a UTF-8 text file."""

    return path.read_text(encoding="utf-8")


def extract_attribute(text: str, attribute_name: str) -> str:
    """Extract an attribute value from a Codex start tag fragment."""

    pattern = re.compile(
        rf'{re.escape(attribute_name)}=(?:"([^"]*)"|([^\s/>]+))'
    )
    match = pattern.search(text)
    if match is None:
        raise VerificationError(f"Missing attribute {attribute_name}")
    return match.group(1) or match.group(2)


def run_codex_command(codex_binary: Path, command: str, file_path: Path) -> str:
    """Run a Codex CLI command on one file and return stdout."""

    result = subprocess.run(
        [str(codex_binary), command, str(file_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise VerificationError(
            f"Codex {command} failed for {file_path}:\n{stderr}"
        )
    return result.stdout


def compute_document_hash(codex_binary: Path, file_path: Path) -> str:
    """Compute the canonical document hash for one Codex document."""

    output = run_codex_command(codex_binary, "identity", file_path).strip()
    if not HEX_PATTERN.fullmatch(output):
        raise VerificationError(
            f"Codex identity returned a non-hash value for {file_path}: {output}"
        )
    return output


def canonicalize_document(codex_binary: Path, file_path: Path) -> str:
    """Canonicalize one Codex document."""

    return run_codex_command(codex_binary, "canonicalize", file_path)


def build_primary_document_index(
    schemas_root: Path,
    codex_binary: Path,
) -> dict[str, PrimaryDocumentRecord]:
    """Index package primary documents by document hash."""

    primary_document_index: dict[str, PrimaryDocumentRecord] = {}

    for manifest_path in sorted(schemas_root.rglob("manifest.cdx")):
        manifest_text = read_text(manifest_path)
        primary_document_relative_path = extract_attribute(
            manifest_text, "primaryDocument"
        )
        primary_document_path = (manifest_path.parent / primary_document_relative_path).resolve()
        if not primary_document_path.is_file():
            raise VerificationError(
                f"Primary document does not exist: {primary_document_path}"
            )

        document_hash = compute_document_hash(codex_binary, primary_document_path)
        record = PrimaryDocumentRecord(
            document_hash=document_hash,
            manifest_path=manifest_path.resolve(),
            primary_document_path=primary_document_path,
        )
        existing_record = primary_document_index.get(document_hash)
        if existing_record is not None and existing_record.primary_document_path != primary_document_path:
            raise VerificationError(
                "Two primary documents share the same document hash:\n"
                f"- {existing_record.primary_document_path}\n"
                f"- {primary_document_path}\n"
                f"hash: {document_hash}"
            )
        primary_document_index[document_hash] = record

    return primary_document_index


def parse_package_dependencies(manifest_text: str) -> tuple[PackageDependencyRecord, ...]:
    """Extract declared PackageDependency records from a manifest."""

    dependency_records: list[PackageDependencyRecord] = []
    dependency_pattern = re.compile(r"<PackageDependency\b(.*?)\/>", re.DOTALL)
    for match in dependency_pattern.finditer(manifest_text):
        dependency_text = match.group(1)
        package_name = extract_attribute(dependency_text, "packageName")
        closure_hash = extract_attribute(dependency_text, "closureHash")
        if not HEX_PATTERN.fullmatch(closure_hash):
            raise VerificationError(
                f"PackageDependency.closureHash is not a lowercase SHA-256 hex string: "
                f"{closure_hash}"
            )
        dependency_records.append(
            PackageDependencyRecord(
                package_name=package_name,
                closure_hash=closure_hash,
            )
        )
    return tuple(dependency_records)


def parse_import_references(canonical_document_text: str) -> tuple[str, ...]:
    """Extract SchemaImport.reference values in canonical document order."""

    import_references: list[str] = []
    schema_import_pattern = re.compile(r"<SchemaImport\b(.*?)\/>", re.DOTALL)
    for match in schema_import_pattern.finditer(canonical_document_text):
        import_text = match.group(1)
        import_reference = extract_attribute(import_text, "reference")
        if not import_reference.startswith(CONTENT_HASH_URN_PREFIX):
            raise VerificationError(
                f"SchemaImport.reference is not a content-hash IRI: {import_reference}"
            )
        import_references.append(import_reference)
    return tuple(import_references)


def hash_node(document_hash: str, dependency_records: list[tuple[str, str]]) -> str:
    """Compute one Merkle node hash."""

    hasher = hashlib.sha256()
    hasher.update(MERKLE_NODE_TAG)
    hasher.update(bytes.fromhex(document_hash))
    for import_reference, dependency_node_hash in dependency_records:
        hasher.update(import_reference.encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(bytes.fromhex(dependency_node_hash))
        hasher.update(b"\0")
    return hasher.hexdigest()


def hash_closure(root_node_hash: str) -> str:
    """Compute the root closure hash."""

    hasher = hashlib.sha256()
    hasher.update(MERKLE_CLOSURE_TAG)
    hasher.update(bytes.fromhex(root_node_hash))
    return hasher.hexdigest()


def compute_closure(
    root_document_path: Path,
    codex_binary: Path,
    primary_document_index: dict[str, PrimaryDocumentRecord],
) -> tuple[str, list[TraceRecord]]:
    """Compute the Merkle closure hash and trace records for one root document."""

    document_hash_cache: dict[Path, str] = {}
    canonical_document_cache: dict[Path, str] = {}
    node_hash_cache: dict[str, str] = {}
    trace_records: dict[str, TraceRecord] = {}
    in_progress_hashes: set[str] = set()

    def get_document_hash(document_path: Path) -> str:
        resolved_path = document_path.resolve()
        if resolved_path not in document_hash_cache:
            document_hash_cache[resolved_path] = compute_document_hash(
                codex_binary, resolved_path
            )
        return document_hash_cache[resolved_path]

    def get_canonical_document(document_path: Path) -> str:
        resolved_path = document_path.resolve()
        if resolved_path not in canonical_document_cache:
            canonical_document_cache[resolved_path] = canonicalize_document(
                codex_binary, resolved_path
            )
        return canonical_document_cache[resolved_path]

    def visit(document_path: Path) -> str:
        resolved_path = document_path.resolve()
        document_hash = get_document_hash(resolved_path)
        cached_node_hash = node_hash_cache.get(document_hash)
        if cached_node_hash is not None:
            return cached_node_hash

        if document_hash in in_progress_hashes:
            raise VerificationError(f"Cycle detected at document hash {document_hash}")

        in_progress_hashes.add(document_hash)
        canonical_document_text = get_canonical_document(resolved_path)
        import_references = parse_import_references(canonical_document_text)

        dependency_records: list[tuple[str, str]] = []
        for import_reference in import_references:
            imported_document_hash = import_reference.removeprefix(CONTENT_HASH_URN_PREFIX)
            if not HEX_PATTERN.fullmatch(imported_document_hash):
                raise VerificationError(
                    f"SchemaImport.reference does not contain a valid document hash: "
                    f"{import_reference}"
                )

            imported_record = primary_document_index.get(imported_document_hash)
            if imported_record is None:
                raise VerificationError(
                    "Could not resolve SchemaImport.reference to any package "
                    f"primary document: {import_reference}"
                )

            actual_imported_document_hash = get_document_hash(imported_record.primary_document_path)
            if actual_imported_document_hash != imported_document_hash:
                raise VerificationError(
                    "Resolved imported document hash does not match the declared "
                    f"SchemaImport.reference: {import_reference} -> "
                    f"{actual_imported_document_hash}"
                )

            dependency_node_hash = visit(imported_record.primary_document_path)
            dependency_records.append((import_reference, dependency_node_hash))

        node_hash = hash_node(document_hash, dependency_records)
        in_progress_hashes.remove(document_hash)
        node_hash_cache[document_hash] = node_hash
        trace_records[document_hash] = TraceRecord(
            document_path=resolved_path,
            document_hash=document_hash,
            node_hash=node_hash,
            import_references=import_references,
        )
        return node_hash

    root_node_hash = visit(root_document_path)
    ordered_trace_records = sorted(
        trace_records.values(), key=lambda record: record.document_path.as_posix()
    )
    return hash_closure(root_node_hash), ordered_trace_records


def verify_root_package_dependencies(
    manifest_text: str,
    root_trace_record: TraceRecord,
    primary_document_index: dict[str, PrimaryDocumentRecord],
) -> tuple[PackageDependencyRecord, ...]:
    """Verify manifest PackageDependency entries against direct imported packages."""

    declared_dependencies = parse_package_dependencies(manifest_text)
    declared_by_name = {
        record.package_name: record for record in declared_dependencies
    }

    expected_by_name: dict[str, PackageDependencyRecord] = {}
    for import_reference in root_trace_record.import_references:
        imported_document_hash = import_reference.removeprefix(CONTENT_HASH_URN_PREFIX)
        imported_record = primary_document_index.get(imported_document_hash)
        if imported_record is None:
            raise VerificationError(
                "Could not resolve direct import while checking PackageDependency "
                f"records: {import_reference}"
            )
        imported_manifest_text = read_text(imported_record.manifest_path)
        imported_package_name = extract_attribute(imported_manifest_text, "packageName")
        imported_package_closure_hash = extract_attribute(
            imported_manifest_text, "closureHash"
        )
        if not HEX_PATTERN.fullmatch(imported_package_closure_hash):
            raise VerificationError(
                "Imported package manifest closureHash is not a lowercase SHA-256 hex "
                f"string: {imported_record.manifest_path}"
            )
        expected_record = PackageDependencyRecord(
            package_name=imported_package_name,
            closure_hash=imported_package_closure_hash,
        )
        previous_record = expected_by_name.get(imported_package_name)
        if previous_record is not None and previous_record != expected_record:
            raise VerificationError(
                "Conflicting direct-import package records for package "
                f"{imported_package_name}"
            )
        expected_by_name[imported_package_name] = expected_record

    if set(declared_by_name) != set(expected_by_name):
        missing_names = sorted(set(expected_by_name) - set(declared_by_name))
        extra_names = sorted(set(declared_by_name) - set(expected_by_name))
        raise VerificationError(
            "PackageDependency names do not match direct imported packages:\n"
            f"missing: {missing_names}\n"
            f"extra: {extra_names}"
        )

    for package_name, expected_record in expected_by_name.items():
        declared_record = declared_by_name[package_name]
        if declared_record.closure_hash != expected_record.closure_hash:
            raise VerificationError(
                "PackageDependency closureHash does not match the imported package "
                f"manifest for {package_name}: declared {declared_record.closure_hash}, "
                f"expected {expected_record.closure_hash}"
            )

    return declared_dependencies


def rewrite_manifest_closure_hash(
    manifest_path: Path,
    manifest_text: str,
    computed_closure_hash: str,
) -> None:
    """Rewrite only the root manifest closureHash attribute."""

    root_manifest_pattern = re.compile(
        r'(\A<[A-Za-z]+PackageManifest\b[^>]*?\bclosureHash=")([0-9a-f]{64})(")',
        re.DOTALL,
    )
    replacement_count = 0

    def replace_match(match: re.Match[str]) -> str:
        nonlocal replacement_count
        replacement_count += 1
        return f"{match.group(1)}{computed_closure_hash}{match.group(3)}"

    rewritten_text = root_manifest_pattern.sub(replace_match, manifest_text, count=1)
    if replacement_count != 1:
        raise VerificationError(
            f"Could not uniquely rewrite root closureHash in {manifest_path}"
        )
    manifest_path.write_text(rewritten_text, encoding="utf-8")


def main() -> int:
    """Program entry point."""

    arguments = parse_arguments()
    start_path = arguments.target.resolve()
    workspace_root = find_workspace_root(start_path)
    codex_binary = resolve_codex_binary(workspace_root, arguments.codex_binary)
    manifest_path = resolve_manifest_path(start_path).resolve()
    manifest_text = read_text(manifest_path)
    stored_closure_hash = extract_attribute(manifest_text, "closureHash")
    primary_document_relative_path = extract_attribute(manifest_text, "primaryDocument")
    primary_document_path = (manifest_path.parent / primary_document_relative_path).resolve()
    schemas_root = (workspace_root / "schemas/paperhat-schemas/spec/1.0.0/schemas").resolve()

    if not primary_document_path.is_file():
        raise VerificationError(
            f"Primary document does not exist: {primary_document_path}"
        )
    if not HEX_PATTERN.fullmatch(stored_closure_hash):
        raise VerificationError(
            f"Manifest closureHash is not a lowercase SHA-256 hex string: {stored_closure_hash}"
        )
    if not primary_document_path.is_relative_to(schemas_root):
        raise VerificationError(
            "Primary document is outside the schema root: "
            f"{primary_document_path}"
        )

    primary_document_index = build_primary_document_index(schemas_root, codex_binary)
    computed_closure_hash, trace_records = compute_closure(
        root_document_path=primary_document_path,
        codex_binary=codex_binary,
        primary_document_index=primary_document_index,
    )
    root_trace_record = next(
        (
            trace_record
            for trace_record in trace_records
            if trace_record.document_path == primary_document_path
        ),
        None,
    )
    if root_trace_record is None:
        raise VerificationError(
            f"Missing root trace record for {primary_document_path}"
        )
    declared_dependencies = verify_root_package_dependencies(
        manifest_text=manifest_text,
        root_trace_record=root_trace_record,
        primary_document_index=primary_document_index,
    )

    if arguments.write_manifest and stored_closure_hash != computed_closure_hash:
        rewrite_manifest_closure_hash(
            manifest_path=manifest_path,
            manifest_text=manifest_text,
            computed_closure_hash=computed_closure_hash,
        )

    print(f"manifest: {manifest_path}")
    print(f"primaryDocument: {primary_document_path}")
    print(f"stored closureHash:   {stored_closure_hash}")
    print(f"computed closureHash: {computed_closure_hash}")
    print("packageDependencies:")
    if declared_dependencies:
        for dependency_record in declared_dependencies:
            print(
                "  - "
                f"{dependency_record.package_name} "
                f"{dependency_record.closure_hash}"
            )
    else:
        print("  []")
    print("trace:")
    for trace_record in trace_records:
        print(f"  - document: {trace_record.document_path}")
        print(f"    documentHash: {trace_record.document_hash}")
        print(f"    nodeHash: {trace_record.node_hash}")
        if trace_record.import_references:
            print("    imports:")
            for import_reference in trace_record.import_references:
                print(f"      - {import_reference}")
        else:
            print("    imports: []")

    if stored_closure_hash != computed_closure_hash:
        if arguments.write_manifest:
            print("status: UPDATED")
            return 0
        print("status: MISMATCH", file=sys.stderr)
        return 1

    print("status: MATCH")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except VerificationError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
