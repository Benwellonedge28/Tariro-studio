# Guarded remote identity and branch update

**ZIP-REPOSITORY-GIT-REMOTE-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/git/remote.rs`

Resolve the authorized canonical endpoint and stable provider repository identity. Obtain scoped credentials through the provider adapter. Inherited remotes and credentials are excluded. Reject endpoint or repository identity changes, including redirect to an unapproved destination. Bind network and execution budgets to the claim. Only the intended branch ref may be created or advanced. Default, protected and shared branches require their distinct authorized operation. Force push, merge, branch deletion and provider settings mutation are separate effects.

The immutable request records repository ID, pinned base ref and expected base commit, target ref, expected old commit or absent sentinel, intended new commit, reviewed diff and instruction digests, grant reference and stable effect key. Before dispatch revalidate the live grant, endpoint, pin and expected target state. Require a provider capability that enforces an atomic target compare plus branch creation or fast-forward update. If the target changes after inspection, reject without overwriting it. A simultaneous compare of the base and target is a separate capability. For providers lacking it, allow a guarded target update only when policy explicitly permits base recheck before and after the effect. A base move observed after push holds PR creation and records the branch effect. Do not automatically undo the branch or relabel it as unused.

Persist the one-use effect claim before sending. Bind verified success to the intended commit at the intended ref. A live ref mismatch after an uncertain reply stays conflicting or unresolved under the repository recovery contract. A dropped response does not authorize a new push. Read and reconcile prior effect identity before any retry.

**ZIP-REPOSITORY-GIT-REMOTE-T01.** Change endpoint or target ref and verify denial. Move the base after a permitted target-only update and verify PR publication stops while the branch receipt is preserved.
