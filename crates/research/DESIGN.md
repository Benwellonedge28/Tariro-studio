# Research crate design

**Contract version** 1.0. Master design §37. Planned implementation.

## Responsibility and dependencies

Select reviewed local or approved external route, store timestamp and bibliographic metadata, extract claim with pinpoint evidence and label corroboration or uncertainty.

First-party dependencies: [foundation](../foundation/DESIGN.md), [networking](../networking/DESIGN.md), [storage](../storage/DESIGN.md), [security](../security/DESIGN.md)

- [Architecture and component boundaries](../../specifications/0100-architecture/component-boundaries.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `query(scope)`
- `fetch_source(uri)`
- `extract_claims(source)`
- `assemble_report()`

Record families: SourceRecord, retrieval time, content digest, citation and claim classification. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `SourceRecord { source_id, uri, retrieved_at, digest, title, publisher, access_scope }`
- `Claim { text, source_ref, pinpoint, status }`

- `fetch_source(request: SourceRequest, grant: GrantRef) -> Result<SourceRecord>`

## Failure, safety and resource limits

No network in offline mode. Limit URL schemes, hosts, redirects, byte count and excerpt duplication. Protect private query content.

- `Offline`
- `SourceUnavailable`
- `IntegrityMismatch`
- `ScopeDenied`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/research/src/
├── lib.rs
├── error.rs
├── question.rs
├── plan.rs
├── source.rs
├── discovery.rs
├── retrieval.rs
├── extraction.rs
├── credibility.rs
├── comparison.rs
├── synthesis.rs
├── citation.rs
├── provenance.rs
├── cache.rs
├── offline_library.rs
├── providers/
│   ├── mod.rs
│   ├── web.rs
│   ├── documentation.rs
│   ├── repository.rs
│   ├── academic.rs
│   └── local.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test dead source, conflicting citations and forbidden destination.
