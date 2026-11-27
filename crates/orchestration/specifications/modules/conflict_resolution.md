# Explicit write conflict handling

**ZIP-ORCHESTRATION-CONFLICT-RESOLUTION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/conflict_resolution.rs`

## Required implementation behavior

Detect path/record conflict from normalized identities and current revision. Serialize or seek owner decision; revalidate exact changed candidate afterward.

## Acceptance

**ZIP-ORCHESTRATION-CONFLICT-RESOLUTION-T01.** Two contested patches cannot both publish under one reviewed revision.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
