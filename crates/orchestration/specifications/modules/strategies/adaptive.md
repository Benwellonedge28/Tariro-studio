# Resource-aware replan

**ZIP-ORCHESTRATION-STRATEGIES-ADAPTIVE-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/adaptive.rs`

## Required implementation behavior

Use current observed pressure to propose admitted alternatives within existing approval. Any widened purpose, scope or quality change is separately reviewed.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-ADAPTIVE-T01.** Memory pressure does not implicitly activate a remote route.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
