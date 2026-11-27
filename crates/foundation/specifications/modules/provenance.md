# Immutable source provenance reference

**ZIP-FND-PROV-001 · v1.0 · Owner:** Foundation maintainers. **Maturity:** Contract candidate. **Planned source:** `crates/foundation/src/provenance.rs`.

## API and ownership

Rust interface declarations (implementation bodies omitted).

```rust
pub struct Provenance { pub source: crate::identity::identifier::Identifier, pub revision_digest: crate::types::digest::Digest, pub observed_at: crate::types::timestamp::Timestamp }
```

## Implementation and invariants

The creator binds observation to immutable bytes and a typed source identity. Value store is immutable by convention after publication; correction creates a new record with independent audit evidence. Validate source kind at the consuming schema. A provenance value is neither verified evidence nor access proof.

## Acceptance

FND-PROV-T01. Construct two observations at different times and require exact values survive enclosing schema round-trip. Verification must reject mismatched revision digest.
