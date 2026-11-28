# File operation authorization

**ZIP-FILESYSTEM-PERMISSIONS-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/permissions.rs`

## Boundary and inputs

Resolve current actor, exact workspace/root, allowed path and requested rights, policy revision and resource constraints. Take normalized path and operation evidence from the owning trusted scope rather than user-supplied authority labels. Determine disclosure permission before querying protected metadata.

## Behavior and failure handling

Before any effect revalidate exact identity, revision and rights. Read authorization does not grant write, and authority over a source says nothing about a rename destination. Unavailable mandatory evidence denies. Preserve visible denial class without exposing concealed target existence.

## Acceptance

**ZIP-FILESYSTEM-PERMISSIONS-T01.** Compare absence and existence of an unapproved target under an unauthorized reader. Both deny without repository metadata disclosure. Configure read-only scope and confirm a write is denied before staging.
