# Version triplet

**ZIP-FND-VER-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/types/version.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct Version { pub major: u16, pub minor: u16, pub patch: u16 } impl Version { pub fn parse(value: &str) -> crate::result::Result<Self>; }
```

## Implementation and invariants

Require exactly three decimal components separated by dots. Accept digit zero alone and reject leading zeros, whitespace, suffixes and missing components as InvalidIdentifier. Accumulate each component with checked multiply/add and return QuantityOverflow at its representational bound. Serialize canonical decimal triplet. Compare using tuple ordering. Provider SemVer prerelease handling belongs to its adapter.

## Acceptance

FND-VER-T01. Check 0.0.0, 65535.0.1, 65536.0.1, 01.1.1 and 1.1.1-beta. Verify ordering across major/minor/patch.
