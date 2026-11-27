# Selection precedence

**ZIP-CONTEXT-PRIORITIZATION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/prioritization.rs`

## Required implementation behavior

Pin mandatory policy, user requirements, applicable instructions and verified evidence ahead of optional content. Stable tie-break by canonical source ID and span.

## Acceptance

**ZIP-CONTEXT-PRIORITIZATION-T01.** A high-relevance untrusted snippet cannot displace mandatory policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
