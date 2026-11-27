# Comparable performance fixtures

**ZIP-TESTING-PERFORMANCE-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/performance.rs`

## Required implementation behavior

Record warmup, measurement window, workload, configuration and admitted/observed resources. Apply only qualified thresholds.

## Acceptance

**ZIP-TESTING-PERFORMANCE-T01.** Mismatch in hardware/profile prevents direct regression claim.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
