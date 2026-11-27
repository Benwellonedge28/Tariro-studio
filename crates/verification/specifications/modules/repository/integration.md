# Observed repository effect verification

**ZIP-VERIFICATION-REPOSITORY-INTEGRATION-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/repository/integration.rs`

## Required implementation behavior

Read exact remote identity, refs, PR/check state and operation evidence. Unknown or stale provider data cannot certify publication.

## Acceptance

**ZIP-VERIFICATION-REPOSITORY-INTEGRATION-T01.** Passing checks for previous head fail current integration gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
