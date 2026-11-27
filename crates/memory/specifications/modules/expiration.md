# Retention expiry projection

**ZIP-MEMORY-EXPIRATION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/expiration.rs`

## Required implementation behavior

Use approved time/retention state, hide expired records before retrieval, schedule bounded cleanup while preserving required evidence.

## Acceptance

**ZIP-MEMORY-EXPIRATION-T01.** Expired record cannot be returned during delayed deletion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
