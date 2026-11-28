# Scoped role eligibility

**ZIP-SECURITY-PERMISSIONS-RBAC-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/rbac.rs`

## Boundary and inputs

Read verified assigned role IDs and role policy edition for the exact principal and workspace membership. Resolve action eligibility from enrolled descriptors at that version. Treat role labels, actor display names and assignments outside the requested workspace as untrusted or out of scope.

## Behavior and failure handling

Apply explicit policy denies and reject unknown roles required by the request. Return candidate actions and review obligations with provenance, preserving distinctions between local and remote scope. Changes take effect at the current membership and policy checks. A role intersection never bypasses typed attributes, effect capability or separate approval.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-RBAC-T01.** Assign Maintainer in one workspace and Reader in another. Verify the first role cannot qualify publish in the second and an unsupported role edition produces no effect eligibility.
