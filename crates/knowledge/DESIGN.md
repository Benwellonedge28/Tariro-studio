# Knowledge crate design

**Contract version** 1.0. Master design §24. Planned implementation.

## Responsibility and dependencies

Canonicalize source identity, stage graph for one revision, atomically switch active pointer and filter edges through authorized nodes. Retract invalidated contributions.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [source-analysis](../source-analysis/DESIGN.md)

- [Knowledge](../../specifications/0900-knowledge/knowledge.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `upsert_revision(graph)`
- `query(scope, revision, pattern)`
- `retract(source)`

Record families: Typed nodes, edges, provenance and revision journal. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `GraphNode { id, entity_kind, revision, source_refs, confidence }`
- `GraphEdge { from, to, relation, evidence_ref }`
- `GraphRevision { id, source_snapshot }`

- `upsert_revision(graph: GraphRevisionDraft) -> Result<GraphRevision>`

## Failure, safety and resource limits

Stop traversal at the resolved `knowledge.max_traversal_depth` and `knowledge.max_results` or the admitted execution budget, whichever is exhausted first. Unknown edges remain uncertain, with provenance.

- `InvalidRelation`
- `RevisionConflict`
- `QueryLimit`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/knowledge/src/
├── lib.rs
├── error.rs
├── entity.rs
├── relationship.rs
├── graph.rs
├── ontology.rs
├── schema.rs
├── extraction.rs
├── ingestion.rs
├── validation.rs
├── inference.rs
├── query.rs
├── traversal.rs
├── provenance.rs
├── versioning.rs
├── conflict.rs
├── domains/
│   ├── mod.rs
│   ├── software.rs
│   ├── architecture.rs
│   ├── dependencies.rs
│   ├── documentation.rs
│   └── organizational.rs
└── persistence.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Reindex changed files, prove stale edges disappear and graph traversal cannot leak private nodes.
