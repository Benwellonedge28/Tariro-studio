# Authorized stream selection

**ZIP-EVENTS-TOPIC-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/topic.rs`

Register each stream UUID against exactly one workspace, event kind and payload protection domain before first append. Keep this mapping immutable. Update supported schema versions through the owning event registry. Retain the mapping while any event, cursor, receipt or producer identity can refer to the stream. A producer derives event kind through registration, so no extra per-row kind field is needed in the [Storage keyspace](../../../storage/specifications/modules/schema.md).

Normalize a topic as one workspace and an optional set of kind identifiers. Resolve it to authorized whole streams in UUID byte order, with bounded pagination under current scope. Subscribe to each stream with a separate cursor. A multi-stream client has no shared sequence and no total delivery order. Never filter rows from within a stream to synthesize a contiguous cursor. New streams require a fresh topic resolution. A stream whose scope changes closes before further disclosure. Payload access is a separate scoped read; possessing metadata does not confer it.

**ZIP-EVENTS-TOPIC-T01.** A wildcard stays inside its authorized workspace. Reusing a registered stream UUID for a different kind or workspace returns conflict.
