# Repository crate design

**Contract version** 1.1 candidate. Master design §30. Planned implementation.

## Responsibility and dependencies

Resolve stable provider identity and commit; traverse applicable instructions shallow-to-deep; isolate a worktree; validate staged path and blob changes; push exact reviewed ref; query remote before retry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [governance](../governance/DESIGN.md), [filesystem](../filesystem/DESIGN.md), [terminal](../terminal/DESIGN.md)

- [Repositories](../../specifications/1400-repositories/repositories.md)
- [Source analysis](../../specifications/1500-source-analysis/source-analysis.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

[Snapshot](specifications/modules/snapshot.md) owns immutable provider and Git object identity. [Instructions](specifications/modules/instructions/discovery.md) owns pinned base traversal and authority provenance. [Diff](specifications/modules/git/diff.md) and [commit](specifications/modules/git/commit.md) verify the exact staged tree. [Remote](specifications/modules/git/remote.md), [PR creation](specifications/modules/pull_requests/creation.md) and [reconciliation](specifications/modules/pull_requests/reconciliation.md) own guarded effects and verified observations. Assignments retains durable effect intents and receipts through the composition boundary.

## Failure, safety and resource limits

No inherited or unscoped credentials. No general grant allows force push, merge or default-branch mutation. Use an isolated, bounded Git adapter. Stop after stale pin, incomplete instructions, conflicting provider state, or uncertain outcomes. Compare provider capabilities with grant requirements, including whether the required comparison is atomic. Preserve observed effects under [typed failures](specifications/modules/error.md).

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

Apply the [publication fixtures](../../contracts/acceptance/repository/publication-fixtures.json) to instruction paths, staged scope, ref movement and response loss. Independently qualify actual Git and provider capabilities.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The publication slice is a candidate for independent review. Other modules retain their recorded maturity.

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
