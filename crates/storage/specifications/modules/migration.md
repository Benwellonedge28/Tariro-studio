# Storage migration and rollback

**ZIP-STO-MIG-001 · v1.0 · Owner:** Storage and release maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/storage/src/migration.rs`.

The operation accepts source generation, exact target version, approved migration descriptor, backup destination and resource lease. Result is Activated(new generation), AbortedBeforeActivation or RecoveryRequired with stage and receipt. Expose `migrate(request: MigrationRequest, cancel: CancellationToken) -> Result<MigrationOutcome, StorageError>`. Source and target are owner-local roots. Unknown migration edges fail before stopping the writer.

| Stage | Durable fact and restart behavior |
| --- | --- |
| Planned | Exact source identity and algorithm digest are pinned; repeat validation |
| BackedUp | Verified manifest preserves source generation and object references |
| Staging | Target cursor is private; resume only if algorithm and source digest match |
| Verified | Keyspace coverage, schema, indexes and all referenced objects validated |
| Activated | Atomic selector points to the target; probe health before deleting any previous generation |
| RolledBack | Verified prior selector restored; retained backup and audit remain available |

Check actual free space against both staging and recovery needs. Quiesce mutation and fence the writer during generation freeze and activation. Cancellation before activation keeps old selector. A crash during activation is reconciled by inspecting selector and journal, without creating a second active generation. Roll back only if the old binary/writer has a compatible generation and no irreversible post-activation effects require recovery; otherwise restore under reviewed authority.

STO-MIG-T01 interrupts at each stage and verifies exactly one active generation. T02 exhausts storage before activation and checks old generation remains readable. T03 injects a bad checksum and denies activation. T04 proves downgrade refusal where the prior writer cannot read new data.
