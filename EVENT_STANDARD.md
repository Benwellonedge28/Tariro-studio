# Durable event standard

**ZIP-EVT-001 · v1.0 · Owner:** Events and storage maintainers. **Maturity:** D4 candidate.

A durable event envelope carries `schema_version, stream_id, sequence, event_id, kind, occurred_at, correlation_id, payload_ref`. Sequence is a checked monotonic integer within a stream. Capture UTC occurrence time for display; order by sequence. Allocate sequence and insert the outbox event in the same transaction as the corresponding domain transition.

Consumers start from an exclusive cursor. Persist their projection mutation and deduplication marker before acknowledging. Delivery is at least once; a broker acknowledgment does not certify processing. An expired cursor returns typed `CursorExpired` and a fresh snapshot reference. Consumer backpressure closes or pauses a bounded subscription using an admitted lease and retains the last durable cursor.

Sharable payloads require separate access controls. Telemetry does not replace a durable effect event. Crash tests cover commit before dispatch, processed before acknowledge, duplicate delivery and cursor compaction. Declare event schema compatibility before changing required fields or meaning.
