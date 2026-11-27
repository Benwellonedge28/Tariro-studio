# Unpinned cache reclamation

**ZIP-RESOURCES-OPTIMIZATION-EVICTION-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/optimization/eviction.rs`

## Required implementation behavior

Rank eligible cache entries within affected pool by expiry/last-use then stable ID. Recheck pin and minimum required evidence retention before delete. Reclaim only after receipt.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-EVICTION-T01.** Artifact referenced by live checkpoint survives eviction under disk pressure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
