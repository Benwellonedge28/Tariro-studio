# Runtime

This crate's design covers taskHandle, supervisor record, durable checkpoint, process ownership handle.

- [Implementation design](DESIGN.md)
- [Crate contributor instructions](AGENTS.md)
- [Runtime](../../specifications/0200-runtime/runtime.md)

Acceptance fixture: Crash on both sides of spawn and checkpoint, verify no orphan and no duplicate effects.
