# Event failure vocabulary

**ZIP-EVENTS-ERROR-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum EventError {
    Denied,
    InvalidEnvelope,
    UnsupportedVersion,
    CorruptEnvelope,
    InvalidCursor,
    CursorExpired,
    SessionLost,
    Backpressure,
    DeadlineExceeded,
    Cancelled,
    Conflict,
    SequenceOverflow,
    Storage,
    OutcomeUnknown,
}
```

Validate authority before disclosing stream or consumer state. Inside authorized scope distinguish malformed input, stale root or truncated history, prior session, invalid forward cursor, corrupt committed envelope and bounded pressure. Conflicts and corrupted entries neither advance progress nor skip delivery. Unknown commit or external effect maps to OutcomeUnknown and requires original-identity reconciliation. A storage or adapter exception cannot imply the operation was absent. Optional context uses a separately authorized result view carrying the durable cursor or approved snapshot reference. Never expose payload bytes in errors.

**ZIP-EVENTS-ERROR-T01.** An outside caller sees Denied for missing, expired, or live private cursors. An authorized caller sees CursorExpired for a compacted position.
