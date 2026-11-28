# GPU memory by device

**ZIP-RESOURCES-DISCOVERY-GPU-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/gpu.rs`

## Boundary and inputs

Bind each registered physical device and isolation domain to a stable adapter identity. Record supported inference capabilities, enforced or measured capacity basis, memory quantities, provenance and age. Expose physical totals as advisory metadata unless the platform proves enforcement to the selected workload. Mark offline, missing or driver-inaccessible capacity as unknown.

## Behavior and failure handling

Give the [allocator](../allocation/allocator.md) capacity evidence per canonical AcceleratorBytes dimension. Multiple device handles pointing to the same accounting domain must not create duplicate pools. Discover sharing topology only as qualified metadata. A shard plan must bind every participating physical pool and remain a separate inference decision. Discovery never pools disjoint device RAM into one admission coordinate.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-GPU-T01.** Provide two adequate summed pools and an unsharded request that exceeds each device. Verify rejection. Add an alias handle for the same device and verify no additional capacity. Inject driver failure and observe unknown capacity instead of physical-total fallback.
