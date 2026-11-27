# Bounded strict output validation

**ZIP-INTELLIGENCE-STRUCTURED-OUTPUT-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/structured_output.rs`

## Required implementation behavior

Decode complete output against versioned schema under byte/depth limits; separate syntactic and semantic failure, no silent defaults on required fields.

## Acceptance

**ZIP-INTELLIGENCE-STRUCTURED-OUTPUT-T01.** Valid JSON with a missing required field fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
