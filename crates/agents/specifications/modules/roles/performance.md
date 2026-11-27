# Performance reviewer role

**ZIP-AGENTS-ROLES-PERFORMANCE-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/performance.rs`

## Required implementation behavior

Measure approved fixture with profiles, resource evidence and exact version. Report unknown baselines instead of inventing thresholds.

## Acceptance

**ZIP-AGENTS-ROLES-PERFORMANCE-T01.** Different hardware claim cannot reuse noncomparable measurement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
