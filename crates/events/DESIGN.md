# Events crate design

**Contract version** 1.1 candidate. Master design §13. Planned implementation.

## Responsibility and dependencies

Allocate sequence in the same write transaction as domain state. Readers replay in order from exclusive cursor. Consumers persist deduplication key and checkpoint before acknowledging.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md)

- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Observability](../../specifications/3100-observability/observability.md)

## API and data

[Publisher](specifications/modules/publisher.md) stages pending events in the caller's Storage batch. Storage owns sequence allocation and commits domain changes and outbox entries together. [Journal](specifications/modules/journal.md) reads committed snapshots. [Subscriber](specifications/modules/subscriber.md) binds its durable cursor and session epoch to the root and stream. [Deduplication](specifications/modules/deduplication.md) defines trusted processing evidence and replay.

Each registered stream has one kind, workspace and payload protection domain. Resolve topics to authorized whole streams and give each stream a separate cursor. Committed rows remain available after a wake or delivery is interrupted. Durable projection state and acknowledgement rules prevent silent skips.

## Failure, safety and resource limits

Apply the [durable event standard](../../EVENT_STANDARD.md). Bound every subscriber queue by `events.max_subscriber_queue_items` and measured admitted memory via an injected permit. Recheck scope on exposure, and close or wait under finite pressure policy. Retain progress across disconnect. For expired cursors require authorized snapshot recovery. Quarantine, ambiguous commits and revoked sessions cannot advance durable progress. See [typed errors](specifications/modules/error.md).

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

Verify the [delivery fixtures](../../contracts/acceptance/events/delivery-fixtures.json) in a logical harness, then exercise a qualified Storage backend and runtime delivery adapter.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The event-delivery slice is a candidate for independent review.

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
