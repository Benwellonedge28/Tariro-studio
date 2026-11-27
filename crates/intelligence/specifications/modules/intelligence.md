# Typed intelligence invocation

**ZIP-INTELLIGENCE-INTELLIGENCE-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/intelligence.rs`

## Required implementation behavior

Validate request and context digest, reserve limits, select approved route and return observed result or partial failure. Audit chosen provider and usage.

## Acceptance

**ZIP-INTELLIGENCE-INTELLIGENCE-T01.** Request without finite admitted envelope never dispatches.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
