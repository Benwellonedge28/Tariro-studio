# Foundation crate design

**Contract version** 1.0. Master design §9. Planned implementation.

## Responsibility and dependencies

Decode, validate, canonicalize, then construct. Cancellation is sticky and wakes all registered observers. Use synchronized monotonic deadlines and UTC wall time for audit only.

First-party dependencies: No first-party crate dependency.

- [Architecture and component boundaries](../../specifications/0100-architecture/component-boundaries.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `parse_identity(raw)`
- `checked_quantity(unit,value)`
- `compatibility(local,peer)`

Record families: Typed UUID IDs, SemVer, tagged SHA-256 digests and bounded byte/count/time newtypes. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Identifier { kind: IdKind, uuid: Uuid }`
- `Digest { algorithm: DigestAlgorithm, bytes: [u8`
- `32] }`
- `MonotonicDeadline(Duration)`
- `Version { major: u16, minor: u16, patch: u16 }`

- `parse_identity(expected_kind: IdKind, value: &str) -> Result<Identifier>`
- `compatibility(local: Version, peer: Version) -> Result<NegotiatedVersion>`

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

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Property-test lossless encode/decode, overflow boundaries and cancellation races.
