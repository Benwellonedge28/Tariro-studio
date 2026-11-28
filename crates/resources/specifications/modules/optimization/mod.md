# Approved optimization boundary

**ZIP-RESOURCES-OPTIMIZATION-MOD-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/optimization/mod.rs`

## Boundary and inputs

Expose bounded proposal interfaces for [adaptive sizing](adaptive.md), [eviction](eviction.md) and [offloading](offloading.md). Inputs are verified current capacity snapshots, effective policy revisions and an approved request. Return typed proposals with affected scope, prerequisites and observations. Route acceptance to the respective owning service through composition.

## Behavior and failure handling

Require a fresh grant and resource admission before new execution, and separate deletion or cleanup authority for reclaim actions. Stale or conflicting observations force recomputation. Pressure can limit eligible choices, and creates no grant, network permission or billing ceiling. The optimization module does not issue an effect, close a reservation or enlarge a lease.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-MOD-T01.** Supply a plausible proposal with a revoked grant, then with stale capacity. Verify no dispatch, cache deletion or transfer. Repeat with a qualified proposal and demonstrate that execution still passes through the owning admission and effect boundary.
