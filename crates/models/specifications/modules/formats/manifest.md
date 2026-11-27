# Portable manifest representation

**ZIP-MODELS-FORMATS-MANIFEST-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/formats/manifest.rs`

## Required implementation behavior

Decode version, canonical asset references, digests and constraints, rejecting unknown required fields. Verify exact signed bytes before trust.

## Acceptance

**ZIP-MODELS-FORMATS-MANIFEST-T01.** Path traversal and conflicting shard identifiers are rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
