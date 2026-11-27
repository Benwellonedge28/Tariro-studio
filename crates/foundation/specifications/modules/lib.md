# Workspace boundary

**ZIP-FND-ROOT-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/lib.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
#![forbid(unsafe_code)]

pub mod cancellation;
pub mod contracts;
pub mod error;
pub mod identity;
pub mod limits;
pub mod prelude;
pub mod provenance;
pub mod result;
pub mod types;
pub mod validation;
```

## Implementation and invariants

Keep constructor fields private through the crate boundary. Load no policy, keyring, platform or async runtime on link. Add no first-party dependency.

## Acceptance

FND-ROOT-T01. Compile a downstream fixture importing each declared module. Verify it cannot construct private fields or enter an unsafe workspace member.
