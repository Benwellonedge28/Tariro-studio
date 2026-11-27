# Privilege-specific merge

**ZIP-REPOSITORY-GIT-MERGE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/merge.rs`

## Required implementation behavior

Require separate scope, approved source and exact target ref, verification gates and conflict policy. Verify resulting tree and commit. Unknown result enters reconciliation.

## Acceptance

**ZIP-REPOSITORY-GIT-MERGE-T01.** A generic branch write grant cannot merge into main.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
