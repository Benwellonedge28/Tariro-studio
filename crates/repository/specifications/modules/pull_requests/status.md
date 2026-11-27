# Versioned PR status

**ZIP-REPOSITORY-PULL-REQUESTS-STATUS-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/status.rs`

## Required implementation behavior

Fetch through authorized provider and retain exact repo ID, PR ID, base/head, open/draft/merged and check state. Use current observation, not inferred success.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-STATUS-T01.** Draft is distinguishable from closed and merged; response mismatch rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
