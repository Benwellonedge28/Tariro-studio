# Fenced workflow execution

**ZIP-WORKFLOWS-EXECUTION-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/execution.rs`

## Required implementation behavior

Schedule steps with immutable plan, current authorization and admitted budgets. Persist outcomes and checkpoints; unknown effects reconcile before retry.

## Acceptance

**ZIP-WORKFLOWS-EXECUTION-T01.** Crash after verified step resumes at next eligible node.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
