# Validated inclusive range

**ZIP-FND-RNG-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/validation/constraints.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct U64Range { min: u64, max: u64 } impl U64Range { pub fn new(min: u64, max: u64) -> crate::result::Result<Self>; pub fn check(&self, value: u64) -> crate::result::Result<()>; }
```

## Implementation and invariants

Reject min greater than max as LimitExceeded. Check ordered comparisons without subtraction; bounds themselves are valid. This shape does not choose numbers for the runtime. Callers own range semantics and provenance.

## Acceptance

FND-RNG-T01. Test inverted bounds, singleton, maximum u64, lower and upper violations.
