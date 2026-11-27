# Durable event envelope

**ZIP-EVENTS-ENVELOPE-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/envelope.rs`

```rust
use std::num::NonZeroU64;
use crate::event::DomainEvent;

pub struct EventEnvelope {
    event: DomainEvent,
    sequence: NonZeroU64,
    kind: Box<str>,
}
```

Construct only from a committed row plus its immutable stream descriptor. Expose borrowed event, sequence and kind accessors, keeping validation and sequence assignment in journal/publisher. An exported envelope has fields `schema_version` with major and minor, `stream_id`, `sequence`, `event_id`, `kind`, `occurred_at`, `correlation_id`, and `payload_ref`. Encode UUIDs as lowercase hyphenated strings in JSON, sequence and payload length as canonical decimal strings, occurrence with Foundation UTC encoding and digest with the Foundation tagged SHA-256 representation. A missing correlation is null. Read known versions through the registered schema. Unsupported versions cannot advance a cursor.

Verify the stream identity, registry ownership and scope, sequence positivity, IDs, and payload reference structure before exposing the envelope. Derive kind from the immutable stream descriptor rather than persisting a second copy with different authority. Validate payload independently on access. A committed row with invalid stored shape is corruption. Any incoming transport envelope must match its registry and committed or trusted event evidence before processing.

**ZIP-EVENTS-ENVELOPE-T01.** Round-trip a valid v1 envelope, including the highest u64 sequence, and reject zero, noncanonical JSON decimal strings and unsupported major versions.
