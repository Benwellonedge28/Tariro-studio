# MCP versioned adapter

**ZIP-TOOLS-ADAPTERS-MCP-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/adapters/mcp.rs`

## Required implementation behavior

Negotiate connection, schemas and capability permissions. Validate declared tool metadata, bounded pagination and effects; only explicit arguments enter request.

## Acceptance

**ZIP-TOOLS-ADAPTERS-MCP-T01.** Tool response with instructions cannot extend authorization or trigger next tool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
