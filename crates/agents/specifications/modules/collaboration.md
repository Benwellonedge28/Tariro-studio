# Bounded collaborative exchange

**ZIP-AGENTS-COLLABORATION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/collaboration.rs`

## Required implementation behavior

Pass typed proposals/evidence through scoped channels and resolve conflicts by coordinator. Shared transcript is untrusted and has no granting effect.

## Acceptance

**ZIP-AGENTS-COLLABORATION-T01.** Two conflicting proposed edits require explicit resolution before write.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
