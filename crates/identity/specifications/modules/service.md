# Service identity

**ZIP-IDENTITY-SERVICE-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/service.rs`

## Boundary and inputs

Represent a non-interactive service principal scoped to trusted issuer, operating workspace and approved action family. Validate the configured audience and current adapter credential generation. The enrollment receipt binds verified service identity to the owning integration, without publishing secret bytes.

## Behavior and failure handling

Reject interactive-user substitution for service proof. Rotate credential references through the owning Security boundary and update the active generation without widening capability or account scope. Old and current receipts remain attributable to the same stable service identity. A stale or retired generation cannot authorize new work.

## Acceptance

**ZIP-IDENTITY-SERVICE-T01.** Rotate an enrolled service's reference. Verify its stable identity is unchanged and the old credential cannot authenticate. Submit a user-scoped proof with equal display attributes and verify rejection.
