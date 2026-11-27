# Authoritative staged tree diff

**ZIP-REPOSITORY-GIT-DIFF-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/git/diff.rs`

Compare the pinned base tree and an immutable tree written from the isolated index under a single writer. Derive add, modify, delete and type/mode change from exact tree entries. Retain both old and new path, mode and blob IDs. Pair records as rename only from an explicit approved rename map and verified old/new entries. Heuristics cannot authorize a move or hide an underlying delete or add. Unknown modes and missing tree/object data fail closed.

Treat Git paths as validated repository-relative components. Do not silently normalize case, Unicode, separator or byte representation. Reject absolute paths, dot/dot-dot components, NUL, ambiguous aliases and targets unsupported by the platform before mutation. Preserve unfamiliar, ignored and unstaged content. Bound enumeration and file inspection. For a documentation-only grant allow only scoped regular non-executable Markdown additions or modifications with valid UTF-8 and no NUL, no mode change and no privileged control path. Explicitly classify and deny binary, symlink, gitlink, deletion and rename under that grant. Authorization for broader grants checks both endpoints, relevant rule sets and operation type.

Sort the complete validated manifest by canonical path bytes, with explicit operation, old/new mode and object ID. Recompute exact count from actual changed outputs. Bind the immutable tree ID and manifest digest to review. Truncation or skipped entries cannot produce a seal. A changed staged tree invalidates the approved review.

**ZIP-REPOSITORY-GIT-DIFF-T01.** Reject moving an authorized file into a disallowed path and deleting a file under a documentation-only grant. A binary or symlink with a Markdown suffix cannot pass.
