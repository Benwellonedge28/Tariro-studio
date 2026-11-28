# Deadline negotiation

**ZIP-TOOLS-TIMEOUT-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/timeout.rs`

## Boundary and inputs

Resolve one finite monotonic deadline from request, resource lease, adapter envelope and governing policy. Use compatible live clock domain and checked conversions. Equality ends eligibility. Revalidate immediately before external dispatch and between bounded pages.

## Behavior and failure handling

Cancel waiting under the owner without inferring that a sent request did not take effect. After uncertain dispatch retain the original identity and recover through a scoped independent observation. Cleanup proceeds only under its own approved authority and bounds. Restart does not recreate the old deadline as live authority.

## Acceptance

**ZIP-TOOLS-TIMEOUT-T01.** Expire a receive wait after a synthetic provider accepts the operation. Verify unresolved outcome and no blind retry. Expire before claim and verify zero calls.
