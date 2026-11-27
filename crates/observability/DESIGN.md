# Observability crate design

**Contract version** 1.0. Master design §53. Planned implementation.

## Responsibility and dependencies

Sanitize fields, aggregate bounded dimensions, preserve correlation with durable events, and export only through authorized local or external adapter.

First-party dependencies: [foundation](../foundation/DESIGN.md), [events](../events/DESIGN.md), [security](../security/DESIGN.md)

- [Observability](../../specifications/3100-observability/observability.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `record_metric(sample)`
- `emit_span(event)`
- `read_local(scope)`
- `export(authorized_sink)`

Record families: MetricDescriptor, span fields, aggregation bucket and exporter plan. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `MetricSample { descriptor_id, value, low_cardinality_labels, timestamp }`
- `TraceEvent { trace_id, span_id, redacted_fields, duration_ms }`

- `record_metric(sample: MetricSample) -> Result<()>`

## Failure, safety and resource limits

Default local. Cap series cardinality and trace queue. Dropped debug telemetry is counted and cannot substitute for audit.

- `InvalidMetric`
- `CardinalityLimit`
- `ExportDenied`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/observability/src/
├── lib.rs
├── error.rs
├── logging.rs
├── tracing.rs
├── metrics.rs
├── health.rs
├── diagnostics.rs
├── profiling.rs
├── alerts.rs
├── dashboards.rs
├── redaction.rs
├── exporters.rs
└── retention.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test disabled external export sends no network traffic and redaction canary stays absent.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`logging.rs`](specifications/modules/logging.md)
- [`tracing.rs`](specifications/modules/tracing.md)
- [`metrics.rs`](specifications/modules/metrics.md)
- [`health.rs`](specifications/modules/health.md)
- [`diagnostics.rs`](specifications/modules/diagnostics.md)
- [`profiling.rs`](specifications/modules/profiling.md)
- [`alerts.rs`](specifications/modules/alerts.md)
- [`dashboards.rs`](specifications/modules/dashboards.md)
- [`redaction.rs`](specifications/modules/redaction.md)
- [`exporters.rs`](specifications/modules/exporters.md)
- [`retention.rs`](specifications/modules/retention.md)
