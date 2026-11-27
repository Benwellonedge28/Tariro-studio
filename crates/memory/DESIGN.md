# Memory crate design

**Contract version** 1.0. Master design §23. Planned implementation.

## Responsibility and dependencies

Validate identity and workspace before insert or search. Deduplicate normalized content within scope. Purge with durable tombstone, projection invalidation and later GC.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [security](../security/DESIGN.md)

- [Memory](../../specifications/0800-memory/memory.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `record(scope, source)`
- `search(scope, query)`
- `export(scope)`
- `purge(scope)`

Record families: MemoryRecord, provenance, sensitivity, expiry, tombstone and access scope. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `MemoryRecord { memory_id, workspace_id, visibility_scope, source_ref, sensitivity, retained_until, payload_ref }`
- `Tombstone { memory_id, generation, purge_time }`

- `search(scope: AuthorizedMemoryScope, query: MemoryQuery) -> Result<MemoryPage>`

## Failure, safety and resource limits

Default ephemeral assignment memory unless persistence is enabled by policy. Enforce retention and per-scope quota. Never share across scope by default.

- `ScopeDenied`
- `CapacityExceeded`
- `RetentionConflict`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/memory/src/
├── lib.rs
├── error.rs
├── memory.rs
├── record.rs
├── scope.rs
├── store.rs
├── retrieval.rs
├── consolidation.rs
├── compression.rs
├── deduplication.rs
├── expiration.rs
├── forgetting.rs
├── encryption.rs
├── provenance.rs
├── isolation.rs
├── layers/
│   ├── mod.rs
│   ├── working.rs
│   ├── session.rs
│   ├── episodic.rs
│   ├── semantic.rs
│   ├── procedural.rs
│   ├── project.rs
│   ├── repository.rs
│   ├── organization.rs
│   └── archival.rs
└── synchronization.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test cross-tenant isolation, expired retrieval and crash during purge.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`memory.rs`](specifications/modules/memory.md)
- [`record.rs`](specifications/modules/record.md)
- [`scope.rs`](specifications/modules/scope.md)
- [`store.rs`](specifications/modules/store.md)
- [`retrieval.rs`](specifications/modules/retrieval.md)
- [`consolidation.rs`](specifications/modules/consolidation.md)
- [`compression.rs`](specifications/modules/compression.md)
- [`deduplication.rs`](specifications/modules/deduplication.md)
- [`expiration.rs`](specifications/modules/expiration.md)
- [`forgetting.rs`](specifications/modules/forgetting.md)
- [`encryption.rs`](specifications/modules/encryption.md)
- [`provenance.rs`](specifications/modules/provenance.md)
- [`isolation.rs`](specifications/modules/isolation.md)
- [`layers/mod.rs`](specifications/modules/layers/mod.md)
- [`layers/working.rs`](specifications/modules/layers/working.md)
- [`layers/session.rs`](specifications/modules/layers/session.md)
- [`layers/episodic.rs`](specifications/modules/layers/episodic.md)
- [`layers/semantic.rs`](specifications/modules/layers/semantic.md)
- [`layers/procedural.rs`](specifications/modules/layers/procedural.md)
- [`layers/project.rs`](specifications/modules/layers/project.md)
- [`layers/repository.rs`](specifications/modules/layers/repository.md)
- [`layers/organization.rs`](specifications/modules/layers/organization.md)
- [`layers/archival.rs`](specifications/modules/layers/archival.md)
- [`synchronization.rs`](specifications/modules/synchronization.md)
