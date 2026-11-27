# Vocabulary integrity

**ZIP-MODELS-TOKENIZATION-VOCABULARY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/tokenization/vocabulary.rs`

## Required implementation behavior

Validate token IDs, duplicates, special tokens and bound size before use. Map unknown tokens only when manifest declares behavior.

## Acceptance

**ZIP-MODELS-TOKENIZATION-VOCABULARY-T01.** Duplicate or missing mandatory special token blocks load.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
