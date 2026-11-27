# Maintenance crate design

**Contract version** 1.0. Master design §56. Planned implementation.

## Responsibility and dependencies

Plan under directory and storage scopes, verify replacement signature, stage backup and apply within maintenance window. Prune only unreachable, unpinned objects.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [audit](../audit/DESIGN.md), [verification](../verification/DESIGN.md)

- [Maintenance](../../specifications/3400-maintenance/maintenance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `check(profile)`
- `stage_update(manifest)`
- `prune(plan)`
- `reconcile()`

Record families: MaintenancePlan, signed manifest, retained-object reachability and result. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `MaintenancePlan { target_scope, action, preconditions, window, prior_manifest, authorized_effects }`
- `PruneCandidate { digest, bytes, reference_age }`

- `prune(plan: MaintenancePlan, grant: GrantRef) -> Result<MaintenanceReceipt>`

## Failure, safety and resource limits

No automatic destructive cleanup by default. Keep backups required by retention. Pause on active database migration or low disk.

- `UpdateUntrusted`
- `ObjectPinned`
- `RollbackFailed`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/maintenance/src/
├── lib.rs
├── error.rs
├── monitoring.rs
├── dependency_updates.rs
├── vulnerability_management.rs
├── technical_debt.rs
├── regression_detection.rs
├── compatibility.rs
├── backup.rs
├── recovery.rs
├── cleanup.rs
├── lifecycle.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Restore after interrupted update and verify artifact retention.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`monitoring.rs`](specifications/modules/monitoring.md)
- [`dependency_updates.rs`](specifications/modules/dependency_updates.md)
- [`vulnerability_management.rs`](specifications/modules/vulnerability_management.md)
- [`technical_debt.rs`](specifications/modules/technical_debt.md)
- [`regression_detection.rs`](specifications/modules/regression_detection.md)
- [`compatibility.rs`](specifications/modules/compatibility.md)
- [`backup.rs`](specifications/modules/backup.md)
- [`recovery.rs`](specifications/modules/recovery.md)
- [`cleanup.rs`](specifications/modules/cleanup.md)
- [`lifecycle.rs`](specifications/modules/lifecycle.md)
- [`reporting.rs`](specifications/modules/reporting.md)
