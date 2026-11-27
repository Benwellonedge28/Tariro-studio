# Tool schema interoperation

**ZIP-INTEROPERABILITY-MCP-TOOLS-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/tools.rs`

## Required implementation behavior

Bind advertised tool, version and schema digest to approved typed request; responses are untrusted data. Track actual receipt independently.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-TOOLS-T01.** Server-provided text cannot extend caller capabilities.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
