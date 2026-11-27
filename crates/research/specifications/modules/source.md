# Immutable source descriptor

**ZIP-RESEARCH-SOURCE-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/source.rs`

## Required implementation behavior

Pin canonical source ID, version/date, medium, author or origin and data class, separating known digest and unverified metadata.

## Acceptance

**ZIP-RESEARCH-SOURCE-T01.** Changed source bytes invalidate exact earlier citation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
