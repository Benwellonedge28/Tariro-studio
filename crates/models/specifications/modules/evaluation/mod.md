# Model qualification boundary

**ZIP-MODELS-EVALUATION-MOD-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/evaluation/mod.rs`

## Required implementation behavior

Route compatibility, benchmark and quality evaluation through pinned fixtures with real observations. Report not run explicitly.

## Acceptance

**ZIP-MODELS-EVALUATION-MOD-T01.** Available model metadata alone does not satisfy tests.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
