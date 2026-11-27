# Distributed profile rules

**ZIP-CONFIGURATION-PROFILES-DISTRIBUTED-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/profiles/distributed.rs`

## Required implementation behavior

Consider remote workers only when both node identity and egress are authorized. Capacity from each node is its own revisioned pool, and local work remains viable without mesh discovery.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-DISTRIBUTED-T01.** Stale node snapshot and disconnected mesh cannot widen local admission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
