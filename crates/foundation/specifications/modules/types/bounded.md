# Bounded byte ownership

**ZIP-FND-BND-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/bounded.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct BoundedBytes(Vec<u8>); impl BoundedBytes { pub fn try_copy(input: &[u8], limit: crate::limits::Limit) -> crate::result::Result<Self>; pub fn as_slice(&self) -> &[u8]; pub fn into_vec(self) -> Vec<u8>; }
```

## Implementation and invariants

Convert usize length with checked conversion to u64 and test the supplied inclusive limit before reserving. Allocate through try_reserve_exact, then copy once without growing; report AllocationFailed on reserve failure. Limit is caller-owned and per construction. Decode through validation, never through direct field assignment. This type does not zeroize or classify data.

## Acceptance

FND-BND-T01. Test exact limit, above limit and zero; ensure denied attempt does not allocate using a test allocator boundary outside first-party code.
