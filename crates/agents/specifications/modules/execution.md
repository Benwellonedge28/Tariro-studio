# Supervised agent run

**ZIP-AGENTS-EXECUTION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/execution.rs`

## Required implementation behavior

Authorize exact task, obtain runtime lease, invoke model/tools through typed ports, record observed effects and cancel via supervisor.

## Acceptance

**ZIP-AGENTS-EXECUTION-T01.** Cancellation after confirmed effect preserves receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
