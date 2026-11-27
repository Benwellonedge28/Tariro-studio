# Model lifecycle errors

**ZIP-MODELS-ERROR-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/error.rs`

## Required implementation behavior

Separate invalid identity, unsupported format, failed integrity, ambiguous download, denied license, unavailable device and revoked scope. Preserve safe IDs.

## Acceptance

**ZIP-MODELS-ERROR-T01.** Digest mismatch cannot be reported as a usable model.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
