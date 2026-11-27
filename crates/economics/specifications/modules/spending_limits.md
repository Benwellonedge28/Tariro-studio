# Last-moment spending guard

**ZIP-ECONOMICS-SPENDING-LIMITS-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/spending_limits.rs`

## Required implementation behavior

Apply exact grant and configured ceiling, finite estimate and current reservation before dispatch. Deny zero and unknown limits for paid effects.

## Acceptance

**ZIP-ECONOMICS-SPENDING-LIMITS-T01.** Budget lowered after plan blocks next spend.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
