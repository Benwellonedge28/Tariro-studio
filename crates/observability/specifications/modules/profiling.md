# Explicit resource profiling

**ZIP-OBSERVABILITY-PROFILING-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/profiling.rs`

## Required implementation behavior

Run approved measured workload under sandbox/budget and collect redacted platform/executable identity. Profiling requires separate scope where it reads sensitive state.

## Acceptance

**ZIP-OBSERVABILITY-PROFILING-T01.** Unapproved target process cannot be profiled.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
