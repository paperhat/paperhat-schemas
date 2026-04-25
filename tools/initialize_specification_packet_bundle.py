#!/usr/bin/env python3
"""Initialize one minimal specification-control packet bundle."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PACKET_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")
STATE_TOKEN_PATTERN = re.compile(r"^\$[A-Za-z][A-Za-z0-9]*$")


class InitializeSpecificationPacketBundleError(RuntimeError):
    """Raised when packet-bundle initialization cannot complete safely."""


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        type=Path,
        required=True,
        help="Empty or non-existent directory that will receive the packet bundle.",
    )
    parser.add_argument(
        "--packet-id",
        required=True,
        help="Stable packet identifier, for example rdf-001.",
    )
    parser.add_argument(
        "--target-specification",
        required=True,
        help="Target specification identifier, for example paperhat-rdf.",
    )
    parser.add_argument(
        "--owner-section",
        required=True,
        help="Normative owner section for the packet.",
    )
    parser.add_argument(
        "--constructs",
        required=True,
        help="Semicolon-delimited construct list for the packet entry.",
    )
    parser.add_argument(
        "--registry-name",
        default=None,
        help="Optional registry name. Defaults to '<target specification> packet registry'.",
    )
    parser.add_argument(
        "--state",
        default="$Proposed",
        help="Initial packet state token (default: $Proposed).",
    )
    parser.add_argument(
        "--invariants",
        default=(
            "Preserve approved capability, avoid undeclared identifiers, and leave no "
            "named dependent location stale."
        ),
        help="Initial invariants text for the packet document.",
    )
    parser.add_argument(
        "--completion-checks",
        default=(
            "Update target nodes, reread declared dependents, rerun deterministic checks, "
            "and clear stale terms before closing the packet."
        ),
        help="Initial completion checks text for the packet document.",
    )
    return parser.parse_args()


def validate_packet_identifier(packet_identifier: str) -> None:
    """Validate one packet identifier for safe file and URN use."""

    if not PACKET_IDENTIFIER_PATTERN.fullmatch(packet_identifier):
        raise InitializeSpecificationPacketBundleError(
            "packet identifier must match [A-Za-z0-9._-]+"
        )


def validate_quoted_attribute_value(value: str, field_name: str) -> None:
    """Reject raw text that would break quoted attribute emission."""

    if '"' in value:
        raise InitializeSpecificationPacketBundleError(
            f"{field_name} must not contain double quotes"
        )
    if "\n" in value or "\r" in value:
        raise InitializeSpecificationPacketBundleError(
            f"{field_name} must not contain line breaks"
        )


def validate_state_token(state_token: str) -> None:
    """Require a safe enumerated token literal for state emission."""

    if not STATE_TOKEN_PATTERN.fullmatch(state_token):
        raise InitializeSpecificationPacketBundleError(
            "state must match $TokenName"
        )


def ensure_directory_is_initializable(output_root: Path) -> None:
    """Require a safe output directory state before writing files."""

    if output_root.exists():
        if not output_root.is_dir():
            raise InitializeSpecificationPacketBundleError(
                f"output root exists and is not a directory: {output_root}"
            )
        if any(output_root.iterdir()):
            raise InitializeSpecificationPacketBundleError(
                f"output root must be empty: {output_root}"
            )
    else:
        output_root.mkdir(parents=True, exist_ok=False)


def packet_registry_text(
    *,
    registry_name: str,
    packet_identifier: str,
    target_specification: str,
    owner_section: str,
    constructs: str,
    state: str,
    packet_document_reference: str,
) -> str:
    """Build the initial packet registry document."""

    return "\n".join(
        [
            "<PacketRegistry",
            f'\tname="{registry_name}"',
            f'\ttargetSpecification="{target_specification}"',
            ">",
            "\t<PacketEntry",
            (
                f"\t\tid=urn:paperhat:specification-control:packet-entry:"
                f"{packet_identifier}"
            ),
            f'\t\tpacketId="{packet_identifier}"',
            f'\t\ttargetSpecification="{target_specification}"',
            f'\t\townerSection="{owner_section}"',
            f'\t\tconstructs="{constructs}"',
            f"\t\tstate={state}",
            f'\t\tpacketDocumentReference="{packet_document_reference}"',
            "\t/>",
            "</PacketRegistry>",
            "",
        ]
    )


def packet_document_text(
    *,
    packet_identifier: str,
    target_specification: str,
    owner_section: str,
    state: str,
    invariants: str,
    completion_checks: str,
) -> str:
    """Build the initial packet document."""

    return "\n".join(
        [
            "<Packet",
            f"\tid=urn:paperhat:specification-control:packet:{packet_identifier}",
            f'\tpacketId="{packet_identifier}"',
            f'\ttargetSpecification="{target_specification}"',
            f'\townerSection="{owner_section}"',
            f"\tstate={state}",
            f'\tinvariants="{invariants}"',
            f'\tcompletionChecks="{completion_checks}"',
            "/>",
            "",
        ]
    )


def main() -> int:
    """Initialize one minimal packet bundle on disk."""

    arguments = parse_arguments()
    packet_identifier = arguments.packet_id
    validate_packet_identifier(packet_identifier)
    validate_state_token(arguments.state)

    output_root = arguments.output_root.resolve()
    ensure_directory_is_initializable(output_root)

    registry_name = (
        arguments.registry_name
        if arguments.registry_name is not None
        else f"{arguments.target_specification} packet registry"
    )
    for field_name, value in [
        ("registry name", registry_name),
        ("target specification", arguments.target_specification),
        ("owner section", arguments.owner_section),
        ("constructs", arguments.constructs),
        ("invariants", arguments.invariants),
        ("completion checks", arguments.completion_checks),
    ]:
        validate_quoted_attribute_value(value, field_name)

    packets_directory = output_root / "packets"
    packets_directory.mkdir(parents=True, exist_ok=False)

    packet_document_path = packets_directory / f"{packet_identifier}.cdx"
    registry_path = output_root / "packet-registry.cdx"

    registry_path.write_text(
        packet_registry_text(
            registry_name=registry_name,
            packet_identifier=packet_identifier,
            target_specification=arguments.target_specification,
            owner_section=arguments.owner_section,
            constructs=arguments.constructs,
            state=arguments.state,
            packet_document_reference=packet_document_path.relative_to(output_root).as_posix(),
        ),
        encoding="utf-8",
    )
    packet_document_path.write_text(
        packet_document_text(
            packet_identifier=packet_identifier,
            target_specification=arguments.target_specification,
            owner_section=arguments.owner_section,
            state=arguments.state,
            invariants=arguments.invariants,
            completion_checks=arguments.completion_checks,
        ),
        encoding="utf-8",
    )

    print(f"Initialized packet bundle: {output_root}")
    print(f"Registry: {registry_path}")
    print(f"Packet: {packet_document_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except InitializeSpecificationPacketBundleError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
