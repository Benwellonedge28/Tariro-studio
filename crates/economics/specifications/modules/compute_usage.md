# Compute usage measurement

**ZIP-ECONOMICS-COMPUTE-USAGE-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/compute_usage.rs`

## Required implementation behavior

Record qualified device and duration/counter with explicit units and distinction between admission estimate and measured use.

## Acceptance

**ZIP-ECONOMICS-COMPUTE-USAGE-T01.** Unsupported hardware meter remains unknown.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
