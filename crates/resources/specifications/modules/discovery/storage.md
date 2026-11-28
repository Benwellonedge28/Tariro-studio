# Volume capacity and containment

**ZIP-RESOURCES-DISCOVERY-STORAGE-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/storage.rs`

## Boundary and inputs

Resolve the actual staging location to a trusted, canonical volume accounting identity using an injected filesystem capability observation. Bind bytes, applicable quota and freshness to the original workspace scope and mounted volume generation. Identify the underlying accounting domain for aliases to avoid counting the same free space twice.

## Behavior and failure handling

Measure the relevant volume and independently enforceable quota in bytes. Preserve additional quota coordinates where their units differ and the consuming contract defines them. Require volume identity to remain current when admitting the write. A path string, a free-space report from another volume or unsupported quota provides no hard guarantee. The [allocator](../allocation/allocator.md) normalizes holds. Discovery neither creates a staging directory nor reserves space.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-STORAGE-T01.** Present equal free bytes on two volumes and bind the request to one. Verify only that pool may satisfy it. Replace the mount after measurement and reject the stale observation. Test overlapping free capacity under a tighter workspace quota without a duplicate debit.
