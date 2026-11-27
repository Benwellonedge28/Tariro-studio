# Qualified MCP transport

**ZIP-INTEROPERABILITY-MCP-TRANSPORT-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/transport.rs`

## Required implementation behavior

Bind origin or explicit local channel, session and deadlines, enforce admitted bytes and handle unknown effects separately.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-TRANSPORT-T01.** Disconnect after mutation does not trigger blind retry.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
