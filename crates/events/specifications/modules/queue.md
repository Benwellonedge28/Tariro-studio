# Admitted subscriber queue

**ZIP-EVENTS-QUEUE-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/queue.rs`

Composition supplies an opaque queue permit tying the consumer, stream, session and finite memory budgets. Capacity is the smaller of `events.max_subscriber_queue_items` and admitted item capacity, with an independent admitted byte ceiling. Zero capacity cannot accept a subscription. Keep committed payload objects by reference. Charge envelope, pointer and owned-buffer memory before enqueue or copy. A bounded scan must also charge its temporary page budget. Events consumes an injected permit and introduces no resource-crate dependency.

Update accounting under one queue lock, or by a single owning task. Compare current generation before transferring an item; validate delivery authorization again at exposure. Popping releases the corresponding queue charge only after the item transfers to an already charged delivery slot. Closing releases unread charges and wakes waiters. All waits obey injected cancellation and deadlines. No queue manipulation writes a cursor.

**ZIP-EVENTS-QUEUE-T01.** At exact item capacity, an additional enqueue stops or waits without allocation. At byte exhaustion, refuse even if a slot remains. Closing neither deletes committed events nor advances progress.
