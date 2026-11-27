# CPU share discovery

**ZIP-RESOURCES-DISCOVERY-CPU-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/cpu.rs`

## Required implementation behavior

Record logical CPU availability, affinity/cgroup quotas where supported and effective schedulable share. Do not substitute physical core totals for enforceable quotas.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-CPU-T01.** Synthetic host with more logical CPUs than sandbox quota yields sandbox bound.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
