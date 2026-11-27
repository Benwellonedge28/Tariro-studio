# MCP integration boundary

**ZIP-INTEROPERABILITY-MCP-MOD-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/mod.rs`

## Required implementation behavior

Expose qualified client/server, tool/resource mapping and security policy by negotiated versions. Discovery cannot create grants.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-MOD-T01.** Imported MCP descriptor is not authorization.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
