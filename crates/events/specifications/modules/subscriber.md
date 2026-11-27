# Durable consumer progress

**ZIP-EVENTS-SUBSCRIBER-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/subscriber.rs`

```rust
use std::{future::Future, num::NonZeroU64, pin::Pin};
use foundation::types::digest::Digest;
use crate::{envelope::EventEnvelope, error::EventError};

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct Cursor {
    pub stream: [u8; 16],
    pub root_epoch: NonZeroU64,
    pub after: u64,
}

pub struct SubscriptionRequest {
    pub consumer: [u8; 16],
    pub cursor: Cursor,
}

pub struct Delivery {
    pub envelope: EventEnvelope,
    pub session_epoch: NonZeroU64,
}

pub trait Subscription: Send {
    fn next(&mut self)
        -> Pin<Box<dyn Future<Output = Result<Delivery, EventError>> + Send + '_>>;
    fn acknowledge(
        &mut self,
        applied: Cursor,
        evidence: Digest,
    ) -> Result<Cursor, EventError>;
}

pub trait Subscriber: Send + Sync {
    fn subscribe(
        &self, request: SubscriptionRequest,
    ) -> Result<Box<dyn Subscription>, EventError>;
}
```

Authorize consumer, stream and credential before loading the cursor or revealing retention. One active session epoch per consumer, stream and root epoch owns acknowledgment. On explicit authorized takeover, atomically increment the session epoch and fence earlier handles. Limits, the cancellation token and trusted processor verifier are bound by composition and checked on each operation. Old sessions fail before writing progress. A dropped pending read cannot lose the corresponding durable event or advance its cursor.

Resume a named consumer only from its durable checkpoint. The caller's cursor must match it, or an authorized snapshot installation must first create a new checkpoint. Initial history starts from zero only while the retained floor is zero and no prior checkpoint exists. New consumers of compacted streams must install an authorized snapshot. A delivered event carries no proof of processing. Validate acknowledgment through [deduplication](deduplication.md). For a local transaction, look up the exact committed marker and already-updated progress. An external receipt may advance progress by exactly one sequence in the same transaction as its processing marker, only after the current session and verifier check pass. Reject a claimed applied cursor that disagrees with the receipt, or a receipt for an event that this session did not deliver unless an existing durable marker proves an exact replay. Return stored progress for a verified replay without changing or regressing it. An out-of-order acknowledgement cannot skip an event. Closing releases queue resources and leaves progress untouched.

**ZIP-EVENTS-SUBSCRIBER-T01.** A repeated valid acknowledgement cannot regress progress or commit an extra projection. A fenced session cannot acknowledge after takeover.
