# Remote inference adapter

**ZIP-INFERENCE-BACKENDS-REMOTE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/remote.rs`

## Required implementation behavior

Revalidate endpoint/audience and prompt disclosure, charge spend before send and reconcile missing final response. No automatic retries with uncertain charge.

## Acceptance

**ZIP-INFERENCE-BACKENDS-REMOTE-T01.** Allowed model alone cannot authorize data transmission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
