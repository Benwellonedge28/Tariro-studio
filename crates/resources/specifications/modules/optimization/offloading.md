# Authorized placement change

**ZIP-RESOURCES-OPTIMIZATION-OFFLOADING-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/optimization/offloading.rs`

## Required implementation behavior

Select eligible node using capability, locality, allowed data classes, lease and cost. Verify node advertisement freshness and transmit only under separate permission.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-OFFLOADING-T01.** Local GPU shortage cannot silently activate a remote provider or alter spending authorization.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
