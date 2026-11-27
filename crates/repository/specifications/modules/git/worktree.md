# Isolated worktree lifecycle

**ZIP-REPOSITORY-GIT-WORKTREE-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/git/worktree.rs`

Under admitted storage and live scope, create a private dedicated worktree and isolated writable Git metadata rooted under a supervisor-owned allocation. Verify the repository identity and pinned head before staging. Bind generated root, its filesystem identity, writer owner, pinned commit and allocation epoch to the lease. Reject unsupported path semantics and untrusted path redirection. Never reuse the user's shell, worktree, index or writable repository configuration. Read-only shared object sources require independently enforced permissions.

Use a bounded trusted adapter with controlled Git arguments and isolated configuration. Do not inherit hooks, filters, external diff helpers, credential helpers, remote definitions, writable alternates or mutable user configuration. Do not traverse submodule or symlink targets in ordinary staging. Any necessary privileged adapter action must have its own explicit scope. Never expose access tokens in arguments, history or resulting patches.

Cleanup verifies the generated root's ownership and absence of live users. Preserve any evidence and required review artifacts first. If root identity or ownership changed, stop and leave the path for recovery. Cleanup never force-removes unrelated worktrees, branches or files.

**ZIP-REPOSITORY-GIT-WORKTREE-T01.** Wrong allocation identity, live users or declined forced cleanup leaves unrelated paths and refs untouched.
