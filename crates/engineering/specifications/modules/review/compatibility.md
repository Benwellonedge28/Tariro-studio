# Compatibility change review

**ZIP-ENGINEERING-REVIEW-COMPATIBILITY-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/review/compatibility.rs`

## Required implementation behavior

Evaluate versions, data migration and downgrade paths under reviewed consumer profiles. Require actual fixture compatibility evidence.

## Acceptance

**ZIP-ENGINEERING-REVIEW-COMPATIBILITY-T01.** Changed mandatory wire semantics cannot pass as backward compatible.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
