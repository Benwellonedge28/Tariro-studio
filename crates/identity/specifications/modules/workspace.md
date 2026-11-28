# Workspace membership boundary

**ZIP-IDENTITY-WORKSPACE-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/workspace.rs`

## Boundary and inputs

Bind membership to a typed workspace and verified principal, authority source, revision and active status. Resolve only the requested scope after authenticating the caller. Iterate or expose membership detail only within the caller's independently permitted audience.

## Behavior and failure handling

Use pinned membership for audit attribution and current membership for new effects. A changed generation or removed membership defeats cached proof and invalidates affected scoped sessions at their next live boundary. Never discover permissions by matching names across workspaces. Keep historical evidence supplied under authorized reads.

## Acceptance

**ZIP-IDENTITY-WORKSPACE-T01.** Resolve the same person in one legitimate and one foreign workspace. Deny the foreign lookup. Remove the allowed membership then replay cached context and verify neither new claim nor private disclosure is accepted.
