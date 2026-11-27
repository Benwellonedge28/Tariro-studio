# Repository crate design

**Contract version** 1.0. Master design §30. Planned implementation.

## Responsibility and dependencies

Resolve stable provider identity and commit; traverse applicable instructions shallow-to-deep; isolate a worktree; validate staged path and blob changes; push exact reviewed ref; query remote before retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [governance](../governance/DESIGN.md), [filesystem](../filesystem/DESIGN.md), [terminal](../terminal/DESIGN.md)

- [Repositories](../../specifications/1400-repositories/repositories.md)
- [Source analysis](../../specifications/1500-source-analysis/source-analysis.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `pin(ref)`
- `instructions(snapshot, paths)`
- `worktree(snapshot)`
- `validate_diff()`
- `publish(request)`
- `reconcile(operation)`

Record families: RepositoryId, pinned Git object ID, worktree lease, instruction bundle, diff and provider operation record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `RepositorySnapshot { provider_repository_id, base_commit, tree_digest, instructions_digest }`
- `PublishRequest { snapshot, expected_remote_ref, target_ref, new_commit, diff_digest, grant_id }`

- `publish(request: PublishRequest, cancel: Cancellation) -> Result<EffectOutcome<PublishReceipt>>`

## Failure, safety and resource limits

No inherited or unscoped credentials. No force push or merge under generic write grants. Bound Git command output and disable hooks and shared mutable configuration.

- `StaleRef`
- `InstructionsIncomplete`
- `ScopeDenied`
- `Conflict`
- `UnknownRemoteOutcome`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/repository/src/
├── lib.rs
├── error.rs
├── repository.rs
├── discovery.rs
├── workspace.rs
├── manifest.rs
├── snapshot.rs
├── indexing.rs
├── instructions/
│   ├── mod.rs
│   ├── discovery.rs
│   ├── agents_md.rs
│   ├── hierarchy.rs
│   ├── precedence.rs
│   └── validation.rs
├── git/
│   ├── mod.rs
│   ├── clone.rs
│   ├── fetch.rs
│   ├── branch.rs
│   ├── worktree.rs
│   ├── commit.rs
│   ├── diff.rs
│   ├── merge.rs
│   ├── rebase.rs
│   ├── history.rs
│   ├── remote.rs
│   ├── tag.rs
│   └── conflict.rs
├── providers/
│   ├── mod.rs
│   ├── github.rs
│   ├── gitlab.rs
│   ├── bitbucket.rs
│   ├── forgejo.rs
│   ├── gitea.rs
│   └── local.rs
├── pull_requests/
│   ├── mod.rs
│   ├── creation.rs
│   ├── review.rs
│   ├── checks.rs
│   ├── status.rs
│   └── reconciliation.rs
├── analysis/
│   ├── mod.rs
│   ├── structure.rs
│   ├── dependencies.rs
│   ├── architecture.rs
│   ├── coverage.rs
│   ├── technical_debt.rs
│   └── placeholders.rs
└── synchronization.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test nested instructions, deleted or renamed paths, concurrent base change and duplicate PR reconciliation.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`repository.rs`](specifications/modules/repository.md)
- [`discovery.rs`](specifications/modules/discovery.md)
- [`workspace.rs`](specifications/modules/workspace.md)
- [`manifest.rs`](specifications/modules/manifest.md)
- [`snapshot.rs`](specifications/modules/snapshot.md)
- [`indexing.rs`](specifications/modules/indexing.md)
- [`instructions/mod.rs`](specifications/modules/instructions/mod.md)
- [`instructions/discovery.rs`](specifications/modules/instructions/discovery.md)
- [`instructions/agents_md.rs`](specifications/modules/instructions/agents_md.md)
- [`instructions/hierarchy.rs`](specifications/modules/instructions/hierarchy.md)
- [`instructions/precedence.rs`](specifications/modules/instructions/precedence.md)
- [`instructions/validation.rs`](specifications/modules/instructions/validation.md)
- [`git/mod.rs`](specifications/modules/git/mod.md)
- [`git/clone.rs`](specifications/modules/git/clone.md)
- [`git/fetch.rs`](specifications/modules/git/fetch.md)
- [`git/branch.rs`](specifications/modules/git/branch.md)
- [`git/worktree.rs`](specifications/modules/git/worktree.md)
- [`git/commit.rs`](specifications/modules/git/commit.md)
- [`git/diff.rs`](specifications/modules/git/diff.md)
- [`git/merge.rs`](specifications/modules/git/merge.md)
- [`git/rebase.rs`](specifications/modules/git/rebase.md)
- [`git/history.rs`](specifications/modules/git/history.md)
- [`git/remote.rs`](specifications/modules/git/remote.md)
- [`git/tag.rs`](specifications/modules/git/tag.md)
- [`git/conflict.rs`](specifications/modules/git/conflict.md)
- [`providers/mod.rs`](specifications/modules/providers/mod.md)
- [`providers/github.rs`](specifications/modules/providers/github.md)
- [`providers/gitlab.rs`](specifications/modules/providers/gitlab.md)
- [`providers/bitbucket.rs`](specifications/modules/providers/bitbucket.md)
- [`providers/forgejo.rs`](specifications/modules/providers/forgejo.md)
- [`providers/gitea.rs`](specifications/modules/providers/gitea.md)
- [`providers/local.rs`](specifications/modules/providers/local.md)
- [`pull_requests/mod.rs`](specifications/modules/pull_requests/mod.md)
- [`pull_requests/creation.rs`](specifications/modules/pull_requests/creation.md)
- [`pull_requests/review.rs`](specifications/modules/pull_requests/review.md)
- [`pull_requests/checks.rs`](specifications/modules/pull_requests/checks.md)
- [`pull_requests/status.rs`](specifications/modules/pull_requests/status.md)
- [`pull_requests/reconciliation.rs`](specifications/modules/pull_requests/reconciliation.md)
- [`analysis/mod.rs`](specifications/modules/analysis/mod.md)
- [`analysis/structure.rs`](specifications/modules/analysis/structure.md)
- [`analysis/dependencies.rs`](specifications/modules/analysis/dependencies.md)
- [`analysis/architecture.rs`](specifications/modules/analysis/architecture.md)
- [`analysis/coverage.rs`](specifications/modules/analysis/coverage.md)
- [`analysis/technical_debt.rs`](specifications/modules/analysis/technical_debt.md)
- [`analysis/placeholders.rs`](specifications/modules/analysis/placeholders.md)
- [`synchronization.rs`](specifications/modules/synchronization.md)
