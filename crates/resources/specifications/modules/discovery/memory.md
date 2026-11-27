# Allocatable host memory

**ZIP-RESOURCES-DISCOVERY-MEMORY-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/memory.rs`

## Required implementation behavior

Observe host and containment ceilings, available bytes and freshness; use the tighter enforceable bound and do not double-count current reservations. Track source for diagnostics.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-MEMORY-T01.** Host free RAM larger than cgroup limit still yields bounded demand.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
