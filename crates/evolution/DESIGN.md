# Evolution crate design

**Contract version** 1.0. Master design §57. Planned implementation.

## Responsibility and dependencies

Stage in isolated worktree, compare against fixed evaluation set and policy baseline, require independent human review, release via normal deployment process.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [verification](../verification/DESIGN.md), [repository](../repository/DESIGN.md)

- [Evolution](../../specifications/3500-evolution/evolution.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `submit_proposal(diff)`
- `evaluate(candidate)`
- `request_review()`
- `promote(receipt)`

Record families: EvolutionProposal, baseline, independent evaluation and approval receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `EvolutionProposal { id, base_revision, diff_digest, objective, policy_delta, evaluation_manifest }`
- `Evaluation { plan_digest, observations, comparison, findings }`

- `evaluate(proposal: EvolutionProposal, baseline: EvaluationManifest) -> Result<Evaluation>`

## Failure, safety and resource limits

Self-proposals confer no write or deploy rights. Governance, security and verification changes require distinct owner approval. Avoid learning from private data without consent.

- `ReviewRequired`
- `EvaluationRegressed`
- `GovernanceChangeDenied`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/evolution/src/
├── lib.rs
├── error.rs
├── proposal.rs
├── experiment.rs
├── baseline.rs
├── evaluation.rs
├── benchmarking.rs
├── regression.rs
├── candidate.rs
├── policy.rs
├── review.rs
├── approval.rs
├── migration.rs
├── rollback.rs
└── history.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test attempted self-grant and proposal that weakens evidence gate.
