# Qualified benchmark execution

**ZIP-MODELS-EVALUATION-BENCHMARK-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/evaluation/benchmark.rs`

## Required implementation behavior

Pin model/backend/device, prompt fixture and seed, run under resource lease and capture exact usage and elapsed metrics.

## Acceptance

**ZIP-MODELS-EVALUATION-BENCHMARK-T01.** Changed device requires separate benchmark provenance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
