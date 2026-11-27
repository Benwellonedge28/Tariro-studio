# Durable workflow checkpoint

**ZIP-WORKFLOWS-CHECKPOINT-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/checkpoint.rs`

## Required implementation behavior

Persist verified stage/step outcome, next eligibility, epoch and artifact refs in one transaction. Resume highest contiguous evidence.

## Acceptance

**ZIP-WORKFLOWS-CHECKPOINT-T01.** Lost acknowledgement does not advance step twice.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
