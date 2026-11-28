# Organization identity boundary

**ZIP-IDENTITY-ORGANIZATION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/organization.rs`

## Boundary and inputs

Maintain typed organization identity with immutable receipt and revisioned membership links, each bound to verified principal, membership status and approved role references. Display names may be duplicated and carry no permission. Authorize readers and writers under exact organization scope.

## Behavior and failure handling

Use canonical organization and principal identifiers as membership coordinates. Revision-check changes, including removal and status transitions. A role projection requires qualified current membership and remains subject to workspace and Security policies. Removed records remain historically attributable but cannot support future authority.

## Acceptance

**ZIP-IDENTITY-ORGANIZATION-T01.** Create two organizations with identical names and independent memberships. Verify updates and reads for the first cannot resolve the second's records and a removed member fails current projection.
