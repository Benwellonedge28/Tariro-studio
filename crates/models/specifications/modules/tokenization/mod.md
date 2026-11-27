# Tokenizer adapter dispatch

**ZIP-MODELS-TOKENIZATION-MOD-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/tokenization/mod.rs`

## Required implementation behavior

Negotiate pinned tokenizer and vocabulary version. Do not infer tokenizer from text or model alias.

## Acceptance

**ZIP-MODELS-TOKENIZATION-MOD-T01.** Unknown tokenizer cannot count input for admission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
