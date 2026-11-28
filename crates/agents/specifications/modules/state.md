# Agent scoped state record

**ZIP-AGENTS-STATE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/state.rs`

## Boundary and inputs

Persist an assignment-scoped record with agent identity, manifest digest, lifecycle, checked revision, mailbox cursor, active attempt/epoch binding and bounded context and evidence references. Keep speculative output and trusted receipts in separate fields or records. An injected journal owns durable I/O and schema migration under the [persistence standard](../../../../PERSISTENCE_STANDARD.md).

## Behavior and failure handling

Use expected-revision transactions with the current attempt and identity scope. Authorized exact receipt replay returns the existing outcome. A changed concurrent result, stale worker epoch or mismatched manifest cannot advance state. Stage immutable context and evidence before referencing them. Preserve unresolved submissions before restart and never serialize live handles, clock instants or authority into reusable state.

## Acceptance

**ZIP-AGENTS-STATE-T01.** Fence an attempt, advance the record and deliver its delayed result. Verify no replacement of current state or duplicate terminal observation. Crash before and after committing a verified observation and compare the recovered cursor and receipt.
