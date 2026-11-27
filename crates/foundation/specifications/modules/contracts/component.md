# Static component declaration

**ZIP-FND-CMP-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/contracts/component.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct ComponentDescriptor<'a> { pub id: &'a super::super::identity::namespace::Namespace, pub version: crate::types::version::Version, pub capabilities: &'a [super::capability::CapabilityDescriptor<'a>] }
```

## Implementation and invariants

Borrow qualified namespace and immutable capabilities from the owning component. Registry checks uniqueness and policy when importing; descriptor confers no execution permission. No closure, dynamic allocator or persistence in the descriptor.

## Acceptance

FND-CMP-T01. Compile descriptor borrowing fixtures and confirm lifetime rejection for a returned descriptor whose declaration expired.
