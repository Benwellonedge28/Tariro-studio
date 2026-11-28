# Private staging lifecycle

**ZIP-FILESYSTEM-TEMPORARY-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/temporary.rs`

## Boundary and inputs

Allocate private staged objects under the authorized destination parent on its qualified volume. Bind attempt identity, owning directory, resource allowance and initial object identity before writing. Choose an exclusive backend-created name and never reuse an unverified preexisting object.

## Behavior and failure handling

Keep the stage private until verification and publication. Reclaim only objects proven owned and abandoned or no longer required after exact promotion reconciliation. An uncertain effect retains staging and its references. Check current cleanup authority before removal and use the owner to settle any resource hold.

## Acceptance

**ZIP-FILESYSTEM-TEMPORARY-T01.** Populate a target directory with an unrelated file and a staged object whose promotion is unresolved. Cleanup leaves both intact. Resolve the stage as owned abandoned and verify only it becomes eligible for removal.
