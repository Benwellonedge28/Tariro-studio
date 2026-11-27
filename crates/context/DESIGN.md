# Context crate design

**Contract version** 1.0. Master design §21. Planned implementation.

## Responsibility and dependencies

Load pinned requirements and applicable instructions, then mandatory evidence, then rank eligible snippets. Dedupe by digest and admit within provider-measured tokens. Preserve origin and trust tags.

First-party dependencies: [foundation](../foundation/DESIGN.md), [repository](../repository/DESIGN.md), [search](../search/DESIGN.md), [security](../security/DESIGN.md)

- [Context](../../specifications/0700-context/context.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `assemble(request, snapshot, budget)`
- `explain(selection)`

Record families: ContextItem with source revision, span, trust, token count and digest. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ContextItem { source_revision, source_path, byte_span, digest, trust_class, sensitivity, token_count }`
- `ContextBundle { items, tokenizer_digest, omissions }`

- `assemble(request: ContextRequest, snapshot: SnapshotRef, budget: TokenBudget) -> Result<ContextBundle>`

## Failure, safety and resource limits

Never silently truncate mandatory policy. Exclude secret-bearing content and out-of-scope items. Record omission counts without content.

- `MandatoryContextTooLarge`
- `ScopeDenied`
- `TokenizerUnavailable`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/context/src/
├── lib.rs
├── error.rs
├── context.rs
├── builder.rs
├── window.rs
├── token_budget.rs
├── prioritization.rs
├── relevance.rs
├── compression.rs
├── summarization.rs
├── truncation.rs
├── retrieval.rs
├── deduplication.rs
├── provenance.rs
├── prompt.rs
├── template.rs
├── isolation.rs
└── cache.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test prompt-like repository text, stable rank ties, token hard ceiling and no cross-scope retrieval.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`context.rs`](specifications/modules/context.md)
- [`builder.rs`](specifications/modules/builder.md)
- [`window.rs`](specifications/modules/window.md)
- [`token_budget.rs`](specifications/modules/token_budget.md)
- [`prioritization.rs`](specifications/modules/prioritization.md)
- [`relevance.rs`](specifications/modules/relevance.md)
- [`compression.rs`](specifications/modules/compression.md)
- [`summarization.rs`](specifications/modules/summarization.md)
- [`truncation.rs`](specifications/modules/truncation.md)
- [`retrieval.rs`](specifications/modules/retrieval.md)
- [`deduplication.rs`](specifications/modules/deduplication.md)
- [`provenance.rs`](specifications/modules/provenance.md)
- [`prompt.rs`](specifications/modules/prompt.md)
- [`template.rs`](specifications/modules/template.md)
- [`isolation.rs`](specifications/modules/isolation.md)
- [`cache.rs`](specifications/modules/cache.md)
