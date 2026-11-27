# Observed check evidence

**ZIP-REPOSITORY-PULL-REQUESTS-CHECKS-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/checks.rs`

## Required implementation behavior

Fetch checks for exact head and map pending/failed/success/skipped/missing distinctly. Record provider check identity and inspected date. Required missing check blocks.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-CHECKS-T01.** A successful older SHA never passes the current PR.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
