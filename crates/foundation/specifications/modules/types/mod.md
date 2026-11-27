# Common value modules

**ZIP-FND-TYP-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/mod.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub mod bounded; pub mod digest; pub mod duration; pub mod quantity; pub mod timestamp; pub mod version;
```

## Implementation and invariants

No runtime setup or blanket serde. Enclosing schemas opt into each value encoding and validate private invariants on decode.

## Acceptance

FND-TYP-T01. A downstream consumer can access all six module paths; linking requires no daemon or provider.
