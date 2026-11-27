# Orchestrator execution loop

**ZIP-ORCHESTRATION-ORCHESTRATOR-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/orchestrator.rs`

## Required implementation behavior

Read pinned plan and checkpoint, determine Ready jobs, admit each through scheduler and apply verified observations with revision fencing. Never replay unknown mutations blindly.

## Acceptance

**ZIP-ORCHESTRATION-ORCHESTRATOR-T01.** Restart after claim preserves one active attempt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
