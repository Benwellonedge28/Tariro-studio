# Bounded authorized retrieval

**ZIP-RESEARCH-RETRIEVAL-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/retrieval.rs`

## Required implementation behavior

Validate destination and every redirect, enforce bytes and excerpt limits, preserve response digest and retrieval status.

## Acceptance

**ZIP-RESEARCH-RETRIEVAL-T01.** Forbidden redirect produces no request to new host.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
