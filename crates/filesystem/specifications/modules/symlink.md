# Qualified link handling

**ZIP-FILESYSTEM-SYMLINK-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/symlink.rs`

## Boundary and inputs

Classify links or redirected objects through qualified no-follow observations tied to the exact parent and object identity. Untrusted writes cannot traverse such objects. Policy may allow bounded link reads only when the adapter can prove the resulting identity and root containment at the actual access.

## Behavior and failure handling

Distinguish finding a link from following it. Reject unsupported link forms, loops and mode changes when the operation cannot prove the applicable constraints. Preserve metadata only within scope. A symlink cannot carry extra rights or be normalized to an assumed regular file.

## Acceptance

**ZIP-FILESYSTEM-SYMLINK-T01.** Prepare permitted and unapproved synthetic targets and a linked entry. Attempt untrusted mutation and verify no linked target is changed. Use a qualified read fixture to prove only the approved scoped path can resolve.
