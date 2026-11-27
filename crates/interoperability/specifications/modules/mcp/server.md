# Scoped MCP server

**ZIP-INTEROPERABILITY-MCP-SERVER-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/server.rs`

## Required implementation behavior

Authenticate session, advertise only approved scoped metadata, validate requests and recheck permission at dispatch. Bound stream and responses.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-SERVER-T01.** Unknown session cannot enumerate private capabilities.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
