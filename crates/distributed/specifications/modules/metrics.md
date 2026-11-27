# Bounded cluster telemetry

**ZIP-DISTRIBUTED-METRICS-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/metrics.rs`

## Required implementation behavior

Export counters, admitted/observed resource and partition state under scoped redaction and bounded dimensions. Audit receipts stay authoritative.

## Acceptance

**ZIP-DISTRIBUTED-METRICS-T01.** Worker payload and credentials never appear in metric labels.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
