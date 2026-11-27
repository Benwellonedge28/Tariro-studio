# Immutable repository snapshot

**ZIP-REPOSITORY-SNAPSHOT-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/snapshot.rs`

```rust
pub enum GitObjectId {
    Sha1([u8; 20]),
    Sha256([u8; 32]),
}

pub struct RepositorySnapshot {
    pub repository: crate::repository::RepositoryId,
    pub base_ref: Box<str>,
    pub commit: GitObjectId,
    pub tree: GitObjectId,
}
```

The byte widths are Git object formats. Verify the provider repository identity independently of the owner/name display path, authorize read and fetch, and validate the ref and repository object format before resolution. The initial publication path accepts an explicitly authorized full branch ref. Resolve that ref once and verify that the resulting object is a commit and resolves to the captured tree. Retain its object graph until the lease ends. Once pinned, read by object ID. A working directory, moving branch and cached convenience name cannot substitute for the captured tree.

Detect missing or unverified objects, incompatible object formats, and traversal exceeding admitted byte, object-count or time budgets. Export bounded snapshot reads and stable provenance. Recheck the live base before publication under [remote](git/remote.md) rules. A changed base creates a new review snapshot and requires fresh review and scoped authority. Never automatically rebase a sealed change.

**ZIP-REPOSITORY-SNAPSHOT-T01.** Move the symbolic branch after pinning. Inspected inputs remain those of the captured commit, and a fresh publication check detects the move.
