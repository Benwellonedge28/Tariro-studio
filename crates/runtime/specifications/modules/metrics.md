# Bounded execution telemetry

**ZIP-RUNTIME-METRICS-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/metrics.rs`

## Required implementation behavior

Record attempt/finish/cancel counts, bounded duration and policy labels. Do not use payload, path, integer task ID or secret as unbounded metric dimensions. Audit is separately durable.

## Acceptance

**ZIP-RUNTIME-METRICS-T01.** High-cardinality inputs do not create series or leak task content.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
