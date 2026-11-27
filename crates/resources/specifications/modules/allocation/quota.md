# Scoped quota intersection

**ZIP-RESOURCES-ALLOCATION-QUOTA-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/allocation/quota.rs`

## Required implementation behavior

Compute effective per-domain maxima as minimum among policies and finite available capacity. Exact constraints remain separately enforced and cannot be silently clipped.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-QUOTA-T01.** A per-workspace override cannot raise system cap; denied demand leaves accounting unchanged.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
