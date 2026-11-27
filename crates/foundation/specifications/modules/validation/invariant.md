# Nonpanicking invariant check

**ZIP-FND-INV-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/validation/invariant.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub fn require(condition: bool, error: crate::error::FoundationError) -> crate::result::Result<()>;
```

## Implementation and invariants

Return Ok on true, otherwise Err with the supplied value. The caller decides which proof and error apply; the function performs no logging, panic, retry, or repair. Never use assertions on untrusted values.

## Acceptance

FND-INV-T01. Test both conditions with every supplied error and assert successful calls have no visible effects.
