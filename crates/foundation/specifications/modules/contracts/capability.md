# Capabilities as data

**ZIP-FND-CAP-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/contracts/capability.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct CapabilityDescriptor<'a> { pub name: &'a crate::identity::namespace::Namespace, pub version: crate::types::version::Version } impl CapabilityDescriptor<'_> { pub fn supports(&self, requested: &Self) -> bool; }
```

## Implementation and invariants

Require namespace equality, equal major and offered minor at least requested minor. Patch is diagnostic only for this feature check; exact patch requirements live in the provider contract. Capability does not confer authorization.

## Acceptance

FND-CAP-T01. Check lower minor denied, equal or higher accepted, new major denied and same version wrong namespace denied.
