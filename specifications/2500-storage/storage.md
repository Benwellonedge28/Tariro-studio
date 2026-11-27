# Durable state and recovery

**Contract version** 1.0. Master design §71.

## Contract

Store mutable revisioned metadata in redb and immutable verified objects under content-addressed storage. Use primary keys defined by type and ID. Keep a transactional outbox near domain state and index projections by generation.

## Execution and integration

Migrations are versioned, staged with backup, checksummed and restart-safe. Backups snapshot metadata and referenced objects as a unit. Validate manifest and restore into staging before atomic activation.

## Verification

Inject failures before/after rename, before/after metadata transaction and during restore. Referenced objects remain valid or the runtime quarantines the store.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Storage keyspace

| Table | Key | Value / invariants |
| --- | --- | --- |
| schema | singleton | format major/minor, migration and generation |
| domain_records | namespace, record ID | typed envelope, revision and checksum |
| objects | tagged digest | byte length, staging state, references |
| event_outbox | stream ID, sequence | complete event and delivery state |
| audit | workspace ID, sequence | redacted hash-chain record |
| migration_ledger | ordered migration ID | input digest, started/verified/completed, output digest |

Use immutable object bytes, one transactionally updated metadata writer, and snapshot reads. Stage file on the same volume, fsync, atomically rename and verify, then commit metadata. Crash before metadata may leave orphan bytes eligible for GC after grace; crash after metadata must never reference a missing object. Mark database corruption and preserve evidence before manual recovery. Restore writes a new data root and retains the previous root until verification passes.

## Implementing components

- [storage crate design](../../crates/storage/DESIGN.md)
- [events crate design](../../crates/events/DESIGN.md)
- [audit crate design](../../crates/audit/DESIGN.md)
