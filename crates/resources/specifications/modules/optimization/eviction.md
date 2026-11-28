# Unpinned cache reclamation

**ZIP-RESOURCES-OPTIMIZATION-EVICTION-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/optimization/eviction.rs`

## Boundary and inputs

Accept bounded candidates for the affected pool. Candidate records identify object, size estimate, last use, expiry, pin/retention generation and owning manager. Exclude pinned, retained or referenced artifacts, including live checkpoints and active model handles. Order eligible expired items first, then by oldest recorded use and stable identity. Rank estimates never imply reclaimed capacity.

## Behavior and failure handling

Call the owning cache or model transition only under valid cleanup or deletion authority. Require the owner to atomically recheck pin and retention generation before deleting or unloading. If generation changed, skip and refresh. Confirm removal and any required teardown evidence before settlement. An ambiguous response retains the hold and requires owner reconciliation by the same operation identity. No runner may directly credit resources from a proposed eviction.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-EVICTION-T01.** Race a pin with eviction and preserve the artifact or handle when the pin commits first. Induce pressure with a live checkpoint and unpinned cache entries on another pool. Retain the checkpoint and reclaim only confirmed eligible entries from the target pool.
