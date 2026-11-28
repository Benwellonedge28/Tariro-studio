# Network capacity probe

**ZIP-RESOURCES-DISCOVERY-NETWORK-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/discovery/network.rs`

## Boundary and inputs

Collect interface and containment scope, supported traffic control, and a qualified directional or aggregate throughput bound from a registered adapter. Units are bytes per second and must correspond to the dimension binding accepted by [allocation](../allocation/allocator.md). Advertised interface speed and measured samples are advisory unless the required guarantee can be enforced.

## Behavior and failure handling

Default to local read-only observation. Any probe that would send external traffic requires separately authorized egress, approved target, bounded budget and the owning networking adapter. Without it, preserve unknown active-measurement evidence and make zero calls. A missing shaper or ambiguous interface mapping prevents hard bandwidth admission. Discovery issues no transfer permit and never modifies network configuration.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-NETWORK-T01.** Run in a local-only fixture with an instrumented adapter and verify zero active traffic. Offer a fast advertised interface without traffic control and verify the hard bound remains unavailable. Distinguish a qualified zero-throughput observation from an unsupported measurement.
