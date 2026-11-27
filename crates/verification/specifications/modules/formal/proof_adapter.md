# Proof evidence validation

**ZIP-VERIFICATION-FORMAL-PROOF-ADAPTER-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/formal/proof_adapter.rs`

## Required implementation behavior

Verify proof artifact with pinned checker/version, model digest and assumptions; separate theorem acceptance from system implementation evidence.

## Acceptance

**ZIP-VERIFICATION-FORMAL-PROOF-ADAPTER-T01.** A valid proof for another model is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
