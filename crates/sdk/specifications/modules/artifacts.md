# Bounded artifact client

**ZIP-SDK-ARTIFACTS-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/artifacts.rs`

## Required implementation behavior

Verify exact ref/digest/scope, stream finite bytes and distinguish partial read, rechecking current policy before transfer.

## Acceptance

**ZIP-SDK-ARTIFACTS-T01.** Invalid digest never returns completed artifact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
