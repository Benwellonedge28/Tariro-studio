# Streaming digest verification

**ZIP-SECURITY-CRYPTOGRAPHY-HASHING-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/hashing.rs`

## Boundary and inputs

Accept an expected tagged digest, expected byte length and bounded input reader. Resolve only an approved algorithm and stream bytes into the qualified adapter. Count bytes with checked arithmetic and require exact end-of-input at the declared length. A digest supplies an integrity binding for bytes. Authority and provenance have their own gates.

## Behavior and failure handling

Reject unsupported tags, excess input, truncation, failed reads and digest mismatch. Publish a verified reference only after the actual stream matches its full expected length and digest. Reuse verification only for the same immutable object. If a mutable source cannot prove identity between verification and use, stage verified immutable bytes before consumption.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-HASHING-T01.** Hash an exact fixture, then alter one byte, remove the final byte and add another byte. Only the exact case yields a verified reference. A source replacement cannot reuse a previous mutable handle.
