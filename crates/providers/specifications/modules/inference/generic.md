# Explicit generic inference adapter

**ZIP-PROVIDERS-INFERENCE-GENERIC-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/generic.rs`

## Required implementation behavior

Require approved versioned schema, destination and capabilities with fixture qualification. Never infer authorization from compatible request syntax.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-GENERIC-T01.** Matching JSON shape without qualified endpoint remains unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
