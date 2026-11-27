# Version negotiation

**ZIP-FND-COMP-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/contracts/compatibility.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct NegotiatedVersion { pub major: u16, pub minor: u16 } pub fn negotiate(local: crate::types::version::Version, peer: crate::types::version::Version) -> Option<NegotiatedVersion>;
```

## Implementation and invariants

Require equal major; select minimum minor. Patch does not alter wire shape. Return None before any effect if major differs. The adapter maps None to its public UnsupportedVersion code and verifies that required features exist at the agreed minor.

## Acceptance

FND-COMP-T01. Check symmetry, mismatched majors and mixed minor ordering. Test that adapter can deny a feature after successful negotiation.
