# Effect-specific tool permissions

**ZIP-TOOLS-PERMISSIONS-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/permissions.rs`

## Boundary and inputs

Resolve current actor, exact approved action, normalized arguments, affected paths or destinations and applicable data class. Compare current grant and epoch, descriptor policy, lease, deadline and required separate approval. Missing protected-path or egress scope denies.

## Behavior and failure handling

Bind the decision to canonical effect evidence and revalidate immediately before the owning claim. A general capability or discovery result cannot authorize another effect class. A revocation committed before claim yields zero calls. Prior claimed effects remain subject to qualified reconciliation.

## Acceptance

**ZIP-TOOLS-PERMISSIONS-T01.** Try to publish to a synthetic remote destination using read-only permission for the same tool. Verify denial before any transfer. Replace policy revision before claim and confirm it is not bypassed by a cached decision.
