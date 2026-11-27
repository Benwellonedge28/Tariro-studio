# Typed completion and evidence

**ZIP-INTELLIGENCE-RESPONSE-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/response.rs`

## Required implementation behavior

Represent complete, incomplete, rejected and cancelled results with usage and provider/adapter provenance. Structured fields validate before acceptance.

## Acceptance

**ZIP-INTELLIGENCE-RESPONSE-T01.** Interrupted output is marked incomplete even if syntactically valid.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
