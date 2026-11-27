# Source analysis crate design

**Contract version** 1.0. Master design §31. Planned implementation.

## Responsibility and dependencies

Select registered parser using path and byte probe, parse under time/byte cap, map spans to the immutable snapshot and update only changed paths plus dependents.

First-party dependencies: [foundation](../foundation/DESIGN.md), [repository](../repository/DESIGN.md)

- [Knowledge](../../specifications/0900-knowledge/knowledge.md)
- [Repositories](../../specifications/1400-repositories/repositories.md)
- [Source analysis](../../specifications/1500-source-analysis/source-analysis.md)
- [Debugging](../../specifications/2000-debugging/debugging.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `detect_language(blob)`
- `parse(snapshot, path)`
- `incremental_update(diff)`

Record families: ParserCapability, SourceSpan with byte bounds, Symbol and diagnostic confidence. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ParseRequest { repository_id, source_blob, grammar_version, limits }`
- `Symbol { key, kind, source_ref, byte_span, confidence }`

- `parse(snapshot: SnapshotRef, path: ScopedPath, limits: ParseLimits) -> Result<ParseObservation>`

## Failure, safety and resource limits

Charge input bytes and elapsed time against the admitted `source_analysis.max_source_bytes` and `source_analysis.max_parse_ms`. Fallback is explicitly text-only. Treat grammar and repository input as untrusted.

- `UnsupportedLanguage`
- `ParseBudget`
- `InvalidSpan`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/source-analysis/src/
├── lib.rs
├── error.rs
├── language.rs
├── detection.rs
├── parser.rs
├── syntax_tree.rs
├── symbol.rs
├── symbol_table.rs
├── reference.rs
├── call_graph.rs
├── dependency_graph.rs
├── control_flow.rs
├── data_flow.rs
├── type_information.rs
├── semantic.rs
├── diagnostics.rs
├── indexing.rs
├── impact_analysis.rs
├── complexity.rs
├── adapters/
│   ├── mod.rs
│   ├── tree_sitter.rs
│   ├── lsp.rs
│   ├── rust.rs
│   ├── python.rs
│   ├── javascript.rs
│   ├── typescript.rs
│   ├── java.rs
│   ├── c.rs
│   ├── cpp.rs
│   ├── go.rs
│   ├── zamani.rs
│   └── generic.rs
└── incremental.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test invalid UTF-8, parser fallback and deterministic changed-file reindexing.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`language.rs`](specifications/modules/language.md)
- [`detection.rs`](specifications/modules/detection.md)
- [`parser.rs`](specifications/modules/parser.md)
- [`syntax_tree.rs`](specifications/modules/syntax_tree.md)
- [`symbol.rs`](specifications/modules/symbol.md)
- [`symbol_table.rs`](specifications/modules/symbol_table.md)
- [`reference.rs`](specifications/modules/reference.md)
- [`call_graph.rs`](specifications/modules/call_graph.md)
- [`dependency_graph.rs`](specifications/modules/dependency_graph.md)
- [`control_flow.rs`](specifications/modules/control_flow.md)
- [`data_flow.rs`](specifications/modules/data_flow.md)
- [`type_information.rs`](specifications/modules/type_information.md)
- [`semantic.rs`](specifications/modules/semantic.md)
- [`diagnostics.rs`](specifications/modules/diagnostics.md)
- [`indexing.rs`](specifications/modules/indexing.md)
- [`impact_analysis.rs`](specifications/modules/impact_analysis.md)
- [`complexity.rs`](specifications/modules/complexity.md)
- [`adapters/mod.rs`](specifications/modules/adapters/mod.md)
- [`adapters/tree_sitter.rs`](specifications/modules/adapters/tree_sitter.md)
- [`adapters/lsp.rs`](specifications/modules/adapters/lsp.md)
- [`adapters/rust.rs`](specifications/modules/adapters/rust.md)
- [`adapters/python.rs`](specifications/modules/adapters/python.md)
- [`adapters/javascript.rs`](specifications/modules/adapters/javascript.md)
- [`adapters/typescript.rs`](specifications/modules/adapters/typescript.md)
- [`adapters/java.rs`](specifications/modules/adapters/java.md)
- [`adapters/c.rs`](specifications/modules/adapters/c.md)
- [`adapters/cpp.rs`](specifications/modules/adapters/cpp.md)
- [`adapters/go.rs`](specifications/modules/adapters/go.md)
- [`adapters/zamani.rs`](specifications/modules/adapters/zamani.md)
- [`adapters/generic.rs`](specifications/modules/adapters/generic.md)
- [`incremental.rs`](specifications/modules/incremental.md)
