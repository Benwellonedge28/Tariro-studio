# Exact batch gate

**ZIP-VERIFICATION-REPOSITORY-BATCH-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/repository/batch.rs`

## Required implementation behavior

Count unique allowed final paths against the assignment's approved count; require verification for each touched file. Record manifest digest.

## Acceptance

**ZIP-VERIFICATION-REPOSITORY-BATCH-T01.** Duplicate path cannot inflate count, short exact batch remains blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
