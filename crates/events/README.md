# Events

This crate's design covers eventEnvelope v1, monotonic sequence per stream, outbox and cursor records.

- [Implementation design](DESIGN.md)
- [Crate contributor instructions](AGENTS.md)
- [Runtime](../../specifications/0200-runtime/runtime.md)
- [Storage](../../specifications/2500-storage/storage.md)
- [Observability](../../specifications/3100-observability/observability.md)

Acceptance fixture: Crash after commit before dispatch, replay duplicates and resume from cursor.
