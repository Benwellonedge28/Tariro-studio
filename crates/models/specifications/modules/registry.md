# Qualified revision lookup

**ZIP-MODELS-REGISTRY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/registry.rs`

## Required implementation behavior

Index immutable model revisions and verified readiness by scope. Reject shadowed identifiers and stale epoch. Register only after admission checks.

## Acceptance

**ZIP-MODELS-REGISTRY-T01.** Multiple candidates under same immutable ID cannot replace reviewed metadata.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
