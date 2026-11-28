# Scoped directory operations

**ZIP-FILESYSTEM-DIRECTORY-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/directory.rs`

## Boundary and inputs

Accept a scoped directory handle with authorized rights and expected generation. List entries as typed names, object categories and authorized metadata. Do not resolve a link merely to classify it. Sort or page under finite resource policy with a stable pinned continuation.

## Behavior and failure handling

Create and move only with explicit rights for all affected targets and verified parent identity. Removal is target-specific. Recursive removal requires a reviewed exact or bounded qualified plan and separate authorization before any mutation. A partial enumeration never certifies subtree contents.

## Acceptance

**ZIP-FILESYSTEM-DIRECTORY-T01.** List a directory with a synthetic linked entry without following it. Try removal without the exact subtree authority and verify zero mutations. Change directory generation and verify an old page cannot continue as current.
