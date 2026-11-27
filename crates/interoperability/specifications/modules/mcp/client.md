# Scoped MCP client

**ZIP-INTEROPERABILITY-MCP-CLIENT-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/client.rs`

## Required implementation behavior

Negotiate exact server identity/version and capabilities, use bounded requests and validate typed response. Separate discovery and effects.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-CLIENT-T01.** A tool changed after negotiation cannot be invoked under stale digest.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
