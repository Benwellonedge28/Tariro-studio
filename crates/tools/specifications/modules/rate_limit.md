# Scoped tool rate accounting

**ZIP-TOOLS-RATE-LIMIT-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/rate_limit.rs`

## Required implementation behavior

Reserve usage for provider/operation under validated budget, account observed charge and release only reconciled unused capacity. Respect retry-after without widening deadline.

## Acceptance

**ZIP-TOOLS-RATE-LIMIT-T01.** Parallel calls cannot overspend a shared scoped rate budget.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
