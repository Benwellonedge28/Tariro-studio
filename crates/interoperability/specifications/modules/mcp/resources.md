# Scoped MCP resource reads

**ZIP-INTEROPERABILITY-MCP-RESOURCES-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/mcp/resources.rs`

## Required implementation behavior

Resolve typed resource identifier, scope/classification and bounded cursor before actual content read. Do not convert a read into external write.

## Acceptance

**ZIP-INTEROPERABILITY-MCP-RESOURCES-T01.** Stale cursor or cross-tenant resource denies before payload.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
