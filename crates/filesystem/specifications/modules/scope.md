# Filesystem scope intersection

**ZIP-FILESYSTEM-SCOPE-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/scope.rs`

## Boundary and inputs

Bind ScopedRoot to a verified workspace, root identity and generation, typed access rights and current owning policy. Authenticate the request before resolving relative targets. Match normalized component-wise scope, exact operation and required target identities, using the approved platform adapter.

## Behavior and failure handling

Require both source and destination grants for rename and both parent and target bindings where needed. Missing scope, stale root or incompatible backend denies before access. Keep authoritative root handles private, and require fresh policy and identity checks after a root is remounted or rebound.

## Acceptance

**ZIP-FILESYSTEM-SCOPE-T01.** Move from one allowed directory to another disallowed directory. Verify no change at either path. Replace the enrolled root and confirm prior handles or snapshots confer no authority.
