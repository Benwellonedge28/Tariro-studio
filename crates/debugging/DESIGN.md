# Debugging crate design

**Contract version** 1.0. Master design §36. Planned implementation.

## Responsibility and dependencies

Group normalized diagnostics, reproduce in same toolchain and snapshot, vary one relevant dimension per attempt and capture deltas. Send proposed fixes through engineering.

First-party dependencies: [foundation](../foundation/DESIGN.md), [terminal](../terminal/DESIGN.md), [source-analysis](../source-analysis/DESIGN.md), [verification](../verification/DESIGN.md)

- [Debugging](../../specifications/2000-debugging/debugging.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `collect_failure(execution)`
- `reproduce(case)`
- `localize(trace)`
- `propose_fix()`

Record families: FailureSignature, Reproduction, hypothesis with evidence and patch recommendation. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Reproduction { source_revision, toolchain_digest, input_refs, failure_signature, attempts }`
- `Hypothesis { evidence_refs, falsification_check }`

- `reproduce(spec: Reproduction, cancel: Cancellation) -> Result<ReproductionResult>`

## Failure, safety and resource limits

Apply resolved `debugging.max_attempts` and `debugging.deadline_ms`; stop before the next attempt if either budget is exhausted. Redact logs before model input. Preserve partial failure evidence and confidence.

- `NotReproducible`
- `ReproductionBudget`
- `ArtifactUnavailable`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/debugging/src/
├── lib.rs
├── error.rs
├── session.rs
├── diagnostic.rs
├── reproduction.rs
├── breakpoint.rs
├── stack_trace.rs
├── variable.rs
├── execution_trace.rs
├── root_cause.rs
├── hypothesis.rs
├── repair.rs
├── validation.rs
├── replay.rs
├── adapters/
│   ├── mod.rs
│   ├── dap.rs
│   ├── gdb.rs
│   └── lldb.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test nonreproducible failure, dependency outage and redaction.
