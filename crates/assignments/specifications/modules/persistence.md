# Assignment aggregate and receipts

**ZIP-ASSIGNMENTS-PERSISTENCE-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/persistence.rs`

Use versioned Storage domain namespaces. Logical keys and the minimum value fields are as follows.

| Record | Logical key | Required data |
| --- | --- | --- |
| Aggregate | workspace and assignment UUID | repository identity, pinned head and instructions, requirement and plan digests, grant reference and policy revision, state and revision, worker epoch, verified prefix, sealed candidate, stop disposition or blocker, outcome evidence |
| Checkpoint | assignment UUID, plan digest, unit index | path identity, immutable artifact and evidence, source revision, committing epoch and aggregate revision |
| Command receipt | assignment and command UUID | authenticated actor reference, canonical request digest, chosen transaction ID, outcome and committed aggregate revision |
| Effect | assignment UUID and stable effect key | phase, frozen provider operation and payload digest, target and expected remote identity, outcome and evidence, relevant claim epoch and grant version |

UUIDs encode in network byte order and integers in big-endian order in logical binary keys. Use Storage's registered per-family namespace and type tags. Derive the fixed-width record ID from the first 16 bytes of SHA-256 over ASCII `ZIP-ASG-ROW-v1` and the canonical logical key for that family. Reject all-zero results or a mismatch to the full logical key stored in the value. No overwrite on hash collision. Store versioned typed payloads and immutable object references. Unsigned JSON values use canonical decimal strings. Register namespace IDs, type tags and canonical request codecs before independent approval.

`AssignmentStore` provides a bounded snapshot and atomic compare-and-swap write of aggregate, affected records, commands and outbox. Use Storage's receipt protocol for an ambiguous submit. Current positive scope is required for reading a receipt. Never use unknown receipt as proof a provider effect was absent. Rebuild projections from committed state and events. Keep unresolved intents, current checkpoints and replay fences durable across retention and restore. Migrate records as a verified snapshot, preserving effect identities and high-water counters. Fencing and transition commits increment checked generation values and never wrap.

**ZIP-ASSIGNMENTS-PERSISTENCE-T01.** Crash before and after the batch submission and compare progress, revision, checkpoint, receipt and event. Recover either the earlier state or one complete new state.
