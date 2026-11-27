# Agent scoped state record

**ZIP-AGENTS-STATE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/state.rs`

## Required implementation behavior

Persist assignment-local revision, role, current attempt and bounded context references. Apply compare-and-swap and separate speculative state from verified receipts.

## Acceptance

**ZIP-AGENTS-STATE-T01.** Stale agent result fails without replacing current state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
