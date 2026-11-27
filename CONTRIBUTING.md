# Contributing to Zipporah

1. Read the master design, applicable root and crate instructions, and the numbered subsystem specification.
2. Identify the requirement IDs and the pinned base. Propose contract changes separately when they affect persisted state, public interfaces or policy.
3. Work in a dedicated branch/worktree. Keep each PR scoped and record dependency changes and migrations explicitly.
4. For implementation PRs, apply the pinned toolchain, formatting, clippy, tests, offline and security gates relevant to scope. Capture exact results. Design-only PRs validate paths, Markdown links, requirement traceability and internal consistency.
5. Include evidence, explicit limitations, upgrade/rollback behavior and the source revision in the PR. The reviewer checks the final commit, not a prior draft.
6. Forward separate approval requests for merge, publication, deployment and other independently privileged operations as required by policy.
