# Traceable source extraction

**ZIP-RESEARCH-EXTRACTION-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/extraction.rs`

## Required implementation behavior

Extract approved excerpts and structured claims with source spans/version, mark uncertain interpretation and validate limits.

## Acceptance

**ZIP-RESEARCH-EXTRACTION-T01.** Malformed range cannot support citation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
