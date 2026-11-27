# Quality verdict composition

**ZIP-VERIFICATION-QUALITY-MOD-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/quality/mod.rs`

## Required implementation behavior

Evaluate correctness, completeness, consistency and maintainability by separate required/optional gates, preserving evidence and unresolved findings.

## Acceptance

**ZIP-VERIFICATION-QUALITY-MOD-T01.** Optional quality finding does not conceal failed mandatory gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
