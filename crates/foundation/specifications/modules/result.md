# Foundation result alias

**ZIP-FND-RESULT-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/result.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub type Result<T> = core::result::Result<T, crate::error::FoundationError>;
```

## Implementation and invariants

A pure type alias. Do not add blanket conversions, wrap the error or alter the original error variant. Error owns stable public codes.

## Acceptance

FND-RESULT-T01. Assign standard Ok and each FoundationError directly to the alias and assert code and equality are unchanged.
