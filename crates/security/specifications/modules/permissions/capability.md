# Effect-specific capability checking

**ZIP-SECURITY-PERMISSIONS-CAPABILITY-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/capability.rs`

## Boundary and inputs

Validate an opaque effect capability against its trusted issuer and supported edition, exact subject, workspace, action, canonical target, scope, expiry and live lineage. Require matching active epochs and constrained parent scope. Presence of the handle, an equal target string or a stored capability ID is insufficient proof.

## Behavior and failure handling

Intersect capability coverage with current assignment and policy. Recheck its binding at each protected boundary and compare exact target and effect digests for any one-time scope. A capability cannot substitute for an approval, resource lease or separate egress permission. Expired or revoked references may support history only.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-CAPABILITY-T01.** Pair a read capability with a write request to the same target and verify rejection. Then try a stale parent epoch and altered destination under a valid effect name. Both deny before an adapter runs.
