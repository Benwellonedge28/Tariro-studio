# Foundation contract modules

**ZIP-FND-PORTS-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/contracts/mod.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub mod capability; pub mod compatibility; pub mod component; pub mod lifecycle;
```

## Implementation and invariants

Keep ports pure. Do not register components or access storage at import. Error types and compatibility checks use foundation types only.

## Acceptance

FND-PORTS-T01. Compile imports for all ports without daemon features.
