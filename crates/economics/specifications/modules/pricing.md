# Versioned approved price rules

**ZIP-ECONOMICS-PRICING-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/pricing.rs`

## Required implementation behavior

Use approved rate, currency, unit, source/effective time and deterministic rounding. Unknown or stale price requires policy.

## Acceptance

**ZIP-ECONOMICS-PRICING-T01.** Changing rate qualifies as new estimate, not a silent charge adjustment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
