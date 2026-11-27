# Backend selection boundary

**ZIP-INFERENCE-BACKENDS-MOD-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/mod.rs`

## Required implementation behavior

Choose qualified versioned backend under policy and scope. Local, external local service, remote and distributed targets remain distinct.

## Acceptance

**ZIP-INFERENCE-BACKENDS-MOD-T01.** Unsupported backend cannot fall back to unapproved provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
