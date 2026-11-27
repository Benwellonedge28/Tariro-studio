# Audit crate design

**Contract version** 1.0. Master design §45. Planned implementation.

## Responsibility and dependencies

Redact before canonically encoding and hashing. Append in same transaction with privileged intent; append result after reconciliation. Sign checkpoint on configured cadence.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [security](../security/DESIGN.md)

- [Verification](../../specifications/2100-verification/verification.md)
- [Security](../../specifications/2300-security/security.md)
- [Governance](../../specifications/2400-governance/governance.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Observability](../../specifications/3100-observability/observability.md)
- [Maintenance](../../specifications/3400-maintenance/maintenance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `append_in(tx, record)`
- `verify_chain()`
- `export(scope, cursor)`

Record families: AuditRecord with sequence, prev hash, hash, actor, policy digest, scope and outcome. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `AuditRecord { sequence, workspace, actor, effect_ref, policy_digest, outcome, prior_hash, hash, timestamp }`

- `append_in(tx: &mut MetadataTransaction, record: AuditDraft) -> Result<AuditRef>`

## Failure, safety and resource limits

Bound fields and retention exports. No raw command environments or tokens. Deletion requires policy-compliant checkpoint/history proof.

- `AuditUnavailable`
- `ChainMismatch`
- `CursorExpired`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/audit/src/
├── lib.rs
├── error.rs
├── record.rs
├── journal.rs
├── actor.rs
├── operation.rs
├── authorization.rs
├── evidence.rs
├── hash_chain.rs
├── integrity.rs
├── redaction.rs
├── query.rs
├── retention.rs
├── export.rs
└── verification.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Mutate one record and detect chain failure. Verify ordering under concurrent writers.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`record.rs`](specifications/modules/record.md)
- [`journal.rs`](specifications/modules/journal.md)
- [`actor.rs`](specifications/modules/actor.md)
- [`operation.rs`](specifications/modules/operation.md)
- [`authorization.rs`](specifications/modules/authorization.md)
- [`evidence.rs`](specifications/modules/evidence.md)
- [`hash_chain.rs`](specifications/modules/hash_chain.md)
- [`integrity.rs`](specifications/modules/integrity.md)
- [`redaction.rs`](specifications/modules/redaction.md)
- [`query.rs`](specifications/modules/query.md)
- [`retention.rs`](specifications/modules/retention.md)
- [`export.rs`](specifications/modules/export.md)
- [`verification.rs`](specifications/modules/verification.md)
