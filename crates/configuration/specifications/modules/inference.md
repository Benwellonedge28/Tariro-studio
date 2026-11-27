# Inference route preferences

**ZIP-CONFIGURATION-INFERENCE-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/inference.rs`

## Required implementation behavior

Resolve local model requirements, context policy and endpoint references. Intersect model/runtime capability and effective token and memory budgets before generation.

## Acceptance

**ZIP-CONFIGURATION-INFERENCE-T01.** A profile requesting more context than its backend supports yields a typed configuration conflict or smaller explicitly permitted request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
