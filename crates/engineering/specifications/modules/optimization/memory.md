# Memory behavior evidence

**ZIP-ENGINEERING-OPTIMIZATION-MEMORY-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/optimization/memory.rs`

## Required implementation behavior

Measure designated workload and peak memory under same profile/reservations. Check failure paths and retained resource ownership.

## Acceptance

**ZIP-ENGINEERING-OPTIMIZATION-MEMORY-T01.** Lower memory after dropping mandatory work fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
