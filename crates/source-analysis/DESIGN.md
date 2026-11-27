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

Default 2 MiB per source file and 10 seconds per parse. Fallback is explicitly text-only. Treat grammar and repository input as untrusted.

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
