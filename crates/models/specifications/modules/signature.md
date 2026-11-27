# Model manifest signature

**ZIP-MODELS-SIGNATURE-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/signature.rs`

## Required implementation behavior

Verify trusted key, domain, exact bytes and required signer policy. Failed or absent signature under mandatory policy is denied.

## Acceptance

**ZIP-MODELS-SIGNATURE-T01.** Valid signature for another manifest does not authorize current weights.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
