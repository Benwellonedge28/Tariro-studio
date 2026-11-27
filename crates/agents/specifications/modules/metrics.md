# Bounded redacted agent measurements

**ZIP-AGENTS-METRICS-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/metrics.rs`

## Required implementation behavior

Record role/state counts and durations using bounded label sets, without prompts, paths or actor credentials. Durable effects use audit separately.

## Acceptance

**ZIP-AGENTS-METRICS-T01.** Canary prompt content and high-cardinality agent IDs absent from metric series.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
