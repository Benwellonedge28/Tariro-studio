# Bounded generation session

**ZIP-INFERENCE-SESSION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/session.rs`

## Required implementation behavior

Bind request, verified model, provider, epoch, resource envelope and cancellation handle. Reuse requires matching revisions and permitted cache scope.

## Acceptance

**ZIP-INFERENCE-SESSION-T01.** Old session cannot accept new request under changed identity or policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
