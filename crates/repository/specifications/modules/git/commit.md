# Commit an approved tree

**ZIP-REPOSITORY-GIT-COMMIT-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/git/commit.rs`

Under current worktree ownership, verify expected parent, immutable tree, staged manifest, instruction bundle, live grant and reviewed evidence. Hold the single-writer worktree gate across the final staged check and publication of the local commit reference. Preserve approved author, committer and message. Build only from the exact approved immutable tree. Do not execute repository hooks or permit subprocess configuration to alter the tree.

Read the local commit back and verify parent, tree and the recorded author/message policy. Persist observed object identity before allowing the remote adapter to act. Failure before ref update does not create a publishable receipt. A lost local response requires reference and object inspection. Cancellation does not erase a committed local object. Do not widen the branch lease or perform a remote mutation here.

**ZIP-REPOSITORY-GIT-COMMIT-T01.** Change the index after review. Commit creation is denied. A valid retried observation retains the original pinned parent and reviewed tree.
