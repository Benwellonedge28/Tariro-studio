# Agent activation and shutdown

**ZIP-AGENTS-LIFECYCLE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/lifecycle.rs`

## Required implementation behavior

Use Configured, Ready, Running, Draining, Stopped or Failed. Require live lease before running; stop closes intake and drains supervised work.

## Acceptance

**ZIP-AGENTS-LIFECYCLE-T01.** Revocation stops new tasks and preserves committed evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
