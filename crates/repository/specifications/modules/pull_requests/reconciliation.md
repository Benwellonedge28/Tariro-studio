# External PR effect reconciliation

**ZIP-REPOSITORY-PULL-REQUESTS-RECONCILIATION-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/reconciliation.rs`

## Required implementation behavior

Search exact provider repo, immutable base/head and recorded effect marker; verify actual returned identity. One exact result completes, ambiguity blocks, confirmed absence permits authorized retry.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-RECONCILIATION-T01.** Two candidate matches cause blocked without another create.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
