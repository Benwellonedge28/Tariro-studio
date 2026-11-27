# Provenance-preserving summaries

**ZIP-CONTEXT-SUMMARIZATION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/summarization.rs`

## Required implementation behavior

Create summary with exact input refs and transformation metadata. Mark uncertainty and do not promote summaries to verified citations.

## Acceptance

**ZIP-CONTEXT-SUMMARIZATION-T01.** A fabricated summary assertion cannot become observed evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
