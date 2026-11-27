# Lexical pipeline boundary

**ZIP-SEARCH-LEXICAL-MOD-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/lexical/mod.rs`

## Required implementation behavior

Use qualified tokenizer, postings and ranker versions under scoped storage. Unsupported language features remain explicit.

## Acceptance

**ZIP-SEARCH-LEXICAL-MOD-T01.** Unqualified tokenizer never claims exact rank compatibility.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
