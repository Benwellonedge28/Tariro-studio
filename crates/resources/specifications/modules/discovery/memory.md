# Allocatable host memory

**ZIP-RESOURCES-DISCOVERY-MEMORY-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/memory.rs`

## Boundary and inputs

Collect enforceable host and containment memory ceilings plus observations necessary to normalize each scope. Record byte counts, scope, sampling generation and whether a sample represents enforced total and outside workload use, or observed free and measured managed occupants. Measurement for one scope cannot be copied into a different accounting basis.

## Behavior and failure handling

Normalize using the [allocator](../allocation/allocator.md). Require coherent scope for total, free, managed occupancy and headroom. Compare the applicable normalized ceilings and use the strictest before deducting holds exactly once. Treat omitted enforcement or stale observations as unknown for a hard guarantee. A known zero capacity is meaningful and never triggers a fallback.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-MEMORY-T01.** Compare host free memory and a tighter containment limit. Verify that the authoritative cap remains contained. Reuse ZIP-RES-FIX-002 in the [admission fixtures](../../../../../contracts/acceptance/resources/admission-fixtures.json) to check equivalent evidence bases and no double deduction.
