# Subscriber pressure decisions

**ZIP-EVENTS-BACKPRESSURE-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/backpressure.rs`

On unavailable capacity stop admitting pages to the affected subscription. An approved pressure policy can wait under a finite stall deadline or close immediately. It cannot exceed admitted memory or block other consumers. Expiry, cancellation or revocation closes the subscription and wakes pending operations. Distinguish queue pressure from permission loss. A slow consumer receives its last durable cursor only under current scope. Dropping an unread item cannot acknowledge it, and a resolved pressure condition may re-read committed rows from durable progress.

**ZIP-EVENTS-BACKPRESSURE-T01.** Cancel while waiting with a full queue. Verify waiters stop, charged memory is reclaimed after all buffered work exits, and acknowledged progress is unchanged.
