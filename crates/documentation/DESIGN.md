# Documentation crate design

**Contract version** 1.0. Master design §33. Planned implementation.

## Responsibility and dependencies

Inventory real files and instructions; form dependency order; author one document; independently validate claims, links, interfaces and acceptance; checkpoint; seal exact diff.

First-party dependencies: [foundation](../foundation/DESIGN.md), [assignments](../assignments/DESIGN.md), [repository](../repository/DESIGN.md), [context](../context/DESIGN.md), [verification](../verification/DESIGN.md)

- [Documentation](../../specifications/1700-documentation/documentation.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `inventory(snapshot)`
- `design_document(target)`
- `review(draft)`
- `seal_batch(batch)`

Record families: DocumentPlan, Reference, ReviewFinding, VerifiedDocument and batch manifest. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `DocumentPlan { target_path, source_refs, required_sections, requirements }`
- `VerifiedDocument { path, document_digest, plan_digest, evidence_ref }`
- `BatchManifest { documents, staged_diff_digest }`

- `seal_batch(batch: VerifiedBatch, scope: DocumentationGrant) -> Result<BatchManifest>`

## Failure, safety and resource limits

Only approved Markdown paths in documentation mode. Zero broken internal references or placeholders. Do not fill short batches with unrelated files.

- `MissingSource`
- `UnsupportedClaim`
- `BatchSizeMismatch`
- `ScopeDenied`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/documentation/src/
├── lib.rs
├── error.rs
├── discovery.rs
├── inventory.rs
├── classification.rs
├── requirements.rs
├── templates.rs
├── generation.rs
├── editing.rs
├── validation.rs
├── coverage.rs
├── consistency.rs
├── source_references.rs
├── traceability.rs
├── design/
│   ├── mod.rs
│   ├── architecture.rs
│   ├── subsystem.rs
│   ├── component.rs
│   ├── interface.rs
│   ├── data_model.rs
│   ├── algorithms.rs
│   ├── integration.rs
│   └── acceptance.rs
├── formats/
│   ├── mod.rs
│   ├── markdown.rs
│   ├── asciidoc.rs
│   ├── html.rs
│   └── plain_text.rs
├── diagrams.rs
├── publishing.rs
└── batching.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test fixed 30-file Vimbai workflow, factual references and restart after document 17.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`discovery.rs`](specifications/modules/discovery.md)
- [`inventory.rs`](specifications/modules/inventory.md)
- [`classification.rs`](specifications/modules/classification.md)
- [`requirements.rs`](specifications/modules/requirements.md)
- [`templates.rs`](specifications/modules/templates.md)
- [`generation.rs`](specifications/modules/generation.md)
- [`editing.rs`](specifications/modules/editing.md)
- [`validation.rs`](specifications/modules/validation.md)
- [`coverage.rs`](specifications/modules/coverage.md)
- [`consistency.rs`](specifications/modules/consistency.md)
- [`source_references.rs`](specifications/modules/source_references.md)
- [`traceability.rs`](specifications/modules/traceability.md)
- [`design/mod.rs`](specifications/modules/design/mod.md)
- [`design/architecture.rs`](specifications/modules/design/architecture.md)
- [`design/subsystem.rs`](specifications/modules/design/subsystem.md)
- [`design/component.rs`](specifications/modules/design/component.md)
- [`design/interface.rs`](specifications/modules/design/interface.md)
- [`design/data_model.rs`](specifications/modules/design/data_model.md)
- [`design/algorithms.rs`](specifications/modules/design/algorithms.md)
- [`design/integration.rs`](specifications/modules/design/integration.md)
- [`design/acceptance.rs`](specifications/modules/design/acceptance.md)
- [`formats/mod.rs`](specifications/modules/formats/mod.md)
- [`formats/markdown.rs`](specifications/modules/formats/markdown.md)
- [`formats/asciidoc.rs`](specifications/modules/formats/asciidoc.md)
- [`formats/html.rs`](specifications/modules/formats/html.md)
- [`formats/plain_text.rs`](specifications/modules/formats/plain_text.md)
- [`diagrams.rs`](specifications/modules/diagrams.md)
- [`publishing.rs`](specifications/modules/publishing.md)
- [`batching.rs`](specifications/modules/batching.md)
