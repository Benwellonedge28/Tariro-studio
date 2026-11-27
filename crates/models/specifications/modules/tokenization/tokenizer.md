# Exact token accounting port

**ZIP-MODELS-TOKENIZATION-TOKENIZER-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/tokenization/tokenizer.rs`

## Required implementation behavior

Encode/decode under bounded input and approved template, verify tokenizer digest and enforce context envelope. Distinguish invalid bytes and token excess.

## Acceptance

**ZIP-MODELS-TOKENIZATION-TOKENIZER-T01.** Changing tokenizer invalidates a previously admitted request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
