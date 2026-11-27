# Foundation error module

**ZIP-FND-ERR-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** D4 candidate. **Source:** `crates/foundation/src/error.rs`. Implement before the other file contracts in this batch.

## Interface

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum FoundationError {
    InvalidIdentifier,
    NilIdentifier,
    InvalidDigestEncoding,
    UnsupportedDigestAlgorithm,
    LimitExceeded,
    QuantityOverflow,
    Cancelled,
    ObserverLimit,
    AllocationFailed,
    SynchronizationFailed,
}

impl FoundationError {
    pub const fn code(self) -> &'static str;
}
```

Implement `std::fmt::Display` and `std::error::Error`; omit source errors at this leaf boundary. A sibling result module may alias `Result<T, FoundationError>` without changing semantics. Public mapping is exact: `invalid_identifier`, `nil_identifier`, `invalid_digest_encoding`, `unsupported_digest_algorithm`, `limit_exceeded`, `quantity_overflow`, `cancelled`, `observer_limit`, `allocation_failed`, `synchronization_failed`, in variant order. A message may use the stable code as its complete display text. Callers own correlation IDs, context and retry policy. Re-export decisions belong to the crate root.

## Behavior and boundaries

Use deterministic allocation-free matches for codes and display. Error values own no pointers except static strings returned by the method. Never carry a secret, input document, credential or mutable source. Foundational codes are non-retryable by default; the caller may re-admit after policy or capacity changes. `SynchronizationFailed` blocks the affected handle until it is discarded or explicitly recovered.

The module has no durable state, threads, I/O, runtime configuration, cancellation or platform branches. Wire adapters use the code and their versioned envelope; Rust enum discriminants are private. No implicit retries or telemetry originate here. A newly introduced code must be additive and mapped explicitly at public transport boundaries.

## Acceptance

FND-ERR-T01 asserts every listed code and display value, case and order. FND-ERR-T02 verifies enum equality and that all values are Send and Sync. FND-ERR-T03 injects malformed input containing a synthetic secret through calling contracts and verifies the error surface contains only the prescribed code. Design review compares the enum against the consumers in this batch and the [error standard](../../../../ERROR_STANDARD.md).
