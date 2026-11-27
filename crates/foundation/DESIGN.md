# Foundation crate design

**Contract version** 1.1. Master design §9. Planned implementation. **Maturity:** D3.

## Responsibility and dependencies

Decode, validate, canonicalize, then construct. Cancellation is sticky and wakes all registered observers. Use synchronized monotonic deadlines and UTC wall time for audit only.

First-party dependencies: No first-party crate dependency.

- [Architecture and component boundaries](../../specifications/0100-architecture/component-boundaries.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `identity::identifier::Identifier::parse(expected_kind, input)`
- `types::quantity::Quantity<U>::checked_add(self, other)`
- `contracts::compatibility::negotiate(local, peer)`

Record families: Typed UUID IDs, numeric protocol-version triplets, tagged SHA-256 digests and bounded byte/count/time newtypes. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Identifier { kind: IdKind, uuid: Uuid }`
- `Digest { algorithm: DigestAlgorithm, bytes: [u8; 32] }`
- `types::duration::DurationMillis` is an elapsed duration; the runtime owns monotonic deadline anchors.
- `Version { major: u16, minor: u16, patch: u16 }`

Exact signatures, ownership and result behavior are defined by the file contracts below.

## Failure, safety and resource limits

Reject nil IDs where identity is required, unknown digest algorithms, negative or overflowing quantities, and incompatible protocol majors.

- `InvalidIdentifier`
- `LimitExceeded`
- `UnsupportedVersion`
- `Cancelled`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/foundation/src/
├── lib.rs
├── error.rs
├── result.rs
├── identity/
│   ├── mod.rs
│   ├── identifier.rs
│   ├── namespace.rs
│   └── generation.rs
├── types/
│   ├── mod.rs
│   ├── timestamp.rs
│   ├── duration.rs
│   ├── version.rs
│   ├── digest.rs
│   ├── quantity.rs
│   └── bounded.rs
├── contracts/
│   ├── mod.rs
│   ├── component.rs
│   ├── capability.rs
│   ├── lifecycle.rs
│   └── compatibility.rs
├── validation/
│   ├── mod.rs
│   ├── constraints.rs
│   └── invariant.rs
├── cancellation.rs
├── limits.rs
├── provenance.rs
└── prelude.rs
```

## File contracts

The file-level drafts below cover the planned Foundation source layout. Independent review and signature validation remain gates before D5.

- [cancellation.rs](specifications/modules/cancellation.md)
- [contracts/capability.rs](specifications/modules/contracts/capability.md)
- [contracts/compatibility.rs](specifications/modules/contracts/compatibility.md)
- [contracts/component.rs](specifications/modules/contracts/component.md)
- [contracts/lifecycle.rs](specifications/modules/contracts/lifecycle.md)
- [contracts/mod.rs](specifications/modules/contracts/mod.md)
- [error.rs](specifications/modules/error.md)
- [identity/generation.rs](specifications/modules/identity/generation.md)
- [identity/identifier.rs](specifications/modules/identity/identifier.md)
- [identity/mod.rs](specifications/modules/identity/mod.md)
- [identity/namespace.rs](specifications/modules/identity/namespace.md)
- [lib.rs](specifications/modules/lib.md)
- [limits.rs](specifications/modules/limits.md)
- [prelude.rs](specifications/modules/prelude.md)
- [provenance.rs](specifications/modules/provenance.md)
- [result.rs](specifications/modules/result.md)
- [types/bounded.rs](specifications/modules/types/bounded.md)
- [types/digest.rs](specifications/modules/types/digest.md)
- [types/duration.rs](specifications/modules/types/duration.md)
- [types/mod.rs](specifications/modules/types/mod.md)
- [types/quantity.rs](specifications/modules/types/quantity.md)
- [types/timestamp.rs](specifications/modules/types/timestamp.md)
- [types/version.rs](specifications/modules/types/version.md)
- [validation/constraints.rs](specifications/modules/validation/constraints.md)
- [validation/invariant.rs](specifications/modules/validation/invariant.md)
- [validation/mod.rs](specifications/modules/validation/mod.md)

- [Implementation order](specifications/implementation-order.md)
- [Dependency contract](specifications/dependency-contract.md)
- [Error contract](specifications/error-contract.md)
- [Testing contract](specifications/testing-contract.md)

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Property-test lossless encode/decode, overflow boundaries and cancellation races.
