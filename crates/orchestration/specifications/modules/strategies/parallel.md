# Conflict-aware parallel proposals

**ZIP-ORCHESTRATION-STRATEGIES-PARALLEL-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/parallel.rs`

## Required implementation behavior

Partition independent ready tasks by conflict key; submit only admitted candidates. Preserve deterministic selection when resources are scarce.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-PARALLEL-T01.** Overlapping write paths serialize despite available workers.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
