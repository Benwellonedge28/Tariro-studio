# Transactional event publication

**ZIP-EVENTS-PUBLISHER-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/publisher.rs`

```rust
use crate::{error::EventError, event::DomainEvent};
use storage::transaction::WriteBatch;

pub trait Publisher: Send + Sync {
    fn append(&self, batch: &mut WriteBatch, event: DomainEvent) -> Result<(), EventError>;
}
```

Validate registered stream, producer scope and verified payload reference. Convert to Storage's pending event representation after all checks and budget validation. Keep the batch untouched on error. Append only by staging alongside domain mutations. Storage owns sequence allocation, uniqueness and durability. Before commit there is no sequence or delivery receipt. The calling domain submits the stable WriteBatch ID and reconciles unknown commits using that identity. An exact committed replay adds no row or stream sequence. A changed input or event ID reuse from another transaction conflicts. Wake dispatch after a confirmed commit when available, but the journal remains authoritative if the wake is lost.

**ZIP-EVENTS-PUBLISHER-T01.** Interrupt before commit and verify neither domain record nor event appears. Interrupt after commit before wake and verify restart reads the one committed event.
