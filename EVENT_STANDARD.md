# Durable event standard

**ZIP-EVT-001 · v1.1 candidate · Owner** Events and storage maintainers

Storage commits the producer's complete outbox envelope with the originating state change. It allocates a checked sequence per stream. UTC occurrence time is descriptive. Kind comes from the immutable stream registry, while each event carries its supported schema version and scoped immutable payload reference. Producer wake notifications are advisory.

Deliver committed events at least once within the retained stream. Progress is an exclusive cursor scoped to stream, consumer and storage root epoch. A qualified local processor commits projection, marker and cursor together. External processing needs an attributable durable receipt and its own effect reconciliation. A transport acknowledgment alone cannot advance progress. A fenced session, lost response or full queue cannot silently skip an event.

Expire a cursor below the retained floor or from an old root. At equality resume from the next event. Require an authorized, verified snapshot before replacing an expired projection. Backpressure is bounded by admitted memory and may close a slow subscription. Give an authorized caller its last durable cursor on close. Quarantine preserves identity, stays visible and holds the cursor before the failed delivery.

Durable events and payload access follow independent scope checks. Telemetry does not replace a committed effect event. Check delivery, restart, acknowledgement, cursor compaction, pinned retention and scope under the [Events acceptance fixtures](contracts/acceptance/events/delivery-fixtures.json). Declare version compatibility before changing published fields or their meaning.
