# Deterministic lexical tokens

**ZIP-SEARCH-LEXICAL-TOKENIZER-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/lexical/tokenizer.rs`

## Required implementation behavior

Normalize under pinned rules, retain bounded source offsets and reject invalid ranges. Preserve original bytes for citations.

## Acceptance

**ZIP-SEARCH-LEXICAL-TOKENIZER-T01.** Replaying same Unicode fixture gives identical tokens and valid offsets.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
