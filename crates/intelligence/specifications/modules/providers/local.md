# Local inference provider

**ZIP-INTELLIGENCE-PROVIDERS-LOCAL-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/providers/local.rs`

## Required implementation behavior

Use qualified local backend, measured device capacity and balanced lease. Local-only scope forbids external discovery or service invocation.

## Acceptance

**ZIP-INTELLIGENCE-PROVIDERS-LOCAL-T01.** Offline model run emits zero network traffic.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
