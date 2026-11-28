# CPU share discovery

**ZIP-RESOURCES-DISCOVERY-CPU-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/cpu.rs`

## Boundary and inputs

Consume a trusted adapter sample for the same host, execution group and observation generation. Read effective schedulable affinity or CPU set, independently enforceable quota and its period where present. Convert the affinity count to millicores and normalize quota by flooring the checked ratio of quota to period in millicores. A valid observation of no schedulable share is known zero.

## Behavior and failure handling

Apply the smallest compatible hard bound. Reject zero period, arithmetic overflow, stale evidence and a missing mandatory control as unavailable. If a host or sandbox cannot qualify an enforceable CPU bound, expose its descriptive capacity only as advisory. Preserve identity and accounting basis for the [allocator](../allocation/allocator.md), which owns holds and headroom. Probe CPU without task dispatch or quota mutation.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-CPU-T01.** Measure a synthetic host with many logical CPUs and a smaller contained quota. Verify the smaller share sets the bound, a fractional result rounds down, and an unavailable mandatory quota cannot be replaced by the host count.
