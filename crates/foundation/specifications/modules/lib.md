# Workspace boundary

**ZIP-FND-ROOT-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/lib.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
Declare #![forbid(unsafe_code)]. Declare pub mod cancellation, contracts, error, identity, limits, prelude, provenance, result, types, validation in lexical order; do not glob re-export those modules.
```

## Implementation and invariants

Keep constructor fields private through the crate boundary. Load no policy, keyring, platform or async runtime on link. Add no first-party dependency.

## Acceptance

FND-ROOT-T01. Compile a downstream fixture importing each declared module. Verify it cannot construct private fields or enter an unsafe workspace member.
