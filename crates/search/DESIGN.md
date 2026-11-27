# Search crate design

**Contract version** 1.0. Master design §25. Planned implementation.

## Responsibility and dependencies

Build incremental generation, atomically promote when complete, apply ACL before retrieval, then combine ranks deterministically. Preserve lexical mode on missing embedding service.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md)

- [Memory](../../specifications/0800-memory/memory.md)
- [Knowledge](../../specifications/0900-knowledge/knowledge.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `index_revision(snapshot)`
- `query(criteria)`
- `drop_scope(scope)`

Record families: Index manifest, postings, symbol keys, embedding version and result cursor. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Query { scope, generation?, kind, text, limit, cursor? }`
- `SearchHit { source_ref, byte_span, score, explanation }`
- `IndexGeneration { source_revision, version, analyzer_digest }`

- `query(criteria: Query) -> Result<SearchPage>`

## Failure, safety and resource limits

Default 100 results, opaque generation-bound cursor; separate incompatible embedding dimensions. Private indexes inherit source retention.

- `StaleIndex`
- `UnsupportedQuery`
- `CursorExpired`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/search/src/
├── lib.rs
├── error.rs
├── query.rs
├── index.rs
├── document.rs
├── ingestion.rs
├── lexical/
│   ├── mod.rs
│   ├── tokenizer.rs
│   ├── inverted_index.rs
│   └── ranking.rs
├── semantic/
│   ├── mod.rs
│   ├── embeddings.rs
│   ├── vector.rs
│   ├── similarity.rs
│   └── index.rs
├── hybrid/
│   ├── mod.rs
│   ├── fusion.rs
│   └── reranking.rs
├── code_search.rs
├── filters.rs
├── incremental.rs
└── persistence.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Check index restart, stable ranking and permission filtered snippets.
