# Observed correctness review

**ZIP-ENGINEERING-REVIEW-CORRECTNESS-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/review/correctness.rs`

## Required implementation behavior

Compare actual requirement evidence to exact artifact, mark unverified assumptions and use stable verdict.

## Acceptance

**ZIP-ENGINEERING-REVIEW-CORRECTNESS-T01.** Missing mandatory observation blocks success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
