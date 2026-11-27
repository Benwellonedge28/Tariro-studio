# Typed content modalities

**ZIP-INTELLIGENCE-MODALITY-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/modality.rs`

## Required implementation behavior

Tag input/output modality, MIME and scoped artifact references. Validate availability and admitted sizes without decoding heavyweight content prematurely.

## Acceptance

**ZIP-INTELLIGENCE-MODALITY-T01.** Unsupported modality rejected before provider call.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
