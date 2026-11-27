# Consumer idempotency ledger

**ZIP-EVENTS-DEDUPLICATION-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/deduplication.rs`

For an in-store processor, commit the projection changes, processing marker and exclusive checkpoint together through Storage. Key the marker by root epoch, consumer, stream and event UUID. Store sequence, canonical envelope digest and the processing receipt. Bind the digest to stream and event IDs, registered kind, version, sequence, occurrence, correlation and immutable payload reference. Compute the SHA-256 over ASCII `ZIP-EVT-MARKER-v1`, then stream UUID, event UUID, sequence u64, major/minor u16, kind byte length u64 plus UTF-8 kind, occurrence Unix seconds i64 plus nanoseconds u32, correlation presence byte 0 or 1 plus UUID if present, protection-domain UUID, SHA-256 algorithm tag byte 1 plus 32 digest bytes, and logical payload length u64. Integers are big-endian and UUIDs use network byte order. Reject invalid fields before hashing. Qualify the codec against golden vectors before independent approval. Check an existing marker before applying the projection. Matching identity and digest replay the receipt. A different digest or sequence for the same ID conflicts. A sequence above the next unprocessed sequence cannot commit.

An external consumer may acknowledge only a durable, attributable processing receipt accepted by its configured verifier. For external effects, use the external effect's separately authorized idempotency and reconciliation protocol. A transport acknowledgment or worker assertion cannot prove processing. If a downstream commit is uncertain, hold the checkpoint before that event, surface recovery and reconcile before reapplying any effect. The event system promises at-least-once delivery while the prefix is retained. Only a qualified transactional consumer can show one application of its projection.

Producer ID history is independent of the per-consumer ledger. Retire marker rows only under retention that proves replay cannot reach them, or preserves an equivalent authoritative receipt fence. An old sequence without surviving evidence cannot prove an exact duplicate.

**ZIP-EVENTS-DEDUPLICATION-T01.** Lose the response after a committed projection, deliver the same event again and observe one projection mutation. Reusing the event ID with a different digest conflicts.
