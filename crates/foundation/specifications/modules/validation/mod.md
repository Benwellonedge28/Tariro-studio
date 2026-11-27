# Validation module wiring

**ZIP-FND-VAL-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/validation/mod.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub mod constraints; pub mod invariant;
```

## Implementation and invariants

Keep sibling modules pure and callable from adapters without IO dependencies. Expose no fallback validation mode.

## Acceptance

FND-VAL-T01. Compile both module paths and confirm omitted raw construction remains inaccessible.
