# Comparable runtime improvement

**ZIP-ENGINEERING-OPTIMIZATION-PERFORMANCE-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/optimization/performance.rs`

## Required implementation behavior

Compare before/after fixture, host and limits, and quantify uncertainty. Check no correctness regression.

## Acceptance

**ZIP-ENGINEERING-OPTIMIZATION-PERFORMANCE-T01.** Different host configuration does not qualify claimed improvement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
