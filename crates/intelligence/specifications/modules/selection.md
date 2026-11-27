# Deterministic model selection

**ZIP-INTELLIGENCE-SELECTION-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/selection.rs`

## Required implementation behavior

Compare admitted candidates using configured order and stable identifiers with declared capability fit. Preserve tie behavior and provider status.

## Acceptance

**ZIP-INTELLIGENCE-SELECTION-T01.** Changing input order leaves selected route stable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
