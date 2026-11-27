# Documentation crate design

**Contract version** 1.1 candidate. Master design §33. Planned implementation.

## Responsibility and dependencies

Inventory real files and instructions; form dependency order; author one document; independently validate claims, links, interfaces and acceptance; checkpoint; seal exact diff.

First-party dependencies: [foundation](../foundation/DESIGN.md), [assignments](../assignments/DESIGN.md), [repository](../repository/DESIGN.md), [context](../context/DESIGN.md), [verification](../verification/DESIGN.md)

- [Documentation](../../specifications/1700-documentation/documentation.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

[Inventory](specifications/modules/inventory.md) freezes eligible paths and dependencies at the pin. [Generation](specifications/modules/generation.md) returns one staged candidate, then [validation](specifications/modules/validation.md) verifies its bytes, facts and citations. Assignments owns durable checkpoints. [Batching](specifications/modules/batching.md) verifies the complete staged tree before [publication](specifications/modules/publishing.md) asks Repository for scoped effects. Keep existing dependency direction.

## Failure, safety and resource limits

Only scoped Markdown creates and modifications are allowed in documentation-only mode. Bind readers, staging and review to admitted budgets. Reject missing or false authoritative evidence, unresolved placeholders and broken final-tree links. Short exact batches preserve checkpoints and await renewed scope. Keep observations, proposed behavior and independent approval distinct.

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

Apply the [publication fixtures](../../contracts/acceptance/documentation/publication-fixtures.json) to the Vimbai profile, factual references, final-tree verification and restart after document 17.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The publication slice is a candidate for independent review. Other modules retain their recorded maturity.

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
