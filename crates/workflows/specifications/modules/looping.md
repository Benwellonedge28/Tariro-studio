# Statically bounded iteration

**ZIP-WORKFLOWS-LOOPING-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/looping.rs`

## Required implementation behavior

Require declared finite bound and tighten by configured budget. Give iterations stable identity and checkpoint before next effect; overflow rejects before expansion.

## Acceptance

**ZIP-WORKFLOWS-LOOPING-T01.** Oversized loop never creates a partial executable graph.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
