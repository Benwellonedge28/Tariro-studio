# Events crate design

**Contract version** 1.0. Master design §13. Planned implementation.

## Responsibility and dependencies

Allocate sequence in the same write transaction as domain state. Readers replay in order from exclusive cursor. Consumers persist deduplication key and checkpoint before acknowledging.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Observability](../../specifications/3100-observability/observability.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `append_in(tx, event)`
- `subscribe(topic, after)`
- `acknowledge(consumer, seq)`

Record families: EventEnvelope v1, monotonic sequence per stream, outbox and cursor records. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `EventEnvelope { stream_id, seq, event_id, schema_major, timestamp, correlation_id, kind, payload_ref }`
- `ConsumerCursor { stream_id, last_seq }`

- `subscribe(topic: TopicFilter, after: ConsumerCursor) -> Result<BoundedEventStream>`

## Failure, safety and resource limits

At-least-once delivery. Admit each subscriber queue under `events.max_subscriber_queue_items` and observed memory capacity. Disconnect a slow stream with its last cursor. Reject expired cursors with snapshot instructions.

- `Backpressure`
- `CursorExpired`
- `CorruptEnvelope`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/events/src/
├── lib.rs
├── error.rs
├── event.rs
├── envelope.rs
├── topic.rs
├── publisher.rs
├── subscriber.rs
├── dispatcher.rs
├── queue.rs
├── journal.rs
├── ordering.rs
├── replay.rs
├── deduplication.rs
├── backpressure.rs
├── dead_letter.rs
└── retention.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Crash after commit before dispatch, replay duplicates and resume from cursor.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`event.rs`](specifications/modules/event.md)
- [`envelope.rs`](specifications/modules/envelope.md)
- [`topic.rs`](specifications/modules/topic.md)
- [`publisher.rs`](specifications/modules/publisher.md)
- [`subscriber.rs`](specifications/modules/subscriber.md)
- [`dispatcher.rs`](specifications/modules/dispatcher.md)
- [`queue.rs`](specifications/modules/queue.md)
- [`journal.rs`](specifications/modules/journal.md)
- [`ordering.rs`](specifications/modules/ordering.md)
- [`replay.rs`](specifications/modules/replay.md)
- [`deduplication.rs`](specifications/modules/deduplication.md)
- [`backpressure.rs`](specifications/modules/backpressure.md)
- [`dead_letter.rs`](specifications/modules/dead_letter.md)
- [`retention.rs`](specifications/modules/retention.md)
