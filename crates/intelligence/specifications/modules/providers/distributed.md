# Distributed inference provider

**ZIP-INTELLIGENCE-PROVIDERS-DISTRIBUTED-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/providers/distributed.rs`

## Required implementation behavior

Select authenticated admitted node, bind context/epoch and resource lease, verify final output and stale state. Transfer needs explicit egress scope.

## Acceptance

**ZIP-INTELLIGENCE-PROVIDERS-DISTRIBUTED-T01.** Old node result cannot replace current verified response.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
