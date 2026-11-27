# Committed outbox dispatch

**ZIP-EVENTS-DISPATCHER-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/dispatcher.rs`

1. On start scan committed rows after the durable cursor. A producer notification prompts a scan. Lost notifications are covered by startup and bounded periodic scans under the injected runtime policy.
2. Read bounded pages in sequence order. Track a volatile enqueue position separately from the durable cursor. Check current scope, root and session before each enqueue and before delivering to the caller. On session loss discard volatile positions and queued values.
3. Enqueue only with current [queue](queue.md) admission. Commit of producer event remains valid when the subscriber is disconnected, slow or revoked. A stopped worker has no authority to read another subscriber's queue.
4. After reconnect start from authorized durable progress. Redelivery preserves original event ID and sequence. Processing and acknowledgement use a separate durable boundary. Pending external outcomes and quarantined head events block later processing for that consumer.

Serialize dequeue ownership per subscription. An implementation may buffer ahead within admitted bounds, but cannot acknowledge across a gap. No linkage or constructor spawns a background task; runtime supervises dispatcher lifetimes and shutdown.

**ZIP-EVENTS-DISPATCHER-T01.** Crash after producer commit before dispatch and disconnect after enqueue before processing. Both recover the original event exactly at the expected cursor boundary.
