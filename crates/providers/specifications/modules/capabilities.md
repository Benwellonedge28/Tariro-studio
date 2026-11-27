# Versioned provider qualifications

**ZIP-PROVIDERS-CAPABILITIES-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/capabilities.rs`

## Required implementation behavior

Distinguish supported, unsupported and unknown for exact operations and format versions. Capability is independent from availability and rate limit.

## Acceptance

**ZIP-PROVIDERS-CAPABILITIES-T01.** Unhealthy provider with known capability remains supported but unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
