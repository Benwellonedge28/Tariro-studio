# Independent reviewed candidate

**ZIP-REPOSITORY-PULL-REQUESTS-REVIEW-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/review.rs`

## Required implementation behavior

Read exact base and head; capture reviewer and gate results bound to immutable PR head. Fresh head invalidates prior review evidence for changed content.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-REVIEW-T01.** Approval against previous head cannot authorize new candidate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
