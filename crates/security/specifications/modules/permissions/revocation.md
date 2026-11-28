# Revocation epoch enforcement

**ZIP-SECURITY-PERMISSIONS-REVOCATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/revocation.rs`

## Boundary and inputs

Compare the current principal, session, membership, capability lineage and grant epoch where applicable at the protected claim boundary. Read authoritative generation rather than relying on cached permits or asynchronously delivered events. Identity and Governance commit their own revocations under expected revisions.

## Behavior and failure handling

A newer relevant epoch rejects new work from the old snapshot. Require live verification again after restart. Previously claimed or committed operations retain original receipts and reconcile under separate cleanup or read authority. State or clock unavailability blocks newly protected work. No stale reference can regain authority through snapshot restoration.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-REVOCATION-T01.** Revoke a capability, lose the invalidation notification and restart. Verify the old reference cannot start a new effect and an already confirmed operation remains auditable through its original receipt.
