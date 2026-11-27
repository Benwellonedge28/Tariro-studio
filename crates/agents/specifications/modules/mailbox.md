# Admitted mailbox queue

**ZIP-AGENTS-MAILBOX-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/mailbox.rs`

## Required implementation behavior

Bound queued count via agents.max_mailbox_items and charged bytes. Use FIFO per sender where promised; on overflow return backpressure, keep cursor.

## Acceptance

**ZIP-AGENTS-MAILBOX-T01.** Concurrent writers cannot exceed remaining shared capacity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
