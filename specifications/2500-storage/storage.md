# Durable state and recovery

**Contract version** 1.1 candidate. Master design §§12 and 71.

Store mutable revisioned metadata using the [backend port](../../crates/storage/specifications/modules/backend.md) and immutable verified bytes using the [object contract](../../crates/storage/specifications/modules/objects/content_addressed.md). The embedded redb backend is the preferred candidate. Each enabled backend must qualify writer exclusivity, snapshot isolation and its durability boundary. Logical tables and keys come from the [storage schema](../../crates/storage/specifications/modules/schema.md).

A domain batch commits record changes, references, stream sequences, outbox entries and its receipt in one transaction. For a lost acknowledgement, reconcile under the original transaction identity. Never infer missing effects from an absent receipt in a rewound store. Promotion can leave orphan bytes before metadata commit. Metadata must never commit a reference to absent bytes.

A backup pins its metadata generation and complete reachable object set. A restore verifies a new root, records intent outside the replaceable root and activates under a durable selector and writer fence. Preserve the prior root according to policy. Newly restored workers cannot emit external effects until their identity and outcome evidence reconcile.

Run the [durability fixtures](../../contracts/acceptance/storage/durability-fixtures.json) against the deterministic test backend, then exercise each qualified adapter at process and filesystem fault points. Record exact inputs, bounds, outcome and evidence. Map applicable release requirements in [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Implementing components

- [Storage](../../crates/storage/DESIGN.md)
- [Events](../../crates/events/DESIGN.md)
- [Audit](../../crates/audit/DESIGN.md)
