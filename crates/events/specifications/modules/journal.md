# Durable event journal

**ZIP-EVENTS-JOURNAL-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/journal.rs`

Use Storage's [schema](../../../storage/specifications/modules/schema.md) and [transaction](../../../storage/specifications/modules/transaction.md) boundaries for producer rows. Events does not allocate stream sequences or divide a domain update from its outbox transaction.

Store event-owned logical records in revisioned namespaces. Stream descriptor and retained floor key by stream UUID. Consumer progress keys by root epoch, consumer and stream. Processing markers append event UUID. Dead letters key by that same event marker tuple. Durable uint fields use u64 big-endian in binary keys and decimal strings in JSON values. Use a registered Storage namespace and type tag for each event-owned record family. Within that family derive the 16-byte record ID from the first 16 bytes of SHA-256 over the ASCII tag `ZIP-EVT-ROW-v1` and the fixed-width logical key. If the result is all zero, fail as an invalid derived key. Verify the full logical key stored in the value on every read or CAS. A digest collision fails closed and never overwrites state. Assigning namespace UUIDs and type tags is required before independent approval. Producer sequence keys remain Storage-owned. Bind persisted subscriber sessions to root and consumer; increment epoch by checked CAS under the same writer as checkpoint updates and reject an old epoch.

Within one bounded read snapshot obtain the root epoch, retained floor, stream head and events in ascending sequence. Recheck live scope before exposing results. Empty streams have head and floor zero. A missing row inside the retained range is corruption. Preserve the prior cursor and block that scan. Use no volatile notification as evidence that all events have been seen. On startup resume scans from durable checkpoints and recover any unresolved external consumer outcome first.

**ZIP-EVENTS-JOURNAL-T01.** A missing or damaged row within the retained range causes typed corruption and blocks later events.
