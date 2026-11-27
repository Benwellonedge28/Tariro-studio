# Identity module boundary

**ZIP-FND-IDENT-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/identity/mod.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub mod generation; pub mod identifier; pub mod namespace;
```

## Implementation and invariants

Expose modules without re-exporting a raw Uuid or granting identity roles. No generation or registry side effect on link.

## Acceptance

FND-IDENT-T01. Compile a consumer for the three paths and reject direct access to internal representation fields.
