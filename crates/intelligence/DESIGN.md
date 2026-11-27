# Intelligence crate design

**Contract version** 1.0. Master design §18. Planned implementation.

## Responsibility and dependencies

Intersect requested capabilities, local policy, provider route and model readiness. Pick deterministic ordered preference. Validate structured output before forwarding as a proposal.

First-party dependencies: [foundation](../foundation/DESIGN.md), [models](../models/DESIGN.md), [resources](../resources/DESIGN.md), [providers](../providers/DESIGN.md)

- [Intelligence](../../specifications/0400-intelligence/intelligence.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `capabilities()`
- `generate(request, stream)`
- `embed(request)`
- `cancel(id)`

Record families: GenerationRequest, ModelRef, usage records, chunks with sequence and finish reason. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `GenerationRequest { request_id, context_ref, sensitivity, model_requirements, max_input_tokens, max_output_tokens, deadline, route_grant }`
- `GenerationChunk { seq, delta, usage, finish_reason }`

- `generate(request: GenerationRequest, cancel: Cancellation) -> Result<GenerationStream>`

## Failure, safety and resource limits

Budget tokens before dispatch and release reservation on terminal outcome. No automatic remote downgrade or escalation. Partial text remains partial after failed streams.

- `NoRoute`
- `BudgetExceeded`
- `InvalidOutput`
- `TransportUnavailable`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/intelligence/src/
├── lib.rs
├── error.rs
├── intelligence.rs
├── request.rs
├── response.rs
├── capability.rs
├── modality.rs
├── router.rs
├── selection.rs
├── fallback.rs
├── evaluation.rs
├── confidence.rs
├── structured_output.rs
├── tool_calling.rs
├── streaming.rs
├── usage.rs
├── budget.rs
├── caching.rs
└── providers/
    ├── mod.rs
    ├── local.rs
    ├── remote.rs
    ├── embedded.rs
    └── distributed.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test offline routing, strict provider policies, chunk sequencing and partial stream interruption.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`intelligence.rs`](specifications/modules/intelligence.md)
- [`request.rs`](specifications/modules/request.md)
- [`response.rs`](specifications/modules/response.md)
- [`capability.rs`](specifications/modules/capability.md)
- [`modality.rs`](specifications/modules/modality.md)
- [`router.rs`](specifications/modules/router.md)
- [`selection.rs`](specifications/modules/selection.md)
- [`fallback.rs`](specifications/modules/fallback.md)
- [`evaluation.rs`](specifications/modules/evaluation.md)
- [`confidence.rs`](specifications/modules/confidence.md)
- [`structured_output.rs`](specifications/modules/structured_output.md)
- [`tool_calling.rs`](specifications/modules/tool_calling.md)
- [`streaming.rs`](specifications/modules/streaming.md)
- [`usage.rs`](specifications/modules/usage.md)
- [`budget.rs`](specifications/modules/budget.md)
- [`caching.rs`](specifications/modules/caching.md)
- [`providers/mod.rs`](specifications/modules/providers/mod.md)
- [`providers/local.rs`](specifications/modules/providers/local.md)
- [`providers/remote.rs`](specifications/modules/providers/remote.md)
- [`providers/embedded.rs`](specifications/modules/providers/embedded.md)
- [`providers/distributed.rs`](specifications/modules/providers/distributed.md)
