# Scoped shared-proposal strategy

**ZIP-ORCHESTRATION-STRATEGIES-COLLABORATIVE-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/collaborative.rs`

## Required implementation behavior

Share only approved artifacts and typed proposal findings. Preserve distinct authors, conflicts and roles; require verified merge of outputs.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-COLLABORATIVE-T01.** Malformed shared recommendation is rejected without mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
