# Injected UUID creation

**ZIP-FND-GEN-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/identity/generation.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub trait UuidSource { fn next_uuid(&mut self) -> crate::result::Result<uuid::Uuid>; } pub fn generate(source: &mut dyn UuidSource, kind: super::identifier::IdKind) -> crate::result::Result<super::identifier::Identifier>;
```

## Implementation and invariants

Call the injected source exactly once, propagate typed failures, and apply Identifier::from_uuid. Reject nil without retry. Production source quality and duplicate detection belong to the consuming registry; fixture sources must be deterministic. No global PRNG or hidden clock.

## Acceptance

FND-GEN-T01. Inject valid and nil outputs and failing source; record one call on each path. Verify kind is copied exactly.
