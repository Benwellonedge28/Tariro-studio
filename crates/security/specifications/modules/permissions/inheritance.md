# Attenuated scope inheritance

**ZIP-SECURITY-PERMISSIONS-INHERITANCE-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/inheritance.rs`

## Boundary and inputs

Build the effective child scope from a bounded verified ancestor chain, including exact principal and grant lineage. Reject unknown nodes, cycles, stale parent epochs and scope mismatches. Keep originating reasons for denies and affirmative bounds. A role relationship alone cannot supply ancestor proof.

## Behavior and failure handling

Intersect actions, paths, audience and destinations, take tighter comparable ceilings and earlier expiry, and retain required obligations and explicit denies. Exact requirements must agree. A child receives no independent consumable budget beyond the accounted parent limits. Parent revocation blocks new child effects when the authoritative check runs.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-INHERITANCE-T01.** Build nested scopes whose final role allows an ancestor-denied path and a larger quota. Verify both requests deny. Revoke the top-level parent and check the existing descendant reference cannot start work.
