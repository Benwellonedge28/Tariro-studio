# Lease-safe unload

**ZIP-MODELS-UNLOADING-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/unloading.rs`

## Required implementation behavior

Stop new sessions, drain or cancel admitted users, release storage/device resources only after confirmed teardown. Respect active cache pins.

## Acceptance

**ZIP-MODELS-UNLOADING-T01.** Pinned model cannot be unloaded during active admitted execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
