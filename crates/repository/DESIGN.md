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
