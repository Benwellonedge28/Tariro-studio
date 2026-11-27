# Local and remote ref reconciliation

**ZIP-REPOSITORY-SYNCHRONIZATION-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/synchronization.rs`

## Required implementation behavior

Compare exact expected refs and reviewed ancestry. Fetch and report divergence; apply approved update only under current lease/scope. Never force by default.

## Acceptance

**ZIP-REPOSITORY-SYNCHRONIZATION-T01.** Concurrent remote head movement reports conflict and leaves reviewed local work intact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
