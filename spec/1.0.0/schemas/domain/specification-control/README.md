# Specification Control

`paperhat-specification-control` defines a minimal control-plane schema for managing small,
dependency-aware specification-authoring packets without restating the normative content of
the governed specification.

## Primary Purpose

This schema exists to coordinate tiny, reviewable authoring units:

- packet registries that list admitted work items
- packet documents that carry local invariants and completion checks
- dependency edges that declare reread obligations
- open issue entries for unresolved blockers
- terminology entries for canonical naming discipline
- banned token lists for stale-term sweeps

The schema is intentionally operational rather than domain-semantic. It tracks authoring
control state; it does not duplicate the meaning of the governed specification.

## Packet Lifecycle

The pilot packet lifecycle is intentionally minimal:

- `$Proposed` means the packet has been admitted but work has not yet started.
- `$InProgress` means active authoring, repair, or audit work is still underway.
- `$Completed` means the packet's declared completion checks have been satisfied for the governed batch.

`$Completed` does not require every follow-up concern in the same area to be resolved. Open
follow-up items may remain as `OpenIssueEntry` records with `issueStatus=$Open`, provided the
packet's own declared work and declared checks are complete.

## DependencyEdge Semantics

`DependencyEdge` is a packet-scoped control artifact, not a whole-specification citation graph.

- A `DependencyEdge` declares that if the `sourceKey` changes during packet work, the packet
  MUST reread or recheck the `targetKey` before closure.
- Absence of an edge does not mean no semantic relationship exists in the governed
  specification. It means only that the packet does not rely on that relationship as part of
  its declared closure set.
- Packet ledgers therefore stay intentionally smaller than the full transitive citation graph
  of the governed specification.

## BannedTokenList Enforcement

`BannedTokenList` remains primarily a control document, but local gates may enforce it.

- `tokens` carries a semicolon-delimited set of forbidden phrases for the packet.
- `appliesTo` remains human-readable scope text.
- `appliesToPaths`, when present, carries a semicolon-delimited set of repository-relative
  files that local gates MUST scan for those tokens.

## Concepts

| Concept | Purpose |
| --- | --- |
| `PacketRegistry` | Ordered registry of admitted packet entries for one target specification. |
| `PacketEntry` | One registry row naming a packet, its target specification, section, and state. |
| `Packet` | Detailed packet document containing local invariants, completion checks, and control children. |
| `DependencyEdge` | Packet-scoped directed control dependency used to declare reread obligations before closure. |
| `OpenIssueEntry` | One unresolved ambiguity, blocker, or deferred repair item. |
| `BannedTokenList` | Tokens or phrases that must not survive after a cleanup or rename batch, optionally with machine-readable target paths. |
| `TerminologyEntry` | Canonical term record with location, forbidden synonyms, and usage notes. |

## Minimal Package Shape

This initial package is deliberately small. It is intended as a pilot control schema and may
be extended later only if the added structure remains operational and does not restate
normative specification semantics.

## Packet Bundle Initialization

The repository provides a small scaffold tool for creating one fresh packet bundle outside
active specifications:

```bash
python3 /Users/guy/Workspace/@paperhat/schemas/paperhat-schemas/tools/initialize_specification_packet_bundle.py \
  --output-root /tmp/specification-packet \
  --packet-id rdf-001 \
  --target-specification paperhat-rdf \
  --owner-section "Section 4.2 IRI lowering" \
  --constructs "IriNode; CanonicalOrderingRule"
```

The tool creates:

- one `packet-registry.cdx`
- one `packets/<packet-id>.cdx`

This is a bundle initializer only. It does not close packets, audit packets, or edit the
governed specification.
