# Qualified remote capability claims

**ZIP-DISTRIBUTED-CAPABILITIES-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/capabilities.rs`

## Required implementation behavior

Match exact protocol, target, platform and isolation capabilities with reviewed evidence. Reject unknown mandatory traits.

## Acceptance

**ZIP-DISTRIBUTED-CAPABILITIES-T01.** Unqualified platform is not assigned work requiring containment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
