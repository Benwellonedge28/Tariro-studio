# Repository, instructions and Git effects

**Contract version** 1.0. Master design §71.

## Contract

Pin provider repo identity, commit ID, tree digest and applicable instruction bundle. Starting at root, read applicable ancestor AGENTS.md to the target path; concatenate with provenance. Reject missing required instructions or unresolved conflict before mutation.

## Execution and integration

Run Git in isolated worktree. Compare staged old/new paths, modes and blobs to grant. Commit reviewed diff only; reconcile remote branch identity and PR marker before retry. Merge and force push are distinct operations.

## Verification

Fixture contains ignored, renamed, binary and unusual filenames. Validate exact batch and preserve unfamiliar content. Simulate base advance and lost network acknowledgment.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Provider request and outcome

A publish request carries stable provider repository ID, pinned base SHA, target ref, expected old ref or absent sentinel, intended new commit SHA, verified diff digest and grant reference. For PR creation also bind exact base and head refs and a deterministic effect marker. A provider adapter returns confirmed receipt, definitive failure, or unknown outcome. Never interpret an HTTP timeout as rejection.

Reconciliation reads branch head and candidate PRs by immutable repository ID, exact base/head and marker. An exact match records receipt. A different head or multiple matching PRs blocks. A confirmed absent operation is retryable only if the original compare conditions and grant still hold. Worktree creation and cleanup use an owner-scoped lease and may touch only the generated worktree root.

A diff entry is `{operation,old_path?,new_path?,before_blob?,after_blob?,before_mode?,after_mode?}`. Both paths of a rename must be authorized. Detect binary, symlink, submodule and mode changes before applying assignment policy. A documentation-only grant blocks every category except allowed text Markdown creates or modifications.

## Implementing components

- [repository crate design](../../crates/repository/DESIGN.md)
- [source-analysis crate design](../../crates/source-analysis/DESIGN.md)
