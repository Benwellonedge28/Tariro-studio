# Contradictory fact resolution

**ZIP-KNOWLEDGE-CONFLICT-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/conflict.rs`

## Required implementation behavior

Preserve competing scoped evidence, source quality and reviewed resolution, keeping unknown if unresolved. No automatic overwrite by latest timestamp.

## Acceptance

**ZIP-KNOWLEDGE-CONFLICT-T01.** Conflicting evidence remains visible and does not become one confirmed claim.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
