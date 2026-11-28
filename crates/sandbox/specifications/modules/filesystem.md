# Sandbox filesystem policy adapter

**ZIP-SANDBOX-FILESYSTEM-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/filesystem.rs`

## Boundary and inputs

Bind the requested file operations to approved canonical root and workspace, permitted rights and verified object identity. Translate the scope to enrolled backend handles. Separate read and mutation permissions and deny unreviewed mount or path resolution. Revalidate identity at controlled access when the source can change.

## Behavior and failure handling

Do not inherit arbitrary mounts, ambient working directory rights or broad host handles. Require a qualified safe resolution mode for linked objects and out-of-scope targets. An unavailable identity proof denies the operation. Record only safe scope references and typed denials. Cleanup verifies temporary roots and resources are retired under their owners.

## Acceptance

**ZIP-SANDBOX-FILESYSTEM-T01.** Stage an approved synthetic root alongside a second root. Attempt an out-of-scope read and confirm no file access. Alter the scope identity after staging and verify a stale handle cannot cross the access boundary.
