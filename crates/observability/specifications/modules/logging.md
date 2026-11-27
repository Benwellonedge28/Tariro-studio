# Bounded structured local logs

**ZIP-OBSERVABILITY-LOGGING-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/logging.rs`

## Required implementation behavior

Use typed stable fields, configurable size/time retention and redact before queue/persist. Record dropped counts safely.

## Acceptance

**ZIP-OBSERVABILITY-LOGGING-T01.** Canary secret and unbounded payload absent from output.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
