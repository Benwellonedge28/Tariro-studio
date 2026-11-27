# Atomic checkpoint publication

**ZIP-RUNTIME-CHECKPOINT-STORE-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/checkpoint/store.rs`

## Required implementation behavior

Write checkpoint/receipt revision and event together via storage. Exact replay returns prior receipt; content conflict rejects. External staging is immutable before reference.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-STORE-T01.** Crash before commit leaves prior checkpoint. Crash after commit replays receipt and one outbox event.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
