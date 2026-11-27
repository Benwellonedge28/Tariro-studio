# Digest and reference validation

**ZIP-STORAGE-INTEGRITY-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/integrity.rs`

## Required implementation behavior

verify_object(expected: ObjectRef, reader: BoundedReader) -> Result<VerifiedObject, StorageError>. Charge bytes and reject wrong digest, length or trailing bytes. Use streaming hashing and do not expose verified handle prematurely.

## Acceptance

**ZIP-STORAGE-INTEGRITY-T01.** Corrupt byte, truncation, extra byte and valid object fixtures produce distinct outcomes as designed.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
