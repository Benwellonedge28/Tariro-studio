# Durable progress view

**ZIP-ASSIGNMENTS-PROGRESS-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/progress.rs`

## Required implementation behavior

Read completed/pending counts, current unit and cursor from a single snapshot. Expose separate verified, staged and blocked counts. Projection never advances authoritative state.

## Acceptance

**ZIP-ASSIGNMENTS-PROGRESS-T01.** Concurrent subtask commit cannot splice counts from different generations.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
