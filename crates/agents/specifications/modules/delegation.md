# Agent task delegation

**ZIP-AGENTS-DELEGATION-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/delegation.rs`

## Required implementation behavior

Bind child task to parent role, scope, deadline and depth from configured policy. Record lineage and reject cycles and output under stale grants.

## Acceptance

**ZIP-AGENTS-DELEGATION-T01.** Subagent cannot exceed parent scope or configured delegation bound.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
