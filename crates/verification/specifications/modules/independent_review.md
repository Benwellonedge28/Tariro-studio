# Independent reviewer gate

**ZIP-VERIFICATION-INDEPENDENT-REVIEW-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/independent_review.rs`

## Required implementation behavior

Compare author and reviewer identity and role/conflict policy. Bind review to candidate digest, actual findings and closed status. Agent role labels do not establish independence.

## Acceptance

**ZIP-VERIFICATION-INDEPENDENT-REVIEW-T01.** Author reviewing own restricted change cannot satisfy an independent gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
