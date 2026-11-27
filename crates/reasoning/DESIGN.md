# Reasoning crate design

**Contract version** 1.0. Master design §22. Planned implementation.

## Responsibility and dependencies

Validate proposal schema and cited evidence IDs, label assumptions, score alternatives against approved criteria, and route conflicts to oversight. Produce concise decision rationale.

First-party dependencies: [foundation](../foundation/DESIGN.md), [intelligence](../intelligence/DESIGN.md), [context](../context/DESIGN.md)

- [Intelligence](../../specifications/0400-intelligence/intelligence.md)
- [Context](../../specifications/0700-context/context.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `propose(input)`
- `validate_output(proposal)`
- `resolve_conflict(options)`

Record families: Structured proposal with evidence, alternatives, uncertainty and next action. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Proposal { objective_id, suggested_actions, evidence_refs, assumptions, uncertainty, verdict }`
- `Conflict { proposal_ids, conflicting_claims, required_decision }`

- `validate_output(candidate: Proposal, schema: ProposalSchema) -> Result<ValidatedProposal>`

## Failure, safety and resource limits

Bound iterations and proposal size. Proposals have no execution authority. Unsupported assertions remain unverified.

- `InvalidProposal`
- `MissingEvidence`
- `BudgetExhausted`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/reasoning/src/
├── lib.rs
├── error.rs
├── problem.rs
├── decomposition.rs
├── planning.rs
├── constraints.rs
├── decision.rs
├── alternatives.rs
├── evaluation.rs
├── uncertainty.rs
├── reflection.rs
├── critique.rs
├── symbolic/
│   ├── mod.rs
│   ├── rules.rs
│   ├── logic.rs
│   └── solver.rs
├── hybrid/
│   ├── mod.rs
│   ├── deterministic.rs
│   └── model_assisted.rs
└── evidence.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Use contradictory evidence and check abstention. Ensure hallucinated citation cannot become acceptance evidence.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`problem.rs`](specifications/modules/problem.md)
- [`decomposition.rs`](specifications/modules/decomposition.md)
- [`planning.rs`](specifications/modules/planning.md)
- [`constraints.rs`](specifications/modules/constraints.md)
- [`decision.rs`](specifications/modules/decision.md)
- [`alternatives.rs`](specifications/modules/alternatives.md)
- [`evaluation.rs`](specifications/modules/evaluation.md)
- [`uncertainty.rs`](specifications/modules/uncertainty.md)
- [`reflection.rs`](specifications/modules/reflection.md)
- [`critique.rs`](specifications/modules/critique.md)
- [`symbolic/mod.rs`](specifications/modules/symbolic/mod.md)
- [`symbolic/rules.rs`](specifications/modules/symbolic/rules.md)
- [`symbolic/logic.rs`](specifications/modules/symbolic/logic.md)
- [`symbolic/solver.rs`](specifications/modules/symbolic/solver.md)
- [`hybrid/mod.rs`](specifications/modules/hybrid/mod.md)
- [`hybrid/deterministic.rs`](specifications/modules/hybrid/deterministic.md)
- [`hybrid/model_assisted.rs`](specifications/modules/hybrid/model_assisted.md)
- [`evidence.rs`](specifications/modules/evidence.md)
