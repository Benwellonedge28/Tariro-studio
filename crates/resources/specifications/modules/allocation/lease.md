# Epoch fencing and scoped charging

**ZIP-RESOURCES-ALLOCATION-LEASE-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/allocation/lease.rs`

## Required implementation behavior

Use opaque lease with assignment, attempt, policy and allocation epoch. Reject charge after expiry or replacement. Expiry marks recovery; it does not prove cleanup or reclaim resources.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-LEASE-T01.** Expired worker cannot publish; occupied capacity remains reserved until confirmed cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
