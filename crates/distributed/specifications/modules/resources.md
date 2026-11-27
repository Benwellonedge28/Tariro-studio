# Node-local capacity budgets

**ZIP-DISTRIBUTED-RESOURCES-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/resources.rs`

## Required implementation behavior

Pin capacity revision and admissible units per node, enforce separate finite leases and note unknown bounds. Do not aggregate unrelated pools by default.

## Acceptance

**ZIP-DISTRIBUTED-RESOURCES-T01.** Advertised total differs from enforceable capacity and latter limits placement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
