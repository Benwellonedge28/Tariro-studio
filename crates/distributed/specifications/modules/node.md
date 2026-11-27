# Versioned node descriptor

**ZIP-DISTRIBUTED-NODE-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/node.rs`

## Required implementation behavior

Bind stable node ID, authenticated service identity, scope, qualified capabilities and freshness. Keep display names untrusted.

## Acceptance

**ZIP-DISTRIBUTED-NODE-T01.** Duplicate name cannot impersonate previously approved node.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
