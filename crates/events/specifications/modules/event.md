# Typed event payload

**ZIP-EVENTS-EVENT-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/event.rs`

```rust
use foundation::types::{digest::Digest, timestamp::Timestamp};

pub struct PayloadRef {
    pub protection_domain: [u8; 16],
    pub digest: Digest,
    pub length_bytes: u64,
}

pub struct DomainEvent {
    pub stream_id: [u8; 16],
    pub event_id: [u8; 16],
    pub major: u16,
    pub minor: u16,
    pub occurred_at: Timestamp,
    pub correlation_id: Option<[u8; 16]>,
    pub payload: PayloadRef,
}
```

All IDs are nonnil UUID bytes in network order. Bind each stream to one stable event kind through the [topic registry](topic.md). The event's version identifies the registered schema for that kind. Before append, validate producer scope, supported major/minor, payload schema, logical digest and declared object length through the owning adapter. Payload is immutable and bounded. The owning domain decides what causal references are public fields of that payload. An unknown kind or unsupported schema at the producer fails before append. Discovery of an unsupported committed envelope at the consumer stops the affected stream at that sequence. Treat event bytes as data, never as authorization or a tool instruction.

**ZIP-EVENTS-EVENT-T01.** Unknown kind, unsupported version and cross-scope object reference cannot enter the outbox or authorize effects.
