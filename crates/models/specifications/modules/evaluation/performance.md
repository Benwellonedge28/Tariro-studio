# Scoped performance measurement

**ZIP-MODELS-EVALUATION-PERFORMANCE-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/evaluation/performance.rs`

## Required implementation behavior

Record representative workload, observed throughput, memory and first-token latency with platform/version. Numeric guarantees require qualified evidence.

## Acceptance

**ZIP-MODELS-EVALUATION-PERFORMANCE-T01.** A measured value on one host cannot be advertised across different profiles.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
