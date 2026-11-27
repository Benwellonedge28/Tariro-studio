# Model capability advertisement

**ZIP-MODELS-CAPABILITIES-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/capabilities.rs`

## Required implementation behavior

Expose qualified modality, token window, tokenizer/version and safe resource assumptions. Unknown advertised metadata remains unqualified.

## Acceptance

**ZIP-MODELS-CAPABILITIES-T01.** Claimed vision in manifest without adapter support is not advertised as usable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
