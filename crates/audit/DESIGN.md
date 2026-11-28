# Audit crate design

**Contract version** 1.1 candidate. Master design §45. Planned implementation.

## Responsibility and dependencies

Redact before canonical encoding and hashing. Append required audit evidence in the same transaction as privileged intent. Append unresolved and verified outcome observations under the original operation identity. Use qualified checkpoint signing when required by configured policy.

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

Record families: AuditRecord with workspace sequence, predecessor and body digests, actor, decision, scope and outcome. [Record codec](specifications/modules/record.md) owns candidate hash-input bytes and [hash chain](specifications/modules/hash_chain.md) owns framing. A provisional append reference becomes authoritative only with its containing Storage commit. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

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

Every planned Audit source path has a candidate file contract. See the [requirements map](../../contracts/requirements/modules/audit.json). Canonical codec vectors, Storage namespace and index integration, checkpoint signer qualification and independent review remain open.

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
