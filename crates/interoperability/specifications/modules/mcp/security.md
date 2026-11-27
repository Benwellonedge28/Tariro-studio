# MCP authorization and egress

**ZIP-INTEROPERABILITY-MCP-SECURITY-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/security.rs`

## Required implementation behavior

Require exact actor, target, operation, destination and budget authority. Ignore content-derived privilege claims and redact sensitive diagnostics.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-SECURITY-T01.** A server resource cannot self-authorize escalation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
