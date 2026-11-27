# Bounded static checker adapter

**ZIP-VERIFICATION-STATIC-ANALYSIS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/static_analysis.rs`

## Required implementation behavior

Run qualified checker on immutable snapshot without executing candidate changes. Normalize findings with tool version and source evidence.

## Acceptance

**ZIP-VERIFICATION-STATIC-ANALYSIS-T01.** Partial scan or timed-out checker cannot pass mandatory gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
